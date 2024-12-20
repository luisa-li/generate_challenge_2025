from fastapi import FastAPI, Query, HTTPException, Request 
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from typing import Optional, Literal
from util import parse_categories, load_data, prods_to_list

app = FastAPI()

ALL_CATEGORIES = ["electronics", "apparel", "home goods", "sports", "beauty", "grocery", "office supplies", "outdoor", "toys", "health", "automotive", "luxury", "books"]

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/api/v1/products", response_model=list[dict])
async def get_products(
    sort: Optional[Literal["name", "price", "stars"]] = Query("name", description="Sort by field"),
    order: Optional[Literal["asc", "desc"]] = Query("asc", description="Sort order"),
    categories: Optional[str] = Query(None, description="Filter by one or more categories"),
    offset: Optional[int] = Query(0, description="Number of pages of size limit to skip"),
    limit: Optional[int] = Query(3, description="Maximum number of items to return"),
    price_min: Optional[int] = Query(0, description="Minimum price in cents"),
    price_max: Optional[int] = Query(4294967295, description="Maximum price in cents"),
    star_min: Optional[int] = Query(0, description="Minimum star rating, in 0.01 stars"),
    star_max: Optional[int] = Query(500, description="Maximum star rating, in 0.01 stars"),
):
    """
    Fetches a list of products based on specified attributes
    """
    
    if categories == None:
        filter_categories = set(ALL_CATEGORIES)
    else:
        # manually parsing the categories
        processed_categories = []
        for category in parse_categories(categories.split(",")):
            if category not in ALL_CATEGORIES: 
                raise HTTPException(
                    status_code=400,
                    detail="Category not accepted"
                )
            else:
                processed_categories.append(category)
        filter_categories = set(processed_categories)
    ascending = True if order == "asc" else False
    
    data = load_data()
    
    # first, we filter everything as needed 
    price_filtered = data[(data['price'] >= price_min) & (data['price'] <= price_max)]
    star_filtered = price_filtered[(price_filtered['stars'] >= star_min) & (price_filtered['stars'] <= star_max)]
    category_filtered = star_filtered[
        star_filtered['categories'].apply(
            lambda categories: bool(set(categories).intersection(filter_categories))
        )
    ]
    
    if len(category_filtered) == 0:
        # empty
        return []
    
    # then, we sort by the order given
    sorted = category_filtered.sort_values(by=sort, ascending=ascending)
    
    # finally, do offset and limit 
    offset_limited = sorted.iloc[offset:offset+limit]
        
    final = prods_to_list(offset_limited)
    
    return final

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": str(exc)},
    )

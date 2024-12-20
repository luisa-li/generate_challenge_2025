from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
import json 

DATA = "data.json"

app = FastAPI()

def load_data() -> dict:
    return json.load(DATA)
    

@app.get("/books", response_model=List[dict])
async def get_books(
    title: Optional[str] = Query(None, description="Filter by book title"),
    author: Optional[str] = Query(None, description="Filter by author name"),
    year: Optional[int] = Query(None, description="Filter by publication year"),
):
    """
    Get a list of books with optional filters for title, author, and year.
    """
    filtered_books = books

    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book["title"].lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book["author"].lower()]
    if year:
        filtered_books = [book for book in filtered_books if book["year"] == year]

    if not filtered_books:
        raise HTTPException(status_code=404, detail="No books found matching the criteria.")

    return filtered_books

if __name__ == "__main__":
    data = load_data()
    breakpoint()
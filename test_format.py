from util import parse_categories

def test_single():
    categories = ["office%20supplies"]
    expected = ["office supplies"]
    assert parse_categories(categories) == expected

def test_multiple():
    categories = ["office%20supplies", "electronics", "home%20goods"]
    expected = ["office supplies", "electronics", "home goods"]
    assert parse_categories(categories) == expected

def test_no_replace():
    categories = ["electronics", "sports"]
    expected = ["electronics", "sports"]
    assert parse_categories(categories) == expected

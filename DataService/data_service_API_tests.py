import data_service as db

import requests

API_BASE = "https://group-b-paste-site.azurewebsites.net/api/"

# Tests for database functions
def main():
    test1()
    print("Test 1 passed.")
    test2()
    print("Test 2 passed.")
    test3()
    print("Test 3 passed.")
    db.delete({})

def test1():
    """
    Test ReadRecords after deleting all records returns empty list
    """
    db.delete({})
    req = requests.get(API_BASE + "ReadRecords")
    assert req.status_code == 200
    data = req.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test2():
    """
    Test CreateRecord returns error on missing title parameter
    """
    req = requests.post(API_BASE + "CreateRecord")
    assert req.status_code == 400
    data = req.json()
    assert data.get("error") is not None

def test3():
    """
    Test CreateRecord creates record with given title parameter as post body
    """
    create = requests.post(API_BASE + "CreateRecord", json={
        "title":"test3",
        "author":"tester",
        "content":"test content",
        "unlisted":False
    })
    assert create.status_code == 200
    read = requests.get(API_BASE + "ReadRecords")
    assert read.status_code == 200
    data = read.json()
    assert isinstance(data, list)
    # raises StopIteration exception if record is not present
    next(record for record in data if record["title"] == "test3")

# Run on file exectution
if __name__ == "__main__":
    main()
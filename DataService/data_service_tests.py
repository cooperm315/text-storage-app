import data_service as db

from bson import ObjectId

import random

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
    Test if resetting, then re-initializing the database creates an empty collection
    """
    assert db.reset()
    assert db.initialize()
    records = db.read({})
    assert isinstance(records, list)
    assert len(records) == 0

def test2():
    """
    Test if create has the correct return type, and read/delete target the correct records.
    """
    for i in range(5):
        assert isinstance(db.create({"name":"test2", "value":i}), ObjectId)

    # read records
    records = db.read({"name":"test2"})
    assert isinstance(records, list)
    assert len(records) == 5

    # delete first created record only
    assert db.delete({"value":0}) == 1
    records = db.read({"name":"test2"})
    assert isinstance(records, list)
    assert len(records) == 4

    # delete all created records
    assert db.delete({"name":"test2"}) == 4
    records = db.read({"name":"test2"})
    assert isinstance(records, list)
    assert len(records) == 0


def test3():
    """
    Test read one returns the correct value, and update modifies the correct records.
    """
    for i in range(5):
        assert isinstance(db.create({"name":"test3", "value":i}), ObjectId)
    
    # read record with value 0
    records = db.read({"value":0}, one=True)
    assert isinstance(records, dict)

    # update all records to have the same value
    rand = random.randint(50, 100)
    assert db.update({"name":"test3"}, {"value":rand}) == 5

    # read all updated records
    records = db.read({"value":rand})
    assert isinstance(records, list)
    assert len(records) == 5

# Run on file exectution
if __name__ == "__main__":
    main()
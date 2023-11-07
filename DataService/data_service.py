# pymongo allows python to speak with mongoDB
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from bson import ObjectId

# use a global parameter
mycol = None

# Constants for the project
DB_NAME = "groupB"
COL_NAME = "records"
CONNECTION_URL = "mongodb+srv://group-b:Keyboard_Warriors112@cluster0.twgidxv.mongodb.net/test"
# CONNECTION_URL = "mongodb://localhost:27017/"

def initialize() -> bool:
    """
    Establish a connection to MongoDB and set the global collection variable

    :returns: whether initialization was successful
    """

    global mycol
    myclient = MongoClient(CONNECTION_URL, serverSelectionTimeoutMS=5000)

    try:
        myclient.server_info()
    except ServerSelectionTimeoutError as e:
        print(e)
        return False
    
    try:
        mydb = myclient[DB_NAME]   
        mycol = mydb[COL_NAME]
    except Exception:
        return False
    else:
        return True

def reset() -> bool:
    """
    Reset the collection
    
    :returns: whether the reset was successful
    """
    try:
        global mycol
        mycol.drop()
        mycol = None
    except Exception:
        return False
    else:
        return True

def create(data:dict) -> ObjectId:
    """
    Insert a record

    :param data: a python dict where each key/value is a field to add to the record
    :returns: insert object ID for successful insertion, otherwise None
    """
    if mycol is None: return None
    insert = mycol.insert_one(data)
    return insert.inserted_id or None

def read(query:dict, one:bool=False) -> list[dict] or dict:
    """
    Read record(s)
    
    :param query: a python dict of which keys/values the targeted records must have
    :param one: whether to only read a single record
    :returns: either a list of matching records or a single record, depending on the value of the one param
    """
    if mycol is None: return []
    if one:
        return mycol.find_one(query)
    else:
        return list(mycol.find(query))


def update(query:dict, data:dict) -> int:
    """
    Update a record

    :param query: a python dict of which keys/values the targeted records must have
    :param data: a python dict of key/value pairs that will be replaced in the targeted records
    :returns: the number of record modified by this action, or -1 on failure
    """
    if mycol is None: return False
    try:
        res = mycol.update_many(query, {'$set':data})
    except Exception:
        return -1
    else:
        return res.modified_count
    

def delete(query:dict) -> int:
    """
    Delete record(s)

    :param query: a python dict of which keys/values the targeted records must have
    :returns: the number of record modified by this action, or -1 on failure
    """
    if mycol is None: return False
    try: 
        res = mycol.delete_many(query)
    except Exception:
        return -1
    else:
        return res.deleted_count

def incViewCount(query:dict) -> bool:
    """
    Increment view count for a record

    :param query: a python dict of which keys/values the targeted records must have
    :returns: whether the view count was successfully updated
    """
    if mycol is None: return False
    try:
        mycol.update_one(query, {'$inc':{"viewCount":1}})
    except Exception:
        return False
    else:
        return True

# On import, initialize the database
if __name__ != "__main__":
    initialize()
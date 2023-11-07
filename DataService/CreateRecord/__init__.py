import data_service
import json
import time
import uuid

import azure.functions as func

REQUIRED_PARAMS = ["title", "author", "content", "unlisted"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Creates a new paste from a given title, author, and content.
    Automatically associates this paste with a timestamp and unique ids (can be used to view, update, and delete later)
    """
    try:
        record = req.get_json()
    except ValueError:
        return func.HttpResponse(json.dumps({"error":"Missing request body."}), status_code=400)

    # Check to make sure all parameters are present
    if not all(param in record for param in REQUIRED_PARAMS):
        return func.HttpResponse(json.dumps({"error":"Missing parameters."}), status_code=400)

    # Create paste values
    view_id = uuid.uuid4()
    edit_id = uuid.uuid4()
    timestamp = time.time()
    paste = {
        "title": record.get("title", "[Untitled]"),
        "author": record.get("author", "[Anonymous]"),
        "content": record.get("content", ""),
        "unlisted": record.get("unlisted", False),
        "viewId": str(view_id),
        "editId": str(edit_id),
        "createdAt": timestamp,
        "editedAt": timestamp,
        "viewCount": 0,
    }

    # Insert paste into database
    if data_service.create(paste) is None:
        return func.HttpResponse(json.dumps({"error":"Failed to insert record."}), status_code=500)

    return func.HttpResponse(json.dumps({"message":"Inserted record successfully.", "viewId": str(view_id), "editId": str(edit_id)}), status_code=200)
        

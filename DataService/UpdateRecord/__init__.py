import data_service
import json
import time

CHANGEABLE_VALUES = ["title", "author", "content", "unlisted"]

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Update a paste given the unique editing ID of the paste and a set of values to change.
    """
    try:
        record = req.get_json()
    except ValueError:
        return func.HttpResponse(json.dumps({"error":"Missing request body."}), status_code=400)
    
    edit_id = record.get("editId")
    if not edit_id:
        return func.HttpResponse(json.dumps({"error":"Missing editing ID of paste to update."}), status_code=400)

    # Construct query from editable values and add edited timestamp
    query = {key:value for key, value in record.items() if key in CHANGEABLE_VALUES}
    query["editedAt"] = time.time() 

    # Update paste in database
    update = data_service.update({"editId": edit_id}, query)
    if update == -1:
        return func.HttpResponse(json.dumps({"error":"Failed to update record."}), status_code = 500)
    
    if update == 0:
        return func.HttpResponse(json.dumps({"error":"No records updated. Edit ID does not exist."}), status_code = 404)

    return func.HttpResponse(json.dumps({"message":"Updated record successfully."}),status_code = 200)
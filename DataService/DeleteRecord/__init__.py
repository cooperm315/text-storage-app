import data_service
import json

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Delete a paste given its unique editing ID
    """

    # Get edit ID from request body
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(json.dumps({"error":"Missing request body"}), status_code=400)
    
    edit_id = req_body.get("editId")
    if not edit_id:
        return func.HttpResponse(json.dumps({"error":"Missing editing ID of paste to delete."}), status_code=400)
        

    # Delete paste from database
    delete = data_service.delete({"editId": edit_id})

    if delete == -1:
        return func.HttpResponse(json.dumps({"error":"Failed to delete paste."}), status_code=500)
    
    if delete == 0:
        return func.HttpResponse(json.dumps({"error":"No records deleted. Edit ID does not exist."}), status_code=404)

    return func.HttpResponse(json.dumps({"message":"Successfully deleted paste."}), status_code=200)
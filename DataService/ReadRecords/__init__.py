import data_service
from bson import json_util

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Read one or all records from the database.
    """
    record = None

    # Get record data, view-only
    if req.params.get("viewId"):
        record = data_service.read({"viewId":req.params.get("viewId")}, one=True)
        if not record:
            return func.HttpResponse(json_util.dumps({"error":"Paste with given view ID not found."}), status_code=404)
        record.pop("editId")
        data_service.incViewCount(record)
    
    # Get record data from editId. Allow editing, and send editId back
    elif req.params.get("editId"):
        record = data_service.read({"editId":req.params.get("editId")}, one=True)
        if not record:
            return func.HttpResponse(json_util.dumps({"error":"Paste with given edit ID not found."}), status_code=404)
        data_service.incViewCount(record)

    # Get all listed records
    else:
        record = data_service.read({"unlisted":False}, one=False)
        if not record:
            return func.HttpResponse(json_util.dumps({"error":"No pastes have been made yet!"}), status_code=404)
        
        # FIX: don't expose editing IDs on public record reads!!!
        for r in record:
            r.pop("editId")

    return func.HttpResponse(json_util.dumps(record), status_code=200)

from flask import Flask, redirect, render_template, request
import requests

from datetime import datetime

API_URL = "https://group-b-paste-site.azurewebsites.net/api/"
# API_URL = "http://localhost:7071/api/"
 
app = Flask(__name__, template_folder="./templates", static_folder="./static")

@app.route("/")
def home_page():
    return render_template("home.html"), 200

@app.route("/view") 
def view_page():
    """ View all pastes
    """

    read = requests.get(API_URL + "ReadRecords")
    response = read.json()

    if read.status_code != 200:
        return render_template("status.html", status=read.status_code, message=response.get("error")), read.status_code

    return render_template("view.html", formatter=formatter, pastes=response), 200

@app.route("/view/<view_id>") 
def view_paste_page(view_id):
    """ View a specific paste

    Variable Params:
        view_id: the id of the paste to view

     Query Params:
        editID: If included, the paste will also display an "editing link"
        This is good for when the owner of a paste is viewing it after creating/editing
    """

    read = requests.get(API_URL + "ReadRecords?viewId=" + view_id)
    response = read.json()
    
    if read.status_code != 200:
        return render_template("status.html", status=read.status_code, message=response.get("error")), read.status_code
    
    return render_template("paste.html", formatter=formatter, paste=response, edit_id=request.args.get("editId")), 200

@app.route("/create", methods=["POST", "GET"])
def create_page():
    """ Create a new paste

    Accepts a POST request to create a new paste, or a GET request to display the create page
    """

    if request.method == "POST":

        create = requests.post(API_URL + "CreateRecord", json={
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "content": request.form.get("content"),
            "unlisted": request.form.get("unlisted") == "on"
        })
        response = create.json()

        # return error page on failure
        if create.status_code != 200 or "viewId" not in response:
            return render_template("status.html", status=create.status_code, message=response.get("error")), create.status_code
        
        return redirect("/view/" + response.get("viewId") + "?editId=" + response.get("editId"))
    
    # Handle get request for create page
    else:
        return render_template("create.html"), 200

@app.route("/edit/<edit_id>", methods=["POST", "GET"])
def edit_page(edit_id):
    """ Edit a paste

    Accepts a POST request to edit a paste, or a GET request to display the edit page
    """

    # Handle form submission
    if request.method == "POST":

        edit = requests.put(API_URL + "UpdateRecord", json={
            "editId": edit_id,
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "content": request.form.get("content"),
            "unlisted": request.form.get("unlisted") == "on"
        })
        response = edit.json()

        # return error page on failure
        if edit.status_code != 200:
            return render_template("status.html", status=edit.status_code, message=response.get("error")), edit.status_code
        
        return redirect("/view/" + request.form.get("viewId") + "?editId=" + edit_id)
    
    # Handle request for create page
    else:
        read_req = requests.get(API_URL + "ReadRecords?editId=" + edit_id)
        read_res = read_req.json()
    
        if read_req.status_code != 200:
            return render_template("status.html", status=read_req.status_code, message=read_res.get("error")), read_req.status_code

        return render_template("edit.html", formatter=formatter, paste=read_res), 200

@app.route("/delete/<edit_id>", methods=["POST"])
def delete_action(edit_id):
    """ Delete a paste

    Accepts a POST request. There is no delete page, so you cannot GET this endpoint.
    The delete button is on the edit page, using a different form/button that submits here.
    """
    
    delete = requests.delete(API_URL + "DeleteRecord", json={
        "editId": edit_id,
    })
    response = delete.json()

    # return error page on failure
    if delete.status_code != 200:
        return render_template("status.html", status=delete.status_code, message=response.get("error")), delete.status_code
    
    return render_template("status.html", status=delete.status_code, message=response.get("message")), delete.status_code


# Error Handling
@app.errorhandler(404)
def not_found(*_):
    return render_template("status.html", status=404, message="Page Not Found")

@app.errorhandler(500)
def internal_server_error(*_):
    return render_template("status.html", status=500, message="Internal Server Error")

# Helper Methods
def formatter(timestamp:float) -> str:
    return "" if not timestamp else datetime.strftime(datetime.fromtimestamp(timestamp), "%b %d, %Y at %#I:%M %p")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
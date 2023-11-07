# Web Server Documentation

This is documentation for all routes and functions that are part of the Flask webserver, located in `app.py`

Error handling is not detailed extensively here because all errors are handled by rendering the template `status.html`.

If the error is caught, the relevant status code and message will be displayed. If it is not caught, it will contain the defauly `500: Internal Server Error` status code and message.

The types of errors that might occur are outline in the Azure API docs.

# Routes

## home_page()

The basic home page of this site

### Route
GET: `/`

### Returns (GET)
- Template: `home.html`

---
## view_page()

The page that displays all the records posted to this site

### Route
GET: `/view`

### Returns (GET)
- Template: `view.html`
- Context:
    - formatter (function): the timestamp formatting utility function
    - pastes (list): a list of all pastes to be rendered on this page

---
## view_paste_page()

The page that displays a read-only version of a specific paste

### Route
GET: `/view/<view_id>`

### URL Variables (GET)
- view_id: the id of the paste to view

### Query Params (GET)
- editId: if included, the paste will also show an "editing link." This is good if the owner of the paste is viewing it after creating/editing it

### Returns (GET)
- Template: `paste.html`
- Context:
    - formatter (function): the timestamp formatting utility function
    - paste (dict): the paste to be rendered on this page
    - edit_id (str | None): the editing ID that will be displayed on this page, if provided

--- 
## create_page()

On a GET request, this displays a form for creating a page. On a POST request, this adds a new paste with the specified values

### Route
GET | POST: `/create`

### Form Body (POST)
- title (string): the title of the new paste
- author (string): the author of the new paste
- content (string): the content of the new paste
- unlisted (string): "on" if the checkbox was selected to hide the paste from the public viewing page

### Returns (GET)
- Template: `create.html`

### Returns (POST)
- Redirect: `/view/<viewId>?editId=<editId>` where viewId and editId are values of the newly created paste

---
## edit_page()

On a GET request, this displays a form for editing a paste. On a POST request, this edits the paste given the specified values.

### Route
GET | POST: `/edit/<edit_id>`

### URL Variables (GET | POST)
- edit_id: the editing ID of the record to edit

### Form Body (POST)
- title (string): the new title of the paste
- author (string): the new author paste
- content (string): the new content paste
- unlisted (string): "on" if the checkbox was selected to hide the paste from the public viewing page

### Returns (GET)
- Template: `edit.html`
- Context:
    - formatter (function): the timestamp formatting utility function
    - paste (dict): the paste which will populate the default values of the form fields

### Returns (POST)
- Redirect: `/view/<viewId>?editId=<editId>` where viewId and editId are values of the newly edited paste

---
## delete_action()

A post-only function that the delete button submits to. This will delete a record.

### Route
POST: `/delete/<edit_id>`

### Query Params (POST)
- edit_id: the editing ID of the record to delete

### Returns (POST)
- Template: `status.html`
- Context:
    - status (int): 200
    - message (string): a message indicating successful deletion

# Default Error Handlers

## 404

Called when a user requests a page that does not exist.

### Returns
- Template: `status.html`
- Context:
    - status (int): 404
    - message (string): "Page Not Found"

---
## 500

Called when an uncaught internal server error occurs.

### Returns
- Template: `status.html`
- Context:
    - status (int): 500
    - message (string): "Internal Server Error"


# Helper functions

## formatter(timestamp)

Helper method that converts a UTC timestamp (seconds since the epoch) into a human-readable string.

### Parameters
- timestamp (float): the timestamp to format, in seconds

### Returns
- (string): A formatted timestamp, or an empty string if the value for timestamp is NoneType
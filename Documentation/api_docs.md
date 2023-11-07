# Azure API Documentation

This documentation outlines the request type, parameters, responses, and possible errors for all Azure API endpoints.

Required parameters are indicated with a star (*). Errors are returned like this:
```json
{
    "error": "This is the error message"
}
```

---

## CreateRecord

### Accepts:
- POST
- JSON body

### Parameters
- **title*** (string): the title of the new paste
- **author*** (string) : the author of the new paste
- **content*** (string): the content of the paste
- **unlisted*** (boolean): whether to exclude from all-record reads (like on the public record list page)

### Reponses
- **message** (string): success message
- **viewId** (string): ID to use to view the paste
- **editId** (string): ID to use to edit the paste

### Errors
- **400**: Missing request body
    - Azure was unable to get the JSON request body
- **400**: Missing parameters
    - Title, author, content, or unlisted were not in the request body
- **500**: Failed to insert record
    - Something went wrong with the database create action


### Example
Sample Successful Request:
```json
{
	"title": "New Snippet",
	"author": "Group B",
	"content": "Hello World!",
	"unlisted": false
}
```
Sample Successful Response:
```json
{
	"message": "Inserted record successfully.",
	"viewId": "e5d4c5ac-6213-4ba4-bb28-ca465a17b9fd",
	"editId": "d1c827b8-1342-4367-9cde-6e4fc273c6ff"
}
```

---

## ReadRecord

### Accepts:
- GET
- URL Parameters

### Parameters
One type of ID is required for a single record retrival. No URL parameters will return all records.
- **viewId** (string): viewing ID that corresponds to the desired record
- **editId** (string): editing ID that corresponds to the desired record

### Reponses
Single record will be a single object. Multiple records will be a list of objects.
- **message** (string): success message
- **_id** (ObjectID): MongoDB object ID
- **title** (string): title of the paste
- **author** (string): author of the paste
- **content** (string): content of the paste
- **unlisted** (boolean): whether or not the paste is excluded from all-record reads
- **viewId** (string): viewing ID of the paste
- **editId**** (string): editing ID of the paste
- **createdAt** (float): UTC timestamp of paste creation
- **editedAt** (float): UTC timestamp of laste paste edit
- **viewCount** (int): times the paste was viewed (as an individual record)

**Note: editId field will not be present if the record was not retrived using editId

### Errors
- **404**: Paste with given view ID not found.
    - A viewing ID was used to find a paste, but no paste has that viewing ID.
- **404**: Paste with given edit ID not found.
    - An editing ID was used to find a paste, but no paste has that editing ID.
- **404**: No pastes have been made yet!
    - All pastes were searched for, but none were found.


### Example
Sample Successful Request:
```
/ReadRecord?viewId=e5d4c5ac-6213-4ba4-bb28-ca465a17b9fd
```
Sample Successful Response:
```json
{
	"_id": {
		"$oid": "63955a76b977b0cadfbda8be"
	},
	"title": "New Snippet",
	"author": "Group B",
	"content": "Hello World!",
	"unlisted": false,
	"viewId": "e5d4c5ac-6213-4ba4-bb28-ca465a17b9fd",
	"createdAt": 1670732406.1382241,
	"editedAt": 1670732406.1382241,
	"viewCount": 0
}
```

---

## UpdateRecord

### Accepts:
- PUT
- JSON body

### Parameters
- **editId*** (string): editing ID of the paste to update
- **title** (string): new title of the new paste
- **author** (string) : new author of the new paste
- **content** (string): new content of the paste
- **unlisted** (boolean): new unlisted status for the paste

### Reponses
- **message** (string): success message

### Errors
- **400**: Missing request body
    - Azure was unable to get the JSON request body
- **400**: Missing editing ID of paste to update.
    - No editing ID was provided in the request body
- **404**: No records updated. Edit ID does not exist.
    - There is no record with the corresponding editing ID
- **500**: Failed to update record.
    - Something went wrong with the database update action

### Example
Sample Successful Request:
```json
{
	"editId": "d1c827b8-1342-4367-9cde-6e4fc273c6ff",
	"title": "New Title"
}
```
Sample Successful Response:
```json
{
	"message": "Updated record successfully."
}
```

---

## Delete Record

### Accepts:
- DELETE
- JSON body

### Parameters
- **editId*** (string): editing ID of the paste to delete

### Reponses
- **message** (string): success message

### Errors
- **400**: Missing request body
    - Azure was unable to get the JSON request body
- **400**: Missing editing ID of paste to delete.
    - No editing ID was provided in the request body
- **404**: No records deleted. Edit ID does not exist.
    - There is no record with the corresponding editing ID
- **500**: Failed to delete paste.
    - Something went wrong with the database delete action

### Example
Sample Successful Request:
```json
{
	"editId":"d1c827b8-1342-4367-9cde-6e4fc273c6ff"
}
```
Sample Successful Response:
```json
{
	"message": "Successfully deleted paste."
}
```
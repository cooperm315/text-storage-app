# Data Service Documentation

This is documentation for parameters and return values for all MongoDB/Python functions used in `data_service.py` (the database controller script)

---
## initialize()

Establish a connection to MongoDB and set the global collection variable

### Parameters
None

### Returns
- (boolean): whether the initialization was successful

---
## reset()

Reset the collection

### Parameters
None

### Returns
- (boolean): whether the reset was succesful

---
## create(data)

Insert a record

### Parameters
- data (dict): a python dict where each key/value is a field to add to the record

### Returns
- (ObjectId | None): insert object ID for successful insertion, otherwise None

---
## read(query, one)

Read one or more records

### Parameters
- query (dict): a python dict of which keys/values the targeted records must have
- one (boolean): whether to only read a single record

### Returns
- (list | dict): either a list of matching records or a single record, depending on the value of the one param


---
## update(query, data)

Update a record

### Parameters
- query (dict): a python dict of which keys/values the targeted records must have
- data (dict): a python dict of key/value pairs that will be replaced in the targeted records

### Returns 
- (int) the number of record modified by this action, or -1 on failure


--- 
## delete(query)

Delete record(s)

### Parameters
- query (dict): a python dict of which keys/values the targeted records must have

### Returns
- (int) the number of record modified by this action, or -1 on failure

---
## incViewCount(query)

Increase the view count of a record by one

### Parameters
- query (dict): a python dict of which keys/values the targeted records must have

### Returns
- (boolean): whether the view count was successfully updated
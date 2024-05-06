# FastAPI
This is a FastAPI Tutorials

**Video_1.py**
- create 3 bastic endpoints.
- run server using uvicorn.
- explore swagger UI.
---
**Video_2.py**
- create path parameter endpoint.
- define its datatype.
- order of endpoints (static then dynamic).
---
**Video_3.py**
- create query parameter endpoint.
- difference between path and query parameter.
- make query parameter required.
---
**Video_4.py**
- create from body parameter endpoint.
- using pydantic model or dict.
---
**Video_5.py**
- query parameter validation.
- make the parameter required or not.
- tried these validations (default value, min_length, max_length, regex, title, description, deprecated, alias, include_in_schema).
- multiple values.
---
**Video_6.py**
- path parameter validation.
- make the parameter required or not.
- tried these validations (default value, ge, gt, lt, le).
- non-default argument after default argument.
---
**Video_7.py**
- create multiple body parameters.
- using embed in single body parameter.
---
**Video_8.py**
- the Field function is used to customize and add metadata to fields of models.
- the field validation appear in swagger docs in schema part.
---
**Video_9.py**
- create nested models.
- using HttpUrl function to validate an url link.
- try out different nested models eg. list[Image], dict[int, Image], Offer.
---
**Video_10.py**
- create example value for attribute of body parameter.
- method 1 using Config class in origin class.
- method 2 using example for each attribute from Field function.
- method 3 using example in body function.
---
**Video_11.py**
- try out different datatype as UUID, Datetime, deltatime.
---
**Video_12.py**
- using cookie and header to retrive data.
---
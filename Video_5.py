import uvicorn

from fastapi import FastAPI, Query

app = FastAPI()

# using Query to add validation on the string query parameter.
# None ---> as default value when means that this parameter is not required.
# ... or leave it emply ---> which means that this parameter is required.
# Query(), Query(...) 
# min_length, max_length, regex (to follow certain pattern), title, description, deprecated
# alias --> change the name of query parameter in url only not in code.
@app.get("/items/")
async def items(q: str = Query("111Hello", 
                                min_length=3, 
                                max_length=10,
                                regex="\d{3}.+",
                                title="This Query Validation Endpoint",
                                description="we use this endpoint to test string validation of query parameter.",
                                deprecated=True,
                                alias="query-search")):
    
    results = {"Items": [{"1": "Personal Computer"}, {"2": "PlayStation 5"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/lists")
async def items_list(q: list[str] = Query(["foo", "boo"])):
    
    results = {"Items": [{"1": "Personal Computer"}, {"2": "PlayStation 5"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/hidden_query")
async def hidden_query_route(q: str = Query(None, include_in_schema=False)):
    if q:
        return {"q": q}
    return {"q": "Not Found"}


if __name__ == "__main__":
    uvicorn.run("Video_5:app", host="127.0.0.1", port=8000, reload=True)
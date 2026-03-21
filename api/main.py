from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

from search.search_client import get_index

app = FastAPI(title="Personal Library Search API")
index = get_index()


@app.get("/")
def root():
    return {"message": "Personal Library Search API is running"}


@app.get("/search")
def search(q: str = Query(..., min_length=1)):
    try:
        results = index.search(q)

        hits = []
        for hit in results.get("hits", []):
            hits.append({
                "title": hit.get("title"),
                "path": hit.get("path"),
                "url": hit.get("url"),
            })

        return {
            "query": q,
            "count": len(hits),
            "results": hits,
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
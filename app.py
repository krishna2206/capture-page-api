from fastapi import FastAPI, Request, Response

from webpagecapture import test_webpage

webserver = FastAPI()


@webserver.post("/")
async def root(request: Request):
    if request.headers.get("Content-Type") == "application/json":
        json_payload = await request.json()
        page_url = json_payload.get("page_url")

        if page_url is not None:
            response_content = await test_webpage(page_url)
            return Response(
                status_code=200,
                content=response_content)
        return Response(
            status_code=400,
            headers={"Content-Type": "application/json"},
            content='{"error": "page_url is required"}')
    return Response(
        status_code=400,
        headers={"Content-Type": "application/json"},
        content='{"error": "Invalid request"}')

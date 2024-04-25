from fastapi import FastAPI
from presentation.routers import main_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from presentation.constants import UPROCESSABLE
import uvicorn

app = FastAPI()
app.include_router(main_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(UPROCESSABLE, status_code=200)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
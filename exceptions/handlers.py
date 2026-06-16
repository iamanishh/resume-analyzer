from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from utils.logger import logger

def register_exception_handlers(app: FastAPI):

    @app.exception_handler(Exception)
    async def global_exception_handler(
            request: Request,
            exc: Exception
    ):
        logger.exception(f"Unhandled exception occurred")

        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "message": "Something went wrong."
            }
        )



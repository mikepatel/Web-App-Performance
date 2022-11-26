################################################################################
# Imports
from fastapi import FastAPI


################################################################################
# FastAPI app
app = FastAPI()


@app.get("/data")
async def get_data():
    data = {
        "Message": "This is the message"
    }
    return data


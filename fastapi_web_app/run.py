################################################################################
# Imports
from fastapi import FastAPI


################################################################################
# FastAPI app
app = FastAPI()


@app.get("/data")
async def get_data():
    data = _helper()
    return data


################################################################################
# Helper function
def _helper():
    output = []
    for i in range(100000):
        output.append({"Index": i, "Value": i*i})

    return output


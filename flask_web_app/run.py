################################################################################
# Imports
from flask import Flask


################################################################################
# Flask app
app = Flask(__name__)


@app.route("/data", methods=["GET"])
def get_data():
    data = _helper()
    return data


################################################################################
# Helper function
def _helper():
    output = []
    for i in range(100000):
        output.append({"Index": i, "Value": i*i})

    return output


################################################################################
# Main
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

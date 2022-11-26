################################################################################
# Imports
from flask import Flask


################################################################################
# Flask app
app = Flask(__name__)


@app.route("/data", methods=["GET"])
def get_data():
    data = {
        "Message": "This is the message."
    }
    return data


################################################################################
# Main
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

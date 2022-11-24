################################################################################
# Imports
from flask import Flask


################################################################################
# Flask app
app = Flask(__name__)


@app.route("/get", methods=["GET"])
def get_data():
    data = {

    }
    return data


################################################################################
# Main
if __name__ == "__main__":
    app.run(host="localhost", debug=True)

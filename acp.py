from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    difference = None

    if request.method == "POST":
        date1 = request.form["date1"]
        date2 = request.form["date2"]

        date1 = datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.strptime(date2, "%Y-%m-%d")

        difference = abs((date2 - date1).days)

    return render_template("acp.html", difference=difference)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
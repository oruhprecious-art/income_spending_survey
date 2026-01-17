from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import csv
from models.user import User

app = Flask("Income Spending Survey")

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["users"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = User(
            age=request.form["age"],
            gender=request.form["gender"],
            income=request.form["income"],
            utilities=request.form.get("utilities", 0),
            entertainment=request.form.get("entertainment", 0),
            school_fees=request.form.get("school_fees", 0),
            shopping=request.form.get("shopping", 0),
            healthcare=request.form.get("healthcare", 0),
        )

        # MongoDB disabled for now
        # collection.insert_one(user.to_dict())

        save_to_csv(user)

        return redirect("/")

    return render_template("index.html")

def save_to_csv(user):
    with open("data/users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(user.to_list())

if __name__ == "__main__":
    app.run(debug=True)


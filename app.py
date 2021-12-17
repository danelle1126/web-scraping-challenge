from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.marsData.find_one()
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape():
    marsTable = mongo.db.marsData
    mongo.db.marsData.drop()
    mars_data = scrape_mars.scrape_all()
    marsTable.insert_one(mars_data)
    return redirect("/")

if __name__ == "__main__":
    app.run()
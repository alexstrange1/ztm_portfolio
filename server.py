from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<file>")
def page(file):
    if file[-5:] == ".html":
        file = file[:-5]
    if str(file) == "index":
        return render_template("index.html")
    elif str(file) not in ["about","components","contact","thankyou","work","works"]:
        return "Page requested doesn't exist"
    else:
        return render_template(f"{file}.html")

def dump(data):
    with open("db.csv", "a", newline="") as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route("/submit_form", methods=["POST","GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            dump(data)
            return redirect("thankyou.html")
        except:
            return "Something went wrong. Try again later"
    else:
        return "Something went wrong. Try again later"
from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    email = request.form.get("email_address")
    return render_template("success.html", user_email=email)

if __name__=="__main__":
    app.run(debug=True)
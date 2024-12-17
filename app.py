from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Save text in memory (persistent during the session)
saved_text = ""

@app.route("/", methods=["GET", "POST"])
def home():
    global saved_text
    if request.method == "POST":
        saved_text = request.form["note"]
        return redirect(url_for("home"))
    return render_template("index.html", saved_text=saved_text)

if __name__ == "__main__":
    app.run(debug=True)

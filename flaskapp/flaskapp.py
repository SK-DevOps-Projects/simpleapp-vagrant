from flask import Flask, render_template

app = Flask(__name__)

# Dictionary with the corresponding string that needs to be displayed for each path
app_redirect = {
    "check.txt":"Its working!!!",
    "404": "Not Found",
    "403": "Forbidden",
    "500": "Application error",
    "502": "Bad Gateway"
}

# To capture the base url
@app.route('/', defaults={'var': ''})

# To capture all the other URL paths navigated by user
@app.route("/<path:var>/")
# Function to process the path navigated by user
def show_page(var):
    # Getting the values from dictionary for the path and if not in dictionary then return empty string
    app_redirect_value = app_redirect.get(var, "")
    if app_redirect_value != "":
        if var != "check.txt":
            return render_template("index.html", display_text=app_redirect_value), var 
    return render_template("index.html", display_text=app_redirect_value)
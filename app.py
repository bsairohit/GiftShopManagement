from flask import Flask,render_template
app=Flask(__name__)#creating flask class obj

@app.route("/")
def main():
    return render_template("index.html")
@app.route("/demo")
def demo():
    return "Demo Page"
@app.route("/admin")
def admin():
    return "Admin Page"
@app.route("/user/<name>")
def user(name):
    return "Hello %s" %name
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/customer")
def customer():
    return render_template("customer.html")
@app.route("/shopowner")
def shopowner():
    return render_template("shopowner.html")
@app.route("/stockmanager")
def stockmanager():
    return render_template("stockmanager.html")



if __name__=='__main__':
    app.run(debug=True)

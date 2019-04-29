from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./home.html') 

@app.route('/contact2')
def contact():
    return render_template('/contact2.html')
@app.route('/about')
def about():
    return render_template("./about.html")
@app.route('/terms')
def terms():
    return render_template("./terms.html")

@app.route('/policy')
def policy():
    return render_template("./policy.html")

@app.route('/faqs')
def faqs():
    return render_template("./faqs.html")

@app.route('/work')
def work():
    return render_template("./work2.html")

@app.route('/projects2')
def projects2():
    return render_template("./projects2.html")

@app.route('/fellowship')
def fellowship():
    return render_template("./fellowship.html")
@app.route('/services')
def services():
    return render_template("./services.html")

if __name__ == "__main__":
    app.run()
    
    #python -m flask run --host=0.0.0.0
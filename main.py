from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/post')
def test():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)

#THINKING NOTES#
# Add an <a> before the <img> to link outside of the website. 
# Think about adding a cell posty thing for each thing in the repository?
# Look up SQL Alchemy again. Work on that.
from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /caleb path to render caleb.html
@app_projects.route('/toby/')
def toby():
    return render_template("toby.html")

# connects /caleb path to render caleb.html
@app_projects.route('/caleb/')
def caleb():
    return render_template("caleb.html")

@app_projects.route('/gene/')
def gene():
    return render_template("gene.html")

@app_projects.route('/nathan/')
def nathan():
    return render_template("nathan.html")
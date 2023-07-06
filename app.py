from flask import Flask, render_template, request, redirect, url_for
from locations import Locations
from forms import AddLocationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_PROJECT'

visit = Locations()
categories = {"recommended": "Recommended", "tovisit": "Places To Go", "visited": "Visited!!!", }

UP_ACTION = "\u2197"
DEL_ACTION = "X"

@app.route("/<category>", methods=["GET", "POST"])
def locations(category):
    locations = visit.get_list_by_category(category)
    ## Check the request for form data and process
    if request.method == "POST":
        [(name, action)] = request.form.items()

        if action == UP_ACTION:
            visit.moveup(name)
        elif action == DEL_ACTION:
            visit.delete(name)
    return render_template('locations.html', template_category=category, template_categories=categories, template_locations=locations, add_location=AddLocationForm())

@app.route("/add_location", methods=["POST"])
def add_location():
    add_location = AddLocationForm()

    if add_location.validate_on_submit:
        name = add_location.name.data
        description  = add_location.description.data
        category = add_location.category.data
        visit.add(name, description, category)
    # else:
        # category = "recommended"

    ## Redirect to locations route function
    return redirect(url_for("locations", category=category, _external=True, _scheme='https'))

@app.route("/")
def index():
    ## Redirect to locations route function
    return redirect(url_for("locations", category="recommended", _external=True, _schema='https'))
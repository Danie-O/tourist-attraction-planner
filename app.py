from flask import Flask, render_template, request, redirect, url_for
from locations import Locations

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
  return render_template('locations.html', template_category=category, template_categories=categories, template_locations=locations)

@app.route("/add_location", methods=["POST"])
def add_location():
  ## Validate and collect the form data

  if True:
      name=None
      description=None
      category=None
      visit.add(name, description, category)

  ## Redirect to locations route function
  return ""

@app.route("/")
def index():

  ## Redirect to locations route function
  return redirect(url_for('locations', category="recommended", _external=True, _schema='https'))
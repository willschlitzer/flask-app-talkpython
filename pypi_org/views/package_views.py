import flask

import pypi_org.services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

# Takes the package_name as a variable
@blueprint.route("/project/<package_name>")
def package_details(package_name: str):
    #return flask.render_template("packages/details.html", packages="Package details for {}".format(package_name))
    return "Package details for {}".format(package_name)

# Using the "int:" sets a specific type of input for the function
@blueprint.route("/<int:rank>")
def popular(rank: int):
    #return flask.render_template("packages/details.html", packages="Package details for {}".format(package_name))
    return "The details for the {}th most popular package".format(rank)
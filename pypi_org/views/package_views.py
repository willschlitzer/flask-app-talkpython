import flask
import pypi_org.services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
def index(package_name: str):
    test_packages = package_service.get_latest_packages()
    #return flask.render_template('packages/details.html', "Package details for {}".format(package_name))
    return "Package details for {}".format(package_name)
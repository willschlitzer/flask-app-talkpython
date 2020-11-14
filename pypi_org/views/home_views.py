import flask

import pypi_org.services.package_service as package_service
import pypi_org.services.user_service as user_service


blueprint = flask.Blueprint('home', __name__, template_folder='templates')

@blueprint.route("/")
def index():
    test_packages = package_service.get_latest_packages()
    return flask.render_template("home/index.html",
                                 packages=test_packages,
                                 package_count=package_service.get_package_count(),
                                 release_count=package_service.get_release_count(),
                                 user_count=user_service.get_user_count())

#user_service.get_user_count()


@blueprint.route("/about")
def about():
    return flask.render_template("home/about.html")
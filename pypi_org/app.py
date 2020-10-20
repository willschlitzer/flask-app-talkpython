import flask

app = flask.Flask(__name__)
import pypi_org.services.package_service as package_service


@app.route("/")
def index():
    test_packages = package_service.get_latest_packages()
    return flask.render_template("home/index.html", packages=test_packages)


@app.route("/about")
def about():
    return flask.render_template("home/about.html")


if __name__ == "__main__":
    app.run(debug=True)

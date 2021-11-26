from flask import Blueprint, render_template

homepage_blueprint = Blueprint('homepage', __name__)


@homepage_blueprint.route('/', methods=['GET'])
def homepage():
    """
    Route to render the homepage page
    """

    return render_template('/homepage/homepage.html')

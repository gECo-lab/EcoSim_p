from flask import Blueprint, render_template

homepageSimulation_blueprint = Blueprint('homepageSimulation', __name__)


@homepageSimulation_blueprint.route('/', methods=['GET'])
def homepageSimulation():
    """
    Route to render the homepage page
    """

    return render_template('/homepage/homepageSimulation.html')
from flask import Blueprint, render_template

homepage_blueprint = Blueprint('homepage', __name__)


@homepage_blueprint.route('/', methods=['GET'])
def selectModel():
    """
    Route to render the *selectModel* page
    """

    return render_template('/pages/homepage/subpages/selectModel.html')

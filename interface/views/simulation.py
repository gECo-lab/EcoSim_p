from flask import Blueprint, request
from common.utils import get_csv_result_paths
from common.utils import execute_selected_simulation
from common.utils import write_simulation_results_in_results_html
from common.utils import generate_zip_csv_result


simulation_blueprint = Blueprint('simulation', __name__)


@simulation_blueprint.route("/execution", methods=['POST'])
def execution():
    """
    Execute the simulation
    """

    if request.method == 'POST':

        model = request.form['model']

        older_csv_files_paths = get_csv_result_paths(model)

        execute_selected_simulation(model)

        write_simulation_results_in_results_html(model)

        generate_zip_csv_result(model, older_csv_files_paths)

    return ('', 204)

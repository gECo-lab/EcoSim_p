import os
import shutil


def execute_selected_simulation(model: str) -> None:
    """
    Execute the simulation by executing the .sh of the model
    """

    cwd = os.getcwd()

    folders = ["examples", "models"]

    root_path = os.sep.join(os.getcwd().split(os.sep)[:-1])

    paths = map(lambda folder: os.path.join(root_path, folder), folders)

    path = next(filter(lambda path: model in os.listdir(path), paths), None)

    path_model = os.path.join(path, model)

    sh_file = next(filter(
        lambda file: ".sh" in file, os.listdir(path_model)), None)

    os.chdir(path_model)

    os.system(f'./{sh_file}')

    os.chdir(cwd)


def write_simulation_results_in_results_html(model: str) -> None:
    """
    Copy the html data visualization of the model to pages/result/result.html
    """

    path_interface = os.getcwd()

    folders = ["examples", "models"]

    root_path = os.sep.join(os.getcwd().split(os.sep)[:-1])

    paths = map(lambda folder: os.path.join(root_path, folder), folders)

    path = next(filter(lambda path: model in os.listdir(path), paths), None)

    path_model_results = os.path.join(path, model, "results")

    html_results_file = next(filter(
        lambda file: ".html" in file, os.listdir(path_model_results)), None)

    path_html_results_ecos_file = os.path.join(
        path_model_results, html_results_file)

    path_html_results_web_file = os.path.join(
        path_interface, 'pages', 'results', 'results.html')

    with open(path_html_results_ecos_file, 'r') as f_html_ecos:

        with open(path_html_results_web_file, 'w') as f_html_web:

            f_html_web.writelines(f_html_ecos.readlines())


def get_csv_result_paths(model: str) -> list:
    """
    Return a List of csv result paths
    """

    folders = ["examples", "models"]

    root_path = os.sep.join(os.getcwd().split(os.sep)[:-1])

    paths = map(lambda folder: os.path.join(root_path, folder), folders)

    path = next(filter(lambda path: model in os.listdir(path), paths), None)

    path_model_runs = os.path.join(path, model, "runs")

    csv_result_files = list(filter(
        lambda file: ".csv" in file, os.listdir(path_model_runs)))

    paths_csvs = list(map(
        lambda file: os.path.join(path_model_runs, file), csv_result_files))

    return paths_csvs


def generate_zip_csv_result(model: str, older_csv_files_paths: str) -> None:
    """
    Get and compress CSV result files
    """

    path_interface = os.getcwd()

    path_files = os.path.join(path_interface, 'files')

    # Delete older result files

    os.system(f'rm {path_files}/*.csv')

    os.system(f'rm {path_files}/*.zip')

    # copy csv files to interface/files

    older_and_new_csv_files_paths_together = get_csv_result_paths(model)

    paths_csvs = filter(
        lambda file: file not in older_csv_files_paths,
        older_and_new_csv_files_paths_together)

    for path_csv in paths_csvs:

        file_csv = path_csv.split('/')[-1]

        new_path_csv = os.path.join(path_files, file_csv)

        shutil.copy(path_csv, new_path_csv)

    # write zip file form interface/files

    path_zip = os.path.join(path_files, 'result.zip')

    os.system(f'zip -r {path_zip} {path_files}')

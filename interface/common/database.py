import os
# import json
# import redis
from typing import Dict, List, Any


class Database:
    """
    Colections of methods to initializate and
    access in memory Database
    """

    # Redis
    # r = redis.Redis(host='localhost', port=6379, db=0)
    parameters: Dict = {}

    files: Dict = {}

    ##############
    # Model List #
    ##############
    @classmethod
    def _initialize_example_and_model_files(cls) -> None:

        example_and_model_files: List[str] = []

        path_examples = os.path.join(os.sep.join(
            os.getcwd().split(os.sep)[:-1]), 'examples')

        path_models: str = os.path.join(os.sep.join(
            os.getcwd().split(os.sep)[:-1]), 'models')

        example_and_model_files.extend(os.listdir(path_examples))

        example_and_model_files.extend(os.listdir(path_models))

        list_models = sorted(list(set(filter(
            lambda file: '__' not in file, example_and_model_files))))

        # Redis
        # Database.r.set("models", json.dumps(list_models))
        Database.parameters['models'] = list_models

    #################
    # Zip file path #
    #################
    @classmethod
    def _initialize_files(cls) -> None:

        path_interface = os.getcwd()

        path_files = os.path.join(path_interface, 'files')

        path_zip_result_file = os.path.join(path_files, 'result.zip')

        Database.files['path_zip_result'] = path_zip_result_file

    @staticmethod
    def initialize() -> None:
        """
        Initialize database
        Get examples from the examples directory
        Get models from the models directory
        Get path of zip, wich contains csv simulation results
        """
        Database._initialize_example_and_model_files()
        Database._initialize_files()

    @staticmethod
    def get(key: str) -> Dict:
        # Redis
        # return {key: json.loads(Database.r.get(key))}
        return {key: Database.parameters[key]}

    @staticmethod
    def set(key: str, value: Any) -> None:
        Database.parameters[key] = value
        return None

    @staticmethod
    def get_file(key: str) -> Dict:
        return {key: Database.files[key]}

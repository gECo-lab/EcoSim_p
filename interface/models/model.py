from dataclasses import dataclass

from models.abstract_data_model import AbstractDataModel
from common.database import Database


@dataclass
class Models(AbstractDataModel):
    """
    Access data (parameters) from implicit database
    Retrive data in a format to send to the interface (webpage)
    """

    def json(self):
        """
        Get examples from the examples directory
        Get models from the models directory
        """

        return Database.get_parameter("models")

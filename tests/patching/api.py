import json
from unittest.mock import patch, Mock
from pathlib import Path
from requests import Session
from pyawx import Client

BASE_PATH = Path(__file__).parents[1]


# @patch.object(Session, "get")
# @contextmanager
# def mock_get_results(json_data, mock_get):
#     mock_get.return_value = Mock(
#         status_code=200,
#         json=Mock(
#             return_value={
#                 "results": [json_data]
#             }
#         )
#     )
#     return


def get_api_client():
    with patch.object(Session, "get"):
        api = Client("https://", token="123")
    return api


def load_model(model):
    model_name = model.__name__.lower()
    with BASE_PATH.joinpath(f"mock_data/{model_name}.json").open("r") as model_fp:
        model_data = json.load(model_fp)
    return model_data

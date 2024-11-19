import unittest
from unittest.mock import Mock, patch

from requests import Session

from pyawx.models.projects import Project
from tests.patching.api import get_api_client, load_model


class TestApi(unittest.TestCase):
    def test_model_get(self):
        get_api_client()

        with patch.object(Session, "get") as mock_get:
            mock_model = load_model(Project)

            mock_get.return_value = Mock(
                status_code=200, json=Mock(return_value={"results": [mock_model]})
            )

            data = Project.get()
            project = data[0]

            self.assertIsInstance(project, Project)
            self.assertTrue(project.__internal__)


if __name__ == "__main__":
    unittest.main()

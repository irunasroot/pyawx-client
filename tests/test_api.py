import unittest
from unittest.mock import patch, Mock
from requests import Session

from tests.patching.api import get_api_client, load_model

from pyawx.models.projects import Project
from pyawx.actions import delete


class TestApi(unittest.TestCase):
    def test_api_client(self):
        api = get_api_client()

        with patch.object(Session, "get") as mock_get:
            mock_model = load_model(Project)

            mock_get.return_value = Mock(
                status_code=200,
                json=Mock(
                    return_value={
                        "results": [mock_model]
                    }
                )
            )

            data = api.get_data(Project)
            project = data[0]

            self.assertIsInstance(project, Project)
            self.assertTrue(project.__internal__)

        with patch.object(Session, "put") as mock_put:
            mock_put.return_value = Mock(
                status_code=200
            )

            project.name = "New Name"
            self.assertTrue(project.is_changed)

            api.add(project)
            api.commit()

            self.assertFalse(project.is_changed)
            self.assertEqual(len(api._write_back), 0)

        with patch.object(Session, "post") as mock_post:
            mock_post.return_value = Mock(
                status_code=200
            )
            new_project = Project()
            self.assertFalse(new_project.__internal__)

            api.add(new_project)
            api.commit()

        with patch.object(Session, "delete") as mock_delete:
            mock_delete.return_value = Mock(
                status_code=200
            )
            api.add(delete(new_project))
            self.assertTrue(new_project.is_deleted)
            api.commit()


if __name__ == "__main__":
    unittest.main()

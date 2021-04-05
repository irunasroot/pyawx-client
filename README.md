# pyawx-client
A python library for interacting with Ansible AWX instances

# Installation
You can install from pypi using pip
``bash
pip install pyawx-client
``

# Usage
AWX provides an API v2 for interacting with it. Most of the API is supported but keep in mind this is in alpha
and not everything will be built yet

The Client object sort of works in the idea of SQLAlchemy... at least for now.

Also, please be aware that models, or the python API could change since this project is still in Apha.

Get a list of Jobs
```python
from pyawx import Client
from pyawx.models.jobs import Job

client = Client("https://awx.mycompany.com", username="me", password="password")

jobs = client.get_data(Job)
```

Create a job template
```python
from pyawx import Client
from pyawx.models.jobs import JobTemplate

client = Client("https://awx.mycompany.com", username="me", password="password")

new_job = JobTemplate(name="My Job", description="Do some stuff", project=1)

client.add(new_job)
client.commit()
```

Delete a job template
```python
from pyawx import Client
from pyawx.actions import delete
from pyawx.models.jobs import JobTemplate

client = Client("https://awx.mycompany.com", username="me", password="password")

job_template = client.get_data(JobTemplate)[0]

delete(job_template)
client.add(job_template)
client.commit()
```

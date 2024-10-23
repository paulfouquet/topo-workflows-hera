from hera.shared import global_config
from hera.workflows import Container, Workflow

global_config.host = "http://localhost:2746"

with Workflow(generate_name="test-env-", entrypoint="env", namespace="argo") as w:
    Container(
        name="env",
        image="019359803926.dkr.ecr.ap-southeast-2.amazonaws.com/topo-imagery:latest",
        command=["env"],
    )

w.create()

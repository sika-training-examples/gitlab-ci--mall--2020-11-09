
import json

SERVICES = (
    "foo",
    "bar",
    "baz",
    "hello",
)

def make_service(name):
    return {
        "build %s" % name: {
            "stage": "build",
            "script":[
                "echo Build %s" % name,
            ]
        },
        "deploy %s" % name: {
            "stage": "deploy",
            "needs": ["build %s" % name]
            "script":[
                "echo Deploy %s" % name,
            ]
        }
    }

with open(".gitlab-ci.generated.yml", "w") as f:
    pipeline = {}
    pipeline.update({
        "stages": ["build", "deploy"]
    })
    for service in SERVICES:
        pipeline.update(make_service(service))
    f.write(json.dumps(pipeline))

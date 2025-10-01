import json
from judge.models import Judge

with open("/root/site/hvtham/judges.json") as f:
    judges = json.load(f)

for j in judges:
    obj, created = Judge.objects.get_or_create(
        name=j["id"],
        defaults={
            "auth_key": j["key"],
            "is_disabled": False,
        }
    )
    if created:
        print(f"Created judge {j['id']}")
    else:
        print(f"Judge {j['id']} already exists, updated key")
        obj.auth_key = j["key"]
        obj.save()

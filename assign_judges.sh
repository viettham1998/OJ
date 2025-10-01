#!/bin/bash
# assign_judges.sh

python3 manage.py shell -c "
from judge.models import Problem, Judge

judges = list(Judge.objects.all())

for p in Problem.objects.all():
    p.judges.set(judges)
    p.save()

print(f'Assigned {len(judges)} judges to {Problem.objects.count()} problems.')
"

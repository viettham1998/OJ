import os
import secrets
import json

output_dir = "/root/site/hvtham"
os.makedirs(output_dir, exist_ok=True)

judges_info = []

start_index = 6
end_index = 35  # 30 judges: fit06 -> fit35

for i in range(start_index, end_index + 1):
    judge_id = f"fit{i:02d}"
    key = secrets.token_hex(16)
    filename = os.path.join(output_dir, f"{judge_id}-02.yml")

    content = f"""id: "{judge_id}"
key: "{key}"
problem_storage_globs:
  - /problem_data/*
"""
    with open(filename, "w") as f:
        f.write(content)

    judges_info.append({"id": judge_id, "key": key})

# Lưu thông tin để import vào OJ host
with open(os.path.join(output_dir, "judges.json"), "w") as f:
    json.dump(judges_info, f, indent=2)

print(f"Generated {len(judges_info)} judge config files + judges.json")

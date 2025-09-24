"""
os.path.dirname(__file__) → folder containing the script
    __file__ → path of the current Python script
    # Suppose script is /home/user/project/src/main.py

os.path.join(os.path.dirname(__file__), '..')
    .. → parent directory
    Joins current directory + '..' → /home/user/project/src/..

os.path.abspath(...)
    Converts /home/user/project/src/.. → /home/user/project
"""

import requests
from pathlib import Path
import sys
import os

import json


# Append the root directory (D:\test) to sys.path
# sys.path.append(
#     os.path.abspath(
#         os.path.join(os.path.dirname(__file__), '..')
#     )
# )


sys.path.append(str(Path(__file__).resolve().parent.parent))

# Now we can import from tem.module.test
from tem.module.test import ReadClass


data = {"name": "Alice", "age": 25}

# Serialize
json_str = json.dumps(data)
print(json_str)

loaded = json.loads(json_str)
print(loaded)
#obj = ReadClass()
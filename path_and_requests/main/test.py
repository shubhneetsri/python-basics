import requests
import sys
import os

# Append the root directory (D:\test) to sys.path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

# Now we can import from tem.module.test
from tem.module.test import ReadClass

#obj = ReadClass()
import sys
import os
import importlib.util

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app_py_path = os.path.join(BASE_DIR, "app.py")

if os.path.exists(app_py_path):
    spec = importlib.util.spec_from_file_location("app_root_module", app_py_path)
    app_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app_module)
    for attr in dir(app_module):
        if not attr.startswith("__"):
            globals()[attr] = getattr(app_module, attr)
    app = app_module.app


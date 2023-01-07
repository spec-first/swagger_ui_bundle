from pathlib import Path

try:
    import importlib.resources as importlib_resources
except ImportError:  # < Python 3.9
    import importlib_resources as importlib_resources


swagger_ui_path: Path = importlib_resources.files("py-swagger-ui") / "vendor/swagger-ui-4.15.5"

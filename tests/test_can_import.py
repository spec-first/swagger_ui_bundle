

def test_import_ui():
    from py_swagger_ui import swagger_ui_path
    open(swagger_ui_path / "index.html")

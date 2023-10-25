

def test_import_ui():
    from swagger_ui_bundle import swagger_ui_path
    open(swagger_ui_path / "index.html")

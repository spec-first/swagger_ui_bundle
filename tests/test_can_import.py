
import pytest


def test_import_ui():
    from swagger_ui_bundle import swagger_ui_path
    open(swagger_ui_path + "/index.html")

def test_import_ui_v2():
    from swagger_ui_bundle import swagger_ui_2_path
    open(swagger_ui_2_path + "/index.html")

def test_import_ui_v3():
    from swagger_ui_bundle import swagger_ui_3_path
    open(swagger_ui_3_path + "/index.html")


def test_import_ui_v4():
    from swagger_ui_bundle import swagger_ui_4_path
    open(swagger_ui_4_path + "/index.html")

#!/usr/bin/env python

import os

__author__ = "Daniel Grossmann-Kavanagh"
__version__ = '0.0.9'


def get_path(rel):
    return os.path.join(
        os.path.abspath(os.path.dirname(os.path.realpath(__file__))), rel
    )


swagger_ui_3_52_0_path = get_path("vendor/swagger-ui-3.52.0")
swagger_ui_4_4_0_path = get_path("vendor/swagger-ui-4.4.0")

# latest major versions
swagger_ui_3_path = swagger_ui_3_52_0_path
swagger_ui_4_path = swagger_ui_4_4_0_path

# default to swagger 3
swagger_ui_path = swagger_ui_3_path

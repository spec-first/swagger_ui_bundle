#!/usr/bin/env python

import os

__author__ = "Daniel Grossmann-Kavanagh, Bartolomé Sánchez Salado"
__version__ = '0.0.2'


def get_path(rel):
    return os.path.join(
        os.path.abspath(os.path.dirname(os.path.realpath(__file__))), rel
    )


swagger_ui_4_14_0_path = get_path("vendor/swagger-ui-4.14.0")

# latest major versions
swagger_ui_4_path = swagger_ui_4_14_0_path

# default to swagger 4
swagger_ui_path = swagger_ui_4_path

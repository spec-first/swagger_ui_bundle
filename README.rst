swagger_ui_bundle
=================
This package contains the static files for swagger-ui as a python package.

Basic configuration options are templated with the Jinja2 templating language.

This package is intended to be webserver-agnostic, so it only includes the
static files, and some very basic configuration.

Getting Started
===============
You can import the swagger_ui_path from the swagger_ui_bundle package like so:

.. code-block:: python
  
    from swagger_ui_bundle import swagger_ui_path

    # or if you need a specific version
    from swagger_ui_bundle import swagger_ui_2_path
    from swagger_ui_bundle import swagger_ui_3_path

You can easily serve up this directory as all static files to get the default
swagger-ui distribution. Here's an example in flask:

.. code-block:: python

    from swagger_ui_bundle import swagger_ui_path
    
    from flask import Flask, Blueprint, send_from_directory, render_template
    
    swagger_bp = Blueprint(
        'swagger_ui',
        __name__,
        static_url_path='',
        static_folder=swagger_ui_path,
        template_folder=swagger_ui_path
    )
    
    app = Flask(__name__, static_url_path='')
    app.register_blueprint(swagger_bp, url_prefix='/ui')
    
    if __name__ == "__main__":
        app.run()

You may wish to override some of the configuration variables. Included
is a jinaj2 templated file where you can modify these parameters.
You can add another route to render this template with your
desired configuration like so:

.. code-block:: python

    SWAGGER_UI_CONFIG = {
        "openapi_spec_url": "https://petstore.swagger.io/v2/swagger.json"
    }

    @swagger_bp.route('/')
    def swagger_ui_index():
        return render_template('index.j2', **SWAGGER_UI_CONFIG)


Have a look at `example.py` for a complete server for the Flask webserver.


License
=================
Since this is just repackaging swagger-ui releases, the license comes from
the swagger ui project (https://github.com/swagger-api/swagger-ui).

All vendored code is published by SmartBear Software under the Apache 2.0
License.

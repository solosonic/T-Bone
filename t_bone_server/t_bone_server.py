from flask import Flask, render_template
import logging
import helpers
import json_config_file

app = Flask(__name__)
_logger = logging.getLogger(__name__)
#this is THE printer - just a dictionary with anything
_printer = None


@app.route('/')
def hello_world():
    template_dictionary = templating_defaults()
    return render_template("index.html", **template_dictionary)


def templating_defaults():
    return {
        'name': 'T-Bone',
    }


if __name__ == '__main__':
    #somehow we can get several initializations - hence we store a global printer
    try:
        if not _printer:
            _printer = helpers.create_printer()
            config = json_config_file.read()
            _printer.connect()
            _printer.configure(config)
        app.run(
            host='0.0.0.0',
            debug=True
        )
    finally:
        #reset the printer
        _printer = None
#!/bin/bash

set -e
export FLASK_APP=src:create_app
gunicorn -w 4 -b 0.0.0.0:${PORT:-8080} src:create_app &
python3 -m src

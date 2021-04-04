#!/bin/bash

export FLASK_APP=src/server.py
export FLASK_ENV=development

poetry run python src/server.py
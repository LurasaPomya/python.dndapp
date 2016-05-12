#!/bin/bash
#
# Simple init wrapper script for pydndapp
# By: James McGrew

cd /path/to/project/root
. /path/to/venv
gunicorn dndapp:app --pid ./dndapp.pid -b localhost:5001

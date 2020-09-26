#!/bin/bash

source venv/Scripts/activate

export FLASK_APP=main.py

flask test

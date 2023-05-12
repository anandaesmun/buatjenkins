#!/bin/bash

# export DJANGO_SETTINGS_MODULE=untuktesting.settings
pytest --junitxml=/testresults/out_report.xml

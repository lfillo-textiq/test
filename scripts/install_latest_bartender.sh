#!/bin/bash

source /usr/local/etc/secrets.config
export GITHUB_PAT=$GITHUB_PAT
python3 ./scripts/install_latest_bartender.py

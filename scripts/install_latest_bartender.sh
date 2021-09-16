#!/bin/bash

source /usr/local/etc/secrets.config
export GITHUB_PAT=$GITHUB_PAT
python3 /opt/textiq/config/scripts/bartender/install_latest_bartender.py

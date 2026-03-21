#!/bin/bash

cd /opt/personal-library || exit 1
sudo -u www-data /opt/personal-library/venv/bin/python3 -m indexer.index_documents
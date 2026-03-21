# Installation Guide

This document describes the setup process for the private knowledge library and search engine.

## Prerequisites

- Debian Linux
- Python 3
- Nextcloud already deployed
- Access to the Nextcloud data directory
- systemd

## Install Python Dependencies

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```
## Install Required Packages

```
pip install fastapi uvicorn meilisearch pdfminer.six
```

## Install Meilisearch

```
curl -L
https://install.meilisearch.com | sh sudo mv meilisearch /usr/local/bin/
```

**Run Meilisearch with a master key:**

```
meilisearch --master-key [YOU_MASTER_KEY]
```


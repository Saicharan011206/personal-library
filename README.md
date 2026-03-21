# Private Knowledge Library & Search Engine

<p align="center">
  <img src="https://img.shields.io/badge/status-active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/backend-FastAPI-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/search-Meilisearch-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/platform-Linux-important?style=for-the-badge">
  <img src="https://img.shields.io/badge/license-MIT-purple?style=for-the-badge">
</p>

---

## Overview

Have you ever wondered if there’s an alternative to paying cloud providers to store and search your files?

That old laptop collecting dust can become your own **private knowledge engine**.

This project builds a **self-hosted document search system** that indexes files stored in Nextcloud and enables fast, full-text search using Meilisearch — exposed through a FastAPI backend.

---

## Features

- Full-text search across PDFs, notes, and documents  
- Seamless integration with self-hosted Nextcloud  
- Sub-second search powered by Meilisearch  
- REST API using FastAPI  
- Direct links to open files inside Nextcloud  
- Fully self-hosted — no external dependencies  

---

## Architecture

```
Nextcloud Storage
      ↓
Document Scanner
      ↓
Text Extraction
      ↓
Meilisearch Index
      ↓
FastAPI Search API
      ↓
Client Search Requests
```

---

## Tech Stack

| Layer        | Technology        |
|-------------|------------------|
| Backend API  | FastAPI          |
| Search Engine| Meilisearch      |
| Processing   | pdfminer.six     |
| Runtime      | Python           |
| OS           | Debian Linux     |
| Storage      | Nextcloud        |

---

## Project Structure

```bash
.
├── api/
├── config/
├── indexer/
├── integration/
├── search/
├── scripts/
├── docs/
├── requirements.txt
├── README.md
└── LICENSE
```

---

## How It Works

- Documents are stored in Nextcloud

- Scanner detects files in selected folders

- Text is extracted from documents

- Content is indexed into Meilisearch

- FastAPI exposes a /search endpoint

- Results include direct Nextcloud links

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Future Improvements

- Automated indexing (cron jobs)

- Apache reverse proxy (/search)

- OCR support for scanned documents

- Lighweight frontend UI

---

## Documentation

Detailed documentation is available in [!docs/](docs/)

---

## Licensing

This project is licensed under the MIT License.

See [!License](LICENSE) for details.

---

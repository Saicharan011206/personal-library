# System Architecture

This project implements a private document search engine integrated with a self-hosted Nextcloud instance.

Documents stored in selected Nextcloud folders are scanned, processed, indexed into Meilisearch, and exposed through a FastAPI search API.

## High-Level Flow
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

## Core Components

### Nextcloud Storage

Documents are stored in the Nextcloud data directory:

`/storage/nextcloud-data/admin/files`

The search engine scans only selected folders such as:

- Books
- Docs
- Notes

### Scanner

The scanner walks through configured folders and detects supported files.

Supported formats:

- PDF
- TXT
- Markdown

### Text Extraction

PDF content is extracted using `pdfminer.six`.

Plain text and Markdown files are read directly from disk.

### Search Engine

Meilisearch stores indexed documents and provides fast full-text search.

Each indexed document stores:

- safe document ID
- file title
- extracted content
- original file path
- generated Nextcloud URL

### API Layer

FastAPI exposes the search functionality through HTTP endpoints.

Example endpoint:

`GET /search?q=debian`

### Nextcloud Integration

Search results include a generated Nextcloud URL so files can be opened directly from the Nextcloud web interface.

## Deployment Model

The project runs on a Debian server alongside Nextcloud.

Meilisearch and FastAPI are deployed as systemd services.
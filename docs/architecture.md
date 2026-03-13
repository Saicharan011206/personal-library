# System Architecture

The Private Knowledge Library indexes documents stored in a Nextcloud instance and provides full text-search capabilities.

## Components

### Nextcloud

Stores user documents including PDFs, ebooks, and text files.

### Indexer

Python-based service that scans configured Nextcloud folders, extracts document text, and sends data to the search index.

### Meilisearch

Full-text search engine responsible for indexing and retrieving documents.

### FastAPI

Provides a REST API interface for performing document searches.

## Workflow

- User uploads file -> Nextcloud storage
- Indexer scans configured folders
- Text extracted from documents
- Documents indexed into Meilisearch
- Search API returns results with links to open files in Nextcloud


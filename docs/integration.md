# Nextcloud Integration

This project is designed to work with a self-hosted Nextcloud instance.

## Storage Integration

Documents are read directly from the Nextcloud user files directory:

`/storage/nextcloud-data/admin/files`

Only selected folders are scanned.

This makes the search engine a companion service to Nextcloud rather than a separate storage system.

## Execution User

The indexer must run with access to Nextcloud-managed files.

In the deployed setup, indexing is executed through `www-data` because Nextcloud storage is owned and managed by the web server user.

Example:

```bash
sudo -u www-data /opt/personal-library/venv/bin/python3 -m indexer.index_documents
```
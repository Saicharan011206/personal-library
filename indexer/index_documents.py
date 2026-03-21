import hashlib
from pathlib import Path

from indexer.scanner import scan_documents
from indexer.extract_text import extract_document
from integration.nextcloud_links import generate_nextcloud_url
from search.search_client import get_index


def generate_safe_id(file_path: str) -> str:
    return hashlib.md5(file_path.encode("utf-8")).hexdigest()


def build_document(file_path: str):
    content = extract_document(file_path)

    if not content:
        return None

    return {
        "id": generate_safe_id(file_path),
        "title": Path(file_path).name,
        "content": content[:20000],
        "path": file_path,
        "url": generate_nextcloud_url(file_path),
    }


def main():
    index = get_index()
    files = scan_documents()
    documents = []

    print(f"Found {len(files)} files to index...\n")

    for i, file_path in enumerate(files, start=1):
        print(f"[{i}/{len(files)}] Processing: {file_path}")

        doc = build_document(file_path)

        if doc is None:
            print("  -> Skipping (no content)")
            continue

        documents.append(doc)

    if documents:
        print("\nUploading to Meilisearch...")
        task = index.add_documents(documents)
        print("Indexing task submitted!")
        print(task)
    else:
        print("No documents to index.")


if __name__ == "__main__":
    main()
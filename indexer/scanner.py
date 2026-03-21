import os
from config.settings import NEXTCLOUD_ROOT, INDEX_FOLDERS, SUPPORTED_EXTENSIONS


def scan_documents():
    documents = []

    for folder in INDEX_FOLDERS:
        folder_path = os.path.join(NEXTCLOUD_ROOT, folder)

        if not os.path.exists(folder_path):
            continue

        for root, _, files in os.walk(folder_path):
            for file in files:
                file_ext = os.path.splitext(file)[1].lower()

                if file_ext in SUPPORTED_EXTENSIONS:
                    full_path = os.path.join(root, file)
                    documents.append(full_path)

    return documents


if __name__ == "__main__":
    docs = scan_documents()

    for doc in docs:
        print(f"Found document: {doc}")
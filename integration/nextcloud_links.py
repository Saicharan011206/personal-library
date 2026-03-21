from config.settings import NEXTCLOUD_BASE_URL


def generate_nextcloud_url(file_path: str) -> str:
    relative_path = file_path.split("/files/")[-1]
    parts = relative_path.rsplit("/", 1)

    if len(parts) == 2:
        folder, filename = parts
    else:
        folder = ""
        filename = parts[0]

    return f"{NEXTCLOUD_BASE_URL}/apps/files/?dir=/{folder}&openfile={filename}"
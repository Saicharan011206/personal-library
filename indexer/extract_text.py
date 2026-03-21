from pathlib import Path
from pdfminer.high_level import extract_text


def extract_pdf(file_path: str) -> str:
    try:
        return extract_text(file_path).strip()
    except Exception as e:
        print(f"PDF extraction failed for {file_path}: {e}")
        return ""


def extract_plain_text(file_path: str) -> str:
    try:
        return Path(file_path).read_text(encoding="utf-8", errors="ignore").strip()
    except Exception as e:
        print(f"Text extraction failed for {file_path}: {e}")
        return ""


def extract_document(file_path: str) -> str:
    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":
        return extract_pdf(file_path)
    elif suffix in [".txt", ".md"]:
        return extract_plain_text(file_path)
    else:
        return ""


if __name__ == "__main__":
    sample_file = input("Enter file path: ").strip()
    content = extract_document(sample_file)

    print("\n--- Extracted Preview ---\n")
    print(content[:2000] if content else "No text extracted.")
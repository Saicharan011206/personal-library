import meilisearch
from config.settings import (
    MEILISEARCH_HOST,
    MEILISEARCH_MASTER_KEY,
    MEILISEARCH_INDEX,
)


def get_client():
    return meilisearch.Client(
        MEILISEARCH_HOST,
        MEILISEARCH_MASTER_KEY
    )


def get_index():
    client = get_client()
    return client.index(MEILISEARCH_INDEX)
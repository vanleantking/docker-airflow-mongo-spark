from pymongo import DeleteMany


def index_collection(collection, idx, name, is_unique=False, drop_if_exist=False):
    """
    index_report_date: create index for collection db
    Args:
        drop_if_exist:
        is_unique:
        collection:
        idx:
        name:

    Returns:

    """
    if drop_if_exist:
        collection.drop_index(index_or_name=name)

    return collection.create_index(idx, name=name, background=True, unique=is_unique)


def drop_indexes(collection):
    collection.drop_indexes()

from pymongo import DeleteMany, UpdateOne
from pkg.common.utils import batch_df


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


def upsert_df_into_db(collection, report_detail, filter_cl=None, chunk_size=1000):
    """
    upsert_df_into_db:
        separate large of dataframe into batch and insert multiple batches into mongodb
        use bulk_write to upsert bulk data
    Args:
        filter_cl:
        collection:
        report_detail:
        chunk_size:

    Returns:

    """

    for batch_report_detail in batch_df(report_detail):
        report_detail_docs = batch_report_detail.to_dict('records')
        len_report_detail_docs = len(report_detail_docs)
        bulk_write = []

        # prepare data on bulk_wite
        for x in report_detail_docs:
            it_filter = get_filter_item(x, filter_cl)
            it = UpdateOne(
                filter=it_filter,
                update={
                    '$set': x,
                },
                upsert=True)
            bulk_write.append(it)

        ran = range(len_report_detail_docs)
        steps = list(ran[chunk_size::chunk_size])
        steps.extend([len_report_detail_docs])

        # Insert chunks of the dataframe
        i = 0
        for j in steps:
            collection.bulk_write(bulk_write[i:j])  # fill de collection
            i = j

    print('Done')
    return


def get_filter_item(x, filter_cl=None):
    if filter_cl is None:
        raise Exception('specified at least one of type keys index for filter collection')
    filter_item = {}
    for k in filter_cl:
        filter_item[k] = x[k]
    return filter_item

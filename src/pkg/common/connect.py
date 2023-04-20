from pymongo import MongoClient


def connect_mongodb(dct):
    uri_link = "mongodb://" + dct["AdServerUserName"] + ":" + dct["AdServerPassword"] \
               + "@" + dct["AdServerHost"] + ":" + dct["AdServerPort"] + "/" + dct["AdServerDatabase"]
    print('uri_link, ', uri_link)
    return MongoClient(uri_link)


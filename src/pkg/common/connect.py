from pymongo import MongoClient


def connect_mongodb(dct):
    uri_link = "mongodb://" + dct["SpotifySongUserName"] + ":" + dct["SpotifySongPassword"] \
               + "@" + dct["SpotifySongHost"] + ":" + dct["SpotifySongPort"] + "/" + dct["SpotifySongDatabase"]
    print('uri_link, ', uri_link)
    return MongoClient(uri_link)


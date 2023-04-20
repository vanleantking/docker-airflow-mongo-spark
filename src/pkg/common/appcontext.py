class AppContext(object):
    def __init__(self, mysqldbs, mongodbs, logger, platform=None, args=None, api=None):
        self.args = args
        self.api = api
        self.mysqldbs = mysqldbs
        self.mongodbs = mongodbs
        self.logger = logger
        self.platform = platform

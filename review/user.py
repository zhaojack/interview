from attrdict import AttrDict


class User(object):

    def __init__(self, user_data):
        self.__dict__ = user_data
        self.address = AttrDict(self.address)
        self.company = AttrDict(self.company)
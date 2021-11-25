class Base(object):
    def update(self, params=None):
        if isinstance(params, dict):
            for item in params.items():
                setattr(self, item[0], item[1])
        return self.serialize()

    def serialize(self):
        return self.__dict__

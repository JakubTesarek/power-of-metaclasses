class Attribute:
    pass


class ModelMeta(type):
    def __new__(meta, name, bases, dct):
        return super().__new__(meta, name, bases, dct)


class Model(metaclass=ModelMeta):
    pass

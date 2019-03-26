class Attribute:
    def __init__(self, default=None, maximum=None):
        self.default = default
        self.maximum = maximum

    def get_setter(self, name):
        def setter(this, value):
            if self.maximum is not None and value > self.maximum:
                raise ValueError(f'{value} is larger than {self.maximum}')
            setattr(this, name, value)
        return setter

    def get_getter(self, name):
        def getter(this):
            return getattr(this, name, self.default)
        return getter


class ModelMeta(type):
    def __new__(meta, name, bases, dct):
        for key in list(dct):
            attr = dct[key]
            if isinstance(attr, Attribute):
                dct[f'set_{key}'] = attr.get_setter(key)
                dct[f'get_{key}'] = attr.get_getter(key)
                del dct[key]
        return super().__new__(meta, name, bases, dct)


class Model(metaclass=ModelMeta):
    pass

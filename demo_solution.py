""" Solution to problem presented in 'The Power of Metaclasses' presentation. """

class Attribute:
    """ Attribute generates methods that can be attached to another classes. """

    def __init__(self, default=None, maximum=None):
        """
        Args:
            default (float): default value for getter (is not validated)
            maximum (float): max value for setter
        """
        self.default = default
        self.maximum = maximum

    def get_setter(self, name):
        """ Creates valitading setter method.

        Args:
            name (str): Name of attribute to save the value to. This is
            provided to the setter via closure.

        Returns:
            func: Closured setter that validates max input value and sets it to
            provided object
        """
        def setter(this, value):
            """ Closured setter that validates max input

            Args:
                this (obj): Object this method is attached to after it's
                generated. NOT instance of Attribute.
                value (obj): Value to be set
            """
            if self.maximum is not None and value > self.maximum:
                raise ValueError(f'{value} is larger than {self.maximum}')
            setattr(this, name, value)
        return setter

    def get_getter(self, name):
        """ Creates getter method.

            Args:
                name (str): Name of the attribute to retrieve. This is provided
                to the getter via closure.

            Returns:
                func: Closured getter method
        """
        def getter(this):
            return getattr(this, name, self.default)
        return getter


class ModelMeta(type):
    """ Meta class generating model classes """

    def __new__(meta, name, bases, dct):
        """ Class generator
        Args:
            meta (type): Metaclass to create new class
            name (str): Name of newly created class
            bases (tuple of type): Tuple of base classes to inherit from
            dct (dict of str:obj): Dictionary with local attributes for newly
                created class. Can contain methods.

        Returns:
            type: New class object instance.
        """
        for key in list(dct):
            attr = dct[key]
            if isinstance(attr, Attribute):
                dct[f'set_{key}'] = attr.get_setter(key)
                dct[f'get_{key}'] = attr.get_getter(key)
                del dct[key]
        return super().__new__(meta, name, bases, dct)


class Model(metaclass=ModelMeta):
    """Base class for all model classes.

    Extending this class (or using it directly) saves us from having to use the
    `metaclass=ModelMeta` every time we construct new model class
    """
    pass

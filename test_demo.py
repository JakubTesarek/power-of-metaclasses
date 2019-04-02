""" Tests to problem presented in 'The Power of Metaclasses' presentation. """

import pytest
from demo import Model, Attribute

def test_attributes_removed():
    class Mock(Model):
        attr = Attribute()

    assert 'attr' not in dir(Mock)


def test_has_setter():
    class Mock(Model):
        attr = Attribute()

    assert 'set_attr' in dir(Mock)


def test_has_getter():
    class Mock(Model):
        attr = Attribute()

    assert 'get_attr' in dir(Mock)


def test_set_and_get_value():
    class Mock(Model):
        attr = Attribute()

    mock = Mock()
    mock.set_attr(42)
    assert mock.get_attr() == 42


def test_default_value():
    class Mock(Model):
        attr = Attribute(default=3.14)

    mock = Mock()
    assert mock.get_attr() == 3.14


def test_rewrite_default_value():
    class Mock(Model):
        attr = Attribute(default=3.14)

    mock = Mock()
    mock.set_attr(42)
    assert mock.get_attr() == 42


def test_exceeding_maximum_raises_exception():
    class Mock(Model):
        attr = Attribute(maximum=10)

    mock = Mock()
    with pytest.raises(ValueError):
        mock.set_attr(10000)


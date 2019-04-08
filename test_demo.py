""" Tests to problem presented in 'The Power of Metaclasses' presentation. """

import pytest
from demo import Model, IntegerAttribute

def test_attributes_removed():
    class Mock(Model):
        attr = IntegerAttribute()

    assert 'attr' not in dir(Mock)


def test_has_setter():
    class Mock(Model):
        attr = IntegerAttribute()

    assert 'set_attr' in dir(Mock)


def test_setter_is_callable():
    class Mock(Model):
        attr = IntegerAttribute()

    assert callable(Mock.set_attr)


def test_has_getter():
    class Mock(Model):
        attr = IntegerAttribute()

    assert 'get_attr' in dir(Mock)
    assert callable(Mock.get_attr)


def test_getter_is_callable():
    class Mock(Model):
        attr = IntegerAttribute()

    assert callable(Mock.get_attr)


def test_set_and_get_value():
    class Mock(Model):
        attr = IntegerAttribute()

    mock = Mock()
    mock.set_attr(42)
    assert mock.get_attr() == 42


def test_default_value():
    class Mock(Model):
        attr = IntegerAttribute(default=42)

    mock = Mock()
    assert mock.get_attr() == 42


def test_rewrite_default_value():
    class Mock(Model):
        attr = IntegerAttribute(default=42)

    mock = Mock()
    mock.set_attr(0)
    assert mock.get_attr() == 0


@pytest.mark.parametrize('invalid_argument', [
    (object()),
    ('string'),
    (['list']),
    (1.61803398875),
    (None)
])
def test_accept_only_integers(invalid_argument):
    class Mock(Model):
        attr = IntegerAttribute()

    mock = Mock()
    with pytest.raises(TypeError, match='is not of type int'):
        mock.set_attr(invalid_argument)


def test_exceeding_maximum_raises_exception():
    class Mock(Model):
        attr = IntegerAttribute(maximum=10)

    mock = Mock()
    with pytest.raises(ValueError):
        mock.set_attr(10000)


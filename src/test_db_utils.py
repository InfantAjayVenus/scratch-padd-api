from db_utils import add_pad

def test_add_pad():
    value = add_pad('Test', 'Content')
    assert type(value.id) == type(1)


import main
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 3), reason="do not run number add test")
def test_add():
    assert main.add(7, 3) == 10
    assert main.add(7) == 9
    print(main.add(7, 3), '-----------------------------------')


@pytest.mark.number
def test_product():
    assert main.product(5, 5) == 25
    assert main.product(5) == 10


@pytest.mark.string
def test_add_strings():
    result = main.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello ' in result


@pytest.mark.skip(reason="do not run number product test")
def test_product_strings():
    assert main.product('Hello ', 3) == 'Hello Hello Hello '
    result = main.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
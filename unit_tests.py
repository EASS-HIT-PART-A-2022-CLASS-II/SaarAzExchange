import pytest
import main

@pytest.mark.prod_exchange
def test_get_all_currency():
    list_from_main = main.get_all_currency()


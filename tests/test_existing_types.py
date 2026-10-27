from adapter_example.duck_client import DuckClient
from adapter_example.mallard_duck import MallardDuck
from adapter_example.wild_turkey import WildTurkey


def test_duck_client_works_with_duck_contract():
    sound, flights = DuckClient().test_duck(MallardDuck())
    assert sound == "quack"
    assert flights == ["fly"]


def test_turkey_has_useful_but_different_interface():
    turkey = WildTurkey()
    assert turkey.gobble() == "gobble"
    assert turkey.fly() == "short flight"

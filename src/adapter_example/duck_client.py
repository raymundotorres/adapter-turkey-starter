from .duck import Duck


class DuckClient:
    def test_duck(self, duck: Duck) -> tuple[str, list[str]]:
        return duck.quack(), duck.fly()

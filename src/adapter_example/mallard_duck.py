from .duck import Duck


class MallardDuck(Duck):
    def quack(self) -> str:
        return "quack"

    def fly(self) -> list[str]:
        return ["fly"]

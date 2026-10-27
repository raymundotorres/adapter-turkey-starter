from .turkey import Turkey


class WildTurkey(Turkey):
    def gobble(self) -> str:
        return "gobble"

    def fly(self) -> str:
        return "short flight"

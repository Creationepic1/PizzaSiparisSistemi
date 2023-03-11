from structures.decorators.base_decorator import Decorator


class Mushroom(Decorator):

    def __init__(self) -> None:
        super().__init__("Mantarlar", 20.10)
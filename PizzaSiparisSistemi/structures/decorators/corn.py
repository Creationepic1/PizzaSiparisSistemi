from structures.decorators.base_decorator import Decorator


class Corn(Decorator):

    def __init__(self) -> None:
        super().__init__("Mısır", 12.99)
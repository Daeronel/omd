class ComputerColor:
    def __str__(self) -> str:
        raise ValueError()

    def __repr__(self) -> str:
        pass

    def __eq__(self, o: object) -> bool:
        pass

    def __add__(self, other) -> "ComputerColor":
        pass

    def __mul__(self, other) -> "ComputerColor":
        pass

    def __rmul__(self, other) -> "ComputerColor":
        pass

    def __hash__(self, other) -> int:
        pass


class RGBColor(ComputerColor):
    END = "\033[0"
    START = "\033[1;38;2"
    MOD = "m"

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}"

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other, RGBColor):
            return False
        return (
                self.blue == other.blue
                and self.green == other.green
                and self.red == other.red
        )

    def __add__(self, other):
        if not isinstance(other, RGBColor):
            raise ValueError(f'Сложение {type(other)} и Color недопустимо')
        return RGBColor(min(self.red + other.red, 255), min(self.green + other.green, 255),
                        min(self.blue + other.blue, 255))

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, other):
        if not (0 <= other <= 1):
            raise ValueError(f'С должен лежать в интервале [0, 1]')
        cl = -256 * (1 - other)
        f = (259 * (cl + 255)) / (255 * (259 - cl))

        return RGBColor(int(f * (self.red - 128) + 128),
                        int(f * (self.green - 128) + 128),
                        int(f * (self.blue - 128) + 128))

    __rmul__ = __mul__


if __name__ == '__main__':
    random = RGBColor(100, 180, 132)
    print(random)
    red = RGBColor(255, 0, 0)
    blue = "blue"
    print(red == blue)

    green = RGBColor(0, 255, 0)
    print(red + green)
    print(red + red)
    #    print(red + 2)

    orange1 = RGBColor(255, 165, 0)
    green = RGBColor(0, 255, 0)
    orange2 = RGBColor(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))

    print(red * 0.5)
    print(0.25 * red)

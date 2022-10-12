class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self) -> str:
        return f'{self.real} + i{self.imag}'


def div_complex(left, right) -> Complex:
    divisor = right.real**2 + right.imag**2
    a_top = left.real * right.real + left.imag * right.imag
    b_top = left.imag * right.real + left.real * right.imag

    return Complex(a_top/divisor, b_top/divisor)


if __name__ == '__main__':
    pass
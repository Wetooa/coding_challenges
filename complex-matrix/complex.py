from dataclasses import dataclass
from functools import reduce
import numpy as np


@dataclass
class ComplexNumber:
    real: int = 0
    imaginary: int = 0

    def __mul__(self, another: "ComplexNumber") -> "ComplexNumber":
        a = self.real
        b = self.imaginary
        c = another.real
        d = another.imaginary

        return ComplexNumber(real=(a * c - b * d), imaginary=(a * d + b * c))

    def __add__(self, another: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(
            real=self.real + another.real, imaginary=self.imaginary + another.imaginary
        )

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i"


@dataclass
class Matrix:

    def __init__(
        self, n: int, m: int, matrix: list[list[ComplexNumber]] | None = None
    ) -> None:
        self.n = n
        self.m = m
        self.matrix: list[list[ComplexNumber]] = (
            [[ComplexNumber()] * self.m for _ in range(self.n)]
            if not matrix
            else matrix
        )

    def __mul__(self, another: "Matrix") -> "Matrix":
        if self.n != another.m:
            raise Exception("Matrix dimensions don't match")

        answer = Matrix(n=self.n, m=another.m)

        for i in range(self.n):
            for j in range(another.m):
                answer.matrix[i][j] = reduce(
                    ComplexNumber.__add__,
                    [self.matrix[i][k] * another.matrix[k][j] for k in range(self.m)],
                )

        return answer

    def __str__(self) -> str:
        result = ""
        for i in range(self.n):
            for j in range(self.m):
                result += (self.matrix[i][j]).__str__() + "     "
            result += "\n"
        return result


a = Matrix(
    n=2,
    m=3,
    matrix=[
        [ComplexNumber(1, 1), ComplexNumber(2, -1), ComplexNumber(0, 0)],
        [ComplexNumber(-1, 2), ComplexNumber(0, 1), ComplexNumber(3, 0)],
    ],
)


b = Matrix(
    n=3,
    m=2,
    matrix=[
        [ComplexNumber(2, 0), ComplexNumber(-1, 1)],
        [ComplexNumber(0, 1), ComplexNumber(0, 2)],
        [ComplexNumber(1, -1), ComplexNumber(0, 0)],
    ],
)


print(a * b)

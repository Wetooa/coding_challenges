class Book:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def __format__(self, __format_spec: str) -> str:
        match __format_spec:
            case "caps":
                return self.name.upper()
            case _:
                raise ValueError(f"Unknown format specifier {__format_spec}")


a = Book("harry potter")

print(f"{a:caps}")

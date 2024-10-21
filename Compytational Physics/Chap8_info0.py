class Device:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self) -> str:
        return f"{self.year} {self.brand} {self.model}"

    def __str__(self) -> str:
        return f"Device(brand={self.brand}, model={self.model}, year={self.year})"

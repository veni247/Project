from Chap8_info0 import Device

class Laptop(Device):
    def __init__(self, brand: str, model: str, year: int, storage: int):
        super().__init__(brand, model, year)
        self.storage = storage

    def upgrade_storage(self, additional_storage: int):
        if additional_storage < 0:
            raise ValueError("Dung lượng bổ sung không thể là số âm.")
        self.storage += additional_storage
        print(f"Đã nâng cấp dung lượng lưu trữ thêm {additional_storage} GB. Tổng dung lượng hiện tại là {self.storage} GB.")

    def display_info(self) -> str:
        return f"{super().display_info()}, Dung lượng lưu trữ: {self.storage} GB"

    def __str__(self) -> str:
        return f"Laptop(brand={self.brand}, model={self.model}, year={self.year}, storage={self.storage})"

class person:
    def __init__(self, name: str, age:str):
        self.name=name
        self.age=age
    def __str__(self) -> str:
        return f"info(name={self.name}, age={self.age})"
    def greet(self) -> str:
        return f"Xin Chào, tôi tên là {self.name}, năm nay tôi {self.age}"
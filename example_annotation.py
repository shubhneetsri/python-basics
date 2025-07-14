from pydantic import BaseModel, ValidationError

class TestInput(BaseModel):
    def test(self, a: int, label: str) -> str:
        return [str(a), label]

try:
    obj = TestInput()
    print(obj.test(1,' Type hint'))
    # print(test('string','Type hint'))
    print(obj.test(3,int(2)))
except ValidationError as e:
    print("Validation error:", e)
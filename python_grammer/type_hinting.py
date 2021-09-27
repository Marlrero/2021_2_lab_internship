# %%
# type hinting
# %%
name: str = "John Doe"

age: int = 25

emails: list = ["john1@doe.com", "john2@doe.com"]

address: dict = {
  "street": "54560 Daugherty Brooks Suite 581",
  "city": "Stokesmouth",
  "state": "NM",
  "zip": "80556"
}

print(name)
print(age)
print(emails)
print(address)
# %%
def stringify(num: int) -> str:
    """[summary]

    Args:
        num (int): [description]

    Returns:
        str: [description]
    """
    return str(num)

def plus(num1: int, num2: float = 3.5) -> float:
    return num1 + num2

def greet(name: str) -> None:
    return "Hi! " + str

def repeat(message: str, times: int = 2) -> list:
    return [message] * times

# 참고로 콜론(:)과 화살표(->)를 사용할 때는 파이썬의 관행을 따라 콜론은 뒤에만 한 칸을 뛰우고, 화살표는 앞뒤로 한 칸을 띄웁니다.
# %%
# 내장 타입을 이용해서 좀 더 복잡한 타입 어노테이션을 추가할 때는 스탠다드 라이브러리의 typing 모듈을 사용할 수 있습니다.
# https://www.daleseo.com/python-typing/
from typing import List, Set, Dict, Tuple

nums: List[int] = [1]

unique_nums: Set[int] = {6, 7}

vision: Dict[str, float] = {'left': 1.0, 'right': 0.9}

john: Tuple[int, str, List[float]] = (25, "John Doe", [1.0, 0.9])

print(nums)
print(unique_nums)
print(vision)
print(john)

# %%
print(__annotations__)

# %%
print(repeat.__annotations__)

# %%
# repeat
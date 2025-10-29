from mathlib.arithmetic import add
from mathlib.vector import multi
from mathlib.etc import crazymath


def main():
    print("Hello from python-lib-package-module!")
    print(add(1, 2))
    print(multi([1, 2, 3], [4, 5, 6]))
    print(crazymath(1, 2))

if __name__ == "__main__":
    main()

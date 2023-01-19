# 9.8 generators
# 일반 함수와 달리 마지막 값을 반환 한다.
# 제너레이터는 한 번 순회 하면 다시 순회 하지 않는다.

# 9.8.1


def a():  # generator
    yield 1
    yield 2
    yield 3


def b():  # normal function
    return 1  # stop
    return 2
    return 3


# print(a(), b())
# c = a()
# print(c)
# for i in a():
#     print(i)

def my_range(first=0, last=10, step=1):
    numbers = first
    while numbers<last:
        yield numbers
        numbers += step


# ranger = my_range(1, 5)
# print(ranger)
# for x in ranger:
#     print(x)
# for try_again in ranger:
#     print(try_again)

# 9.8.2 generator comprehension
genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
# for thing in genobj:
#     print(thing)

# 9.9 decorators
def document_it(func):
    def new_function(*args, **kwargs):
        print('실행 중인 함수:', func.__name__)
        print('위치 기반 인수:', args)
        print('키워드 기반 인수:', args)
        result = func(*args, **kwargs)
        print('실행 결과:', result)
        return result
    return new_function

# def sub_int(a, b):
#     return a - b
# print(sub_int(3, 5))
# cooler_add_int = document_it(sub_int)
# print(cooler_add_int(3, 5))


# @document_it
# def square_it(n):
#     return n
#
#
# @document_it
# def add_int(a, b):
#     return a + b
#
# add_int(1, 3)
# square_it(4)


# 9.10 Namespaces and Scope

animal = 'fruitbat'  # global variables


def print_global():
    # animal = 'fruitbat' # local variables
    print('inside print_global:', animal)

# print('at the top level:', animal)
# print_global()

def change_print_global():
    global animal  # global variables
    print(animal)
    animal = 'wombat'  # local variables
    print(animal)

# change_print_global()
# print(locals())

# 9.11

# 9.12 Recursion

def factorial_iter(n):
    """
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return:  팩토리얼 계산 결과 값
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recu(n):
    """
    재귀 함수를 사용한 팩토리얼 계산 함수
    :param n: n!
    :return: 자기 자신을 호출 or 1
    """
    if n == 1:  # 끝나는 조건
        return 1
    else:
        return factorial_recu(n-1) * n


# print(factorial_iter(5))
# print(factorial_recu(5))

# 9.14.1~2 exception

# try:
#     expr = input('분자 분모 입력 (띄어 쓰기로 구분):').split()
#     if len(expr) > 2:
#         raise IndexError('개수 초과')  # as
#     print(int(expr[0]) / int(expr[1]))
# except ZeroDivisionError as err:
#     print(f'분모에 0이 아닌 다른 수를 입력해 주십시오. ({err})')
# except ValueError as err:
#     print(f'숫자가 아닌 다른 값을 입력 하셨습니다. ({err})')
# except IndexError as err:
#     print(f'숫자 2개를 입력해 주십시오. ({err})')
# except Exception as other:
#     print(f'예외 발생! :{other}')
# else:  # 예외가 발생 하지 않았을 때
#     print('프로그램 정상', end=' ')
# finally:  # 예외 발생 여부와 상관 없이 무조건 실행
#     print('종료')


# def div_calc(a, b):
#     """
#     나누기 함수
#     :param a: 분자
#     :param b: 분모
#     :return: 계산결과
#     """
#     return a / b


# print(div_calc(15, 3))


# chap 10 object, class


# 10.2.3 method

# class
class Pokemon:
    def __init__(self, name, type, skills): # 객체 초기화 메서드
        print(f"{type} 포켓몬 {name} 생성됨")
        self.name = name
        self.type = type
        self.skills = skills.split('/')
    def info(self):
        print(f"{self.type} 포켓몬은 {self.name}입니다.")
        # print(f"기술의 이름은 {self.skills} 입니다.")
        for skill in self.skills:
            print(skill)


# p1 = Pokemon('피카츄', '전기타입', '50만 볼트/100만 볼트/번개')
# p2 = Pokemon('이상해씨', '풀타입', '몸통박치기/풀베기/드레인')
# p2.info()
# p1.info()
# print(p2.skills)


# 10.3 Inheritance

class Pikachu(Pokemon):  # Inheritance
    pass


pi1 = Pikachu('피카츄', '전기타입', '50만 볼트/100만 볼트/번개') # Pokemon 클래스를 상속 받은 Pikachu 클래스 사용하기.
pi1.info()

p1 = Pokemon('피카츄', '전기타입', '50만 볼트/100만 볼트/번개')


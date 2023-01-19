9-3
# def test_deco(func):
#     def new_function(*args, **kwargs):
#         print('start: \n 함수 이름:', func.__name__)
#         print('end:')
#     return new_function()
#
# @test_deco
# def some_func():
#     pass



# groups = {'빅뱅': ['GD', '태양', '탑', '대성', '승리'],
#           '마마무': ['문별', '솔라', '휘인', '화사']}
# print(groups['빅뱅'].pop())
# for groups, member in groups.items():
#     print(f'{groups}의 멤버')
#     for member in member:
#         if member != '승리':
#             print(member)


9-4
# class OopsException(Exception):
#     pass
#
# try:
#     raise OopsException('oops')  # as
# except OopsException as err:
#     print(f'Caught an ({err})')

10-1
class Thing():
    pass

Thing()
example = Thing
# print(Thing)
# print(example)

10-2
class Thing2():
    pass
example = Thing2
example.letters = 'abc'
# print(example.letters)


10-3
class Thing3():
    def __init__(self, letters):
        self.letters = letters
        print(f'문자열 {letters}를 생성합니다.')


# a = Thing3('xyz')
# print(a.letters)  # 추가적으로 객체를 생성하지 않고도 출력할 수 있다.

10-4
class element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
        print(f'원소 번호는 {number}번 기호는 {symbol}인 {name}이 확인 되었습니다. ')

# obj = element('Hydrogen', 'H', '1')


10-5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# hydrogen = element(el_dict['name'], el_dict['symbol'], el_dict['number'])

10-6
class elements():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
        print(f'원소 번호는 {number}번 기호는 {symbol}인 {name}이 확인 되었습니다. ')
    def dump(self):
        print(f'원소 이름은 {self.name}이고 기호는 {self.symbol}이며 원소 번호는 {self.number}입니다.')

hydrogen = elements(el_dict['name'], el_dict['symbol'], el_dict['number'])
hydrogen.dump()
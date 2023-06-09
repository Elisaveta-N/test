#����������� �������, ����������� ��������� ����� :
# https://kispython.ru/docs/4/%D0%98%D0%9D%D0%91%D0%9E-11-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-40
import math


def main(y, z):
    sum = 0
    n = len(y)
    y = [0] + y
    z = [0] + z
    for i in range(1, n + 1):
        a = (y[n + 1 - i] ** 3)
        b = (-18 * z[n + 1 - math.ceil(i / 2)] - 71)
        sum += 96 * (a + b) ** 2
    return 86 * sum

def main(z, x):
    f = 0
    for i in range(1, len(z) + 1):
        f += pow(math.fabs(90 + 52 * pow(z[(i-1)//2], 2) + x[(i-1)//2]), 7)
    return 31 * f

print(main([0.36, -0.31, 0.58], [0.74, -0.18, 0.01]))



#����������� ������� ��� ���������� ������ �������.
# https://kispython.ru/docs/5/%D0%98%D0%9D%D0%91%D0%9E-11-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-40
def grace_lua(x, left, middle, right):
    if x[1] == 'GRACE':
        return left
    if x[1] == 'LUA':
        return middle
    return right


def bro(x, left, right):
    if x[0] == 'BRO':
        return left
    return right


def four(x, left, middle, right):
    if x[4] == 1978:
        return left
    if x[4] == 2006:
        return middle
    return right


def main(x):
    if x[3] == 2015:
        if x[2] == 'UNO':
            return grace_lua(x, bro(x, 0, 1), four(x, 2, 3, 4), bro(x, 5, 6))
        if x[2] == 'BRO':
            return four(x, grace_lua(x, 7, 8, 9), 10, 11)
    if x[3] == 1983:
        return 12
    return 13


#����������� ������� ��� �������������� ������� �����.

#������ �� ������� ����� � ������� �� ������� ��� � �������. 
#�������� ������� ����� ����� ���: ���������� ������.
# https://kispython.ru/docs/6/%D0%98%D0%9D%D0%91%D0%9E-11-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-40
def main(s):
    i = int(s)
    c1 = 0b1111111 & i
    c2 = 0b1111111111 & (i >> 7)
    c3 = 0b11 & (i >> 17)
    c5 = 0b111111111 & (i >> 27)
    return tuple(map(str, (c1, c2, c3, c5)))

#����������������� ������.
# http://kispython.ru/docs/6/%D0%98%D0%9A%D0%91%D0%9E-10-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-16
def main(q):
    q1 = int(q, 16) & 0b11111
    q2 = int(q, 16) & 0b1111100000
    q2 = q2 >> 5
    q3 = int(q, 16) >> 18
    return [('Q1', str(hex(q1))), ('Q2', str(hex(q2))), ('Q4', str(hex(q3)))]


#����������� ������� ��� ������� ������, ���������� ������ � ��������� �������.
# http://kispython.ru/docs/7/%D0%98%D0%9A%D0%91%D0%9E-10-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-16
import re


def main(str):
    pat1 = r'\(\w+\)'
    res1 = re.findall(pat1, str)

    pat2 = r'(\|>(\s)?\w+)'
    res2 = re.findall(pat2, str)

    i = 0
    for val in res1:
        res1[i] = val[1:-1]
        i += 1
    i = 0

    for val in res2:
        res2[i] = val[0][2:].strip()
        i += 1
    res = list(zip(res2, res1))

    return res

print(main("[[ begin opt q(rexele_541) |>oncera_358 end, begin optq(rianbi)|>tiabe end, ]]"))

import re


def func4(str):
    pat1 = r'q\(\w+\)'
    res1 = re.findall(pat1, str)
    i = 0
    for val in res1:
        res1[i] = val[2:-1]
        i+=1
    pat2 = r'\|.\w+;'
    res2 = re.findall(pat2, str)
    i = 0
    for val in res2:
        res2[i] = val[1:-1]
        if res2[i][0] == ' ':
            res2[i] = res2[i][1:]
        i+=1
    res = {}
    for i in range(0, len(res1)):
        res[res1[i]] = res2[i]   
    print(res)
    
func4('<block> {let q(arlaso) <|-8318; } {let q(xeon) <|-5427;} { letq(ondi_649) <| 327; } \
{ let q(cere) <| 6908;}</block>')


#����������� �������� ������� ���� � ���� ������.
# https://kispython.ru/docs/9/%D0%98%D0%9D%D0%91%D0%9E-07-21.html#%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82-40
class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def spin(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'B':
            self.state = 'E'
            return 3
        if self.state == 'E':
            self.state = 'F'
            return 6
        raise MealyError('spin')

    def punch(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'E':
            self.state = 'A'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('punch')

    def stand(self):
        if self.state == 'B':
            self.state = 'G'
            return 2
        if self.state == 'E':
            self.state = 'G'
            return 8
        raise MealyError('stand')


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.spin() == 0
    assert o.punch() == 1
    assert o.spin() == 4
    assert o.spin() == 5
    assert o.punch() == 7
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.spin() == 6
    assert o.punch() == 9
    o = main()
    assert o.spin() == 0
    assert o.stand() == 2
    o = main()
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.stand() == 8
    raises(lambda: o.stand(), MealyError)
    raises(lambda: o.punch(), MealyError)
    raises(lambda: o.spin(), MealyError)

#Variation 2
    class MealyError(BaseException):
    def __init__(self, method_name) -> None:
        self.method_name = method_name
        super().__init__(method_name)


class MealyAutomata:
    _state_dict = {
        'A': {'mix': ('B', 0), 'dash': None},
        'B': {'mix': None, 'dash': ('C', 1)},
        'C': {'mix': ('D', 2), 'dash': None},
        'D': {'mix': ('G', 4), 'dash': ('E', 3)},
        'E': {'mix': ('F', 5), 'dash': ('G', 6)},
        'F': {'mix': None, 'dash': ('G', 7)},
        'G': {'mix': ('A', 9), 'dash': ('G', 8)}
    }

    def __init__(self):
        self._state = 'A'

    def _run_method(self, method_name):
        supposed_state = self._state_dict[self._state][method_name]
        if supposed_state is not None:
            self._state = supposed_state[0]
            return supposed_state[1]
        else:
            raise MealyError(method_name)

    def mix(self):
        return self._run_method('mix')

    def dash(self):
        return self._run_method('dash')


def main():
    return MealyAutomata()


def test():
    o = main()
    o.mix()  # 0
    o.dash()  # 1
    o.mix()  # 2
    o.dash()  # 3
    o.mix()  # 5
    o.dash()  # 7
    o.mix()  # 9
    try:
        o.dash()  # MealyError
    except MealyError:
        pass
    o.mix()  # 0
    try:
        o.mix()  # MealyError
    except MealyError:
        pass
    o.dash()  # 1
    o.mix()  # 2
    o.mix()  # 4
    o.dash()  # 8

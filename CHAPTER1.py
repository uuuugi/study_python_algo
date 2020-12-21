
#1.1 정수
print((999).bit_length()) #int는 불변형 4바이트 bit_lenth 를 이용하여 바이트수 확인 가능

print()
s = '11'
d = int(s)#casting
print('\'11\'을 정수로 변환:', d)
b = int(s, 2) # 10진수로 변환하기 --> int(문자열, 밑)
print('\'11\'을 밑이 2인 10진법으로 변환:', b)

print('====================================')
# 1.2 부동소수점
# 1.2.1 부동소수점끼리 비교
# 32비트 부동소수점에서 1비트=부호 | 8비트=지수 | 23비트=유효 숫자 자릿수(가수)
print('0.2 * 3 == 0.6: ', 0.2 * 3 == 0.6)
print('1.2 - 0.2 == 1.0: ', 1.2 - 0.2 == 1.0)
print('1.2 - 0.1 == 1.1: ', 1.2 - 0.1 == 1.1)
print('0.1 * 0.1 == 0.01: ', 0.1 * 0.1 == 0.01)

def compare_floating_point(x, y, places=7): #unittest 모듈에 assertAlmostEqual() 메소드 있음
    return round(abs(x-y), places) == 0

print('====================================')
# 1.2.2 정수와 부동소수점 메서드
# / 연산자는 부동소수점 반환 //연산자는 정수 반환 %연산자는 나머지 반환

print('divmod(45,6) 몫과 나머지 반환 :', divmod(45, 6)) #몫과 나머지 반환
print('round(100.96, -2) 반올림:', round(100.96, -2)) #반올림함수인데 이해 잘 안됨
print('2.75.as_integer_ratio() 부동소수점을 분수로 표현:', 2.75.as_integer_ratio()) #부동소수점을 분수로 표현

print('====================================')
#1.3 복소수
#cmath모듈을 임폴트해야함. 책에 상세설명 없음

#1.4 fraction 모듈
print('fraction모듈에 관한 내용 --코드참조')
from fractions import Fraction

def rounding_floats(num1, places): #반올림
    return round(num1, places)

def float_to_fractions(num): #분수로반환
    return Fraction(*num.as_integer_ratio())

def get_denominator(num1, num2):#분모반환
    a = Fraction(num1, num2)
    return a.denominator

def get_numerator(num1, num2):#분자반환
    a = Fraction(num1, num2)
    return a.numerator

def test_testing_floats(): #test
    num1 = 1.25
    num2 = 1
    num3 = -1
    num4 = 5/4
    num6 = 6
    assert(rounding_floats(num1, num2) == 1.2)
    assert(rounding_floats(num1*10, num3) == 10)
    assert(float_to_fractions(num1) == num4)
    assert(get_denominator(num2, num6) == num6)
    assert (get_numerator(num2, num6) == num2)
    print('test ok')

if __name__ == "__main__":
    test_testing_floats()

del Fraction
print('========================================')
#1.5 decimal 모듈

print('소수점 계산은 정확하지 않을 수 있음 sum(0.1 for i in range(10)) == 1.0: ', sum(0.1 for i in range(10)) == 1.0)

from decimal import Decimal
print('정확한 계산을 원하면 Decimal 모듈을 사용할것 sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"): ',
      sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))

del Decimal

print('========================================')
#1.6 2진수 8진수 16진수
print('bin(999) 2진수로 반환 :', bin(999))
print('oct(999) 8진수로 반환 :', oct(999))
print('hex(999) 16진수로 반환 :', hex(999))

print('========================================')
#1.7 연습문제

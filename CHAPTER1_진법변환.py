#진법 변환 (2<= base <= 10)


#2->10 변환
def convert_bin_to_dec(num, base):
    mult, result = 1, 0
    while num > 0:
        result += num % 10 * mult#1의자리수를 구한후 mult와 곱해줌
        mult *= base#한턴마다 mult도 한칸씩 왼쪽으로 시프트이동
        num = num // 10#num을 잘라서 1의자리수를 계속 가져올수 있게 함
    return result

def test_convert_bin_to_dec():
    num, base = 1001, 2
    assert (convert_bin_to_dec(num, base) == 9)
    print('bin_to_dec() test ok')

if __name__ == "__main__":
    test_convert_bin_to_dec()

#=======================================================
#10->2변환
def convert_dec_to_bin(num, base):
    mult, result = 1, 0
    while num > 0:
        result += num % base * mult#숫자를 base로 mod연산하여 mult와 곱해준후 더함
        mult *= 10#한턴마다 왼쪽으로 이동
        num = num//base#base로 나눠 다음자리수 계산하게끔 함
    return result

def test_convert_dec_to_bin():
    num, base = 9, 2
    assert (convert_dec_to_bin(num, base) == 1001)
    print('dec_to_bin() test ok')

if __name__ =="__main__":
    test_convert_dec_to_bin()

#===========================================================
#10 -> 16

def convert_dec_to_hex(num,base):
    strings = "0123456789ABCEDF"
    result = ""
    while num >0:
        digit = num % base #나머지구하기
        result = strings[digit] + result #나머지(정수) 를 배열과 매핑해서 들고오기
        num = num//base # 한칸 이동
    return result

def test_convert_dec_to_hex():
    num, base = 31,16
    assert (convert_dec_to_hex(num, base) == "1F")
    print('dec_to_hex() test ok')

if __name__ == "__main__":
    test_convert_dec_to_hex()

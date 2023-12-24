print("wellcome")  # 텍스트 출력는 한 줄에 나와야함
print(
    """
      well
      come
      """
)  # """ 앞 뒤 각각 3번씩 하면 줄 바꿈을 할 수 있음

print("'1'+'1'", "1" + "1")
# " " 쌍 따옴표는 문자 그대로 출력하게함
print("1" + "1")
# 쌍따옴 안에 숫자들만 출력 (붙어서 출력됨)
print("1", "1")
# 쌍따옴 안에 숫자들만 출력 (띄어서 출력됨)
print("'1'+'1'")
# 쌍따옴 안에 따옴표랑 같이 출력
print("1+1")
# 쌍따옴 안에 텍스트를 그대로 출력
print(1 + 1)
# 숫자를 더한 값

print("SSS" * 20)
# SSS를 20번 출력
print("len('ABCDEF'*1000)", len("ABCDEF" * 1000))
# 좌측은 텍스를 출력 , 우측은 len(갯수)를 이용한 값 출력

print(
    "'hello world'.replace('world','seungsoo')",
    "hello world".replace("world", "seungsoo"),
)
# replace = 문자 치환(바꿈) / "출력할 기존 문자".replace("치환전 문자", "최환후 문자")

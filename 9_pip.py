import pandas  # pandas 모듈 실행(import)

house = pandas.read_csv(
    "house.csv"
)  # 변수값 = pandas(모듈).read(읽다)_csv(파일형태)("house.csv")<-파일명
print(house)  # house.csv 전체 읽기
print(house.head())  # house.csv의 head(위에서 5개)읽기
print(house.head(2))  # house.csv의 head(위에서 2개)읽기
print(house.describe())  # house.csv의 각 열 데이터의 정보(갯수, 평균값, 최소값, 최대값, 표준편차 등 표시됨)


##pandas외에도 정말 많은 pip들이 있으니 많이 배우면 좋음 ^^..;;

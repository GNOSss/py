students = ["egoing", "sori", "maru", "jack", "sdas", "ads"]
grades = [2, 123, 4, 56, 3324, 235]
#'students','grades' = 변수 (단순 이름 부여)
print(students[1])
print("1번째 학생은", students[0])
print("2번째 학생은", students[1])
# @번째 호출의 첫 기준은 "0"부터 시작함 즉, [1]은 2번째이다.
print("학생들의 수는?", len(students), "명")
# len = 카운팅, 원소의 갯수를 셀때 / len(변수 명)

print("가장 작은 값은", min(grades))
print("min(grades)", min(grades))
# min = minimum , 가장 최소&작은 값 / min(변수 명)
print("가장 큰 값은", max(grades))
# max = max , 가장 최대,큰 값 / max(변수 명)
print("총 합은?", sum(grades))
# sum = 더하기 , sum(변수 명) / 변수 안에 있는 숫자들은 계산 할 수 있음 *단, 텍스트 포함시 에러

import statistics  # statistics = 통계 관련 기능이 내장되어 있음

print("grades의 평균값은?", statistics.mean(grades))
# mean = 값의 평균 , 변수의 평균 값 / statistics.mean(변수)
print("grades의 평균값은?", statistics.median(grades))
# median = 중앙 값 , statistics.median(변수) * 위 grades 기준 56, 123의 중앙 값 반환함

import random  # random = 무작위 랜덤 모듈

print("random으로 뽑힌 학생은 ?", random.choice(students))
# choice = 선택하다 , random.choive(변수)

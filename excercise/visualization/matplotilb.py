import matplotlib.pyplot as plt
%matplotlib inline  # 매직 매서드

# 그래프 데이터
subject = ['English', 'Math', 'Korean', 'Science', 'Computer']
points = [40, 90, 50, 60, 100]

# 축 그리기
figure = plt.figure()
axis1 = figure.add_subplot(1, 1, 1)

# 그래프 그리기
axis1.bar(subject, points)

# 라벨, 타이틀 달기
plt.xlabel('Subject')
plt.ylabel('Point')
plt.title("Result")

# 보여주기
plt.savefig('/barplot.png')  # 그래프를 이미지로 출력
plt.show()                   # 그래프를 화면으로 출력
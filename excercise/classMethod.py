class Person:
    count = 0  # 클래스 속성

    def __init__(self):
        Person.count += 1  # 인스턴스가 만들어질 때
                           # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print(f"{cls.count}명 생성되었습니다")

James = Person()
Kim = Person()
Lee = Person()

Person.print_count()
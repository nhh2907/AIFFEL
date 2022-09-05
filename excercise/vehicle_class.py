class vehicle:

    def __init__(self, *args):
        self.max_speed = args[0]
        self.milieage = args[1]
        self.capacity = args[2]

    def run(self):
        self.milieage += int(input('Enter a milieage: '))


class bus(vehicle):

    def fare(self):
        return self.capacity * 200


c = bus(10, 500, 5)
fee = c.fare()

print(f"Bus 속도 {c.max_speed}, 마일리지 {c.milieage}, 인원 {c.capacity} ")
print(f"요금은 {fee} 원")

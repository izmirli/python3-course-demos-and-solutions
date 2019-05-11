import lib.car as car

from lib.race import Race

c1 = car.Car('blue', 40)
c2 = car.Car('green', 60)
race = Race([c1, c2])

print('Cars:')
c1.show()
c2.show()

print('c1 is faster then c2:', c1.is_faster_than(c2))

print(car.hello)

print('Race winner:')
race.winner().show()

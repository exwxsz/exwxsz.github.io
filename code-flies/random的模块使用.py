import random
x = random.getstate()
print(random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
random.randint(1,10))
random.setstate(x)
print(random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
random.randint(1,10),
random.randint(1,10))

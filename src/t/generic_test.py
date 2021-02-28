class TestClass:
    def __init__(self):
        self.x = 7

d = {}
d['t'] = TestClass

print(type(d['t']))

h = d['t']()

h.x = 2

y = d['t']()

y.x = 5

print('hi')
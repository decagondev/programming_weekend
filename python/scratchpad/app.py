# a scratchpad playgound to talk about some concepts and write snippets of code

# possibly python basics

# python datatypes

# python classes
    # OOP ideas
    # - abstraction
    # - visibility
    # - inheritance

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

class Vec3(Vec2):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

     def __add__(self, other):
        return self


v = Vec2(2, 4)
v2 = Vec2(4, 8)
v3 = v + v2
v3 = v.__add__(v2)
print(v)
x = 2
y = 4




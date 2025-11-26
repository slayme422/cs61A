# 这是数据抽象的一种方式
def make_point(x, y):
    return (x, y)

def get_x(point):
    return point[0]

def get_y(point):
    return point[1]

first_point=make_point(1,2)
print(first_point)
print(get_x(first_point))
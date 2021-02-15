def calculate_y_coordinate(point1,point2,x):
    m = (point2[1]-point1[1])/(point2[0]-point1[0])
    b = point1[1]-m*point1[0]
    y = m*x+b
    return y
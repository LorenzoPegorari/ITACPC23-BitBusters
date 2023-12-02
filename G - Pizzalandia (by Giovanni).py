# ITACPC 2023
# G - Pizzalandia
# (pizzalandia)
# Made by Giovanni Alberto Sartorato

# Assign each number to a variable

def solve(rectangle_width,rectangle_height,tx,ty,wx,wy):
    distances=[]
    if wx<=clockwise_distance(rectangle_width, rectangle_height, tx, ty,0,wy):
        distances.append(clockwise_distance(rectangle_width, rectangle_height, tx, ty,0,wy))
    if rectangle_height-wy<=clockwise_distance(rectangle_width, rectangle_height, tx, ty,wx,rectangle_height):
        distances.append(clockwise_distance(rectangle_width, rectangle_height, tx, ty,wx,rectangle_height))
    if rectangle_width-wx<=clockwise_distance(rectangle_width, rectangle_height, tx, ty,rectangle_width,wy):
        distances.append(clockwise_distance(rectangle_width, rectangle_height, tx, ty,rectangle_width,wy))
    if wy<=clockwise_distance(rectangle_width, rectangle_height, tx, ty,wx,0):
        distances.append(clockwise_distance(rectangle_width, rectangle_height, tx, ty,wx,0))
    return min(distances)


def distance_from_origin(rectangle_width, rectangle_height, x, y):
    if x==rectangle_width:
        #train border=east
        return rectangle_height+rectangle_width+rectangle_height-y
    if x==0:
        #train border=west
        return y
    if y==rectangle_height:
        #train border=north
        return rectangle_height+x
    if y==0:
        #train border=south
        return 2*rectangle_height+2*rectangle_width-x
    return perimeter_distance

def clockwise_distance(rectangle_width, rectangle_height, tx, ty,wx,wy):
    perimeter=2*rectangle_height+2*rectangle_width
    t_dist=distance_from_origin(rectangle_width, rectangle_height, tx, ty)
    w_dist=distance_from_origin(rectangle_width, rectangle_height, wx, wy)
    if w_dist>=t_dist:
        return w_dist-t_dist
    else:
        return perimeter-t_dist+w_dist


number_of_testCases=int(input())
results=[]
for i in range(0,number_of_testCases):
    inputList=input().split()
    px, py, tx, ty, wx, wy = map(int, inputList)
    results.append(solve(px,py,tx,ty,wx,wy))

for res in results:
    print(res)






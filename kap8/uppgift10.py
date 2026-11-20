def grader(points):
    for c in range (0, len(points)):
        if points[c]>=25:
            print(f'Elev {c+1}: Godkänd')
        else:
            print(f'Elev {c+1}: Underkänd')

poang_1 = 32
poang_2 = 18
poang_3 = 25
pointslist=[poang_1, poang_2, poang_3]
grader(pointslist)


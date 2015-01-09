
def eq(a, b):
    return abs(a - b) < .01

def parse_triangle(coord_string):
    coords = map(float, coord_string.split())
    return ((coords[0], coords[1]),
            (coords[2], coords[3]),
            (coords[4], coords[5]))

def main():
    n = int(raw_input())
    case = 1

    while n != 0:
        if n != 1:
            print ""

        holes = []
        for i in range(n):
            holes.append(parse_triangle(raw_input()))

        triangles = []
        for i in range(n * 2):
            triangles.append(parse_triangle(raw_input()))

        print "Case %d:" % case

        n = int(raw_input())
        case += 1

if __name__ == "__main__":
    main()

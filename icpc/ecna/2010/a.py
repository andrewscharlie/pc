from collections import deque
import math

class Triangle:
    def __init__(self, vertices):
        self.vertices = vertices
        self.sides = get_sides(vertices)
        self.angles = get_angles(self.sides)

    def __repr__(self):
        return repr(self.vertices)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        sides1, sides2 = deque(self.sides), deque(other.sides)

        for i in range(3):
            if eq(sides1[0], sides2[0]) and eq(sides1[1], sides2[1]) and eq(sides1[2], sides2[2]):
                return True
            sides1.rotate(1)

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

def add_triangles(t1, t2):
    """Returns a list of all possible triangles that can be formed by merging
    the two given triangles."""
    solutions = []
    for i in range(3):
        for j in range(3):
            # See if t1 angle 0 and t2 angle i can be merged
            if eq(t1.angles[i] + t2.angles[j], math.pi):
                # The two angles (t1[i] and t2[j]) fit together to form a straight
                # line. Now we just need to make sure that the sides that are
                # merging are the same length
                if eq(t1.sides[(i + 1) % 3], t2.sides[(j + 2) % 3]):
                    # Calculate the dx and dy on the side of t1 that's being "extended"
                    dx = t1.vertices[i][0] - t1.vertices[(i + 1) % 3][0]
                    dy = t1.vertices[i][1] - t1.vertices[(i + 1) % 3][1]

                    v3x = t1.vertices[i][0] + dx * t2.sides[(j + 1) % 3] / t1.sides[(i + 2) % 3]
                    v3y = t1.vertices[i][1] + dy * t2.sides[(j + 1) % 3] / t1.sides[(i + 2) % 3]
                    solutions.append(Triangle([t1.vertices[(i + 1) % 3],
                                               t1.vertices[(i + 2) % 3],
                                               (v3x, v3y)]))

                if eq(t1.sides[(i + 2) % 3], t2.sides[(j + 1) % 3]):
                    # Calculate the dx and dy on the side of t1 that's being "extended"
                    dx = t1.vertices[i][0] - t1.vertices[(i + 2) % 3][0]
                    dy = t1.vertices[i][1] - t1.vertices[(i + 2) % 3][1]

                    v3x = t1.vertices[i][0] + dx * t2.sides[(j + 2) % 3] / t1.sides[(i + 1) % 3]
                    v3y = t1.vertices[i][1] + dy * t2.sides[(j + 2) % 3] / t1.sides[(i + 1) % 3]
                    solutions.append(Triangle([t1.vertices[(i + 1) % 3],
                                               t1.vertices[(i + 2) % 3],
                                               (v3x, v3y)]))

    return solutions

def eq(a, b):
    """Determines whether a and b are equal within epsilon (.05)."""
    return abs(a - b) < .05

def dist(a, b):
    """Returns the distance between two coordinates, a and b."""
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

def get_angle(a, b, c):
    """Given three side lengths of a triangle, a, b, and c, returns the measure
    of angle C, in radians."""

    # Law of cosines:
    # C = acos((a^2 + b^2 - c^2) / (2ab))
    return math.acos((a * a + b * b - c * c) / (2 * a * b))

def get_angles(sides):
    """Given a list of side lengths for a triangle, returns a list of the angles
    opposing each side."""
    return [get_angle(sides[1], sides[2], sides[0]),
            get_angle(sides[2], sides[0], sides[1]),
            get_angle(sides[0], sides[1], sides[2])]

def get_sides(vertices):
    """Given the vertices of a triangle, returns a list containing the lengths
    of that triangle's sides."""
    return [dist(vertices[1], vertices[2]),
            dist(vertices[2], vertices[0]),
            dist(vertices[0], vertices[1])]

def is_clockwise(vertices):
    """Given a list of vertices (as tuples), returns whether the vertices are
    specified in a clockwise order."""
    v = vertices
    area = ((v[1][0] - v[0][0]) * (v[1][1] + v[0][1]) +
            (v[2][0] - v[1][0]) * (v[2][1] + v[1][1]) +
            (v[0][0] - v[2][0]) * (v[0][1] + v[2][1])) / 2
    return (area > 0)

def parse_triangle(vertices_string):
    """Parses a string containing the vertices of a triangle and returns a
    Triangle representing that triangle."""
    vertices = map(float, vertices_string.split())
    vertices_as_tuples = [(vertices[0], vertices[1]),
                          (vertices[2], vertices[3]),
                          (vertices[4], vertices[5])]

    # Make sure that all triangles are specified in the same CCW direction
    if (is_clockwise(vertices_as_tuples)):
        vertices_as_tuples.reverse()

    return Triangle(vertices_as_tuples)

def get_fits(holes, triangles):
    """Given N holes and N * 2 triangles, returns a 2 dimensional array
    where each row is the index of the hole and each entry is a list specifying
    the two triangles that can fit together to fill that hole."""
    fits = []
    for hole in holes:
        hole_fits = []

        for i1, t1 in enumerate(triangles):
            for i2, t2 in enumerate(triangles[i1 + 1:], i1 + 1):
                if hole in add_triangles(t1, t2):
                    hole_fits.append((i1, i2))

        fits.append(hole_fits)

    return fits

def get_solution(fits, solutions = None, usedTriangles = None, nextIndex = 0):
    """Given a 2 dimensional array where each row is the index of the hole and
    each entry in that row is a tuple of the indices of two triangles that can
    fill that hole, the solutions found thus far, the indices of the triangles
    that have been used so far, and the index of the first hole to fit, returns
    a 2 dimensional array where each row is the index of the hole and each entry
    is a tuple specifying the triangles that should be used to fill that hole.
    """
    if solutions is None: solutions = []
    if usedTriangles is None: usedTriangles = set([])

    if nextIndex == len(fits):
        # We're done. Were we successful in fitting all holes?
        if len(solutions) == len(fits):
            # We were successful
            return solutions
        else:
            # We weren't successful - return None to signify this
            return None

    for possibility in fits[nextIndex]:
        if (possibility[0] not in usedTriangles) and (possibility[1] not in usedTriangles):
            solutions.append(possibility)
            newUsedTriangles = usedTriangles | set([possibility[0], possibility[1]])

            solution = get_solution(fits, solutions, newUsedTriangles, nextIndex + 1)

            if solution is not None:
                return solution

            solutions.pop()

    # Because we're guaranteed a solution, we shouldn't reach here

def main():
    n = int(raw_input())
    case = 1

    while n != 0:
        if case > 1:
            print ""

        holes = []
        for i in range(n):
            holes.append(parse_triangle(raw_input()))

        triangles = []
        for i in range(n * 2):
            triangles.append(parse_triangle(raw_input()))

        fits = get_fits(holes, triangles)

        solutions = get_solution(fits)

        print "Case %d:" % case
        for i, fit in enumerate(solutions):
            print "Hole %d: %d, %d" % (i + 1, fit[0] + 1, fit[1] + 1)

        n = int(raw_input())
        case += 1

if __name__ == "__main__":
    main()

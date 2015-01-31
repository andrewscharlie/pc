import Queue
"""
              z
              |
              |
          x   |
           \  |
            \ |
             \|
y -------------
"""

class Node:
    def __init__(self, x, y, z):
        # The coordinates of the node
        self.coords = (x, y, z)
        # The node that was visited before this one
        self.prev = None
        # The direction taken from the previous node to this node
        self.dir = None

def is_passable(coords, faces):
    """Returns true if the rods can be focused on the given node."""
    n = len(faces[0])
    (x, y, z) = coords

    # Check that the "slot" is open on all faces
    return (
        faces[0][n - 1 - z][n - 1 - y] != "X" and       # front
        faces[1][n - 1 - z][x] != "X" and               # right
        faces[2][n - 1 - z][y] != "X" and               # back
        faces[3][n - 1 - z][n - 1 - x] != "X" and       # left
        faces[4][n - 1 - x][n - 1 - y] != "X" and       # top
        faces[5][x][n - 1 - y] != "X"                   # down
    )

def solve(faces):
    """Given a list of maze faces (in front, right, back, left, up, down order),
    gives a sequence of moves to move from (1, 1, 1) to (n-2, n-2, n-2)"""
    n = len(faces[0])

    cube = [[[Node(x, y, z) for z in range(n)] for y in range(n)] for x in range(n)]

    next = Queue.Queue()
    next.put((1, 1, 1))
    while not next.empty():
        (x, y, z) = next.get()
        node = cube[x][y][z]

        if (node.coords == (n - 2, n - 2, n - 2)):
            # We've reached our destination
            break
        
        adjacent_coords = get_adjacent_coords(node.coords)

        for adjacent_coord in adjacent_coords:
            (next_x, next_y, next_z) = adjacent_coord[0:3]
            next_node = cube[next_x][next_y][next_z]

            if not is_passable(next_node.coords, faces):
                # Skip this node - it's not passable
                continue;
            
            if next_node.prev is not None:
                # Skip this node - we've already visited it
                continue;

            next_node.prev = node
            next_node.dir = adjacent_coord[3]
            next.put(next_node.coords)

    # Trace the path back from the final node to the first
    path = ""
    (x, y, z) = (n - 2, n - 2, n - 2)
    while (x, y, z) != (1, 1, 1):
        path += cube[x][y][z].dir
        (x, y, z) = cube[x][y][z].prev.coords

    # Return the reversed path
    return path[::-1]

def get_adjacent_coords(coords):
    """Given a set of coordinates, returns a tuple containing the coordinates of
    all adjacent nodes as well as the direction traveled to reach those nodes."""
    adjacent_node_coords = []
    (x, y, z) = coords
    
    # Consider the nodes in the order that ties are broken among equidistant
    # solutions. This guarantees that we'll always reach the preferred solution
    # first.
    adjacent_node_coords.append((x - 1, y, z, "F")) # F
    adjacent_node_coords.append((x + 1, y, z, "B")) # B
    adjacent_node_coords.append((x, y + 1, z, "L")) # L
    adjacent_node_coords.append((x, y - 1, z, "R")) # R
    adjacent_node_coords.append((x, y, z + 1, "U")) # U
    adjacent_node_coords.append((x, y, z - 1, "D")) # D

    return adjacent_node_coords
    
def main():
    while True:
        n = int(raw_input())

        if n == 0:
            break;

        faces = []
        for i in range(6):
            face = []
            for j in range(n):
                face.append(raw_input())

            faces.append(face)

        print solve(faces)

if __name__ == "__main__":
    main()

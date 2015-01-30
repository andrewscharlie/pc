"""
Beautiful axis drawing
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
    def __init__(self, coords):
        self.coords = ()
        self.adjacent_to = None
        self.is_passable = 

    def is_passable(self, faces):
        """Returns true if the rods can be focused on the given node."""
        n = len(faces[0])
        
        return (
            faces[0][n - 1 - coords[y]][ != "X" and       # front
            faces[1][                                     # right
            faces[2]                                     # back
            faces[3]                                     # left
            faces[4]                                     # up
            faces[5]                                     # down
            
        and faces[


        
        

def solve(faces):
    """Given a list of maze faces (in front, right, back, left, up down order),
    gives a sequence of moves to move from (1, 1, 1) to (n-2, n-2, n-2)"""

    return ""

def parse_face(face_strs):
    face = []
    for row in face_strs:
        face.append(list(row))

    return face

def print_faces(faces):
    for face in faces:
        for row in face:
            print "".join(row)    
def main():
    while True:
        n = int(raw_input())

        if n == 0:
            break;

        faces = []
        for i in range(6):
            face_strs = []
            for j in range(n):
                face_strs.append(raw_input())

            faces.append(parse_face(face_strs))

        print solve(faces)

if __name__ == "__main__":
    main()

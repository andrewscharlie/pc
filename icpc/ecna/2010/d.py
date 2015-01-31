import math
import sys

def tween(start, end):
    """Calculates the angle (rads) required to move counter-clockwise
    from angle a to angle b (both rads)."""
    return (end - start + 2 * math.pi) % (2 * math.pi)
    
def count_shots(s, subject_angles, f):
    """Determines the minimum number of shots required for a camera
    with field of view f (rads) to capture the subjects at the
    specified angles (rads), starting at the subject at index s."""
    rotated_subject_angles = subject_angles[s + 1:] + subject_angles[0:s]
    
    shots = 1
    current_shot_start_angle = subject_angles[s]
    
    for subject_angle in rotated_subject_angles:
        if tween(current_shot_start_angle, subject_angle) > f:
            # End the new shot, start a new one
            shots += 1
            current_shot_start_angle = subject_angle

    return shots
    
def solve(camera, subjects, f):
    """Determines the minimum number of shots for a camera at the
    specified coordinates to capture all of the subjects at the
    specified coordinates with field of view f (rads)."""
    if (len(subjects) == 0): return 0
    
    subjects_relative = map(lambda(s): [s[0] - camera[0], s[1] - camera[1]], subjects)
    subject_angles = map(lambda(s): math.atan2(s[1], s[0]), subjects_relative)

    # Make sure all angles are in domain [0, 2 * pi)
    subject_angles = map(lambda(s): (s + 2 * (math.pi)) % (2 * math.pi), subject_angles)
    subject_angles.sort()

    # Count the minimum number of shots if we start shooting at each subject
    min_shots = sys.maxint
    for i in range(len(subject_angles)):
        min_shots = min(count_shots(i, subject_angles, f), min_shots)

    return min_shots

def main():
    case = 1

    while True:
        (n, x, y, f) = map(int, raw_input().split())

        if n == x == y == f == 0:
            break

        f = math.radians(f)

        # Collection subjects in form [[x1, y1], [x2, y2], ..., [xn, yn]]
        subjects = []
        while len(subjects) < n:
            subjects_unsplit = map(float, raw_input().split())

            subjects.extend(
                [subjects_unsplit[i:i+2] for i in range(0, len(subjects_unsplit), 2)])

        print "Case %d: %d" % (case, solve((x, y), subjects, f))
        case += 1
        
if __name__ == "__main__":
    main()

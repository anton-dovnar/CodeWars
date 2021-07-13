import re


def count_smileys(arr):
    smile_faces_counter = 0
    for face in arr:
        if bool(re.match(r'^[:;]{1}[-~]?[D)]{1}$', face)):
            smile_faces_counter += 1
    return smile_faces_counter

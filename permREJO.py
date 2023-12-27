#lets do a simple code to print out the perms of REJO

from itertools import permutations

def permJO(str):

    permlist = permutations(str)

    #Iterate the list
    for perm in list(permlist):
        print(''.join(perm))

if __name__ == "__main__":
    str = "REJO"
    permJO(str)
"""
Input 1 : [5, 10, 3, 7]
Output 1 : Fencing will be done with rods 3 and 7 - Max height: 10

----------------------------------------------------------------------

Input 2 : [3, 12, 8, 8]
Output 2 : No two rods found whose heights sum up to the maximum height.
"""

# Solution

def find_rod_pair(rod_heights):
    maxHeight = max(rod_heights)
    found = False
    for i in range(len(rod_heights)):
        for j in range(i + 1, len(rod_heights)):
            if rod_heights[i] + rod_heights[j] == maxHeight:
                print("Fencing will be done with rods {} and {} - Max height: {}".format(rod_heights[i], rod_heights[j], maxHeight))
                found = True
                return
            
    if found == False:
        print("No two rods found whose heights sum up to the maximum height.")

rod_heights = list(map(int, input().strip("[]").split(',')))
find_rod_pair(rod_heights)

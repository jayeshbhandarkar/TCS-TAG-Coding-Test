# Solution

def generateSeq(elements, result, path, used):
    if len(path) == len(elements):
        result.add(''.join(path))
        return
    
    for i in range(len(elements)):
        if used[i]:
            continue
        
        path.append(elements[i])
        used[i] = True
        generateSeq(elements, result, path, used)
        used[i] = False
        path.pop()

a, b, c = map(int, input().split())
elements = ['A'] * a + ['B'] * b + ['C'] * c
result = set()
path = []
used = [False] * len(elements)
generateSeq(elements, result, path, used)
print(*result)

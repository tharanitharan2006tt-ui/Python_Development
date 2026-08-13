import copy

original = [[1,2,3],[4,5,6],[7,8,9]]
shallow = copy.copy(original)

shallow[0][1] = 100
shallow[1][1] = 200

print(original)
print(shallow)

import copy
original = [[1,2],[3,4]]
deep = copy.deepcopy(original)

deep[0][1] = 100
deep[1][1] = 200

print(original)
print(deep)


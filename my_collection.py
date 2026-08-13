from collections import Counter, deque, OrderedDict, ChainMap, namedtuple, defaultdict
from email.policy import default

# ==============================
# Deque Example
# ==============================

dq = deque([10, 20, 30, 40, 50])

print("Before Rotate:", dq)
dq.rotate(-1)
print("After Rotate :", dq)

# ==============================
# Counter Example
# ==============================

data = [
    "apple", "banana", "orange",
    "apple", "orange", "banana",
    "apple", "a", "a", "a",
    "n", "n", "b"
]

count = Counter(data)

print("\nCounter:", count)
print("Most Common:", count.most_common())
print("Top 2 Most Common:", count.most_common(2))
print("Total Elements:", count.total())

# Update Counter
count.update(["apple", "grape", "grape"])
print("\nAfter Update:", count)

# Subtract Counter
count.subtract(["banana"])
print("After Subtract:", count)

# ==============================
# OrderedDict Example
# ==============================

od = OrderedDict()
od["a"] = 4
od["b"] = 5
od["c"] = 6
od["d"] = 7

print("\nOrderedDict:", od)

# Move 'a' to end
od.move_to_end("a")
print("After move_to_end('a'):", od)

# Update
od.update({"e": 8})
print("After Update:", od)

# Copy
od2 = od.copy()
print("Copied OrderedDict:", od2)

# Pop last item
print("Pop Last Item:", od.popitem())
print("After popitem():", od)

# Compare OrderedDict
l1 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
l2 = OrderedDict([("b", 1), ("a", 2), ("c", 3)])

print("l1:", l1)
print("l2:", l2)
print("Are Equal?:", l1 == l2)

# ==============================
# ChainMap Example
# ==============================

dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"B": 3, "C": 4}

cm = ChainMap(dic1, dic2)

print("\nChainMap:", cm)
print("A =", cm["A"])
print("B =", cm["B"])
print("C =", cm["C"])

# ==============================
# namedtuple Example
# ==============================

Student = namedtuple(
    "Student",
    ["name", "age", "course"],
    defaults=["Python"]
)

data = ["tom", 22, "Java"]
s = Student._make(data)

print("\nStudent:", s)

s1 = Student("tharani", 20, "Python")
print("As Dictionary:", s1._asdict())

s2 = s1._replace(age=22)
print("After Replace:", s2)

print("Fields:", s2._fields)
print("Field Defaults:", Student._field_defaults)

# ==============================
# Deque Methods
# ==============================

dq = deque([1, 2, 3])

dq.appendleft(4)
print(dq)

dq.appendleft(5)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

dq.extend([4, 5, 6])
print("ex",dq)

dq.extendleft([4, 5, 6])
print(dq)

dq.remove(2)
print(dq)

dq.rotate(-1)
# ==============================
# defaultdict with int
# ==============================

dd = defaultdict(int)
dd["a"] += 1
print(dd)

# ==============================
# defaultdict with list
# ==============================

dd_list = defaultdict(list)

dd_list["fruits"].append("apple")
dd_list["fruits"].append("banana")
dd_list["chocolate"].append("munch")

print(dd_list)
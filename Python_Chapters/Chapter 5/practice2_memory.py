# Define two variables with the same small integer
a = 10
b = 10

# Define two lists with the same content
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Print memory addresses (id) and comparison results
print(f"{a=}, {id(a)=}")
print(f"{b=}, {id(b)=}")
print(f"a is b: {a is b}")  # Should be True due to interning

print(f"\n{list1=}, {id(list1)=}")
print(f"{list2=}, {id(list2)=}")
# Should be False because lists are mutable and created separately
print(f"list1 is list2: {list1 is list2}")

# Modify a list and check if the address changes
old_id = id(list1)
list1.append(4)
new_id = id(list1)
print(f"\nModified list1: {list1}")
print(f"ID before: {old_id}")
print(f"ID after:  {new_id}")
print(f"ID changed? {old_id != new_id}")

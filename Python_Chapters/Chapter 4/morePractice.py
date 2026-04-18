even_numbers_to_20 = list(range(2, 21, 2))
second_holder = even_numbers_to_20.copy()
third_holder = even_numbers_to_20[::]

print(even_numbers_to_20, "\n", second_holder, "\n", third_holder)
print(f"* Is the content of original list equal to second copy? =>",
      even_numbers_to_20 == second_holder)
print(f"* Is original list exactly the same as second copy? =>",
      even_numbers_to_20 is second_holder)
print(f"* Is the content of original list equal to ",
      even_numbers_to_20 == third_holder)
print(f"* Is original list exactly the same as third copy?",
      even_numbers_to_20 is third_holder)
print("Ok")
print(f"* Is the content of second copy and third copy the same? =>",
      second_holder == third_holder)
print(f"* Is the second list exactly the same as the third list? =>",
      second_holder is third_holder)

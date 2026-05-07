def print_models(unprinted, completed):
    while unprinted:
        current = unprinted.pop()
        print(f"Printing: {current}")
        completed.append(current)

unprinted = ['phone case', 'pendant']
completed = []
print_models(unprinted, completed)
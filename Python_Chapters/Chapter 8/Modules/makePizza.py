def make_pizza2(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def pie(size, *flavors):
    """Summarize the pie we are about to make."""
    print(f"\nMaking a {size}-inch pie with the following flavors:")
    for flavor in flavors:
        print(f"- {flavor}")
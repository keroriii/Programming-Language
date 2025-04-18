def birthday_budget_planner():
    print("=== Birthday Celebration Budget Planner ===")
    print("Please enter estimated costs for each category:\n")
    
    # Predefined budget
    BUDGET = 5000
    
    while True:
        try:
            venue = float(input("Venue cost: $"))
            catering = float(input("Catering cost: $"))
            decorations = float(input("Decorations cost: $"))
            entertainment = float(input("Entertainment cost: $"))
            miscellaneous = float(input("Miscellaneous costs: $"))
            break
        except ValueError:
            print("Invalid input. Please enter numerical values only.\n")
            continue
    
    total_cost = 0.0
    total_cost += venue
    total_cost += catering
    total_cost += decorations
    total_cost += entertainment
    total_cost += miscellaneous
    
    print("\n=== Budget Summary ===")
    print(f"Total Estimated Cost: ${total_cost:.2f}")
    print(f"Predefined Budget: ${BUDGET:.2f}")
    
    if total_cost <= BUDGET:
        print("The estimated expenses are within the budget.")
    else:
        excess = total_cost - BUDGET
        print(f"Warning! Your estimated costs exceed the budget by ${excess:.2f}.")

birthday_budget_planner()
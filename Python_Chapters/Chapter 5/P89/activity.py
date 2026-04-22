# 5-12 & 5-13 Chapter 5 Review

# 5-12 Styling if Statements: All conditional tests in Chapter 5 files follow PEP 8:
# - 4-space indentation
# - if/elif/else aligned
# - Single space around operators (==, in, etc.)
# - No unnecessary parens
# - Reviewed: practice.py (5-1), P88/alien.py (5-3-5-7), this file (5-8-5-11), P77/conditionals.py, shopping_cart.py
# Styling verified - PEP 8 compliant, no changes needed.

print("5-12: if statement styling verified - PEP 8 compliant across Chapter 5.")

print('''5-13. Programming Ideas:
1. Games: Text-based RPG with if/else story branches; Pygame alien shooter extension.
2. Data: Analyze Python_Tutorials CSV weather data, alert if temp extremes.
3. Web: Flask app for user auth (5-10 style), conditional dashboards.
4. Personal: Expense tracker - if over budget, warn.
5. Quiz app: Score-based feedback with conditionals.
6. File sorter: if/elif for extensions into folders.
7. Simple AI: Rock-paper-scissors vs computer.

Next: Chapter 6 dictionary games.''')

# Example PEP 8 multi-line if (complex condition)
age = 25
is_student = True
income = 30000

if (
    (age >= 18 and age < 65) and
    (is_student or income < 50000)
):
    print("Eligible for discount.")
else:
    print("Not eligible.")

a = 12
b = 10

# walrus operator
#print("Sum is",c := a + b)

print(f"""
1. Sum is {(c := a + b)}
2. Sub is {(d := a - b)}
3. Mul is {(e := a * b)}
4. Div is {(f := a / b)}
""")

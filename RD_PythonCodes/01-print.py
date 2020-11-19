a = 12
b = 10
c = a + b
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum of {} and {} is {}".format(a,b,c))

#f-strings
print(f"Sum of {a} and {b} is {c}")
print(f"Sum of {a=} and {b=} is {c=}")

# Multiline Print
print(f"""
1. Sum is {a+b}
2. Sub is {a-b}
3. Mul is {a*b}
4. Div is {a/b}
""")

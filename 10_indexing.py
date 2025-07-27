# indexing = accessing elements of sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])

# :: everything in the string and
# ::2 ever 2nd character from the string
print(credit_number[::3])

last_digits = credit_number[-4:]

print(f"XXXX-XXXX-XXXX-{last_digits}")

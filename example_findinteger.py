value = "asdf 45gGH 96 gKd 02sa"

digits = []

for char in value:
    if char.isdigit():
        digits.append(char)

print(digits)

digits = re.findall(r'\d', value)
print(digits)
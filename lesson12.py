
#########################
# Ex #
#########################

product_code = "  book-582  "

clean_code = product_code.strip() # 1. Removes the surrounding spaces

name = clean_code[0:4] # 2. Takes the product name out of the clean text with a slice — the characters before the -.
print("Name:", name.upper())

number = clean_code[5:] # 3. Takes the number out of it with a second slice — the characters after the -.
print("Number:", number.zfill(6))

# 6. Prints the product name in uppercase, and the number padded to six digits using zfill().


print("Valid name:", name.isalpha()) # 4. Checks whether the product name contains only letters.
print("Valid number:", number.isdigit()) # 5. Checks whether the number contains only digits.







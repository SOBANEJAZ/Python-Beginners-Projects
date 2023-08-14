# Open the "currency data.txt" file
with open("currency data.txt") as f:
    date = f.readlines()

# Create an empty dictionary to store the currency data
currency_dict = {}

# Parse each line of the file and populate the currency dictionary
for lines in date:
    parsed = lines.split("\t")  # Split the line at the tab character
    currency_dict[parsed[0]] = parsed[1]  # Store currency symbol as key and exchange rate as value

# Prompt the user to enter the amount they want to convert
amount_input = int(input("Please enter the amount you want to convert: \t"))

# Print the available currencies for conversion
for item in currency_dict.keys():
    print(item)

# Prompt the user to enter the currency they want to convert to
currency_input = input("Please enter the currency you want to convert to: \t")

# Calculate the converted amount based on the exchange rate
actual_currency = amount_input * float(currency_dict[currency_input])

# Create the output message
output = f"\nYour {amount_input} PKR is equal to {actual_currency}{currency_input}"

# Print the output message
print(output)

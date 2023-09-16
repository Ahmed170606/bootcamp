def get_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in.")

def get_float(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Ongeldige invoer. Voer een getal in.")

# Voorbeeldgebruik van de aangepaste functies:
integer_value = get_integer("Voer een geheel getal in: ")
print(f"Je hebt het gehele getal ingevoerd: {integer_value}")

float_value = get_float("Voer een getal in: ")
print(f"Je hebt het getal ingevoerd: {float_value}")

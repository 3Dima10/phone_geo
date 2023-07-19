import phonenumbers
from phonenumbers import geocoder


def col(phone):
    phone1 = phonenumbers.parse(phone)

    return print(geocoder.description_for_number(phone1, "en"))

phone = str(input("Ведите номер телефона:"))

if __name__ == "__main__":
    col(phone=phone)
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

phone_number = int(input("Enter phone number (international format): "))
ch_number = phonenumbers.parse(phone_number, "CH")
print(geocoder.description_for_number(ch_number, "en"))
service_provider = phonenumbers.parse(phone_number, "RO")
print(carrier.name_for_number(service_provider, "en"))

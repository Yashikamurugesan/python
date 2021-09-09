import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number=input("enter your phonenumber: ")
number=ph.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number,'en'))
print(geocoder.description_for_number(number,'en'))



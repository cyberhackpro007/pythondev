

def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()


shipping_lable("Cyber", "Pro", "The", "Other" "ITGUY",
               street="123 Fake St.",
               apt="100", city="Plano",
               state="Tx",
               Zip= "75024")


def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()
    print(f"{kwargs.get('street')} {kwargs.get('apt')} {kwargs.get('city')} {kwargs.get('state')} {kwargs.get('Zip')}")


shipping_lable("Cyber", "Pro", "The", "Other" "ITGUY",
               street="123 Fake St.",
               apt="100", city="Plano",
               state="Tx",
               Zip="75024")
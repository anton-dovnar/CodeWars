import re


def validPhoneNumber(phoneNumber):
    return bool(re.match(r'^\(\d{3}\)\s{1}\d{3}\-\d{4}$', phoneNumber))

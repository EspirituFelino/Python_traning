import jsonpickle
from fixture.application import random_string
from model.contact import Contact
from model.group import Group
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

objects_number = 5
output_file_path = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        output_file_path = a

test_data=[
    Contact(first_name=first_name, middle_name=middle_name, last_name=last_name,
            nickname=nickname, title=title, company=company, address=address,
            homephone=homephone, mobilephone=mobilephone, workphone=workphone,
            email=email, email2=email2, email3=email3, homepage=homepage)
    for first_name in ["", random_string('first name', 10)]
    for middle_name in [random_string('middle name', 10)]
    for last_name in ["", random_string('last name', 10)]
    for nickname in [random_string('nickname', 10)]
    for title in [random_string('title', 10)]
    for company in [random_string('company', 10)]
    for address in ["", random_string('address', 10)]
    for homephone in ["", random_string('home phone', 10)]
    for mobilephone in [random_string('mobilephone', 10)]
    for workphone in [random_string('workphone', 10)]
    for email in [random_string('email', 10)]
    for email2 in [random_string('email2', 10)]
    for email3 in [random_string('email3', 10)]
    for homepage in [random_string('homepage', 10)]
]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", output_file_path)

with open(file_path, "w") as groups_file:
    jsonpickle.set_encoder_options("json", indent=2)
    groups_file.write(jsonpickle.encode(test_data))
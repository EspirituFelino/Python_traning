import jsonpickle
from fixture.application import random_string
from model.group import Group
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10),
          header=random_string("header", 10),
          footer=random_string("footer", 10))
    for i in range(n)
]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file_path, "w") as groups_file:
    jsonpickle.set_encoder_options("json", indent=2)
    groups_file.write(jsonpickle.encode(test_data))
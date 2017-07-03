from model.contact import Contact
import getopt
import json
import os.path
import random
import string
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
     getopt.usage()
     sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.digits + " " *10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", home="", mobile="", email="", address2="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    nickname=random_string("nickname", 10), company=random_string("company", 10),
                    address=random_string("address", 10), home=random_string("home", 10),
                    mobile=random_string("mobile", 10), work=random_string("work", 10),
                    fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10),
                    email3=random_string("email3", 10), address2=random_string("address2", 10),
                    notes=random_string("notes", 10), homepage=random_string("homepage", 10), phone2=random_string("phone2", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open (file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
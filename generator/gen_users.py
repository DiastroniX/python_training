from model.user import User
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [User(firstname="",
                lastname="",
                company="",
                address="",
                home="",
                work="",
                mobile="",
                phone2="",
                email="",
                email2="",
                email3="",
                address2="")] + [
    User(firstname=random_string("firstname", 12), lastname=random_string("lastname", 12), company=random_string("company", 15),
         address=random_string("address", 30), home=random_string("hometel", 15), work=random_string("worktel", 10),
         mobile=random_string("mobiletel", 10), phone2=random_string("phone2tel", 10), email=random_string("email@", 10),
         email2=random_string("email2@", 10), email3=random_string("email3@", 10), address2=random_string("address2", 20),)
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
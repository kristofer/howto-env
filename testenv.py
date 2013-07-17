import os

print os.getenv("SOMENAMEOFSOMETHING")

mySpecialVariable = os.getenv("SOMENAMEOFSOMETHING")

print "Got an enviroment variable: %s" % mySpecialVariable

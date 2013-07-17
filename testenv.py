import os

print os.getenv("SOMENMEOFSOMETHING")

mySpecialVariable = os.getenv("SOMENMEOFSOMETHING")

print "Got an enviroment variable: %s" % mySpecialVariable

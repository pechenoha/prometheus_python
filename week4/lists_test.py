import sys

print "*********************************"
print "all"
print sys.argv
print str(len(sys.argv)-1) + " user's args"
print "=========="
print "[1::]"
print sys.argv[1::]
print str(len(sys.argv[1::])) + " items"
print "=========="
print "[1::3]"
print sys.argv[1::3]
print str(len(sys.argv[1::3])) + " items"
print "=========="
print "[1::6]"
print sys.argv[1::6]
print str(len(sys.argv[1::6])) + " items"
print "=========="
import sys

s = "Line1-abcdef   \nLine2-abc \nLine4-abcd";
print s.split( );
print s.split(' ', 6 );

#tuple
tu = ('lol', 1.0, 'test', 3, '4str')
print tu
print tu[3:5]
print tu[3]


test_int = -2147483647
test_int2 = -2147483648
test_int3 = -2147483649
print "type of -2147483647: " + str(type(test_int))
print "type of -2147483648: " + str(type(test_int2))
print "type of -2147483649: " + str(type(test_int3))
print test_int3


s = 'qwe'
print s[0]
print s[0][0][0]
print s[0][0][0][0][0][0]



tst_1 = 23.187
print "that's a %s: %10.5f" % ("number", tst_1)
print "that's a %s: %010.5f" % ("number", tst_1)


tst_tuple = (0, 1, [2.0, 2.1, 2.2, 2.3])
print tst_tuple
# tst_tuple[0] = 999 - error
tst_tuple[2][0] = 99999
print tst_tuple

print 2 != 3
print 2 <> 3

print "test (7 degits should be there): %07d" % (28)


my_dict = {0 : "zero", "1": "one", 2.0: "two"}
print my_dict[0.0]
# print my_dict[1] - doesn't work
# print my_dict["2"] - doesn't work
print my_dict[2]
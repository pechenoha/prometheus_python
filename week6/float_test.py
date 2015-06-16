def user_test(a,b):
    return a * b
result_test = user_test(0.2, 6)
result_right = 1.2
if result_test == result_right:
    print 'OK'
else:
    print 'ERROR'
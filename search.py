#a is list
a = [1,2,3,4,5]
#It will search entire list whthere value is there or not
check = raw_input("Enter which you want to search in a list : ")
if check not in a:
    a.append(check)
    print "%s is not in the list we are adding into list" %check
    print "This is the latest list : %s" %a
else:
    print a

#b is dictionary

b = {'c':4,'d':5,'e':7}
key = raw_input("Enter which key you want to search in a dictionary : ")
if key in b:
    print "Value of %s is %s" %(key,b[key])
else:
    print "There is no %s as key in Dictionary" %key

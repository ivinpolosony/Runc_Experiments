import time  	

# Open a file
#fo = open("foo.txt", "wb")
#print "Name of the file: ", fo.name
for x in range(0, 300):
	#print "COUNT %d" %(x)
	fo = open("foo.txt", "wb")
	#print "Name of the file: ", fo.name
	fo.write("Count========>%d \n" %(x) );
	time.sleep( 2 )
	fo.close()

# Close opend file
#fo.close()

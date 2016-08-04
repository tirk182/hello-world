#! /usr/bin/python

# simple countdown example 
import time

print 'Simple countdown script '
counter = 5
while counter >=0:
	print '...' + str(counter)
	time.sleep(1)
	counter -=1
	
	if counter <0:
		print '### BOOM! ### '
	


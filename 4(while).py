# declare variables with int values
left = 34 
right = 67
# start a while cycle 
while left <= right :
    	# condition for the cycle if left  divided on 2 not  equal 1 then print left
	if left % 2 != 1:
		print(left)
		# inc left by one to iterate to every in range from left to right. sooner or later it will cease to be True and cycle breaks.
	left += 1

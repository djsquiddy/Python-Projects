# Name : Dylan Jones

def sblr_tank_water_volume( tank, w, h, wl ) :
	volume = 0	
	for column in tank.values() :
		if ( column < wl ) :
			volume = volume + wl - column
	
	return volume
	
myTank = { 0 : 1, 1 : 2, 2 : 1 }
print "The water level of the tank is: " + str( sblr_tank_water_volume( myTank, 3, 3, 3 ) )

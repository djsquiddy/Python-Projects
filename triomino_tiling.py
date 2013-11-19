# Name : Dylan Jones
from random import randint

currentPiece = 1

def set_missing( board, size ) :
	board[ 1 ][ 0 ] = '?'
	return 0, 1
	
def display_board( board, size ) :
	for row in range( size ) :
		for column in range( size ) :
			print board[ row ][ column ], "\t",
		print "\n"
	print "\n"

def clear_board( board, size ) :
	for row in range( size ) :
		for column in range( size ) :
		 board[ row ][ column ] = 0
		 
def create_trominos( board, x, y, size, totallSize ) :
	global currentPiece
	display_board( board, totallSize )   
	half_pos = size / 2	
	if size <= 2 :
		if x < half_pos :
			if y < half_pos :
				base_topLeft( board, x, y )
			else :
				base_bottomLeft( board, x, y )
		else :
			if y < half_pos :
				base_topRight( board, x, y )
			else :
				base_bottomRight( board, x, y )
				
		currentPiece = currentPiece + 1
	else : 
		x_half = half_pos - 1
		y_half = half_pos - 1
		if x < half_pos :
			if y < half_pos :
				place_topLeft( board, half_pos )
				currentPiece = currentPiece + 1 
				create_trominos( board, x, y, half_pos, totallSize )
				print x_half, y_half
				create_trominos( board, x_half + 2, y_half - 1, half_pos, totallSize ) # top right
				create_trominos( board, x_half + 2, y_half + 2, half_pos, totallSize ) # bottom right
				create_trominos( board, x_half - 1, y_half + 2, half_pos, totallSize ) # bottom left
			else :
				place_bottomLeft( board, half_pos )
				currentPiece = currentPiece + 1 
				create_trominos( board, x, y, half_pos, totallSize )
				create_trominos( board, x_half + 2, y_half + 2, half_pos, totallSize ) # bottom right
				create_trominos( board, x_half - 1, y_half - 1, half_pos, totallSize ) # top left
				create_trominos( board, x_half + 2, y_half - 1, half_pos, totallSize ) # top right
		else :
			if y < half_pos :
				place_topRight( board, half_pos )
				currentPiece = currentPiece + 1 
				create_trominos( board, x, y, half_pos, totallSize )
				create_trominos( board, x_half - 1, y_half + 2, half_pos, totallSize ) # bottom left
				create_trominos( board, x_half + 2, y_half + 2, half_pos, totallSize ) # bottom right
				create_trominos( board, x_half + 2, y_half - 1, half_pos, totallSize ) # top right
			else :
				place_bottomRight( board, half_pos )
				currentPiece = currentPiece + 1 
				create_trominos( board, x, y, half_pos, totallSize )
				create_trominos( board, x_half - 1, y_half + 2, half_pos, totallSize ) # bottom left
				create_trominos( board, x_half - 1, y_half - 1, half_pos, totallSize ) # top left
				create_trominos( board, x_half + 2, y_half - 1, half_pos, totallSize ) # top right

		
def tile_board_with_trominos( board, size ) :
	global currentPiece
	currentPiece = 1
	clear_board( board, size )
	x, y = set_missing( board, size )
	create_trominos( board, y, x, size, size )
	display_board( board, size ) 
	
def place_topLeft( board, half_pos ) :
	print "place top left"
	board[ half_pos ][ half_pos ] = currentPiece
	board[ half_pos - 1 ][ half_pos ] = currentPiece
	board[ half_pos ][ half_pos - 1 ] = currentPiece
	
def place_topRight( board, half_pos ) :
	print "place topRight"
	board[ half_pos ][ half_pos ] = currentPiece
	board[ half_pos ][ half_pos - 1 ] = currentPiece
	board[ half_pos - 1 ][ half_pos - 1 ] = currentPiece
	
def place_bottomLeft( board, half_pos ) :
	print "place bottomLeft"
	board[ half_pos ][ half_pos ] = currentPiece
	board[ half_pos - 1 ][ half_pos ] = currentPiece
	board[ half_pos - 1 ][ half_pos - 1 ] = currentPiece
	
def place_bottomRight( board, half_pos ) :
	print "place bottomRight"
	board[ half_pos - 1 ][ half_pos - 1 ] = currentPiece
	board[ half_pos ][ half_pos - 1 ] = currentPiece
	board[ half_pos - 1 ][ half_pos ] = currentPiece
	
def base_topLeft( board, x, y ):
	global currentPiece
	print "base top left"
	board[ y ][ x ] = currentPiece
	board[ y + 1 ][ x ] = currentPiece
	board[ y ][ x + 1 ] = currentPiece
	
def base_topRight( board, x, y ) :
	global currentPiece
	print "base top right"
	board[ y ][ x ] = currentPiece
	board[ y + 1 ][ x ] = currentPiece
	board[ y ][ x - 1 ] = currentPiece
	
def base_bottomLeft( board, x, y ) :
	global currentPiece
	print "base bottom left"
	board[ y ][ x ] = currentPiece
	board[ y ][ x + 1 ] = currentPiece
	board[ y - 1 ][ x ] = currentPiece
	
def base_bottomRight( board, x, y ) :
	global currentPiece
	print "base bottom right"
	board[ y ][ x ] = currentPiece
	board[ y ][ x - 1 ] = currentPiece
	board[ y - 1 ][ x ] = currentPiece

board_22 = \
[ \
	[ 0, 0 ],\
	[ 0, 0 ] \
]

board_44 = \
[ \
	[0, 0, 0, 0], \
	[0, 0, 0, 0], \
	[0, 0, 0, 0], \
	[0, 0, 0, 0] \
]

tile_board_with_trominos( board_22, 2 )
tile_board_with_trominos( board_44, 4 )
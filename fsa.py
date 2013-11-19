# Name: Dylan Jones
# file: fsa
import re

def tran_table_lookup( sym, state, tran_tbl ) :
	if sym in tran_tbl :
		return tran_tbl.get( sym, [] ).get( state, [] )
	else :
		return []
		
def tran_table_epsilon_lookup( state, tran_tbl ) :
	return tran_table_lookup( '', state, tran_tbl )

def get_start_state( fsa ): return fsa[ 0 ]
def get_fin_states ( fsa ): return fsa[ 1 ]
def get_tran_table ( fsa ): return fsa[ 2 ]

def match_fsa( txt, index, textLen, cur_state, fin_states, tran_tbl ) :
	if ( index == textLen ) :
		if ( cur_state in fin_states ) :
			return True
		else :
			next_epsilon_states = tran_table_epsilon_lookup( cur_state, tran_tbl )
			for state in next_epsilon_states :
				if state in fin_states : 
					return True
				else : 
					return False
	else :
		next_states = tran_table_lookup( txt[ index ], cur_state, tran_tbl )
		next_epsilon_states = tran_table_epsilon_lookup( cur_state, tran_tbl )
		
		if  next_states == [] and next_epsilon_states == [] :
			return False
		else :
			for state in next_states :
				rslt = match_fsa( txt, index + 1, textLen, state, fin_states, tran_tbl )
				if rslt == True :
					return True
			for state in next_epsilon_states :
				rslt = match_fsa( txt, index, textLen, state, fin_states, tran_tbl )
				if rslt == True : 
					return True
			return False

tran_tbl_01 = {}
tran_tbl_01[ 'a' ] = { 1: [ 2 ] }
tran_tbl_01[ 'b' ] = { 2: [ 1 ] }

fsa_01 = ( 1, [1], tran_tbl_01 )


tran_tbl_02 = {}
tran_tbl_02[ '' ] = { 1 : [ 3 ] }
tran_tbl_02[ 'a' ] = { 1 : [ 2 ], 2 : [ 1 ], 3 : [ 4 ], 4 : [ 3 ] }
tran_tbl_02[ 'b' ] = { 1 : [ 3 ], 2 : [ 4 ], 3 : [ 1 ], 4 : [ 2 ] }

fsa_02 = ( 1, [3], tran_tbl_02 )

print tran_tbl_01
print tran_tbl_02

for text in [ '', 'ab', 'abab', 'ababab', 'abbb', 'aaaa', 'aaa', 'aaaaaa', 'b', 'bbb', 'bbbbb', 'abbaabba' ] :
	print "fsa_01, on text : " + text + " = " + str( match_fsa( text, 0, len( text ), get_start_state( fsa_01 ), get_fin_states( fsa_01 ), get_tran_table( fsa_01 ) ) )
	print "fsa_02, on text : " + text + " = " + str( match_fsa( text, 0, len( text ), get_start_state( fsa_02 ), get_fin_states( fsa_02 ), get_tran_table( fsa_02 ) ) )


	re_match_pat_01 = re.search( r'(ab)+|((aa|bb|(ab|ba)(aa|bb)*(ba|ab))*(b|(ab|ba)(bb|aa)*a))', text )
	if re_match_pat_01 :
		print re_match_pat_01.group() + " passed the regex"
	else :
		print text + " did not pass the regex"
	print "\n\n"

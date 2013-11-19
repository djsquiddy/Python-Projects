import re

def process_student_record_line( line ) :
	re_match_initials = re.search( r'([A-Z]\.[A-Z]\.)', line )
	re_match_gpa = re.search( r'GPA=\d\.((\d{3})|(\d{2})|(\d))', line )
	re_match_a_num = re.search( r'A(\d){4}', line )
	re_match_date = re.search( r'(\d){2}\/(\d){2}\/(\d){2}', line )
	student = {}
	
	if re_match_initials :
		student[ "Initials" ] = re_match_initials.group()
	else :
		student[ "Initials" ] = 'N/A'
		
	if re_match_date :
		student[ "BirthDate" ] = re_match_date.group()
	else :
		student[ "BirthDate" ] = 'N/A'
		
	if re_match_a_num :
		student[ "ANUM" ] = re_match_a_num.group()
	else :
		student[ "ANUM" ] = 'N/A'
		
	if re_match_gpa :
		student[ "GPA" ] = re_match_gpa.group()
	else :
		student[ "GPA" ] = 'N/A'
		
	
	
	return student

records = ['J.P.;GPA=3.5;A1927;11/01/91',\
'GPA=4.0;N.K.;12/01/90;A2732',\
'A9803;GPA=3.25;M.D.;10/03/87', \
'05/01/89;A1248;GPA=2.87;D.W.',\
'GPA=3.87;L.M.;03/17/89;A6752']

for test in records :
	print str( process_student_record_line( test ) )

	print '\n\n'
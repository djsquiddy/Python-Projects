#!usr/bin/python
# Name : Dylan
# terminal command : data_normalize.py "student_records.txt" "init.txt" "dob.txt" "gender.txt" "gpa.txt"
import sys
import re

# Parse the student_records file into different students and into different sections
def parse_file( file_name ) :
	students_text = open_file( file_name )
	students = []
	
	for currentStudent in students_text :
		student = process_student_record_line( currentStudent )
		if student[ "ANUM" ] != "N/A" : # if the record is N/A don't add it the student records
			students.append( process_student_record_line( currentStudent ) )

	return students
	
def process_student_record_line( line ) :
	re_matchs = search_student_record( line )
	hash_keys = [ "ANUM", "Initials", "GPA", "BirthDate", "Gender" ]
	student = {}
	
	for x in range( 5 ) :
		check_current_student_record( student, hash_keys[ x ], re_matchs[ x ] )
	
	return student

# Check to see if the regex found the correct info
def check_current_student_record( student, hash_key, re_match ) :
	if re_match :
		student[ hash_key ] = re_match.group()
	else :
		student[ hash_key ] = 'N/A'
	return

def search_student_record( line ) :
	re_matchs = []
	re_matchs.append( re.search( r'A((\d){4})', line ) ) # anum
	re_matchs.append( re.search( r'([A-Z]\.[A-Z]\.)', line ) ) ) # initials
	re_matchs.append( re.search( r'(\d\.((\d{3})|(\d{2})|(\d)))', line ) ) # gpa
	re_matchs.append( re.search( r'(\d){2}\/(\d){2}\/(\d){2}', line ) ) # birthdate
	re_matchs.append( re.search( r'(M|F)', line ) ) # gender
	return re_matchs
	
# File Handling
def open_file( file_name ) :
	file_handle = open( file_name, 'r' ) # open the file for reading
	file_text = file_handle.readlines() # read file into a string
	file_handle.close() # close the file
	return file_text
	
def write_file( file_name, student_info ) :
	file_handle = open( file_name, 'w' ) # open the file for writing
	old = sys.stdout # save the current stdout
	sys.stdout = file_handle # change the stdout to out put to the file handle
	
	# add the current student info to the file
	for info in student_info :
		print info 

	sys.stdout = old # change the stdout back to the old old one
	file_handle.close() # close the file
	
def seperate_student_info( students ) :
	students_info 	= [ [], [], [], [] ]
	hash_keys = [ "Initials", "BirthDate", "Gender", "GPA" ]
	
	for student in students :
		currentStudent = []
		anum = student[ "ANUM" ]
		for key in hash_keys :
			currentStudent.append( str( anum ) + '\t' + str( student[ key ] ) )
	
		for x in range( 4 ) :
			add_to_student_info( student_info[ x ], currentStudent[ x ] )
	
	write_student_info( student_info )

def add_to_student_info( student_info, currentStudent ) :
	students_info.append( currentStudent )
		
def write_student_info( student_info ) :
	write_file( sys.argv[ 2 ], students_info[ 0 ] ) # write to the init.txt
	write_file( sys.argv[ 3 ], students_info[ 1 ] ) # write to the dob.txt
	write_file( sys.argv[ 4 ], students_info[ 2 ] ) # write to the gender.txt
	write_file( sys.argv[ 5 ], students_info[ 3 ] ) # write to the gpa.txt

students = parse_file( sys.argv[ 1 ] ) # get the file text from the first file argument
seperate_student_info( students ) # seperate the students records and then write them to the files
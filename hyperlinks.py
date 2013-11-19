# Name : Dylan Jones
import re
		
def get_hyperlink_elements( string ) : 
	hyperlink = []

	re_match_attribute = re.compile( r'(?<= )(href|title|class)="(.*?)"', re.IGNORECASE )
	re_match_name = re.compile( r'(?<=(">| >))(.*?)(?=</a>)', re.IGNORECASE )
	
	attribute_result = re_match_attribute.findall( string )
	name_result = re_match_name.findall( string )
	
	for list in attribute_result :
		hyperlink.append( ( list[0], list[1] ) )
			
	for list in name_result :
			hyperlink.append( ( "name", list[1] ) )
			
	return hyperlink

tests = [ \
	'<a href="/wiki/State_highway" title="State highway">state highway</a>', \
	'<a href="/wiki/U.S." title="U.S." class="mw-redirect">U.S.</a>', \
	'<a href="/wiki/Utah" title="Utah">Utah</a>', \
	'<a href="/wiki/Interstate_84_(Utah)" title="Interstate 84 (Utah)" class="mw-redirect">Interstate 84</a>', \
	'<a href="/wiki/U.S._Route_89_(Utah)" title="U.S. Route 89 (Utah)" class="mw-redirect">U.S. Route 89</a>', \
	'<a href="/wiki/Nevada" title="Nevada">Nevada</a>', \
	'<a href="/wiki/Wyoming" title="Wyoming">Wyoming</a>', \
	'<a href="/wiki/First_Transcontinental_Railroad" title="First Transcontinental Railroad">First Transcontinental Railroad</a>', \
	'<a href="/wiki/California_Trail" title="California Trail">California Trail</a>', \
	'<a href="/wiki/Bear_Lake_(Utah-Idaho)" title="Bear Lake (Utah-Idaho)" class="mw-redirect">Bear Lake</a>', \
	'<a href="/wiki/Utah_Scenic_Byways" title="Utah Scenic Byways">Utah Scenic Byways</a>', \
	'<a href="/wiki/Interstate_70_in_Utah" title="Interstate 70 in Utah">I-70</a>', \
	'<a href="/wiki/Utah_State_Route_72" title="Utah State Route 72">SR-72</a>', \
	'<a href="/wiki/Huntington_State_Park" title="Huntington State Park">Huntington State Park</a>', \
	'<a href="/wiki/Price,_Utah" title="Price, Utah">Price</a> at <a href="/wiki/Utah_State_Route_55" title="Utah State Route 55">SR-55</a>', \
	'<a href="/wiki/U.S._Route_6_(Utah)" title="U.S. Route 6 (Utah)" class="mw-redirect">US-6</a>', \
	'<a href="/wiki/U.S._Route_50_(Utah)" title="U.S. Route 50 (Utah)" class="mw-redirect">/50</a>' ]
	
	
for hyperlink in tests :
	print get_hyperlink_elements( hyperlink )
	print "\n\n"
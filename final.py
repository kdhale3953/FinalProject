import arcpy
from arcpy import env

env.workspace = "P:Python/FinalProJ/GIST3/Data"
df = "P:Python/FinalProj/GIST3/Data"

print("Checking 4-1 item 2:")
print("Should have DataFrame named 'Proposed Rail Station'")

mxd = arcpy.mapping.MapDocument("P:/Python/FinalProj/GIST3/Maps/Tutorial 4-1.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[0]
if df.name != "Proposed Rail Station":
    print "Name should be Proposed Rail Station.  Your name was: {}".format(df.name)
    else:
        print "PASS"
	print "\n"


	###
	### Code to check here
	###
	#if arcpy.Exists("Proposed Rail Stations"):
	#    return "True"
	##arcpy.Exists(df = "Proposed Rail Stations")
	##    

	print("Checking 4-1 item 4:")
	print("""Should have layer named 'Property Base Group'
	         in DataFrame 'Proposed Rail Station'""")
		 if arcpy.Exists("Proposed Rail Station"):
		     print "Proposed Rail Station exists."
		         print "PASS"

			 else:
			     print "Proposed Rail Station does not exist."
			     print "\n"

			     ###Checking to see if Property base group layer exists
			     ###code to check
			     ###
			     print "Checking 4-1 item 5:"
			     print ("Checking to see if Property Base Group Layer exists:")
			     if arcpy.Exists("Property Base Group"):
			         print "Property Base Group Exists."
				     print "PASS"
				     else:
				         print "Property Base group does not exist."
					 print "\n"

					 ###Checking to see if Property base group layer exists
					 ### survey control points was named monument and later
					 ### in the exercise we are asked to change the
					 ### name to survey control points 
					 ###
					 print "Checking 4-1 item 6:"
					 print "Checking to see if Survey Control Points exists:"
					 if arcpy.Exists("Survey Control Points"):
					     print "Survey Control Points Exists."
					         print "PASS"
						 else:
						      print "Survey control points does not exist. Your layers are:"
						      print "\n"
						           

							   ###checking to see if North Oleander Station Data was added to the map
							   ####
							   print "Checking 4-1 item 7:"
							   print "Checking to see if North Oleander Station data was added to the map:"
							   if arcpy.Exists("North Oleander Station Group"):
							       print "North Oleander Data has been added to the map."
							           print "PASS"
								   else:
								       print "North Oleander Station Data has not been added to the map"
								       print "\n"


								       ###Checking to see if building layer exists
								       ###code to check
								       ###
								       print "Checking 4-1 item 8:"
								       print "Checking to see if buildings layer is added to the map:"
								       if arcpy.Exists("buildings"):
								           print "'Buildings' layer has been added to the map"
									       print "PASS"
									       else:
									           print "The buildings layer has not been added to the map."
										   print "\n"

										   ###checking to see if the rail lines layer has been added to the map
										   ###
										   print "Checking 4-1 item 9:"
										   print "Checking to see if 'rail lines' has been added to the map:"
										   if arcpy.Exists("rail lines"):
										       print "'rail lines' layer has been added to the map"
										           print "PASS"
											   else:
											       print "'rail lines' layer has not been added to the map"
											       print "\n"

											       ####checking to see the if the bookmark has been loaded
											       ###

											       print "Checking 4-1 item 10:"
											       print "Checking to see if the extent is set for the bookmark:"
											       df = arcpy.mapping.ListDataFrames(mxd)[0]
											       if len(arcpy.mapping.ListBookmarks(mxd)) == 0:
											           print("Failed to load bookmark.")
												   else:
												       print "Bookmark has been loaded."


												       ##for bkmk in arcpy.mapping.ListBookmarks(mxd, "", df):
												       ##    print bkmk.name
												       for bkmk in arcpy.mapping.ListBookmarks(mxd, "", df):
												           print bkmk


													   

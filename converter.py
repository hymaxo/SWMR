from os import path
import os
from pydub import AudioSegment
from xmlgen import xmlgen
import shutil

try:
	os.mkdir("out")
except:
	pass
	
src = input("Enter file name: ")
destination_path = input("Enter FULL path to main StormWorks folder (Example: C:/Program Files (x86)/Steam/steamapps/common/Stormworks): ") + "/rom/audio/music"

#importing file from location by giving its path
sound = AudioSegment.from_mp3(src)
StrtSec = -15
EndSec = 0
ranges = int((sound.duration_seconds // 15) + 2)
print ("Debug info: \n Count of ogg files: "  + str(ranges))

for i in range (1, ranges):
	StrtSec = StrtSec + 15
	EndSec = EndSec + 15
	
	# Time to milliseconds conversion
	StrtTime = StrtSec*1000
	EndTime = EndSec*1000

	# Opening file and extracting portion of it
	extract = sound[StrtTime:EndTime]
	
	if i <= 9:
		fileout = "out/main_theme_0" + str(i) + ".ogg"
		fileoutname = "main_theme_0" + str(i) + ".ogg"
	else:
		fileout = "out/main_theme_" + str(i) + ".ogg"
		fileoutname = "main_theme_" + str(i) + ".ogg"

	# Saving file in required location
	extract.export(fileout, format="ogg")

	os.remove(destination_path + "/" + fileoutname)
	new_location = shutil.move(fileout, destination_path)

xmlgen(ranges)

os.remove(destination_path + "/main_theme.xml")
new_location = shutil.move("out/main_theme.xml", destination_path)

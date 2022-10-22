from os import path
from pydub import AudioSegment
from xmlgen import xmlgen

src = input("Enter file name: ")

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
	else:
		fileout = "out/main_theme_" + str(i) + ".ogg"

	# Saving file in required location
	extract.export(fileout, format="ogg")

xmlgen(ranges)
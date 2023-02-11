
def xmlgen(filecount):
	f = open('out/main_theme.xml', 'w')
	f.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
	f.write("<audio_tile>" + '\n')
	f.write("	<tiles>" + '\n')
	for i in range (0, filecount):
		if i <= 9:
			f.write('		<tile file_name="audio/music/main_theme_0' + str(i) + '.ogg" data_size="2646000"/>' + '\n')
		else:
			f.write('		<tile file_name="audio/music/main_theme_' + str(i) + '.ogg" data_size="2646000"/>' + '\n')

	f.write("	</tiles>" + '\n')
	f.write("</audio_tile>" + '\n')

import shutil, os

file = open('fold_frontal_4_data.txt', 'r')

for line in file:
	values = line.split()
	img = 'faces/' + values[0] +'/'+ 'coarse_tilt_aligned_face.' + values[2] + '.' + values[1]

	if values[3] == "(0-2)":
		shutil.copy(img, 'Data/Age/(0-2)')
	elif values[3] == "(4-6)":
		shutil.copy(img, 'Data/Age/(4-6)')
	elif values[3] == "(8-12)":
		shutil.copy(img, 'Data/Age/(8-12)')
	elif values[3] == "(15-20)":
		shutil.copy(img, 'Data/Age/(15-20)')
	elif values[3] == "(25-32)":
		shutil.copy(img, 'Data/Age/(25-32)')
	elif values[3] == "(38-43)":
		shutil.copy(img, 'Data/Age/(38-43)')
	elif values[3] == "(48-53)":
		shutil.copy(img, 'Data/Age/(48-53)')
	elif values[3] == "(60-100)":
		shutil.copy(img, 'Data/Age/(60-100)')
	
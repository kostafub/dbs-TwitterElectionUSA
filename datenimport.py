# *.xlsx laden und lesen
from openpyxl import load_workbook
# Verbindung zur Datenbank und string-escape für sql
import pg 
pg=pg.connect(dbname='election', user='julez', passwd='haha')

# workbook mit aufbereiteten Daten laden
wb = load_workbook('american-election-repair.xlsx')
ws = wb['bereinigt']
wslen = ws.max_row-1

# Hilfsfunktion ist_enthalten
def ist_enthalten (cell_value, liste):
	lenListe = len(liste)
	for name in range(0,lenListe):
		if cell_value==liste[name]:
			return True
		else:
			continue
		return False
		
# insert in relation handle
# projektion der möglichen handles
values = []
ids = []
inhalt = []
zaehler = 0
for row in range(0, wslen):
	cell_handle_id = "{col}{row}".format(col='A', row=(row+2))
	cell_handle = "{col}{row}".format(col='B', row=(row+2))
	if (zaehler == 0):
		ids = [ws[cell_handle_id].value]
		values = [ws[cell_handle].value]
		inhalt = [str('INSERT INTO handle VALUES ('+ str(ws[cell_handle_id].value) + ', '+ str('\'' + ws[cell_handle].value) + '\')')]
		zaehler +=1
	else:
		if (ist_enthalten(ws[cell_handle_id].value, ids)):
			continue
		else:
			ids.append(ws[cell_handle_id].value)
			values.append(ws[cell_handle].value)
			zaehler +=1
			inhalt.append(str('INSERT INTO handle VALUES ('+ str(ws[cell_handle_id].value) + ', '+ str('\'' + ws[cell_handle].value) + '\')'))
for eintrag in range(0, len(ids)):
	#print(inhalt[eintrag])
	#pg.query(inhalt[eintrag])

# insert in relation tweet
for row in range(0, wslen):
	cell_handle_id = "{col}{row}".format(col='A', row=(row+2))
	cell_time = "{col}{row}".format(col='F', row=(row+2))
	cell_fav = "{col}{row}".format(col='G', row=(row+2))
	cell_retw = "{col}{row}".format(col='H', row=(row+2))
	cell_text = "{col}{row}".format(col='C', row=(row+2))
	cell_auth = "{col}{row}".format(col='I', row=(row+2))
	inhalt = str('INSERT INTO handle VALUES ('+ str(ws[cell_handle_id].value) + ', ' + str(ws[cell_time].value)+ ', ' + str(ws[cell_fav].value) + ', '+ str(ws[cell_retw].value)+ ', \''+ pg.escape_string(str(ws[cell_text].value)) + '\', '+ str(ws[cell_auth].value) + '\')')
	#print(inhalt)
	#pg.query(inhalt)

# insert in relation hashtag
for row in range(0, wslen):
	cell_tag_id = "{col}{row}".format(col='D', row=(row+2))
	cell_tag = "{col}{row}".format(col='E', row=(row+2))
	if (str(ws[cell_tag].value) == 'NULL'):
		inhalt = str('INSERT INTO handle VALUES ('+ str(ws[cell_tag_id].value) + ', '+ pg.escape_string(str(ws[cell_tag].value)) + ')')
	else:
		inhalt = str('INSERT INTO handle VALUES ('+ str(ws[cell_tag_id].value) + ', '+ str('\'' + ws[cell_tag].value) + '\')')
	#print(inhalt)
	#pg.query(inhalt)

# insert in relation has
for row in range(0, wslen):
	cell_time = "{col}{row}".format(col='F', row=(row+2))
	cell_handle_id = "{col}{row}".format(col='A', row=(row+2))
	cell_tag_id = "{col}{row}".format(col='D', row=(row+2))
	inhalt = str('INSERT INTO handle VALUES ('+ str(ws[cell_time].value) + ', '+ str(ws[cell_handle_id].value) + ', ' + str(ws[cell_tag_id].value) + ')')
	#print(inhalt)
	#pg.query(inhalt)
	
	
	
	

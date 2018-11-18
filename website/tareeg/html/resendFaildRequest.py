#!/usr/bin/python
import os

file = open("faild.csv","r")

for line in file:
 if (len(line) > 1) and (not line.startswith("#")):
  request = line.split(',')
  rName = request[2]
  rEmail = request[3]
  table = request[4]
  latmax = request[5]
  lonmax = request[6]
  latmin = request[7]
  lonmin = request[8]
  command =  'java -jar -Xmx9024m /home/yackel/public_html/app/webroot/osme/OSMExtractor.jar '+ rName+' '+rEmail+' '+ table+' '+ latmax+' '+ lonmax+' '+ latmin+' '+lonmin+' /media/osmeDataset/spatialHadoopPhase/ /home/yackel/public_html/app/webroot/downloads/userData/ /media/Louai/usersData/email/ 1'
  os.system(command)
  print command
file.close()

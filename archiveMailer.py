#!/usr/bin/python
import MySQLdb
import datetime
import os
time = datetime.datetime.now()

print time
fileName = "backup"+ time.strftime("%c") + ".txt"
fileName= ''.join(fileName.split())
print fileName
fileObject = open(fileName, "a")
db = MySQLdb.connect("localhost", "username", "password", "dbName")

cursor = db.cursor()

#get everything from text in order ascending(we don't need to backup the entire database since text is basically the only thing that matters and such an archive is silly otherwise if we go further
textSelectorText = "SELECT * FROM text"
cursor.execute(textSelectorText)
results = cursor.fetchall()
i=0
for row in results:
        fileObject.write(row[1]);
        fileObject.write("---------------------------------------------------------------------------------------------------------------------")
       
fileObject.close()

#zip directory
zipCommand = 'zip -r mediawikiimages.zip /var/lib/mediawiki/images/'
os.system(zipCommand)

#mail backup stuff
emailText = "this is an automated backup message, please do not delete this message and if in spam; please remove it from spam and save the file somewhere secure(like dropbox or google drive etc)"
backupFileName =  fileName
imageZipFileName = "mediawikiimages.zip"
emailSubject = "'archive'"
sendToEmail = 'justinthegooch@gmail.com, emailsRemovedForPrivacyreasons@thisScriptWillStillWo.rk, emailsRemovedForPrivacyreasons@thisScriptWillStillWo.rk, emailsRemovedForPrivacyreasons@thisScriptWillStillWo.rk, emailsRemovedForPrivacyreasons@thisScriptWillStillWo.rk, emailsRemovedForPrivacyreasons@thisScriptWillStillWo.rk'
mailCommand = 'echo "' + emailText + '" | mailx -s ' + emailSubject + ' -a ' + backupFileName + ' -a ' + imageZipFileName + ' -- '+ sendToEmail
print mailCommand


os.system(mailCommand)



import os

def makedbcon(apidir,dbname,dbhost,dbuser,dbpw):
    
    if not os.path.exists('apis/'+apidir+'/dbcon'):
        os.makedirs('apis/'+apidir+'/dbcon')

    
    file= open('apis/'+apidir+'/dbcon'+"/"+"index.php","w+")

    file.write("<?php" + "\n")
    file.write("\t"+"// connect to database"+ "\n")
    file.write("\t"+"$dbcon = mysqli_connect(\""+ dbhost +"\", \""+ dbuser+"\", \""+ dbpw +"\", \""+dbname + "\" );"+"\n")
    file.write("?>")
    
        
    
        

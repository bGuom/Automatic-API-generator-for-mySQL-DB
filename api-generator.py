import os
import scanner
import maker_db_con
import makerC
import makerU
import makerR
import makerD

print '============================================================'
print '                     API-GENERATOR'
print '============================================================\n\n\n'




        
while (True):
    apidir = raw_input("Enter name for output folder\n");

    if not os.path.exists('apis/'+apidir):
        os.makedirs('apis/'+apidir)
        break;
    else:
        print 'Folder alredy exsits\n';
print "Folder created..\n\n"

print"============================================================"
print"Database connection setup with phpMyAdmin >>>\n"
dbname = raw_input("Enter db name\n");
dbhost = raw_input("Enter db host ex:localhost\n");
dbuser = raw_input("Enter db user ex:root\n");
dbpw = raw_input("Enter db password\n");

print"============================================================"
con=raw_input("Start ? Y/N\n");
if (con=='Y' or con=='y'):
    print "Connecting with your databse.."

    con_res = scanner.scan(dbname,dbhost,dbuser,dbpw) 
    tables = con_res[0]
    tablecolumns = con_res[1]

    maker_db_con.makedbcon(apidir,dbname,dbhost,dbuser,dbpw)

    print "Generating..\t0%"
    tot = len(tables)*4
    val=1
    for i in range(len(tables)):
        makerC.makeC(apidir,tables[i],tablecolumns[i])
        print "Generating..\t"+ str((float(val)/float(tot))*100) + "%"
        val+=1
        makerU.makeU(apidir,tables[i],tablecolumns[i])
        print "Generating..\t"+ str((float(val)/float(tot))*100) + "%"
        val+=1
        makerR.makeR(apidir,tables[i],tablecolumns[i])
        print "Generating..\t"+ str((float(val)/float(tot))*100) + "%"
        val+=1
        makerD.makeD(apidir,tables[i],tablecolumns[i])
        print "Generating..\t"+ str((float(val)/float(tot))*100) + "%"
        val+=1
        
    print"============================================================"
    print "Completed 100%"
    print"============================================================"
            
    raw_input("Press enter to exit");
    exit
else:
    exit;




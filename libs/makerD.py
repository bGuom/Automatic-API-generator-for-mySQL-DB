"""
<?php 
	// variable declaration
	$id="";
	$errors = array();	
	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'simpleapi');
	if(isset($_GET['id'])){$id = $_GET['id'];}
	// form validation: ensure that the form is correctly filled
	if (empty($id)) { array_push($errors, "UserID required"); }
	// delete user if there are no errors in the form
	if (count($errors) == 0) {
		$query = "DELETE FROM db WHERE ID=$id";
		mysqli_query($db, $query);
		$msg = array();
		array_push($msg, "result:success");
		echo json_encode($msg);
	}
	if (count($errors) > 0) {echo json_encode($errors);} 
	
?>
"""

import os
import documenter

def makeD(apidir,tablename,columns,primary):
    
    if not os.path.exists('apis/'+apidir+'/'+'delete_'+tablename):
        os.makedirs('apis/'+apidir+'/'+'delete_'+tablename)

    tailstring=''
    var_arr=[]
    if (len(primary)==1):
        tailstring = primary[0] + " = $" + primary[0].lower()
    elif (len(primary) > 0):
        for key in primary:
            var_arr.append(key + " = $" + key.lower())
        tailstring= (" AND ".join(var_arr))
    else:
        tailstring = columns[0]+" = $" + columns[0].lower()
        
    
    file= open('apis/'+apidir+'/'+'delete_'+tablename+"/"+"index.php","w+")
    
    file.write("<?php" + "\n")
    file.write("\t"+"include '../dbcon/index.php';"+ "\n")
    file.write("\t"+"// variable declaration"+ "\n")
    
    for column in primary:
        file.write("\t"+"$"+column.lower()+" = \"\";"+ "\n")

    file.write("\t"+"$errors = array();\n"+ "\n")
    file.write("\t"+"// getting data and validation"+ "\n")

    for column in primary:
        file.write("\t"+"if(isset($_GET[\'"+column.lower()+"\'])){$"+column.lower()+" = $_GET[\'"+column.lower()+"\'];}"+ "\n")
        file.write("\t"+"if (empty($"+column.lower()+")) { array_push($errors, \""+column.lower()+" required\"); }"+ "\n")
    
    file.write("\t"+"// If there is no errors delete"+ "\n")
    file.write("\t"+"if (count($errors) == 0) {"+ "\n")
    file.write("\t\t"+"$query = \"DELETE FROM "+tablename + " WHERE " + tailstring + "\";" + "\n")
    file.write("\t\t"+"mysqli_query($dbcon, $query);"+ "\n")
    file.write("\t\t"+"$msg = array();"+ "\n")
    file.write("\t\t"+"array_push($msg, \"result:success\");"+ "\n")
    file.write("\t\t"+"echo json_encode($msg);"+ "\n")
    file.write("\t"+"}"+ "\n")
    file.write("\t"+"if (count($errors) > 0) {echo json_encode($errors);} "+  "\n")
    file.write("?>")
    file.close()

    documenter.document(apidir,'delete_'+tablename,primary,'d')

    
    
        
    
        

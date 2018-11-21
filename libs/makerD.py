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

def makeD(apidir,tablename,columns):
    
    if not os.path.exists('apis/'+apidir+'/'+'delete_'+tablename):
        os.makedirs('apis/'+apidir+'/'+'delete_'+tablename)

    var_arr=[]        
    file= open('apis/'+apidir+'/'+'delete_'+tablename+"/"+"index.php","w+")

    file.write("<?php" + "\n")
    file.write("\t"+"include '../dbcon/index.php';"+ "\n")
    file.write("\t"+"// variable declaration"+ "\n")
    file.write("\t"+"$"+columns[0].lower()+" = \"\";"+ "\n")
    file.write("\t"+"$errors = array();\n"+ "\n")
    file.write("\t"+"// getting data and validation"+ "\n")
    file.write("\t"+"if(isset($_GET[\'"+columns[0].lower()+"\'])){$"+columns[0].lower()+" = $_GET[\'"+columns[0].lower()+"\'];}"+ "\n")
    file.write("\t"+"if (empty($"+columns[0].lower()+")) { array_push($errors, \""+columns[0].lower()+" required\"); }"+ "\n")    
    file.write("\t"+"// If there is no errors delete"+ "\n")
    file.write("\t"+"if (count($errors) == 0) {"+ "\n")
    file.write("\t\t"+"$query = \"DELETE FROM "+tablename + " WHERE " + columns[0]+" = $" + columns[0].lower() + "\";" + "\n")
    file.write("\t\t"+"mysqli_query($dbcon, $query);"+ "\n")
    file.write("\t\t"+"$msg = array();"+ "\n")
    file.write("\t\t"+"array_push($msg, \"result:success\");"+ "\n")
    file.write("\t\t"+"echo json_encode($msg);"+ "\n")
    file.write("\t"+"}"+ "\n")
    file.write("\t"+"if (count($errors) > 0) {echo json_encode($errors);} "+  "\n")
    file.write("?>")

    documenter.document(apidir,'delete_'+tablename,columns,'d')

    
    
        
    
        

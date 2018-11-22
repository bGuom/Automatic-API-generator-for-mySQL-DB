"""
<?php 
	// variable declaration
	$id="";
	$name ="";
	$errors = array();	
	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'simpleapi');
	if(isset($_GET['id'])){$id = $_GET['id'];}
	if(isset($_GET['name'])){$name = $_GET['name'];}
	// form validation: ensure that the form is correctly filled
	if (empty($id)) { array_push($errors, "UserID required"); }
	if (empty($name)) { array_push($errors, "UserName required"); }
	// update user if there are no errors in the form
	if (count($errors) == 0) {
		$query = "UPDATE db SET NAME= '$name' WHERE ID=$id";
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

def makeU(apidir,tablename,columns,primary):
    
    if not os.path.exists('apis/'+apidir+'/'+'update_'+tablename):
        os.makedirs('apis/'+apidir+'/'+'update_'+tablename)

    tailstring=''
    temp_arr=[]
    var_arr=[]
    if (len(primary)==1):
        tailstring = primary[0] + " = $" + primary[0].lower()
    elif (len(primary) > 0):
        for key in primary:
            temp_arr.append(key + " = $" + key.lower())
        tailstring= (" AND ".join(temp_arr))
    else:
        tailstring = columns[0]+" = $" + columns[0].lower()
        
    file= open('apis/'+apidir+'/'+'update_'+tablename+"/"+"index.php","w+")

    file.write("<?php" + "\n")
    file.write("\t"+"include '../dbcon/index.php';"+ "\n")
    file.write("\t"+"// variable declaration"+ "\n")
    for column in columns:
        file.write("\t"+"$"+column.lower()+" = \"\";"+ "\n")
        var_arr.append(column+" = $"+column.lower())
    file.write("\t"+"$errors = array();\n"+ "\n")
    file.write("\t"+"// getting data and validation"+ "\n")
    for column in columns:
        file.write("\t"+"if(isset($_GET[\'"+column.lower()+"\'])){$"+column.lower()+" = $_GET[\'"+column.lower()+"\'];}"+ "\n")
        file.write("\t"+"if (empty($"+column.lower()+")) { array_push($errors, \""+column.lower()+" required\"); }"+ "\n")
    file.write("\t"+"// If there is no errors update"+ "\n")
    file.write("\t"+"if (count($errors) == 0) {"+ "\n")
    file.write("\t\t"+"$query = \"UPDATE "+tablename + " SET "+(",".join(var_arr))+ " WHERE " + tailstring +"\";"+ "\n")
    file.write("\t\t"+"mysqli_query($dbcon, $query);"+ "\n")
    file.write("\t\t"+"$msg = array();"+ "\n")
    file.write("\t\t"+"array_push($msg, \"result:success\");"+ "\n")
    file.write("\t\t"+"echo json_encode($msg);"+ "\n")
    file.write("\t"+"}"+ "\n")
    file.write("\t"+"if (count($errors) > 0) {echo json_encode($errors);} "+  "\n")
    file.write("?>")
    file.close()

    documenter.document(apidir,'update_'+tablename,columns,'u')

    
    
        
    
        

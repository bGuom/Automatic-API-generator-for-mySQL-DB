"""
<?php   
	$db = mysqli_connect("localhost", "root", "", "simpleapi");  
	$sql = "SELECT * FROM db";  
	$result = mysqli_query($db, $sql);  
	$json_array = array();  
	while($row = mysqli_fetch_assoc($result))  
	{  
		$json_array[] = $row;  
	}  
	 
	echo json_encode($json_array);  
?>  
"""

import os
import documenter

def makeR(apidir,tablename,columns):
    
    if not os.path.exists('apis/'+apidir+'/'+'get_'+tablename):
        os.makedirs('apis/'+apidir+'/'+'get_'+tablename)

    var_arr=[]        
    file= open('apis/'+apidir+'/'+'get_'+tablename+"/"+"index.php","w+")

    file.write("<?php" + "\n")
    file.write("\t"+"include '../dbcon/index.php';"+ "\n")
    file.write("\t"+"$query = \"SELECT * FROM "+tablename + " \";"+ "\n")
    file.write("\t"+"$result =  mysqli_query($dbcon, $query);"+ "\n")
    file.write("\t"+"$json_array = array();"+ "\n")
    file.write("\t"+"while($row = mysqli_fetch_assoc($result))"+ "\n")
    file.write("\t"+"{"+ "\n")
    file.write("\t\t"+"$json_array[] = $row;"+"\n")
    file.write("\t"+"}"+ "\n")
    file.write("\t"+"echo json_encode($json_array);"+  "\n")
    file.write("?>")

    documenter.document(apidir,'get_'+tablename,columns,'r')

    
    
        
    
        

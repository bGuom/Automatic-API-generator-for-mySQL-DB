import os

def document(apidir,name,columns,curd):
    new = 1
    if (os.path.exists('apis/'+apidir+'/index.html')):
        new = 0
    else:
        new = 1

    strarr = []
    for  column in columns:
        strarr.append(column.lower()+"="+column.upper())
        
    file= open('apis/'+apidir+'/index.html',"a+")

    if (new ==1):
        file.write("<html>" + "\n")
        file.write("<head> <title> " + apidir + " API documentation </title>" + "\n")
        file.write("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\" integrity=\"sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO\" crossorigin=\"anonymous\">"+" </head> " + "\n")
        file.write("<body>"+ "\n\n")
        

    file.write("<h5>" + name.upper() + "</h5>" +"\n")
    file.write("<p>" + "API URL path >> </p>" +"\n\n")
       

    if (curd=='c'):
        file.write("<code><b>" + apidir + "/" + name +  "?" + ("&".join(strarr)) +"</b></code>" +"\n")
        print (apidir + "/" + name +  "?" + ("&".join(strarr)))
    if (curd=='u'):
        file.write("<code><b>" + apidir + "/" + name +  "?" + ("&".join(strarr)) +"</b></code>" +"\n")
        print (apidir + "/" + name +  "?" + ("&".join(strarr)))
    if (curd=='r'):
        file.write("<code><b>" + apidir + "/" + name + "</b></code>" +"\n")
        print(apidir + "/" + name)
    if (curd=='d'):
        file.write("<code><b>" + apidir + "/" + name + "?"+columns[0].lower()+"="+columns[0].upper()+ "</b></code>" +"\n")
        print(apidir + "/" + name + "?"+columns[0].lower()+"="+columns[0].upper())

    file.write("<hr>")
   
    
    
        
    
        

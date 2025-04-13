def is_valid(username, password):
    # Write code here
    if username=="admin" : 
     return True 
    elif username=="user" and password=="qweasd":
     return True  
    else :
     return False
  
      
    
username=input()
password=input()       
result = is_valid(username,password)
print(result)
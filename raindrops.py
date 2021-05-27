def convert(number):
   new_string=""
   if(number%3==0):
      new_string=new_string+'Pling'
   if(number%5==0):
       string=string+'Plang'   
   if(number%7==0 ):
       new_string=new_string+'Plang'
   else:
       return str(number)    
   return new_string


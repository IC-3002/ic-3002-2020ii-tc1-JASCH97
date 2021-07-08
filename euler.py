def e_cuadratica(iteraciones):
	if(iteraciones == 0):
		return 1                             
 		
	if(iteraciones == 1):                    
		return 2                             
		
	sumatoria = 2                           
	i = 2                                     
	
	while i <= iteraciones:                   
		sumatoria += (1/factorial(i))         
		i += 1                                
		
	return sumatoria                          
	
		
def factorial(x):  
	
	f = 1
	
	while x > 0:
		f = f*x
		x = x - 1
		
	return f



def e_lineal(iteraciones):
	sumatoria = 0                          
	i = 0
	factorial = 1
 
	
	while i <= iteraciones:
		 sumatoria = sumatoria + (1/factorial)
		 i = i + 1
		 factorial = factorial * i
				                                                      
		
	return sumatoria
	


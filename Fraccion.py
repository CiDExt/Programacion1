def mcd(a,b):
    mcd=1
    c=min(a,b)
    d=max(a,b)
    for i in range(1,c+1):
        if c%i==0:
            if d%i==0:
                mcd=i
    return mcd

class Fraccion:
    def __init__(self,numerador,denominador):

        self.num = numerador
        self.den = denominador
        
        
    def __str__(self):
        M=mcd(self.num,self.den)        
        return str(self.num//M)+"/"+str(self.den//M)
    
    def __add__(self,fraccion2):
        sumanum = self.num*fraccion2.den + self.den*fraccion2.num
        sumaden = self.den * fraccion2.den
        return Fraccion(sumanum,sumaden)
    
    def __sub__(self,fraccion2):
        sumanum = self.num*fraccion2.den - self.den*fraccion2.num
        sumaden = self.den * fraccion2.den
        return Fraccion(sumanum,sumaden)
    
    
    ##Multiplicación     
    def __mul__(self,fraccion2):
        multnum = self.num*fraccion2.num
        multden = self.den * fraccion2.den
        return Fraccion(multnum,multden)
    ## Dividir
    
    def __truediv__(self,fraccion2):
        divnum = self.num * fraccion2.den
        divden = self.den * fraccion2.num
        return Fraccion(divnum,divden)
    
    
    ##Negativos 
    
    def __neg__(self):
        negnum=-self.num
        return Fraccion(negnum,self.den)
    
    
    ## Potencias enteras positivas 
    def __pow__(self,intn): 
        if intn > 0:
            potnum=int((self.num)**intn )
            potden=int((self.den)**intn )
            return Fraccion(potnum,potden) 
        elif intn <0:            
            numeradorPEN=int(self.den**abs(intn))
            denominadorPEN=int(self.num**abs(intn))
            return Fraccion(numeradorPEN,denominadorPEN)
        else:
            return Fraccion(1,1)
    

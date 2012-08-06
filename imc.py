print "bienvenido a su programa de IMC"
print "presione 1 para iniciar"
a = input()

if a==1:

 print "ingrese estatura"
 e = input()
  
 print "ingrese su peso"
 p = input()

 I = p/(e**2)


 if I<16:
  print "usted sufre de infrapeso severo"

 elif I>=16 and I<17:
  print "usted sufre de infrapeso moderado"

 elif I>=17 and I<18.0:
  print  "su peso es menor de lo normal"

 elif I>=18.0 and I<24.9:
  print  "su peso es normal y saludable"
  

 elif I>=24.9 and I<30.0:
  print  "usted sufre de sobrepeso"
 
 elif I>=30 and I<34.9:
  print  "usted sufre de obesidad tipo I"

 elif I>=34.9 and I<39.9:
  print  "usted sufre de obesidad tipo II"
  

 elif I>=39.9: 
  print  "usted sufre de obesidad extrema"
 
  
elif a==0:
 print "gracias por su visita"
elif a!=1 and a!=0:
 print "presione 1 para iniciar"


   

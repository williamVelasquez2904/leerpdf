#https://www.youtube.com/watch?v=izfttyMAW-g

#import pypdf2
import re
from PyPDF2 import PdfReader
    
def  scrappe_data(filename):
   reader = PdfReader(filename)
   page = reader.pages[0]
   texto= page.extract_text()

   lines = texto.split('\n')
   #print(lines)
   i=0
   for line in lines:
       #print(line)
       i=i+1
       #prueba
       if i==1:
           #print("linea: "+str(i))
           #print(line)
           patron = r'V-\d+-\d+\s*([A-Z\s]+)'
           match =re.search(patron,line) 
           if match:
               cliente=match.group(1).strip()
               #print(f'{cliente}')
       if i==2:
           print("linea: "+str(i))
           print(line)      
           patron = r'(\d{2}/\d{2}/\d{4})'  
           match =re.search(patron,line) 
           if match:
               fecha=match.group(1).strip()
               print(f'{fecha}')

       if i==3:
           patron = r'V-\d+-\d+\s*([A-Z\s]+)'
           match =re.search(patron,line) 
           if match:
               cliente=match.group(1).strip()
               
               #print(f'{cliente}')
       if i==4:
           #print(line)
           patron = r'V-\d+-\d+\s*([A-Z\s]+)'
           match =re.search(patron,line) 
           if match:
               direccion=match.group(1).strip()
               #
               #print(f'{direccion}')
       if i==5:
           #print('Num de linea: '+str()+"\n")
           #print(line+"\n")
           patron = r'V-\d+-\d+\s*([A-Z\s]+)'
           match =re.search(patron,line) 
           if match:
               campo5=match.group(1).strip()
               #
               #print(f'{campo5}')

   return texto
   

if __name__ == '__main__':
    scrappe_data('Nota38012 EDIKSON  DUQUE.pdf')



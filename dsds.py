import pyqrcode 
from pyqrcode import QRCode

import time
import xlsxwriter

import xlrd


# Start from the first cell. Rows and columns are zero indexed.
def write(l):
    row = 1
    col = 0
    pos={}
    # Iterate over the data and write it out row by row.
    so=sorted(l.values(),reverse=True)
    worksheet.write(0,0,'name')
    worksheet.write(0,1,'regno')
   # worksheet.write(0,2,'stpck')
    
##
##                worksheet.write(row,col,j)
##                worksheet.write(row,col+1,l[j])
##                #worksheet.write(row,col+2,50-l[j])
##                #worksheet.write(row,col+2,50)
##                
##                row+=1
##                print(j,l[j])

    workbook.close()
wo=xlrd.open_workbook("student.xlsx")
sh=wo.sheet_by_index(0)
l=[]
for i in range(1,sh.nrows):
    s=str(sh.cell_value(i,1))+str(sh.cell_value(i,2))
    l.append(s)
    print(s)
print(l)
##for i in range (0,n):
##    it=int(input("Enter item name : "))
##    s.append(it)
##    l[name[it]]=l[name[it]]+1
### Create a workbook and add a worksheet.
##workbook = xlsxwriter.Workbook('student.xlsx')
##worksheet = workbook.add_worksheet()
##write(l)
##
##liststud=["hari","reema","gorav"]
##print("want to add more students press 1 else any other key")
##x=input()
##if(x=='1'):
##    n=int(input("enter the student number"))
##    for i in range(0,n):
##        name=input()
##        liststud.append(name)
        
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

s = l[0]

# Generate QR code
url = pyqrcode.create(s) 
  

url.svg("myqr1.svg", scale = 8)
url = pyqrcode.create(l[1]) 
  

url.svg("myqr2.svg", scale = 8)
url = pyqrcode.create(l[2]) 
  

url.svg("myqr3.svg", scale = 8) 

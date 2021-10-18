from time import time
cvf=0
Portal=2
import os
import binascii
import math

zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []
namez = input("c, ul2 or for compress cl for extract for e, cl2? ")

#@Author Jurijus pacalovas
class compression:
    def cryptograpy_compression(self):
              
                
                if namez=="ul2" or namez=="cl2":
                    if namez=="ul2":
                        i=1
                    if namez=="cl2":
                        i=2
                        
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-12:nac]!=".bin.bin.bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-12]
                        nac=len(nameas)
                    
                    
                    if nameas[nac-5:nac]==".docx":
                        Portal=1
                    if nameas[nac-4:nac]==".pdf":
                        Portal=3
                    if nameas[nac-4:nac]==".doc":
                        Portal=1
                    if nameas[nac-4:nac]==".png":
                        Portal=7
                    if nameas[nac-4:nac]==".jpg":
                        Portal=9
                    if nameas[nac-4:nac]==".mp4":
                        Portal=8
                      
                    if i==1:
                       
                        nameas=name+".bin.bin.bin"
                    
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=1
                    e4=""
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()

                      
                        if i==1:
                            if Portal==9 and data[0:3]!=b'\xff\xd8\xff':
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==9 and data[0:3]==b'\xff\xd8\xff': 
                                    data=data[3:]
                            if Portal==7 and data[0:4]!=b'\x89\x50\x4e\x47' :
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==7 and data[0:4]==b'\x89\x50\x4e\x47' :             
                                    data=data[4:]
                            if Portal==8 and data[0:11]!=b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34':
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==8 and data[0:11]==b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34':             
                                    data=data[11:]
      
                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1

                                if assxw>=e3%8:
                                                
                                            if e4=="0":
                                                sda3=sda3+"1"
                                                e4="0"
                                                e4=""

                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""

                                

                                if assxw<=e3%8:
                                                
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""

                                            if e4=="1":
                                                sda3=sda3+"1"
                                                e4="0"
                                                e4=""
                                                 
                                  

                                if assxw>=e3%4:
                                                
                                            if e4=="0":
                                                sda3=sda3+"1"
                                                e4="0"
                                                e4=""

                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""
                                                 
                                if e4=="1":
                                	sda3=sda3+"1"
                                	e4="1"
                                	e4=""
                                    
                                if e4=="0":
                                    sda3=sda3+"1"
                                    e4="0"
                                    e4=""    
                                


                                if assxw>=e3%4:
                                                
                                            if e4=="0":
                                                sda3=sda3+"1"
                                                e4="0"
                                                e4=""
                                                 
                                if e4=="1":
                                	sda3=sda3+"1"
                                	e4="1"
                                	e4=""
                                    
                                if e4=="0":
                                    sda3=sda3+"1"
                                    e4="0"
                                    e4=""    
                                
                                if assxw>=e3%2:
                                                
                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""
                                                 
                                if e4=="1":
                                	sda3=sda3+"1"
                                	e4="1"
                                	e4=""
                                    
                                if e4=="0":
                                    sda3=sda3+"1"
                                    e4="0"
                                    e4=""     
                               
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    sw=sw+1
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+2
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                   
                                    n = int(sda3, 2)
                                
                                    qqwslenf=len(sda3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    data=jl
                                    
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==200:
                                        assx=10
                                        if assx==10:
                                            
                                                if i==2:
                                                    if Portal==7:
                                                        jl= b'\x89\x50\x4e\x47'+jl
                                                    if Portal==8:
                                                        jl=b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34'+jl
                                                    if Portal==9:
                                    	                jl=b'\xff\xd8\xff'+jl
                                    	                
                                                f2.write(jl)
                                                x2 = time()
                                                x3=x2-x
                                                return print(x3)



    def cryptograpy_compression2(self):
                
                self.name = "Written: Jurijus pacalovas Date: 29/09/2021 18:06"
                
                if namez=="c" or namez=="e":
                    if namez=="c":
                        i=1
                    if namez=="e":
                        i=2
                    
                    #import mpmath as m
                    #m.mp.dps = 100000
                    #PI=4 * m.atan(1)

                  

                    sda4=""
                    sda5=""
                    sda6=""
                    e4a=""
                    e4b=""
                    ei8=""
                        
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-4:nac]!=".bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-4]
                        nac=len(nameas)
                    
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    Circle_times3=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                    e2=0
                    e3=1
                    e4=""
                    ei4=0
                    ei5=7
                    
                    e4=""
                    
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    block=1
                    block2=0
                    block3=0
                    Spin=0
                    count=0
                    
                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        
                        END_working=0
                        Circle_times2=0
                        ii=0
                        sda20=""
                        
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1

                            with open(nameas, "ab") as f2:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**32)-1:
                                        raise SystemExit
                                        
                                        
                                    
                                    
                                
                                    
                                #########################################################################################################################################################
                                
                                block2=0
                                if i==2:

                                    
                                    
                                    lenf5=len(sda2)

                                    
                                    
                                        
                                    block2=0
                                    ei4=0
                                    ei5=1

                                    Spin=0
                                    sda3=sda2
                                    
                                    block3=0
                                    Colaider3=""
                                   
                                    lenf5=len(sda3)
                                    
                                    Spin3=0

                                    Spin2=0
                                    #Extract
                                    g=1
                                    
                                    s

                                    sda3=sda2
                                    lenf6=len(sda3)
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""
                                    sda8=""
                                    sda9=""
                                    Bytes_row4=""
                                    ei=0

                                    lenf8a=sda3[0:48]
                                    lenf8b=sda3[48:96]

                                    lenf9=int(lenf8a, 2)

                                    lenf8=int(lenf8b, 2)

                                    if Circle_times2==0:
                                        ei=0
                                        while ei<lenf8:
                                            sda5=sda5+"2"

                                            ei=ei+1

                                        sda3=sda5
                                    
                                    ei=0

                                    count_times4=0

                                    while ei<lenf8:

                                        sda9=sda3[0:1][::-1]
                                        sda10=sda3[ei:ei+1][::-1]
                                       
                                        ei=ei+1
                                    
                                        if sda9=="1":
                                            sda4=sda4+"2"
                                            count_times4=count_times4+1

                                        elif sda9=="2":
                                            sda4=sda4+"1"
                                                      
                                        else:
                                           
                                            sda4=sda4+sda10

                                    sda2=sda4
                                    wer=sda4
                                    sda4=""

                                    Circle_times2=Circle_times2+1
                                    
                                    if  Circle_times2==lenf9:
                                         #print(wer)

                                         n = int(wer, 2)
                                         qqwslenf=len(wer)
                                         qqwslenf=(qqwslenf/8)*2
                                         qqwslenf=str(qqwslenf)
                                         qqwslenf="%0"+qqwslenf+"x"
                                         jl=binascii.unhexlify(qqwslenf % n)
                                         sssssw=len(jl)

                                         szxzzza=""
                                         szxzs=""
                                            
                                         f2.write(jl)
                                         x2 = time()
                                         x3=x2-x
                                         return print(x3)
                                        
                                
  
                                if i==1:
                                    Spin=0
                                    sda3=sda2
                                    lenf6=len(sda3)
                                    ei4=0
                                    ei5=20
                                    block3=0
                                    Colaider3=""
                                    block2=0
                                    block3=0

                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda9=""

                                    sda10=""
                                    sda11=""
                                    sda12=""
                                    sda13=""

                                    ei=0
                                    
                                    if Circle_times2>=1:

                                        sda2=sda20

                                    count_times4=0
                                    
                                    while ei<lenf6:

                                        sda9=sda2[0:1][::-1]
                                        sda10=sda2[ei:ei+1][::-1]
                                       
                                        ei=ei+1
                                    
                                        if sda9=="1":
                                            sda4=sda4+"2"
                                            count_times4=count_times4+1

                                        elif sda9=="2":
                                            sda4=sda4+"1"
                                                      
                                        else:
                                           
                                            sda4=sda4+sda10
                                      
                                    #print(ei)
                                    sda6=sda4
                                    sda4=""
                                      
                                    #####################################################################################################################################################
                                                  
                                    block2=0
                                    Spin=1
                                    Spinh=0              
                                    block2=0
                              
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                     
                                    
                                    sda20=sda6

                                    Spin=0   

                                    if i==1:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                        
                                        Circle_times2=Circle_times2+1
                                        
                                    
                                        if  count_times4==lenf7*8:
                                            

                                            szx=""
                                            #print(count_times4)
                                            szx1=bin(count_times4)[2:]
                                            #print(szx1)
                                            lenf=len(szx1)
                                            #print(lenf)

                                            sda14=""
                                                
                                            #print(lenf)
                                            xc=48-lenf%48
                                            z=0
                                            if xc!=0:
                                                if xc!=48:
                                                    while z<xc:
                                                        szx="0"+szx
                                                        z=z+1
                                        
                                            sda14=szx+szx1
                                            #print(sda14)

                                          
                                            szx1=bin(Circle_times2)[2:]
                                            lenf=len(szx1)
                                            #print(lenf)

                                            sda15=""
                                            szx=""    
                                            #print(lenf)
                                            xc=48-lenf%48
                                            z=0
                                            if xc!=0:
                                                if xc!=48:
                                                    while z<xc:
                                                        szx="0"+szx
                                                        z=z+1
                                        
                                            sda15=szx+szx1

                                            wer=sda15+sda14
                                            

                                            n = int(wer, 2)
                                            qqwslenf=len(wer)
                                            qqwslenf=(qqwslenf/8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)

                                            szxzzza=""
                                            szxzs=""
                                            sda2=sda6
                                              
                                            
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)





d=compression()

xw=d.cryptograpy_compression2()
print(xw)

xw2=d.cryptograpy_compression()
print(xw2)

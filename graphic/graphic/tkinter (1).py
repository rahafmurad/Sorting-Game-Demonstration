# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 07:15:59 2022

@author: shahad mohammed
"""
from tkinter import *
import random
import time
import vis
import visQ
import SelectAlgorithm


def partition(A, low, high):
    pivot = A[high]
    i = low-1
    for j in range(low, high):
        if pivot >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i+1



   
title = ""
window = Tk()
window.title("Sorting game")
window.geometry("600x500")

myLabel1 = Label(window, text="Welcome to our Sorting game demonstraion!",fg="white",bg="black",font=("Arial", 15))
myLabel2 = Label(window, text="Choose the Algorithem You Want :",font=("Arial", 14))

myLabel1.place(x=100, y=50)
myLabel2.place(x=150, y=140)

def show():
    if clicked.get()=='Merge Sort' :
        mergeSortDemo("Merge Sort")
    elif clicked.get()=='Selction Sort' :   
       selctionSortDemo("Selction Sort")
    elif clicked.get()=='Quick Sort' :     
        quickSortDemo("Quick Sort")
          
  
  
    
  

options = [
        "Merge Sort",
        "Selction Sort",
        "Quick Sort"]

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(window,clicked, *options)
drop.place(x=240, y=225)

myButton1 = Button(window,text="Next", padx=10,pady=5, command= show,fg="white",bg="purple")
myButton1.place(x=270, y=325)

myButtonExit = Button(window,text="exit",command=window.destroy,fg="white",bg="purple")
myButtonExit.place(x=60, y=450)

def mergeSortDemo(name):
    pro =Tk()

    pro.title(name)
    pro.geometry("600x600")

    myLabel1 = Label(pro, text= name+" Algorithm Demo",fg="white",bg="black",font=("Arial", 15))
    myLabel2 = Label(pro, text="Inputs",font=("Arial", 15))
    myLabel3 = Label(pro, text="Demonstration",font=("Arial", 15))


    myLabel1.place(x=170, y=20)
    myLabel2.place(x=10, y=70)
    myLabel3.place(x=10, y=200)

    
    e1= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e1.place(x=500, y=125)
    
    e2= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e2.place(x=430, y=125)

    e3= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e3.place(x=360, y=125)

    e4= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e4.place(x=290, y=125)

    e5= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e5.place(x=220, y=125)

    e6= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e6.place(x=150, y=125)

    e7= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e7.place(x=80, y=125)
    
    e8= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e8.place(x=10, y=125)
    
    def go():
        myLabel1 = Label(pro, text=e1.get(),width=10,fg="black",font=("Arial", 13))
        myLabel1.place(x=500, y=250)
                
        myLabel2 = Label(pro, text=e2.get(),width=10,fg="black",font=("Arial", 13))
        myLabel2.place(x=430, y=250)
                
        myLabel3 = Label(pro, text=e3.get(),width=10,fg="black",font=("Arial", 13))
        myLabel3.place(x=360, y=250)
                
        myLabel4 = Label(pro, text= e4.get(),width=10,fg="black",font=("Arial", 13))
        myLabel4.place(x=290, y=250)
        
        myLabel5 = Label(pro, text= e5.get(),width=10,fg="black",font=("Arial", 13))
        myLabel5.place(x=220, y=250)
        
        myLabel6 = Label(pro, text= e6.get(),width=10,fg="black",font=("Arial", 13))
        myLabel6.place(x=150, y=250)
        
        myLabel7 = Label(pro, text= e7.get(),width=10,fg="black",font=("Arial", 13))
        myLabel7.place(x=80, y=250)
        
        myLabel8 = Label(pro, text= e8.get(),width=10,fg="black",font=("Arial", 13))
        myLabel8.place(x=10, y=250)
        
        
        
        in8=int(e8.get())
        in7=int(e7.get())
        in6=int(e6.get())
        in5=int(e5.get())
        in4=int(e4.get())
        in3=int(e3.get())
        in2=int(e2.get())
        in1=int(e1.get())
        
        A=[in8,in7,in6,in5,in4,in3,in2,in1]
        #A=[e8.get(),e7.get(),e6.get(),e5.get(),e4.get(),e3.get(),e2.get(),e1.get()]
        #A=[6,5,33,3,2,1]
        #print("e1 :",e1.get())
        #for i in range(len(A)):
            #print("Print A",A[i])
            
        def Next():
            myLabel1 = Label(pro, text=A[7],width=10,fg="black",font=("Arial", 13))
            myLabel1.place(x=500, y=250)
                    
            myLabel2 = Label(pro, text= A[6],width=10,fg="black",font=("Arial", 13))
            myLabel2.place(x=430, y=250)
                    
            myLabel3 = Label(pro, text=A[5],width=10,fg="black",font=("Arial", 13))
            myLabel3.place(x=360, y=250)
                    
            myLabel4 = Label(pro, text= A[4],width=10,fg="black",font=("Arial", 13))
            myLabel4.place(x=290, y=250)
            
            myLabel5 = Label(pro, text= A[3],width=10,fg="black",font=("Arial", 13))
            myLabel5.place(x=220, y=250)
            
            myLabel6 = Label(pro, text=A[2],width=10,fg="black",font=("Arial", 13))
            myLabel6.place(x=150, y=250)
              
            myLabel7 = Label(pro, text= A[1],width=10,fg="black",font=("Arial", 13))
            myLabel7.place(x=80, y=250)
            
            myLabel8 = Label(pro, text= A[0],width=10,fg="black",font=("Arial", 13))
            myLabel8.place(x=10, y=250)
            
       
                
     
      
    myButton2 = Button(pro,text="Go!",command=go,fg="white",bg="purple")
    myButton2.place(x=270, y=160)
    def mergeSort(array):
        if len(array) > 1:
            
            r = len(array)//2
            L = array[:r]
            M = array[r:]
            
            print(L,M)
            if len(M)==4:
              myLabel1 = Label(pro, text=M[3],width=10,fg="black",font=("Arial", 13))
              myLabel1.place(x=490, y=250)
                      
              myLabel2 = Label(pro, text= M[2],width=10,fg="black",font=("Arial", 13))
              myLabel2.place(x=420, y=250)
                      
              myLabel3 = Label(pro, text=M[1],width=10,fg="black",font=("Arial", 13))
              myLabel3.place(x=360, y=250)
                      
              myLabel4 = Label(pro, text= M[0],width=10,fg="black",font=("Arial", 13))
              myLabel4.place(x=300, y=250)
              
              myLabel5 = Label(pro, text= L[3],width=10,fg="black",font=("Arial", 13))
              myLabel5.place(x=195, y=250)
              
              myLabel6 = Label(pro, text=L[2],width=10,fg="black",font=("Arial", 13))
              myLabel6.place(x=130, y=250)
                
              myLabel7 = Label(pro, text= L[1],width=10,fg="black",font=("Arial", 13))
              myLabel7.place(x=65, y=250)
              
              myLabel8 = Label(pro, text= L[0],width=10,fg="black",font=("Arial", 13))
              myLabel8.place(x=8, y=250)  
              if len(M)==2:
                myLabel1 = Label(pro, text=M[1],width=10,fg="black",font=("Arial", 13))
                myLabel1.place(x=490, y=250)
                        
                myLabel2 = Label(pro, text= M[0],width=10,fg="black",font=("Arial", 13))
                myLabel2.place(x=420, y=250)
               
                  
                myLabel7 = Label(pro, text= L[1],width=10,fg="black",font=("Arial", 13))
                myLabel7.place(x=65, y=250)
                
                myLabel8 = Label(pro, text= L[0],width=10,fg="black",font=("Arial", 13))
                myLabel8.place(x=8, y=250) 
                print("-----------------------------------------------------------------------")
                print(L,M)
           
            mergeSort(L)
            mergeSort(M)
           
           
            i = j = k = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1
                
      
            print(array) 
        return array  
      
    
    
    
    
    
    
    
    
    def RandomsNumbers():
        e1= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e1.place(x=500, y=125)
        e1.insert(0,random.randint(1,100))
        
        e2= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e2.place(x=430, y=125)
        e2.insert(0,random.randint(1,100))
        
        e3= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e3.place(x=360, y=125)
        e3.insert(0,random.randint(1,100))
        
        e4= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e4.place(x=290, y=125)
        e4.insert(0,random.randint(1,100))
        
        e5= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e5.place(x=220, y=125)
        e5.insert(0,random.randint(1,100))
        
        e6= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e6.place(x=150, y=125)
        e6.insert(0,random.randint(1,100))
        
        e7= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e7.place(x=80, y=125)
        e7.insert(0,random.randint(1,100))

        e8= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e8.place(x=10, y=125)
        e8.insert(0,random.randint(1,100))
    
    

        
        def myClick():
            myLabel1 = Label(pro, text=e1.get(),width=10,fg="black",font=("Arial", 13))
            myLabel1.place(x=500, y=250)
                    
            myLabel2 = Label(pro, text=e2.get(),width=10,fg="black",font=("Arial", 13))
            myLabel2.place(x=430, y=250)
                    
            myLabel3 = Label(pro, text=e3.get(),width=10,fg="black",font=("Arial", 13))
            myLabel3.place(x=360, y=250)
                    
            myLabel4 = Label(pro, text= e4.get(),width=10,fg="black",font=("Arial", 13))
            myLabel4.place(x=290, y=250)
            
            myLabel5 = Label(pro, text= e5.get(),width=10,fg="black",font=("Arial", 13))
            myLabel5.place(x=220, y=250)
            
            myLabel6 = Label(pro, text= e6.get(),width=10,fg="black",font=("Arial", 13))
            myLabel6.place(x=150, y=250)
            
            myLabel7 = Label(pro, text= e7.get(),width=10,fg="black",font=("Arial", 13))
            myLabel7.place(x=80, y=250)
            
            myLabel8 = Label(pro, text= e8.get(),width=10,fg="black",font=("Arial", 13))
            myLabel8.place(x=10, y=250)
            
            
            
            in8=int(e8.get())
            in7=int(e7.get())
            in6=int(e6.get())
            in5=int(e5.get())
            in4=int(e4.get())
            in3=int(e3.get())
            in2=int(e2.get())
            in1=int(e1.get())
            
            A=[in8,in7,in6,in5,in4,in3,in2,in1]
    
            
                   
            def myButton():
                
                start = time.process_time()
                mergeSort(A)
                myLabel1 = Label(pro, text="Time =")
                myLabel1.place(x=250, y=380)
                myLabel1 = Label(pro, text=time.process_time()-start)
                myLabel1.place(x=290, y=380)
                print("Time :",time.process_time()-start)
                

                
                    
                    
                    
                    
                
            myButton1 = Button(pro,text="Next",command= myButton,padx=10,pady=5,fg="white",bg="purple")
            myButton1.place(x=270, y=300)
                
                
                
                
            
        myButton2 = Button(pro,text="Go!",command=myClick,fg="white",bg="purple")
        myButton2.place(x=270, y=160)
          
               
                
                
            
        
    myButton3 = Button(pro,text="Random",command=RandomsNumbers,fg="white",bg="purple")
    myButton3.place(x=320, y=160)
    
    
    
    myLabele = Label(pro,
                     text= "Merge sort is one of the most efficient sorting algorithms.\n It works on the principle of Divide and Conquer. \n Merge sort repeatedly breaks down a list into several sublists until each sublist consists of a single element \n and merging those sublists in a manner that results into a sorted list.")
    myLabele.place(x=20, y=400)


    myButtonBack = Button(pro,text="back",command= pro.destroy,fg="white",bg="purple")
    myButtonBack.place(x=540, y=550)
    def vi() :
       vis.vis()
    
    myButtonBack = Button(pro,text="Visualize",command= vi,fg="white",bg="purple")
    myButtonBack.place(x=10, y=550)
    pro.mainloop()
    
    pro.mainloop()
    
   
def selctionSortDemo(name):

    pro =Tk()
    pro.title(name)
    pro.geometry("600x600")

    myLabel1 = Label(pro, text= name+" Algorithm Demo",fg="white",bg="black",font=("Arial", 15))
    myLabel2 = Label(pro, text="Inputs",font=("Arial", 15))
    myLabel3 = Label(pro, text="Demonstration",font=("Arial", 15))


    myLabel1.place(x=170, y=20)
    myLabel2.place(x=10, y=70)
    myLabel3.place(x=10, y=200)

    
    e1= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e1.place(x=500, y=125)
    
    e2= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e2.place(x=430, y=125)

    e3= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e3.place(x=360, y=125)

    e4= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e4.place(x=290, y=125)

    e5= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e5.place(x=220, y=125)

    e6= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e6.place(x=150, y=125)

    e7= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e7.place(x=80, y=125)
    
    e8= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e8.place(x=10, y=125)
    
    def go():
        myLabel1 = Label(pro, text=e1.get(),width=10,fg="black",font=("Arial", 13))
        myLabel1.place(x=500, y=250)
                
        myLabel2 = Label(pro, text=e2.get(),width=10,fg="black",font=("Arial", 13))
        myLabel2.place(x=430, y=250)
                
        myLabel3 = Label(pro, text=e3.get(),width=10,fg="black",font=("Arial", 13))
        myLabel3.place(x=360, y=250)
                
        myLabel4 = Label(pro, text= e4.get(),width=10,fg="black",font=("Arial", 13))
        myLabel4.place(x=290, y=250)
        
        myLabel5 = Label(pro, text= e5.get(),width=10,fg="black",font=("Arial", 13))
        myLabel5.place(x=220, y=250)
        
        myLabel6 = Label(pro, text= e6.get(),width=10,fg="black",font=("Arial", 13))
        myLabel6.place(x=150, y=250)
        
        myLabel7 = Label(pro, text= e7.get(),width=10,fg="black",font=("Arial", 13))
        myLabel7.place(x=80, y=250)
        
        myLabel8 = Label(pro, text= e8.get(),width=10,fg="black",font=("Arial", 13))
        myLabel8.place(x=10, y=250)
        
        
        
        in8=int(e8.get())
        in7=int(e7.get())
        in6=int(e6.get())
        in5=int(e5.get())
        in4=int(e4.get())
        in3=int(e3.get())
        in2=int(e2.get())
        in1=int(e1.get())
        
        A=[in8,in7,in6,in5,in4,in3,in2,in1]
        
        def Next(complexity_time):
            myLabel1 = Label(pro, text=A[0],width=10,fg="black",font=("Arial", 13))
            myLabel1.place(x=500, y=250)
                    
            myLabel2 = Label(pro, text= A[1],width=10,fg="black",font=("Arial", 13))
            myLabel2.place(x=430, y=250)
                    
            myLabel3 = Label(pro, text=A[2],width=10,fg="black",font=("Arial", 13))
            myLabel3.place(x=360, y=250)
                    
            myLabel4 = Label(pro, text= A[3],width=10,fg="black",font=("Arial", 13))
            myLabel4.place(x=290, y=250)
            
            myLabel5 = Label(pro, text= A[4],width=10,fg="black",font=("Arial", 13))
            myLabel5.place(x=220, y=250)
            
            myLabel6 = Label(pro, text=A[5],width=10,fg="black",font=("Arial", 13))
            myLabel6.place(x=150, y=250)
              
            myLabel7 = Label(pro, text= A[6],width=10,fg="black",font=("Arial", 13))
            myLabel7.place(x=80, y=250)
            
            myLabel8 = Label(pro, text= A[7],width=10,fg="black",font=("Arial", 13))
            myLabel8.place(x=10, y=250)
            xtime = "time : "+ str(complexity_time)
            timeLabele = Label(pro,text= xtime)
            timeLabele.place(x=20, y=500)
        
        def myButton():
            complexity_time = 0
            start = time.process_time()
            SelectAlgorithm.selectionSort(A)
            complexity_time = time.process_time()-start
            Next(complexity_time)

        
        myButton1 = Button(pro,text="Next",command= myButton,padx=10,pady=5,fg="white",bg="purple")
        myButton1.place(x=270, y=300)
    
    myButton2 = Button(pro,text="Go!",command=go,fg="white",bg="purple")
    myButton2.place(x=270, y=160)
    
    def RandomsNumbers():
        e1= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e1.place(x=500, y=125)
        e1.insert(0,random.randint(1,100))
        
        e2= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e2.place(x=430, y=125)
        e2.insert(0,random.randint(1,100))
        
        e3= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e3.place(x=360, y=125)
        e3.insert(0,random.randint(1,100))
        
        e4= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e4.place(x=290, y=125)
        e4.insert(0,random.randint(1,100))
        
        e5= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e5.place(x=220, y=125)
        e5.insert(0,random.randint(1,100))
        
        e6= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e6.place(x=150, y=125)
        e6.insert(0,random.randint(1,100))
        
        e7= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e7.place(x=80, y=125)
        e7.insert(0,random.randint(1,100))

        e8= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e8.place(x=10, y=125)
        e8.insert(0,random.randint(1,100))

        def myClick():
            myLabel1 = Label(pro, text=e1.get(),width=10,fg="black",font=("Arial", 13))
            myLabel1.place(x=500, y=250)
                    
            myLabel2 = Label(pro, text=e2.get(),width=10,fg="black",font=("Arial", 13))
            myLabel2.place(x=430, y=250)
                    
            myLabel3 = Label(pro, text=e3.get(),width=10,fg="black",font=("Arial", 13))
            myLabel3.place(x=360, y=250)
                    
            myLabel4 = Label(pro, text= e4.get(),width=10,fg="black",font=("Arial", 13))
            myLabel4.place(x=290, y=250)
            
            myLabel5 = Label(pro, text= e5.get(),width=10,fg="black",font=("Arial", 13))
            myLabel5.place(x=220, y=250)
            
            myLabel6 = Label(pro, text= e6.get(),width=10,fg="black",font=("Arial", 13))
            myLabel6.place(x=150, y=250)
            
            myLabel7 = Label(pro, text= e7.get(),width=10,fg="black",font=("Arial", 13))
            myLabel7.place(x=80, y=250)
            
            myLabel8 = Label(pro, text= e8.get(),width=10,fg="black",font=("Arial", 13))
            myLabel8.place(x=10, y=250)
            
            
            
            in8=int(e8.get())
            in7=int(e7.get())
            in6=int(e6.get())
            in5=int(e5.get())
            in4=int(e4.get())
            in3=int(e3.get())
            in2=int(e2.get())
            in1=int(e1.get())
            
            A=[in8,in7,in6,in5,in4,in3,in2,in1]
        
            low, high = 0, len(A)-1
            
            
            def Next(complexity_time):
                myLabel1 = Label(pro, text=A[7],width=10,fg="black",font=("Arial", 13))
                myLabel1.place(x=500, y=250)
                        
                myLabel2 = Label(pro, text= A[6],width=10,fg="black",font=("Arial", 13))
                myLabel2.place(x=430, y=250)
                        
                myLabel3 = Label(pro, text=A[5],width=10,fg="black",font=("Arial", 13))
                myLabel3.place(x=360, y=250)
                        
                myLabel4 = Label(pro, text= A[4],width=10,fg="black",font=("Arial", 13))
                myLabel4.place(x=290, y=250)
                
                myLabel5 = Label(pro, text= A[3],width=10,fg="black",font=("Arial", 13))
                myLabel5.place(x=220, y=250)
                
                myLabel6 = Label(pro, text=A[2],width=10,fg="black",font=("Arial", 13))
                myLabel6.place(x=150, y=250)
                  
                myLabel7 = Label(pro, text= A[1],width=10,fg="black",font=("Arial", 13))
                myLabel7.place(x=80, y=250)
                
                myLabel8 = Label(pro, text= A[0],width=10,fg="black",font=("Arial", 13))
                myLabel8.place(x=10, y=250)
                xtime = "time : "+ str(complexity_time)
                timeLabele = Label(pro,text= xtime)
                timeLabele.place(x=20, y=500)

            def myButton():
                #print("select")
                complexity_time = 0
                start = time.process_time()
                SelectAlgorithm.selectionSort(A)
                complexity_time = time.process_time()-start
                Next(complexity_time)

            
            myButton1 = Button(pro,text="Next",command= myButton,padx=10,pady=5,fg="white",bg="purple")
            myButton1.place(x=270, y=300)
        
        myButton2 = Button(pro,text="Go!",command=myClick,fg="white",bg="purple")
        myButton2.place(x=270, y=160)
        
    myButton3 = Button(pro,text="Random",command=RandomsNumbers,fg="white",bg="purple")
    myButton3.place(x=320, y=160)
    
    
    
    myLabele = Label(pro,
                     text= "What is the base idea behind selection sort ?\n This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts\n, the sorted part at the left end and the unsorted part at the right end.")
    myLabele.place(x=20, y=400)

    

    myButtonBack = Button(pro,text="back",command= pro.destroy,fg="white",bg="purple")
    myButtonBack.place(x=540, y=550)
    
    pro.mainloop()



    

    pro.mainloop()
def quickSortDemo(name):
    pro =Tk()

    pro.title(name)
    pro.geometry("600x600")

    myLabel1 = Label(pro, text= name+" Algorithm Demo",fg="white",bg="black",font=("Arial", 15))
    myLabel2 = Label(pro, text="Inputs",font=("Arial", 15))
    myLabel3 = Label(pro, text="Demonstration",font=("Arial", 15))


    myLabel1.place(x=170, y=20)
    myLabel2.place(x=10, y=70)
    myLabel3.place(x=10, y=200)

    
    e1= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e1.place(x=500, y=125)
    
    e2= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e2.place(x=430, y=125)

    e3= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e3.place(x=360, y=125)

    e4= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e4.place(x=290, y=125)

    e5= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e5.place(x=220, y=125)

    e6= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e6.place(x=150, y=125)

    e7= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e7.place(x=80, y=125)
    
    e8= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
    e8.place(x=10, y=125)
    
    def go():
        myLabel1 = Label(pro, text=e1.get(),width=10,fg="black",font=("Arial", 13))
        myLabel1.place(x=500, y=250)
                
        myLabel2 = Label(pro, text=e2.get(),width=10,fg="black",font=("Arial", 13))
        myLabel2.place(x=430, y=250)
                
        myLabel3 = Label(pro, text=e3.get(),width=10,fg="black",font=("Arial", 13))
        myLabel3.place(x=360, y=250)
                
        myLabel4 = Label(pro, text= e4.get(),width=10,fg="black",font=("Arial", 13))
        myLabel4.place(x=290, y=250)
        
        myLabel5 = Label(pro, text= e5.get(),width=10,fg="black",font=("Arial", 13))
        myLabel5.place(x=220, y=250)
        
        myLabel6 = Label(pro, text= e6.get(),width=10,fg="black",font=("Arial", 13))
        myLabel6.place(x=150, y=250)
        
        myLabel7 = Label(pro, text= e7.get(),width=10,fg="black",font=("Arial", 13))
        myLabel7.place(x=80, y=250)
        
        myLabel8 = Label(pro, text= e8.get(),width=10,fg="black",font=("Arial", 13))
        myLabel8.place(x=10, y=250)
        
        
        
        in8=int(e8.get())
        in7=int(e7.get())
        in6=int(e6.get())
        in5=int(e5.get())
        in4=int(e4.get())
        in3=int(e3.get())
        in2=int(e2.get())
        in1=int(e1.get())
        
        A=[in8,in7,in6,in5,in4,in3,in2,in1]
        #A=[e8.get(),e7.get(),e6.get(),e5.get(),e4.get(),e3.get(),e2.get(),e1.get()]
        #A=[6,5,33,3,2,1]
        #print("e1 :",e1.get())
        #for i in range(len(A)):
            #print("Print A",A[i])
        low, high = 0, len(A)-1
        
        
        def Next():
            myLabel1 = Label(pro, text=A[7],width=10,fg="black",font=("Arial", 13))
            myLabel1.place(x=500, y=250)
                    
            myLabel2 = Label(pro, text= A[6],width=10,fg="black",font=("Arial", 13))
            myLabel2.place(x=430, y=250)
                    
            myLabel3 = Label(pro, text=A[5],width=10,fg="black",font=("Arial", 13))
            myLabel3.place(x=360, y=250)
                    
            myLabel4 = Label(pro, text= A[4],width=10,fg="black",font=("Arial", 13))
            myLabel4.place(x=290, y=250)
            
            myLabel5 = Label(pro, text= A[3],width=10,fg="black",font=("Arial", 13))
            myLabel5.place(x=220, y=250)
            
            myLabel6 = Label(pro, text=A[2],width=10,fg="black",font=("Arial", 13))
            myLabel6.place(x=150, y=250)
              
            myLabel7 = Label(pro, text= A[1],width=10,fg="black",font=("Arial", 13))
            myLabel7.place(x=80, y=250)
            
            myLabel8 = Label(pro, text= A[0],width=10,fg="black",font=("Arial", 13))
            myLabel8.place(x=10, y=250)
        
        def quicksort(A, low, high):
            if low < high:
                parti = partition(A, low, high)
                print(A)
                
                def Next2():
                    Next()
                    start = time.process_time()
                    quicksort(A, low, parti-1)
                    quicksort(A, parti+1, high) 
                    myLabel1 = Label(pro, text="Time =")
                    myLabel1.place(x=250, y=380)
                    myLabel1 = Label(pro, text=time.process_time()-start)
                    myLabel1.place(x=290, y=380)
                    print("Time :",time.process_time()-start)
                    
                
                  
                myButton1 = Button(pro,text="Next",command= Next2,padx=10,pady=5,fg="white",bg="purple")
                myButton1.place(x=270, y=300)
                
            
        def myButton():
            quicksort(A, low, high)

        
        myButton1 = Button(pro,text="Next",command= myButton,padx=10,pady=5,fg="white",bg="purple")
        myButton1.place(x=270, y=300)
    
    myButton2 = Button(pro,text="Go!",command=go,fg="white",bg="purple")
    myButton2.place(x=270, y=160)
    
    
    
    
    
    
    
    
    def RandomsNumbers():
        e1= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e1.place(x=500, y=125)
        e1.insert(0,random.randint(1,100))
        
        e2= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e2.place(x=430, y=125)
        e2.insert(0,random.randint(1,100))
        
        e3= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e3.place(x=360, y=125)
        e3.insert(0,random.randint(1,100))
        
        e4= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e4.place(x=290, y=125)
        e4.insert(0,random.randint(1,100))
        
        e5= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e5.place(x=220, y=125)
        e5.insert(0,random.randint(1,100))
        
        e6= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e6.place(x=150, y=125)
        e6.insert(0,random.randint(1,100))
        
        e7= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e7.place(x=80, y=125)
        e7.insert(0,random.randint(1,100))

        e8= Entry(pro,width=10,fg="black",bg="white",highlightbackground="black", highlightcolor="black",highlightthickness=1)
        e8.place(x=10, y=125)
        e8.insert(0,random.randint(1,100))
    
    

        
        def myClick():
            myLabel1 = Label(pro, text=e1.get(),width=10,fg="black",font=("Arial", 13))
            myLabel1.place(x=500, y=250)
                    
            myLabel2 = Label(pro, text=e2.get(),width=10,fg="black",font=("Arial", 13))
            myLabel2.place(x=430, y=250)
                    
            myLabel3 = Label(pro, text=e3.get(),width=10,fg="black",font=("Arial", 13))
            myLabel3.place(x=360, y=250)
                    
            myLabel4 = Label(pro, text= e4.get(),width=10,fg="black",font=("Arial", 13))
            myLabel4.place(x=290, y=250)
            
            myLabel5 = Label(pro, text= e5.get(),width=10,fg="black",font=("Arial", 13))
            myLabel5.place(x=220, y=250)
            
            myLabel6 = Label(pro, text= e6.get(),width=10,fg="black",font=("Arial", 13))
            myLabel6.place(x=150, y=250)
            
            myLabel7 = Label(pro, text= e7.get(),width=10,fg="black",font=("Arial", 13))
            myLabel7.place(x=80, y=250)
            
            myLabel8 = Label(pro, text= e8.get(),width=10,fg="black",font=("Arial", 13))
            myLabel8.place(x=10, y=250)
            
            
            
            in8=int(e8.get())
            in7=int(e7.get())
            in6=int(e6.get())
            in5=int(e5.get())
            in4=int(e4.get())
            in3=int(e3.get())
            in2=int(e2.get())
            in1=int(e1.get())
            
            A=[in8,in7,in6,in5,in4,in3,in2,in1]
            #A=[e8.get(),e7.get(),e6.get(),e5.get(),e4.get(),e3.get(),e2.get(),e1.get()]
            #A=[6,5,33,3,2,1]
            #print("e1 :",e1.get())
            #for i in range(len(A)):
                #print("Print A",A[i])
            low, high = 0, len(A)-1
            
            
            def Next():
                myLabel1 = Label(pro, text=A[7],width=10,fg="black",font=("Arial", 13))
                myLabel1.place(x=500, y=250)
                        
                myLabel2 = Label(pro, text= A[6],width=10,fg="black",font=("Arial", 13))
                myLabel2.place(x=430, y=250)
                        
                myLabel3 = Label(pro, text=A[5],width=10,fg="black",font=("Arial", 13))
                myLabel3.place(x=360, y=250)
                        
                myLabel4 = Label(pro, text= A[4],width=10,fg="black",font=("Arial", 13))
                myLabel4.place(x=290, y=250)
                
                myLabel5 = Label(pro, text= A[3],width=10,fg="black",font=("Arial", 13))
                myLabel5.place(x=220, y=250)
                
                myLabel6 = Label(pro, text=A[2],width=10,fg="black",font=("Arial", 13))
                myLabel6.place(x=150, y=250)
                  
                myLabel7 = Label(pro, text= A[1],width=10,fg="black",font=("Arial", 13))
                myLabel7.place(x=80, y=250)
                
                myLabel8 = Label(pro, text= A[0],width=10,fg="black",font=("Arial", 13))
                myLabel8.place(x=10, y=250)
                
                
            def quicksort(A, low, high):
                if low < high:                   
                    parti = partition(A, low, high)
                    print(A)
                    
                    def Next2():
                        Next()
                        
                        start = time.process_time()
                        quicksort(A, low, parti-1)
                        quicksort(A, parti+1, high) 
                        myLabel1 = Label(pro, text="Time =")
                        myLabel1.place(x=250, y=380)
                        myLabel1 = Label(pro, text=time.process_time()-start)
                        myLabel1.place(x=290, y=380)
                        print("Time :",time.process_time()-start)
                       


                    myButton1 = Button(pro,text="Next",command= Next2,padx=10,pady=5,fg="white",bg="purple")
                    myButton1.place(x=270, y=300)
                    
            def myButton():
                quicksort(A, low, high)
                

            
            myButton1 = Button(pro,text="Next",command= myButton,padx=10,pady=5,fg="white",bg="purple")
            myButton1.place(x=270, y=300)
        
        myButton2 = Button(pro,text="Go!",command=myClick,fg="white",bg="purple")
        myButton2.place(x=270, y=160)
        
    myButton3 = Button(pro,text="Random",command=RandomsNumbers,fg="white",bg="purple")
    myButton3.place(x=320, y=160)
    
    
    
    myLabele = Label(pro,
                     text= "What is the base idea behind quick sort ?\n It picks an element as pivot from the array and partitions the given array around the picked pivot.\n so that all elements smaller than the picked pivot element move to the left side of the pivot,\n and all greater elements move to the right side. The sub-arrays are then sorted recursively.")
    myLabele.place(x=20, y=400)


    myButtonBack = Button(pro,text="back",command= pro.destroy,fg="white",bg="purple")
    myButtonBack.place(x=540, y=550)
    
    def vi() :
       visQ.visQ()
    
    myButtonBack = Button(pro,text="Visualize",command= vi,fg="white",bg="purple")
    myButtonBack.place(x=10, y=550)
    
  

window.mainloop()

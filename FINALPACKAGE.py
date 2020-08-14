from tkinter import *
from tkinter import font
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               GRAPHS
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def graphs():
   plots=["BAR GRAPH","DONUT PLOT","3D SCATTER PLOT","HORIZONTAL BAR GRAPH","PIE CHART","AREA PLOT","SCATTER PLOT","CORELATION"]
   root2 = Tk()
   x=(root2.winfo_screenwidth()-root2.winfo_reqwidth())/2
   y=(root2.winfo_screenheight()-root2.winfo_height())/2
   root2.geometry("+%d+%d" %(x,y))
   variable = StringVar(root2)
   variable.set("GRAPHS") # default value
   w = OptionMenu(root2, variable, *plots)
   w.pack()
   def ok():
       files=open("file-1.csv","r")
       d=variable.get()
       root2.destroy()
       if(d=="DONUT PLOT"):
          cityname=[]
          lists=[]
          dict1={}
          for line in files:
             
             lists=line.split(",")
             cityname.append(lists[1])
          cityname.pop(0)
          for i in cityname:
             if i not in dict1:
                dict1[i]=1
             else:
                dict1[i]+=1
          count=[]
          cities=[]
          colors=['rosybrown','lightcoral','indianred','brown','firebrick','maroon','red','salmon','bisque','gold','olive','palegreen','lightgreen','lightyellow','crimson','pink','yellow','azure','cyan','lime','royalblue','blue','wheat','goldenrod','khaki','aqua','teal','lavender','navy','violet','chocolate','lightslategray','fuchsia']
          for i in dict1:
             count.append(dict1[i])
             cities.append(i)
             my_circle=plt.Circle( (0,0), 0.7, color='white')
          plt.pie(count,colors=colors)
          p=plt.gcf()
          p.gca().add_artist(my_circle)
          plt.legend(bbox_to_anchor=(0, 1.1565),labels=cities,loc=1,prop={'size':6})
          plt.title("DONUT PLOT-City Vs Number of restaurants")
          plt.show()
          files.close()
       elif(d=="BAR GRAPH"):
          def plot(p,n):
             plot=plt.bar(p,n,color='blue')
             for value in plot:
                height=value.get_height()
                plt.text(value.get_x()+value.get_width()/2,1.002*height,'%d'%int(height),ha='center',va='bottom')
             plt.xlabel("City",color='red')
             plt.ylabel("Number of restaurants",color='red')
             index=np.arange(len(p))
             plt.xticks(index , p, fontsize=7, rotation=10)
             plt.title("BAR GRAPH- City Vs Number of restaurant",color='purple')
             plt.show()
          cityname=[]
          files=[]
          dict1={}
          name=[]
          number=[]
          name1=[]
          number1=[]
          name2=[]
          number2=[]
          name3=[]
          number3=[]
          c=open("file-1.csv","r")
          for line in c:
             files=line.strip("\n").split(',')
             cityname.append(files[1])

          for i in cityname:
              if i not in dict1:
                 dict1[i]=1
              else:
                 dict1[i]+=1
          for i in dict1:
             name.append(i)
             number.append(int(dict1[i]))
          for i in range(0,14):
             name1.append(name[i])
             number1.append(number[i])
          for i in range(14,28):
             name2.append(name[i])
             number2.append(number[i])
          for i in range(28,43):
             name3.append(name[i])
             number3.append(number[i])
          plot(name1,number1)
          plot(name2,number2)
          plot(name3,number3)
          c.close()
       elif(d=="CORELATION"):
          cf=open("file-1.csv","r")
          lists=[]
          avgrate=[]
          rating=[]
          sumsxy=0.0
          sumsx=0.0
          sumsy=0.0
          sumsx2=0.0
          sumsx3=0.0
          for line in cf:
             lists=line.strip("\n").split(",")
             avgrate.append(int(lists[4]))
             rating.append(float(lists[9]))
          for i in range(0,len(avgrate)):
             for j in range(1,len(avgrate)):
                if(avgrate[i]>avgrate[j]):
                   avgrate[i],avgrate[j]=avgrate[j],avgrate[i]
                   rating[i],rating[j]=rating[j],rating[i]
          for i in range(0,len(avgrate)):
             sumsxy+=avgrate[i]*rating[i]
             sumsx+=avgrate[i]
             sumsy+=rating[i]
             sumsx2+=avgrate[i]*avgrate[i]
             sumsx3+=rating[i]*rating[i]
          m=sumsx*sumsx
          n=sumsy*sumsy
          c=len(avgrate)
          d=0.0
          d=((c*sumsx2)-m)*((c*sumsx3)-n)**0.5
          cor=((c*sumsxy)-sumsxy)/d
          if(cor<1):
             s="Not Co-related"
          if(cor>1):
             s="Co-related"
          m="CORELATION BETWEEN AVERAGE RATE AND RATINGS"+"----"+s
          plt.scatter(rating,avgrate,color="black")
          plt.title(m,color="red")
          plt.xlabel("RATINGS",color="purple")
          plt.ylabel("AVERAGE RATE",color="purple")
          plt.show()
          cf.close()
       elif(d=="HORIZONTAL BAR GRAPH"):
          def barh(p,n):
             plot= plt.barh(p,n,color='olive',ecolor='black')
             plt.ylabel("CUISINE",color='purple')
             plt.xlabel("COUNT OF THE CUISINE",color='purple')
             plt.title(" HORIZONTAL BAR GRAPH-count of cuisine Vs cuisine",color='red')
             plt.show()  
          c3=open("file-1.csv","r")
          l=[]
          cuisine=[]
          for line in c3:
             l=line.strip("\n").split(",")
             cuisine.append(l.pop(3))
          Str=''
          for i in cuisine:
             Str+=i
             Str+='-'
             cuisines=Str.lower().replace(' ','').split('-')
             cuisinedict={}
          for j in cuisines:
             if j  in cuisinedict:
                cuisinedict[j]+=1
             else:
                cuisinedict[j]=1
          del cuisinedict['']
          cuisines=[]
          nocuisines=[]
          c1=[]
          n1=[]
          c2=[]
          n2=[]
          for k in cuisinedict:
             cuisines.append(k)
             nocuisines.append(cuisinedict[k])
          for i in range(0,35):
             c1.append(cuisines[i])
             n1.append(nocuisines[i])
          barh(c1,n1)
          for i in range(35,77):
             c2.append(cuisines[i])
             n2.append(nocuisines[i])
          barh(c2,n2)
          c3.close()
       elif(d=="SCATTER PLOT"):
          
          def scatter(p,n):
             plt.scatter(p,n,color='cyan')
             plt.title("SCATTER PLOT - Average price Vs Number of restaurants ",color='red')
             plt.xlabel("Average price",color='purple')
             plt.xticks(p,rotation=90)
             plt.ylabel("Number of restaurants with the average price",color='purple')
             plt.show()

          l=[]
          price=[]
          dict1={}
          p=[]
          n=[]
          c2=open("file-1.csv","r")
          for line in c2:
             l=line.strip("\n").split(",")
             price.append(int(l[4]))
          for i in price:
             if i not in dict1:
                dict1[i]=1
             else:
                dict1[i]+=1
          for i in dict1:
              p.append(i)
              n.append(dict1[i])
          for i in range(0,len(p)):
               for j in range(i+1,len(p)):
                   if(p[i]>p[j]):
                       p[i],p[j]=p[j],p[i]
                       n[i],n[j]=n[j],n[i]
          l=[]
          for i in p:
              l.append(str(i))
          scatter(l,n)
          c2.close()
       elif(d=="3D SCATTER PLOT"):
          lists=[]
          avg=[]
          dict1={}
          dict2={}
          rate=[]
          votes=[]
          sums=0
          cums=0.0
          s=0
          dict3={}
          x=[]
          y=[]
          z=[]
          file=open("file-1.csv","r")
          for line in file:
             lists=line.strip("\n").split(",")
             rate.append(lists[9])
             votes.append(lists[11])
             avg.append(lists[4])
          for i in rate:
             if i not in dict1:
                dict1[i]=1
             else:
                dict1[i]+=1
          for i in dict1:
             for j in range(0,int(dict1[i])):
                sums+=int(avg[j])
                cums+=float(votes[j])
             dict2[i]=int(sums/1000)
             dict3[i]=int(cums/100000)
          for i in dict2:
             x.append(i)
             y.append(dict2[i])
          for j in dict3:
             z.append(dict3[j])
          fig = plt.figure()
          ax = fig.add_subplot(111, projection='3d')
          ax.set_xlim3d(0,12)
          ax.set_ylim3d(0,2500)
          ax.set_zlim3d(0,2500)
          plt.title("3D SCATTER PLOT- Average rate Vs Average votes Vs Rating",color='red')
          ax.set_xlabel("AVERAGE RATE",color='blue')
          ax.set_ylabel("AVERAGE VOTES",color='green')
          ax.set_zlabel(" RATINGS",color='purple')
          ax.scatter(x,y,z,c='black', s=10)
          ax.view_init(30, 185)
          plt.show()
          file.close()
       elif(d=="PIE CHART"):
          c1=open("file-1.csv","r")
          lists=[]
          m=0
          ratings=[]
          newlist=[]
          newlist2=[]
          percentage=[]
          colors=['rosybrown','lightcoral','indianred','brown','firebrick','maroon','red','salmon','bisque','gold','olive','palegreen','lightgreen','lightyellow','crimson','pink','yellow','azure','cyan','lime','royalblue','blue','wheat','goldenrod','khaki','aqua','teal','lavender','navy','violet','chocolate','lightslategray','fuchsia']
          dict1={}
          for lines in c1:
             lists=lines.strip("\n").split(",")
             ratings.append(lists[10])
          for i in ratings:
             if i not in dict1:
                dict1[i]=1
             else:
                dict1[i]+=1
          for i in dict1:
             newlist.append(i)
             newlist2.append(dict1[i])
          for i in range(0,len(newlist)):
             for j in range(i,len(newlist)):
                if(newlist[i]<newlist[j]):
                   newlist[i],newlist[j]=newlist[j],newlist[i]
                   newlist2[i],newlist2[j]=newlist2[j],newlist2[i]
          fig1,ax1=plt.subplots()
          patches,texts= ax1.pie(newlist2,startangle=90,colors=colors)
          plt.title("PIE CHART for Total Ratings")
          plt.legend(bbox_to_anchor=(0.0, 1),labels=newlist,loc=1,prop={'size':6})
          plt.show()
          c1.close()
       elif(d=="AREA PLOT"):
          lists=[]
          rate=[]
          dict1={}
          files=open("file-1.csv","r") 
          for line in files: 
             lists=line.split(",")
             rate.append(int(lists[4]))
          for i in rate:
             if i not in dict1:
                dict1[i]=1
             else:
                dict1[i]+=1
          x=[]
          y=[]
          for i in dict1:
             x.append(i)
             y.append(dict1[i])
          for i in range(0,len(x)):
             for j in range(0,len(x)-i-1):
                if(x[j]>x[j+1]):
                   x[j],x[j+1]=x[j+1],x[j]
                   y[j],y[j+1]=y[j+1],y[j]
          plt.title("AREA DENSITY PLOT-Average rate Vs Number of restaurants",color='red')
          plt.fill_between(x,y,color='olive')
          plt.xlabel("Average rate")
          plt.ylabel(" Number of Restaurants with the average rate")
          plt.show()
          files.close()
   button5 = Button(root2, text="SEE", command=ok)
   button5.pack()
   mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                  RESTAURANT NAME
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def search1():
   global master
   master = Tk()
   x=(master.winfo_screenwidth()-master.winfo_reqwidth())/2
   y=(master.winfo_screenheight()-master.winfo_height())/2
   master.geometry("+%d+%d" %(x,y))
   master.title("Search")
   Label(master, text="Restaurant Name").grid(row=0)
   global e1
   e1 = Entry(master)
   e1.grid(row=0, column=1)
   Button(master, text='Search', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)   
def show_entry_fields():
   m=e1.get()
   flag=0
   s=""
   file=open("file-1.csv","r")
   for line in file:
      List=line.strip("\n").split(",")
      if(List[0]==m):
         s+="NAME OF RESTAURANT :"+List[0]+"\nCITY :"+List[1]+"\nADDDRESS: "+List[2]+"\nCUISINES SERVED :"+List[3]+"\nAVERAGE PRICE FOR TWO :"+List[4]+"\nVEGETRAIAN:"+List[5]+"\nPARTY ORDERS TAKEN:"+List[6]+"\nONLINE TABLE BOOKING:"+List[7]+"\nALCOHOL SERVED:"+List[8]+"\nAVERAGE RATING:"+List[9]
         flag=1
         break
   if (flag==1):
      helv30=font.Font(family='Helvetica', size=30)
      master.destroy()
      global root3
      root3=Tk()
      '''x=(root3.winfo_screenwidth()-root3.winfo_reqwidth())/2
      y=(root3.winfo_screenheight()-root3.winfo_height())/2
      root3.geometry("+%d+%d" %(x,y))'''
      root3.configure(bg="white")
      root3.title("Restaurant")
      def exits():
         root3.destroy()
         root.destroy()
      w=Label(root3, text=s, font=helv30,background="white")
      w.grid(row=0,column=0,columnspan=3,rowspan=10)
      b18=Button(root3,text="BACK",command=root3.destroy,background="pink")
      b18.grid(row=12,column=35)
      b19=Button(root3,text="EXIT",command=exits,background="pink")
      b19.grid(row=13,column=35)
   elif (flag==0):
      Msg=messagebox.askquestion("Not Found","Restaurant not found would you like to search again?")
      master.destroy()
      if(Msg=='yes'):
         search1()
      elif(Msg=='no'):
         home()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                 CITY NAME
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def search2():
    file=open("file-1.csv","r")
    OPTIONS=[]
    for line in file:
        List=line.strip("\n").split(",")
        if(List[1]not in OPTIONS):
            OPTIONS.append(List[1])

    master = Tk()
    x=(master.winfo_screenwidth()-master.winfo_reqwidth())/2
    y=(master.winfo_screenheight()-master.winfo_height())/2
    master.geometry("+%d+%d" %(x,y))
    variable = StringVar(master)
    variable.set("CITIES") # default value

    w = OptionMenu(master, variable, *OPTIONS)
    w.pack()
    file.seek(0)
    def ok():
        s=""
        d=variable.get()
        master.destroy()
        helv24=font.Font(family='Helvetica', size=24)
        root4=Tk()
        root4.configure(bg="white")
        c1=Label(root4,text="RESTAURANTS FOUND",font=helv24,background="white")
        c1.pack()
        for line in file:
            List=line.strip("\n").split(",")
            if(List[1]==d):
                i=0 
                for line in file:
                    List=line.strip("\n").split(",")
                    if(List[1]==d):
                       s+="\n\n\n"+"NAME OF RESTAURANT:  "+List[0]+"\nCITY:  "+List[1]+"\nADDRESS:  "+List[2]+"\nCUISINES SERVED:  "+List[3]+"\nAVERAGE PRICE FOR TWO:"+List[4]+"\nVEGETRAIAN :"+List[5]+"\nPARTY ORDERS TAKEN :"+List[6]+"\nONLINE TABLE BOOKING :"+List[7]+"\nALCOHOL SERVED :"+List[8]+"\nAVERAGE RATING :"+List[9]
                       i+=1
        def exit2():
           root.destroy()
           root4.destroy()
        S = Scrollbar(root4)
        T = Text(root4, height=i, width=100)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        T.insert(END, s)
        b2=Button(root4,text="Back",command=root4.destroy,font=helv24,background="pink")
        b2.pack()
        b3=Button(root4,text="Exit",command=exit2,font=helv24,background="pink")
        b3.pack()
        mainloop()        
    button = Button(master, text="SEARCH", command=ok)
    button.pack()
    mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                  FILTERS
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def search3():
   master = Tk()
   '''x=(master.winfo_screenwidth()-master.winfo_reqwidth())/2
   y=(master.winfo_screenheight()-master.winfo_height())/2
   master.geometry("+%d+%d" %(x,y))'''
   master.configure(bg="white")
   helv22=font.Font(family='Helvetica', size=22)
   file=open("file-1.csv","r")
   OPTIONS=[]
   for line in file:
      List=line.strip("\n").split(",")
      if(List[1]not in OPTIONS):
         OPTIONS.append(List[1])

   variable = StringVar(master)
   variable.set("CITY") # default value
   m1=Label(master,text="City :",background="white")
   m1.grid(row=1,column=0)
   w1= OptionMenu(master, variable, *OPTIONS)
   w1.grid(row=1,column=3)
   file.seek(0)
   m2=Label(master,text="Average Rating :",background="white")
   m2.grid(row=2,column=0)
   w2=IntVar()
   w2= Spinbox(master,values=(0,1.8,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9))
   w2.grid(row=2,column=3)
   m3=Label(master,text="Average Price for Two :",background="white")
   m3.grid(row=3,column=0)
   e1 = Entry(master,background="white")
   e1.grid(row=3, column=3)
   CUISINES=[]
   for line in file:
      List=line.strip("\n").split(",")
      List2=List[3].replace(" ",'').split("-")
      for i in List2:
         if(i not in CUISINES):
            CUISINES.append(i)

   variable1= StringVar(master)
   variable1.set("CUISINES") # default value
   m4=Label(master,text="Cuisine:",background="white")
   m4.grid(row=4,column=0)
   w4= OptionMenu(master, variable1, *CUISINES)
   w4.grid(row=4,column=3)
   file.seek(0)
   var1=IntVar()
   var2=IntVar()
   var3=IntVar()
   var4=IntVar()
   var5=IntVar()
   var6=IntVar()
   List=["VEGETRIAN ONLY","HAS ONLINE ORDERING","HAS PARTY ORDERING","SERVES ALCOHOL"]
   chk1=Checkbutton(master,text=List[0],variable=var1,background="white")
   chk1.grid(row=5,column=0)
   chk2=Checkbutton(master,text=List[1],variable=var2,background="white")
   chk2.grid(row=5,column=1)
   chk3=Checkbutton(master,text=List[2],variable=var3,background="white")
   chk3.grid(row=5,column=2)
   chk4=Checkbutton(master,text=List[3],variable=var4,background="white")
   chk4.grid(row=5,column=3)
   def getdata():
       a1=variable.get()
       a2=w2.get()
       a3=e1.get()
       a4=variable1.get()
       a5=var1.get()
       a6=var2.get()
       a7=var3.get()
       a8=var4.get()
       master.destroy()
       s=""
       root4=Tk()
       root4.configure(bg="white")
       c1=Label(root4,text="RESTAURANTS FOUND",background="white")
       c1.pack()
       myfile=open("file-1.csv")
       i=0
       if(a5==1):
          b1="Yes"
       elif(a5==0):
          b1="YesorNo"
       if(a6==1):
          b2="Yes"
       elif(a6==0):
          b2="YesorNo"
       if(a7==1):
          b3="Yes"
       elif(a7==0):
          b3="YesorNo"
       if(a8==1):
          b4="Yes"
       elif(a8==0):
          b4="YesorNo"
       count=0
       for line in myfile:
          List=line.strip("\n").split(",")
          List3=List[3].replace(" ",'').split("-")
          if(a1=="CITY" or a2==0 or a3==None or a4=="CUISINES"):
              s="PLEASE ENTER ALL THE DATAS TO FILTER"
          elif(List[1]==a1 and List[4]==a3 and List[9]==a2 and (a4 in List3)):
              i+=1
              s+="NAME OF RESTAURANT :"+List[0]+"\nCITY :"+List[1]+"\nADDDRESS: "+List[2]+"\nCUISINES SERVED :"+List[3]+"\nAVERAGE PRICE FOR TWO :"+List[4]+"\nVEGETRAIAN:"+List[5]+"\nPARTY ORDERS TAKEN:"+List[6]+"\nONLINE TABLE BOOKING:"+List[7]+"\nALCOHOL SERVED:"+List[8]+"\nAVERAGE RATING:"+List[9]+"\n\n"
          elif(i==0):
             s="Restaurants not found"
       def exit3():
          root4.destroy()
          root.destroy()
       S = Scrollbar(root4)
       T = Text(root4, height=i, width=100)
       S.pack(side=RIGHT, fill=Y)
       T.pack(side=LEFT, fill=Y)
       S.config(command=T.yview)
       T.config(yscrollcommand=S.set)
       T.insert(END, s)
       b2=Button(root4,text="Back",command=root4.destroy,background="pink")
       b2.pack()
       b3=Button(root4,text="Exit",command=exit3,background="pink")
       b3.pack()
       mainloop()        

   s=Button(master,text="SEARCH",background="white",command=getdata)
   s.grid(row=6,column=2)
   mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                  MAIN HOME PAGE
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def home():
   global root
   root=Tk()
   helv24=font.Font(family='Helvetica', size=24)
   root.configure(bg="white")
   a=PhotoImage(file="fhome.png")
   b=PhotoImage(file="fgraphs.png")
   d=PhotoImage(file="zomato.png")
   f=PhotoImage(file="exit.png")
   e=PhotoImage(file="fcity.png")
   g=PhotoImage(file="fname.png")
   h=PhotoImage(file="ffilter.png")
   m4=Label(root,text="WELCOME TO ZOMATO TOP MOST \n RESTAURANT SEARCH ENGINE WITH \n MORE THAN 8 THOUSAND \n RESTAURANTS IN INDIA",bg="white",font=helv24)
   m=Button(root,image=a)
   m1=Button(root,image=b,command=graphs)
   m3=Label(root,image=d)
   m6=Button(root,image=e,command=search2)
   m7=Button(root,image=g,command=search1)
   m8=Button(root,image=h,command=search3)
   m5=Button(root,image=f,command=root.destroy)
   m4.grid(row=1,column=0,columnspan=2)
   m.grid(row=0,column=0)
   m1.grid(row=0,column=1)
   m6.grid(row=0,column=2)
   m7.grid(row=0,column=3)
   m8.grid(row=0,column=4)
   m3.grid(row=2,column=4)
   m5.grid(row=3,column=4)
   m4.grid(row=2,column=0,columnspan=3)
   mainloop()

home()






























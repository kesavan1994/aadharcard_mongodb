import re
import io
import random as r
from datetime import datetime,timedelta,time
from fpdf import FPDF
import pandas as pd
import qrcode
from tabulate import tabulate
from PIL import Image,ImageFont,ImageDraw


# Create a AAdhar Card
def Create():
  def Name():
      Name=input("Enter the Name: ").capitalize()
      F_Name=input("Enter the Father Name: ").capitalize()
      name = Name +' '+F_Name
      return name
   
    #DOB Function
  def Dob():
      DOB_f= re.compile(r'[0-3][0-9]-[0-1][0-2]-([1-2][0-9][0-9][0-9])')
      DOB=input("Enter the valid D-M-Y: " )
      if re.fullmatch(DOB_f,DOB):
        return DOB
      else:
        print("invaild DOB")  
    #Gender Function  
  def Gender():  
      gen="male","female","transgender"  
      gender=input("Ender the Gender: ")

      for i in range(len(gen)):
        if gender == gen[i]:
          return gender
          break
        else:
          print("invaild Gender")  
          
    #Education Function
  def Education():
        print("""please select one option :
                  
                  1.NA
                  2.10th
                  3.12th
                  4.Under Graduate
                  5.Post Graduate
                  6.Master
              
              """)
        option = int(input("Enter your option: "))
        if option<7:
          if option==1:
              Education={
                            "Education"  :'NA',
                            "stream"     :'NA'}
              return Education
          elif option==2:
              Education={
                            "Education"  :'10th',
                            "stream"     :'NA'
              }
              return Education
          elif option==3:
              
              stream=input("Enter the stream in 12th: ").capitalize()
              Education={
                  "Education":"12th",
                  "stream":stream
              }
              return Education
          elif option==4:
              ug=input("Enter the Under Graduate in: ").capitalize()
              stream=input("Enter the stream : ").capitalize()
            
              Education={
                  "Education":ug,
                  "stream":stream
              }
              return Education
          elif option==5:
              pg=input("Enter the Post Graduate in: ").capitalize()
              stream=input("Enter the stream: ").capitalize()
              
              Education={
                  "Education":pg,
                  "stream":stream
              }
              return Education
          elif option==6:
              master=input("Enter the Master in: ").capitalize()
              stream=input("Enter the stream: ").capitalize()
            
              Education={
                  "Master":master,
                  "stream":stream
              }
              return Education 
        else:      
          print("invalid option")
    #address      
  def Address():
      
          No= input("Enter the Door No: ").capitalize()
          street=input("Enter the street: ").capitalize()
          City= input("Enter the City: ").capitalize()
          State=input("Enter the State: ").capitalize()
          Pincode=input("Enter the Pincode: ")

      
          address={
              "No,street":No +','+street+',',
              "City":City+',',
              "State":State+',',
              "Pincode":City+'-'+Pincode+'.'
          }
          return address
    #Email
  def Email(): 
      reg=re.compile(r'([a-zA-Z],{1,})*([0-9.-_])*[a-zA-Z0-9]+@([a-zA-Z]{2,5})+[.a-zA-Z]+')
      email=input("Enter the valid Mail-id: ")
      if re.fullmatch(reg,email):
          return email
      else:
        print("mail-id not valid")    

  def Profile_img():
      picc = input("Enter the pic path: ")
      profile_img = Image.open(picc)#Image
      im_bytes = io.BytesIO() # to convert image into binary values
      profile_img.save(im_bytes,format='jpeg')
      pic={
          'name':"profile_img",
          'image':im_bytes.getvalue()# to getvalues()
      }
      return pic
  def Aadhar():
      c=r.randint(2000,9999)
      d=r.randint(1000,9999)
      adh=(str(c)+'-'+str(d)+'-'+str(d))
      return adh


      records.create_index('Aadhar_Id',unique =True)
  def Created_date():
      x=datetime.now()
      y=datetime.strftime(x,'%d/%m/%Y %H:%M')
      return y
  def Renewal_date():
        z= datetime.now() + timedelta(days=1098)
        y=datetime.strftime(z,'%d/%m/%Y %H:%M')
        return y
    
  a={'Aadhar_Id':Aadhar(),"Name": Name(),'DOB':Dob(),"Gender":Gender(),"Education Details":Education(),
      "Address":Address(),"Email-id":Email(),"Pic":Profile_img(),"Created_date":Created_date(),"renewal_date":Renewal_date()}

  records.insert_one(a)
# Updation in aadhar card

def Update():
  aadhar_num=input("Enter the valid aadhar number: ")
  print(""" Please select the option:
        
        1.Name
        2.Gender
        3.Education Details
        4.Address
        5.profile_pic
            
        """)
  option=int(input("Enter the option: "))
  if option<6:
    if option== 1:    
          find={"Aadhar_Id":aadhar_num}                 #Update of Name
          update={"$set":{"Name":Name()}}
          records.update_one(find,update)
          print("You Name Sucessfully Updated")
    elif option==2:                                 #Update of Gender
          find={"Aadhar_Id":aadhar_num}
          update={"$set":{"Gender":Gender()}}
          records.update_one(find,update)
          print("You Gender Sucessfully Updated")

    elif option==3:                                 #Update of Education
          find={"Aadhar_Id":aadhar_num}
          update={"$set":{"Education Details":Education()}}
          
          records.update_one(find,update)
          print("You Education Details Sucessfully Updated")
    elif option==4:                                  #Update of Address
          
          find={"Aadhar_Id":aadhar_num}
          update={"$set":{"Address":Address() }}
          records.update_one(find,update)
          print("You Address Sucessfully Updated")
    elif option==5:                                   #Update of Profile pics
          find={"Aadhar_Id":aadhar_num}
          update={"$set":{"Pic": Profile_img() }}
          
          records.update_one(find,update)
          print("You Profile Pic Sucessfully Updated")
  else:
      print("Invalid option")


def download():

  pdf=FPDF()
  pdf.add_page()
  pdf.set_font("Arial",size=5)



  obj_qr = qrcode.QRCode(  
      version = 1,  
      error_correction = qrcode.constants.ERROR_CORRECT_L,  
      box_size = 2,  
      border = 4,  
  )  

  d=input("Enter the Aadharid: ")
  data={'Aadhar_Id':d}
  details = records.find(data,{
      '_id':0,'Aadhar_Id':1,"Name":1,'DOB':1,"Gender":1,"Education Details.Education":1,"Education Details.stream":1
      ,"Address.No,street":1,"Address.City":1,"Address.State":1,"Address.Pincode":1,"Email-id":1,'Created_date':1,"renewal_date":1})

  for i in details:
    pdf.set_font("Arial",size=20)
    aadhar= ( "                        {}   "   .format(i['Aadhar_Id']))
    pdf.cell(180,15, aadhar,ln=1,align='C') 
    nam=         ( "           Name                    :        {}           " .format(i["Name"]))        
    dob=         ( "           DOB                     :       {}           "  .format(i['DOB'])  )
    Gender=      ( "           Gender                  :       {}           "  .format(i["Gender"]))
    education=   ( "           Education Details       :         "          )
    education1 = ( "                  Education        :       {}         " .format(i['Education Details']['Education']))
    stream =     ( "                   Stream          :       {}         " .format(i['Education Details']['stream']))
    address=     ( "           Address                 :                   "  )
    street=      ( "                           Street  :    {}     "  .format(i["Address"]['No,street']))
    city=        ( "                City            :       {}          "  .format(i["Address"]['City']))
    state=       ( "                   State           :       {}          "  .format(i["Address"]['State']))
    pincode=     ( "                   Pincode         :       {}          "  .format(i["Address"]['Pincode']))
    email=       ( "           Email-id                :       {}          "  .format(i["Email-id"]))
    createddate= ( "           Created_date            :       {}          "  .format(i["Created_date"])) 
    renewaldate= ( "           renewal_date            :       {}          "  .format(i["renewal_date"])) 
  

  

  pdf.set_font("Arial",size=10)
  pdf.set_fill_color(255, 255, 255)
  pdf.cell(200,10, nam,ln=2,align='C')
  pdf.cell(180,10, dob,ln=3,align='C')
  pdf.cell(182,10, Gender,ln=4,align='C')
  pdf.cell(158,10, education,ln=5,align='C')
  pdf.cell(175,10, education1,ln=6,align='C')
  pdf.cell(175,10, stream,ln=7,align='C')
  pdf.cell(173,10, address,ln=8,align='C')
  pdf.cell(180,10, street,ln=9,align='C')
  pdf.cell(187,10, city,ln=10,align='C')
  pdf.cell(196,10, pincode,ln=11,align='C')
  pdf.cell(211,10, email,ln=12,align='C')
  pdf.cell(196,19, createddate,ln=13,align='C')
  pdf.cell(196,19, renewaldate,ln=13,align='C')

  #binary image to IMAGA
  retival= records.find_one(data)  
  pil_im = Image.open(io.BytesIO(retival['Pic']['image']))
    #df.set_font("Arial",size=10)
  img = pil_im.crop()
  image=img.save("img.jpeg")
    #pdf.cell(300, 10, txt = "hi\n") 

  pdf.image("img.jpeg",20,30,30,40)


  # Qr Code generation

  # using the add_data() function  
  obj_qr.add_data(qr)  
  # using the make() function  
  obj_qr.make(fit = True)  
  # using the make_image() function  
  qr_img = obj_qr.make_image(fill_color = "black", back_color = "white")  
  # saving the QR code image  
  qr_img.save("aadharQrcode.png")  
  pdf.image("aadharQrcode.png",170,40,35,35)

  pdf.output("Aadharcard.pdf")


      
if __name__=="__main__" : 
  print("""Enter the option 
        1.Create Aadhar card
        2.Update Aadhar card
        3.Download Aadhar card
        """)
  option=int(input("Enter the option: "))
  if option<4:
      if option==1:                                   #To Craete the Aadhar card
        Create()
      elif option==2:                                 #To Update the Aadhar card
        Update()
      elif option==3:                                 #To Update the Aadhar card
       download()
  else:
    print("Please enter the valid option")                        
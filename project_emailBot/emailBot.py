# simple mail transport protocol
import smtplib
# # creating a server with smtp lib 
#  argument = server name and port  number 
server = smtplib.SMTP('smtp.gmail.com',587)
# providing traqnsport layer security 
server.starttls() 
# who u are 
server.login('scientistsshrawan12@gmail.com','Shrawan@2050')
server.sentmail('scientistsshrawan12@gmail.com','scientistsshrawan12@gmail.com',"this is testing email bot by shrawan kuma r to vikhyat kumar ")
# Sending emails with Python


Library used: smtplib

Sending emails with Python, the steps include conneccting to an email server, confirming connection, settinga protocol, loggin on, and sending the message. This could be automated using Python built-in smtplib libray.


## SMTP or Simple Mail Transfer Protocol

Each major email provider has their own dedicated STMP server. It is a domain name that it connects to when trying to access an email in program. 
  
|  Provider                | SMTP server domain name  |  
|--------------------------|--------------------------|
|  Gmail                   | smtp.gmail.com           | 
|  Yahoo Mail              | smtp.mail.yahoo.com      |  
| Outlook.com/Hotmail.com  | smtp.mail.outlook.com    |  
|  AT&T                    | smtp.mail.att.com   (Use port 546)| 
|  Verizon                 | smtp.verizon.net (Use port 546)  | 
|  Comcast                 | smtp.comcast.net                 | 


Link required to visit: https://support.google.com/accounts/answer/185839


# Receiving emails with Python 

Library used: imaplib and email library 

Connecting python to gmail with appropriate port and once connceted using email library to search for the particular content. Email library is just the matter of choice any custom code would do the job, better or worse depending on code structure. 



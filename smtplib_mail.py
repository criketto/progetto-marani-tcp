import smtplib as smtp
def invio():
    oggetto_mail = "Prova eliminazione record database\n\n"
    contenuto_mail= "SalVE prOF sa cose uno spof ?"

    messaggio= str(oggetto_mail+contenuto_mail)

    mail_server= "smtp.gmail.com"
    port_mail_server= 587

    mail= "riccardo.marani05@gmail.com" #mail mittente
    password= "kaou amat uuza ciuj" #password mittente
    destination_email= "singh.harman@einaudicorreggio.it" #mail destinatario

    email= smtp.SMTP(mail_server, port_mail_server)

    email.ehlo()

    email.starttls()

    email.login(mail, password=password)

    email.sendmail(mail, destination_email, messaggio)

    email.quit()
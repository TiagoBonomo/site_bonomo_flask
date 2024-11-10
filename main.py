from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText



app = Flask(__name__)


@app.route('/')
def homepage():

    return render_template("index.html")


@app.route("/enviar", methods = ["post"] )
def enviar():
    fname = request.form["fname"] 
    lname = request.form["lname"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]

    memail = f"Nome: {fname} {lname} \n E-mail: {email} \n Assunto: {subject} \n Mensagem: {message}  "

    sender = "projetosbonomo@gmail.com"
    recipients = ["tiagofbonomo@gmail.com"]
    password = "gpst ncoj swve ealt"

    msg = MIMEText(memail)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())

    
    return render_template("index.html")






if __name__ == '__main__':
    app.run(debug=True)

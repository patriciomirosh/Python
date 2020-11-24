import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from decouple import config
import pandas as pd
# This part i enclose the file where i have the mails to send.
df = pd.read_excel('correos.xlsx', sheet_name='Table 1')
df
dfem=df.loc[:, ['empresas', 'mails']]
dfem.head(30)
# Inicializate the scripts:
for i in range(0,len(dfem)):
    remitente = 'mirospatricio@gmail.com'
    try:
        destinatarios = dfem['mails'][i]
    except:
        print('Encoding error')
    asunto = 'Ref: Me postulo para trabajar'
    
    cuerpo = '''Dear {}: 
I send this mail for make contact with our sales department and provide my curriculum, i have experienced in online sales .  '''.format(dfem['empresas'][i])
    ruta_adjunto = 'CV_miroshnitshenko_Patricio_Ing_3010.pdf'
    nombre_adjunto = 'Curriculo Miroshnitshenko Patricio'

    # Create the multipart objecto 
    mensaje = MIMEMultipart()
    
    # we place the attributes of message 
    mensaje['From'] = remitente
    mensaje['To'] = destinatarios
    mensaje['Subject'] = asunto
    
    # add the body of the message at the mime object
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    # Open the files we wish to enclose

    pdfname = 'CV_miroshnitshenko_Patricio_Ing_3010.pdf'
    pdfname2= 'Carta_de_presentacion.pdf'
    # open the file in bynary
    binary_pdf = open(pdfname, 'rb')
    binary_pdf2 = open(pdfname2, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload2 = MIMEBase('application', 'octate-stream', Name=pdfname2)

    payload.set_payload((binary_pdf).read())
    payload2.set_payload((binary_pdf2).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)
    encoders.encode_base64(payload2)
    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    payload2.add_header('Content-Decomposition', 'attachment', filename=pdfname2)

    
    mensaje.attach(payload)
    mensaje.attach(payload2)




    # Create the conexion to the server
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Encoding the conection
    sesion_smtp.starttls()

    # Starting the server conexion
    SECRET_KEY = config('SECRET_KEY')
    sesion_smtp.login('mirospatricio@gmail.com',SECRET_KEY)

    # we convert the object message in to text
    texto = mensaje.as_string()

    # Send the message
    try: # try to catch encode error as '-' in the mails, 
        sesion_smtp.sendmail(remitente, destinatarios, texto)
    except:
        print('Encode Error ')
    #We close the conextion
    sesion_smtp.quit()

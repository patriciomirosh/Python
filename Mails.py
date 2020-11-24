import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from decouple import config
import pandas as pd

df = pd.read_excel('correos.xlsx', sheet_name='Table 1')
df
dfem=df.loc[:, ['empresas', 'mails']]
dfem.head(30)
# Iniciamos los parámetros del script

for i in range(424,len(dfem)):
    remitente = 'mirospatricio@gmail.com'
    try:
        destinatarios = dfem['mails'][i]
    except:
        print('Encoding error')
    asunto = 'Ref: Me postulo para trabajar'
    
    cuerpo = '''Estimados {}: 
Mi nombre es Miroshnitshenko Patricio, si me regalan unos segundos les comento mi situación:  me recibí recientemente de Ingeniero Químico, pero no poseo experiencia profesional aunque sí experiencia en el área de ventas y facturación en pintureria, por esta razón estoy en la búsqueda activa y predispuesto a trabajar sin remuneracion con el objetivo de aprender, obtener experiencia y ofrecer mis conocimientos. 
Estoy dispuesto a trabajar en cualquier área,  tengo conocimientos en muchos programas informaticos como: hysys y Dwsim y se programar en python. Le adjunto mi CV y mi carta de presentación.
Saludos cordiales.  '''.format(dfem['empresas'][i])
    ruta_adjunto = 'CV_miroshnitshenko_Patricio_Ing_3010.pdf'
    nombre_adjunto = 'Curriculo Miroshnitshenko Patricio'

    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = destinatarios
    mensaje['Subject'] = asunto
    
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    # Abrimos el archivo que vamos a adjuntar

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




    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor
    SECRET_KEY = config('SECRET_KEY')
    sesion_smtp.login('mirospatricio@gmail.com',SECRET_KEY)

    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

    # Enviamos el mensaje
    try:
        sesion_smtp.sendmail(remitente, destinatarios, texto)
    except:
        print('Encode Error ')
    # Cerramos la conexión
    sesion_smtp.quit()
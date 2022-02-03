import smtplib
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ("192.168.0.4", 5000) 
sock.bind(address)
data, address = sock.recvfrom(1024)

def datos():
    while True:
        data, address = sock.recvfrom(1024)
        
        acelerometro_x = float(data[44:51])
        acelerometro_y = float(data[53:60])
        acelerometro_z = float(data[61:68])
        #print(acelerometro_x, "   ", acelerometro_y,"   ",acelerometro_z)
        
        norma = (float(((acelerometro_x**2)+(acelerometro_y**2)+(acelerometro_z**2))**(1/2)))      
        print (norma)
        if norma > 25:
            print("WARNING!!")
            def enviarmail():
                mensaje = "HELP!" 
                subject = "ALERTA" # el asunto del mensaje
                mensaje = "Subject: {}\n\n{}".format(subject, mensaje) #el mensaje con asunto
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login('jorgecamachoweb@gmail.com', "6mksyGawWT11190")
                server.sendmail("jorgecamachoweb@gmail.com", "jorgecamachoweb@gmail.com", mensaje)
                server.quit()
                return
            enviarmail()
   
datos()
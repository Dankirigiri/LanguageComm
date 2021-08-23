import socket
import json
from fibonacci import fibonacci

wf = open("config.json", "r")
config = json.load(wf)
server = config.get("SERVER")
port = config.get("PORT")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen()
print("[!] El servidor ha iniciado correctamente")
conn, addr = s.accept()
with conn:
    print("Connected by ", addr)
    while True:
        data = conn.recv(1024)
        datad = data.decode("utf-8")
        args = datad.split(" ")
        print(datad)
        if(args[0] == "close"):
            print("[!] Cerrando el servidor...")
            break
        elif(args[0] == "fibonacci"):
            print("Pasé por acá")
            try:
                fibonacci(int(args[1]))
            except:
                conn.send(str.encode("Por favor, ingrese un numero válido"))
        conn.sendall(data)
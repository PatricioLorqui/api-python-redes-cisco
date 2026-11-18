import requests
import csv

baseUri = "http://localhost:58000/api/v1"
# Ingresar Service Ticket
ticket = "NC-6-b5a954b707244318b3db-nbi"#cambiar token por el generado
headers = {"X-Auth-Token": ticket}
# Consultar dispositivos de red
resp = requests.get(baseUri + "/network-device", headers=headers)
networkDevices = resp.json()["response"]
# Consultar hosts
resp = requests.get(baseUri + "/host", headers=headers)
hosts = resp.json()["response"]
# Exportar inventario a CSV
with open("inventario_red.csv", "w", newline="", encoding="utf-8-sig") as archivo:

    writer = csv.writer(archivo, delimiter=";")
    writer.writerow(["Tipo", "Nombre", "IP", "MAC", "Plataforma"])

    for item in networkDevices:
        writer.writerow([ "Dispositivo de red", item.get("hostname", "Sin nombre"), item.get("managementIpAddress", "Sin IP"), item.get("macAddress", ""), item.get("platformId", "") ])

    for item in hosts:
        writer.writerow([
            "Host",
            item.get("hostName", "Sin nombre"),
            item.get("hostIp", "Sin IP"),
            item.get("hostMac", ""),
            ""
        ])

print("Inventario exportado correctamente.")
print("Dispositivos:", len(networkDevices))
print("Hosts:", len(hosts))

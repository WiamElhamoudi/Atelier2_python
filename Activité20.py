adresses_ip=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
#1. Quelle est la première adresse dans la liste ?
print(f"la première adresse dans la liste: {adresses_ip[0]}")

#2. Quelle est la dernière adresse dans la liste ?
print(f"la première adresse dans la liste: {adresses_ip[4]}")

#3. Quelle est la troisième adresse dans la liste ?
print(f"la première adresse dans la liste: {adresses_ip[2]}")

#4. Ajoutez l’adresse IP "172.31.0.1" à la liste ?
adresses_ip.append("172.31.0.1")
print(f"Après ajout de '172.31.0.1' :{adresses_ip}")

#5. Supprimez l’adresse IP "200.100.50.1" de la liste.
adresses_ip.remove("200.100.50.1")
print(f"Après suppression de '200.100.50.1' :{adresses_ip}")

#6. Combien d’adresses restant dans la liste après les modifications ?
print(f"Nombre d'adresses restantes :{len(adresses_ip)}")

#7. Vérifiez si l’adresse "192.168.0.1" est présente dans la liste.
if "192.168.0.1" in adresses_ip:
    print("'192.168.0.1' est présente dans la liste")
else:
    print("'192.168.0.1' n'est pas présente dans la liste")
    
#8. Quelle est la classe de l’adresse IP "10.0.0.1" ?

def classe(ip):
    premier_octet = int(ip.split(".")[0])
    if 1 <= premier_octet <= 126:
        return "A"
    elif 128 <= premier_octet <= 191:
        return "B"
    elif 192 <= premier_octet <= 223:
        return "C"
    else:
        return "Autre"

ip = "10.0.0.1"
print(f"Classe de l'adresse{ip} est : {classe(ip)}") 

#9. Triez les adresses IP de la liste par ordre croissant.
adresses_ip.sort()
print(f"Liste triée :{adresses_ip}")

#10. Vérifiez si toutes les adresses IP de la liste appartiennent à la classe C.

toutes_ip = all(classe(ip) == "C" for ip in adresses_ip)
if toutes_ip:
    print("Toutes les adresses sont de classe C ")
else:
    print("Toutes les adresses ne sont pas de classe C ")

# 11. Comptez combien d’adresses IP de la liste sont des adresses IP publiques.
nb_publiques=0
for ip in adresses_ip:
    premier, deuxieme = map(int, ip.split(".")[:2])

    if (premier == 10) or \
       (premier == 172 and 16 <= deuxieme <= 31) or \
       (premier == 192 and deuxieme == 168) or \
       (premier == 169 and deuxieme == 254):
        continue     
    else:
        nb_publiques+=1
print("Nombre d'adresses IP publiques :", nb_publiques)
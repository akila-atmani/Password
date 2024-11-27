liste_mdp = []
mot_depasse=input("veuillez entrer votre mot de passe:")
liste_mdp.append(mot_depasse)


lettre_majuscule= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre_miniscule= "abcdefghijklmnopqrstuvwxyz"


if len(mot_depasse) <= 8:
  print("votre mot de passe a moin de 8 caractréres, veuillez réessayer de nouveau.") 
  input("nouveau mot de passe:")


if  not any (caractere.isdigit() for caractere in mot_depasse):
 print("votre mot de passe doit contenir au moin un chiffre, veuillez réessayer de nouveau.")
 input("nouveau mot de passe:")


if not (mot_depasse.__contains__("!") or 
        mot_depasse.__contains__("@") or 
        mot_depasse.__contains__("#") or 
        mot_depasse.__contains__("%") or 
        mot_depasse.__contains__("^") or 
        mot_depasse.__contains__("&") or 
        mot_depasse.__contains__("*")):
 print("Le mot de passe ne contient pas de caractère spécial.")
 input("nouveau mot de passe:")



if not any (char in mot_depasse for char in lettre_majuscule):
  print("votre mot de passe ne contient pas de majiscule, veuillez réessayer de nouveau")
  input("nouveau mot de passe:")


if not any (char in mot_depasse for char in lettre_miniscule):
  print(" votre mot de passe ne contient pas de miniscule,veuillez réessayer de nouveau")
  input("nouveau mot de passe:")


else :
  print("votre mot de passe est correct")



import hashlib
hash_obj = hashlib.sha256() 
hash_obj.update(mot_depasse.encode('utf-8'))
hash_hex = hash_obj.hexdigest()

print(f"mot de passe crypté: {hash_hex}")

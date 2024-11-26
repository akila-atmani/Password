mot_depasse=input("veuillez entrer votre mot de passe:")
lettre_majuscule= "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
lettre_miniscule= "a b c d e f g h i j k l m n o p q r s t u v w x y z"
for i in mot_depasse:
 if i < int(8):
  print("votre mot de passe a moin de 8 caractréres.")
 elif i != int:
  print("votre mot de passe doit contenir au moin un chiffre.")
 elif i != "!" or "@" or "#"or "%" or  "^" or "&" or "*":
  print("votre mot de passe doit contenir au moin un caractére spécial.")
 elif i != lettre_majuscule:
  print("votre mot de passe ne contient pas de majiscule.")
 elif i != lettre_miniscule:
  print(" votre mot de passe ne contient pas de miniscule.")
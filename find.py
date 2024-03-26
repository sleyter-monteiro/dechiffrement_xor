# Recherche de mots-clés dans un fichier DLT (.dlt)
import re

def find_keyword_in_file(file_path, keyword):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    matches = {keyword: len(re.finditer(keyword, content))}
    return matches

# Utilisation de la fonction
keyword = input("Entrez le mot clé à rechercher : ") # ["IMEI", "IOS", "Name", "Serial", "MAC", "IMEI 2", "ICCID"]
matches = find_keyword_in_file('log_132846.dlt', keyword)
print("Résultats de la recherche :")
print("-----------------------------------")
print("| {:<10} | {:<10} |".format("Mot-clé", "Résultat"))
print("-----------------------------------")
for keyword, count in matches.items():
    print("| {:<10} | {:<10} |".format(keyword, count))
print("-----------------------------------")
import os

# Fonction de recherche de mots-clés dans un fichier DLT (.dlt)
import re

def find_keyword_in_file(file_path, keyword):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    matches = {keyword: sum(1 for _ in re.finditer(keyword, content))}
    return matches

# Obtention de la liste des fichiers DLT dans le dossier du script
folder_path = '.' 
dlt_files = [f for f in os.listdir(folder_path) if f.endswith('.dlt')]

# Utilisation de la fonction pour chaque fichier DLT
keyword = input("Entrez le mot clé à rechercher : ")
print("Résultats de la recherche :")
print("---------------------------------------------")
print("| {:<40} | {:<10} |".format("Fichier", "Résultats"))
print("---------------------------------------------")
for dlt_file in dlt_files:
    file_path = os.path.join(folder_path, dlt_file)
    matches = find_keyword_in_file(file_path, keyword)
    for keyword, count in matches.items():
        print("| {:<40} | {:<10} |".format(dlt_file, count))
print("---------------------------------------------")
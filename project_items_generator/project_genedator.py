#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
import pandas as pd
import fileinput

from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

def replace_if_starts_with(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w', encoding='utf-8') as new_file:
        with open(file_path, encoding='utf-8') as old_file:
            for line in old_file:
                if (line.startswith(pattern)):
                    new_file.write(subst)
                else:
                    new_file.write(line)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

project_path = r'C:\Users\borja_sanz\Documents\GitHub\academic-kickstart'
df = pd.read_csv(r'C:\Users\borja_sanz\Documents\GitHub\academic-kickstart\project_items_generator\proyectos_clean.csv', sep=';', encoding='utf-8')


# Pasamos los acrónimos a minúsculas.
df['Acronimo_low'] = df['Acronimo'].str.lower()

create_projects = False

# Cambiamos el directorio

os.chdir(project_path)
print(os.getcwd())

if(create_projects):
    # Lanzamos los comandos
    for index_row, row in df.iterrows():
        path = 'project/' + row[2].lower()
        command = 'hugo new --kind project ' + path
        os.system(command)

# Recorremos los directortios.
directorio = os.path.join(project_path, r'content\project')

# Por cada fichero, modificamos los tags y los 
for item in os.scandir(directorio):
    if(item.is_dir):
        index_path = os.path.join(item, 'index.md')        
        if(os.path.isfile(index_path)):
            # Obtenemos la posición del item
            item_pos = df.index[df['Acronimo_low'] == item.name].tolist()[0]

            titulo = 'title: '
            # Y lo sustimiumos por la columna correspondiente
            titulo_replace = 'title: \"'+ str(df.iloc[item_pos,3]) +'\"\n'

            print(titulo_replace)
            
            categories = 'tags:'
            # Y lo sustimiumos por la columna correspondiente
            categories_replace = 'tags: [\"'+ df.iloc[item_pos,0] +'\"]\n'

            replace_if_starts_with(index_path, titulo, titulo_replace)
            replace_if_starts_with(index_path, categories, categories_replace)
            
            
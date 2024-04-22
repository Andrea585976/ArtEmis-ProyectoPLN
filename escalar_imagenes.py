"""
Programa que escala el tmaño del data set de imágenes

"""
import os
from PIL import Image

path = "A:\Descargas\wikiart\wikiart\Romanticism"  # Ruta en donde se ubican las imagenes
dir_list =  os.listdir(path)  # Lista que contiene el nombre de las imagenes

for i in dir_list:   # Para cada imagen en la lista
    name_image = '\\' + i    #A grega una diagonal inversa '\' al comienzo del nombre de la imagen
    
    im = Image.open(path + name_image)  # Abre la imagen 
    
    width, height = im.size 

    # Resize con una proporción 1/3:1/3, es decir, hace la imagen 1/3 mas pequeña en largo y ancho
    new_size = (round(width/3), round(height/3)) 
    im1 = im.resize(new_size)
    
    # Guardar imagen
    # Color ruta en donde se guardarán las imágenes escaladas 
    im1.save(r"A:\Descargas\wikiart\rescaled_max_size_to_600px_same_aspect_ratio" + name_image)
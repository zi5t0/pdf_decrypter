#!/usr/bin/python3
import os

dir_path = '/directorio/pdfs/a/decodear'
password = 'contraseña'
comprimido = "nombre_zip.zip"

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        filename = path.split(".")[0]
        ext = path.split(".")[1]
        os.system("qpdf --password="+password+" --decrypt "+dir_path+path+" "+dir_path+filename+"_decripted."+ext)
        os.system("rm "+dir_path+path)
        os.system("mv "+dir_path+filename+"_decripted."+ext+" "+dir_path+path)

os.system("zip -r "+comprimido+" "+dir_path)

#!/usr/bin/python3
import os, sys
import fitz

password=sys.argv[1]
file=str(sys.argv[2])
tmp_fn=file+"_tmp"

def decrypt_pdf(file, password):
    pdf = fitz.open(file)
    if pdf.authenticate(password):
        pdf.save(tmp_fn)
        if pdf.save:
            os.system("rm "+file)
            os.system("mv "+tmp_fn+" "+file)
            print("PDF decrypted")
        else:
            print('Incorrect Password')


decrypt_pdf(file, password)

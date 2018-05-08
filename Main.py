# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:12:58 2017

@author: Theo
"""

import pdfkit, os, glob, time
config_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'#Don't forget to configure wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=config_path)
options = {
   'footer-right': '[page]'
   }

def exists(path):
    """Test whether a path exists.  Returns False for broken symbolic links"""
    try:
        st = os.stat(path)
    except os.error:
        return False
    return True

def filterLines(lines):#Here you can replace the text
    lines = [x.replace('whatYouWant', 'whatYouWant').replace('font-size: 1em;', 'font-size: 1.5em;') for x in lines]
    return lines

def main():
    print('Ok')
    os.chdir("YourFiles")
    for htm in glob.glob("*.htm"):
        print('Gestion de ',htm)
        pdf = htm.replace('\'','').replace(' ','').replace('\'','').replace('.htm','')+'.pdf'#Renaming the file
        export = open(htm, 'a+')
        export.seek(0)
        lines = export.readlines()
        lines = filterLines(lines)
        export.close()
        text = ''
        for line in lines:
            text = text + line
        if not exists(pdf):
            print('creation pdf 1')
            pdfkit.from_string(text, pdf, configuration=config, options=options)
        else:
            print('creation pdf 2')
            os.remove(pdf)
            time.sleep(1)
            pdfkit.from_string(text, pdf, configuration=config, options=options)
            
if __name__ == '__main__':
    main()
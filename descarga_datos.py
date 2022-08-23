import os  # Para manejo de archivos y directorios
import urllib.request  # Para la descarga de los archivos 
import datetime  # Para registrar la fecha de descarga
import zipfile  # Para el manejo de archivos .zip

# URL para las descargas y directorios donde se guardarán
# Datos de crímenes por trimestre del año 2019
robosSON_INEGI_url_1 = "https://www.inegi.org.mx/contenidos/programas/ensu/datosabiertos/conjunto_de_datos_ENSU_2019_1t_csv.zip"
robosSON_INEGI_archivo_1= "robosINEGI_1.zip"

robosSON_INEGI_url_2 = "https://www.inegi.org.mx/contenidos/programas/ensu/datosabiertos/conjunto_de_datos_ENSU_2019_2t_csv.zip"
robosSON_INEGI_archivo_2= "robosINEGI_2.zip"

robosSON_INEGI_url_3 = "https://www.inegi.org.mx/contenidos/programas/ensu/datosabiertos/conjunto_de_datos_ENSU_2019_3t_csv.zip"
robosSON_INEGI_archivo_3= "robosINEGI_3.zip"

robosSON_INEGI_url_4 = "https://www.inegi.org.mx/contenidos/programas/ensu/datosabiertos/conjunto_de_datos_ENSU_2019_4t_csv.zip"
robosSON_INEGI_archivo_4= "robosINEGI_4.zip"

# Datos del censo económico nacional 2019
ce2019_INEGI_url = "https://www.inegi.org.mx/contenidos/programas/ce/2019/Datosabiertos/ce2019_son_csv.zip"
ce2019_INEGI_archivo = "ce2019.zip"
subdir = "./datos_veh/"

if not os.path.exists(robosSON_INEGI_archivo_1):  # Comprueba si el archivo existe
    if not os.path.exists(subdir):  # Comprueba si el directorio ya existe
        os.makedirs(subdir)  # Crea el directorio en subdir
    urllib.request.urlretrieve(robosSON_INEGI_url_1, subdir + robosSON_INEGI_archivo_1)  # Descarga los datos de la URL
    with zipfile.ZipFile(subdir + robosSON_INEGI_archivo_1, "r") as zip_ref:
        zip_ref.extractall(subdir) # Extrae el archivo zip descargado

if not os.path.exists(robosSON_INEGI_archivo_2):  # Comprueba si el archivo existe
    urllib.request.urlretrieve(robosSON_INEGI_url_2, subdir + robosSON_INEGI_archivo_2)  # Descarga los datos de la URL
    with zipfile.ZipFile(subdir + robosSON_INEGI_archivo_2, "r") as zip_ref:
        zip_ref.extractall(subdir) # Extrae el archivo zip descargado

if not os.path.exists(robosSON_INEGI_archivo_3):  # Comprueba si el archivo existe
    urllib.request.urlretrieve(robosSON_INEGI_url_3, subdir + robosSON_INEGI_archivo_3)  # Descarga los datos de la URL
    with zipfile.ZipFile(subdir + robosSON_INEGI_archivo_3, "r") as zip_ref:
        zip_ref.extractall(subdir) # Extrae el archivo zip descargado

if not os.path.exists(robosSON_INEGI_archivo_4):  # Comprueba si el archivo existe
    urllib.request.urlretrieve(robosSON_INEGI_url_4, subdir + robosSON_INEGI_archivo_4)  # Descarga los datos de la URL
    with zipfile.ZipFile(subdir + robosSON_INEGI_archivo_4, "r") as zip_ref:
        zip_ref.extractall(subdir) # Extrae el archivo zip descargado

if not os.path.exists(ce2019_INEGI_archivo):  # Comprueba si el archivo existe
    urllib.request.urlretrieve(ce2019_INEGI_url, subdir + ce2019_INEGI_archivo)  # Descarga los datos de la URL
    with zipfile.ZipFile(subdir + ce2019_INEGI_archivo, "r") as zip_ref:
        zip_ref.extractall(subdir) # Extrae el archivo zip descargado

    with open(subdir + "info.txt", 'w') as f:
        f.write("Archivos sobre datos nacionales de delitos y actividad económica de 2019 en México\n")
        info = """
        Los datos corresponden a los Resultados definitivos de los Censos Económicos 2019, y de la Encuesta
        Nacional de Seguridad Pública Urbana (ENSU).

        """ 
        f.write(info + '\n')
        f.write("Nombre: " + robosSON_INEGI_archivo_1 + "\n")
        f.write("Desde: " + robosSON_INEGI_url_1 + "\n\n")
        f.write("Nombre: " + robosSON_INEGI_archivo_2 + "\n")
        f.write("Desde: " + robosSON_INEGI_url_2 + "\n\n")
        f.write("Nombre: " + robosSON_INEGI_archivo_3 + "\n")
        f.write("Desde: " + robosSON_INEGI_url_3 + "\n\n")
        f.write("Nombre: " + robosSON_INEGI_archivo_4 + "\n")
        f.write("Desde: " + robosSON_INEGI_url_4 + "\n\n")
        f.write("Nombre: " + ce2019_INEGI_archivo + "\n")
        f.write("Desde: " + ce2019_INEGI_url + "\n\n")
        f.write("Descargado el " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        
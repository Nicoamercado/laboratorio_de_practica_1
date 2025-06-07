from abc import ABC, abstractmethod
import pandas as pd
import os

class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

@property
def datos(self):
    return self.__datos

@datos.setter
def datos(self, value):
    self.__datos = value

@property
def fuente(self):
    return self.__fuente

def validar_archivos(self):
    if not os.path.exists(self.__fuente):
        print (f"Error Archivo no encontrado {self.__fuente}")
        return False
    
    extension = self.__fuente.lower().split('.')[-1]
    extensiones_validas = self._obtener_extensiones_validas()

    if extension not in extensiones_validas:
        print(f"Error: Tipo de archivo no validop para {self.__fuente}. Esperando: {extensiones_validas}")
        return False
    
    return

@abstractmethod
def _obtener_extensiones_validas(self):
    pass

@abstractmethod
def cargar_datos(self):
    pass

def validar_datos(self):
    if self.__datos is None:
        print("Error: No se han cargado los datos de {self.__fuente}")
        return False
    
    #validar que pandas pudo procesar el archivo correctamente
    if not isinstance(self.__datos, pd.DataFrame):
        print(f"Error: Los datos no son de un DataFrame válido para {self.__fuente}")
        return False
    
    if self.__datos.isnull().sum().sum() > 0:
        print("Datos faltantes detectados.")
    if self.__datos.duplicated().sum() > 0:
        print("Filas duplicadas detectadas.")
    return True

def transformar_datos(self):
    if self.__datos is not None:
        # normalizar nombres de columnas
        self.__datos.columns = self.__datos.columns.str.lower().str.replace(" ", "_")
        # eliminar duplicados
        self.__datos = self.__datos.drop_duplicates()
        # limpiar strings
        for col in self.__datos.select_dtypes(include = "object").columns:
            self.__datos[col] = self.__datos[col].astype(str).str.strip()
        print("transformaciones aplicadas")
    else:
        print("No hay datos para transformar.")

    def mostrar_resumen(self):
        if self.__datos is not None:
            print(self.__datos.describe(inlcude = "all"))
        else:
            print("No hay datos.")
from abc import ABC, abstractmethod
import pandas as pd
import os


class Dataset(ABC):
    def __init__(self, fuente):
        self._fuente = fuente
        self._datos = None

    @property
    def datos(self):
        return self._datos

    @datos.setter
    def datos(self, value):
        self._datos = value

    @property
    def fuente(self):
        return self._fuente

    def validar_archivo(self):
        if not os.path.exists(self._fuente):
            print(f"Error: Archivo no encontrado {self._fuente}")
            return False
        
        extension = self._fuente.lower().split('.')[-1]
        extensiones_validas = self._obtener_extensiones_validas()
        
        if extension not in extensiones_validas:
            print(f"Error: Tipo de archivo no válido para {self._fuente}. Esperado: {extensiones_validas}")
            return False
            
        return True

    @abstractmethod
    def _obtener_extensiones_validas(self):
        pass

    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_datos(self):
        if self._datos is None:
            print(f"Error: No se pudieron cargar datos de {self._fuente}")
            return False
        
        if not isinstance(self._datos, pd.DataFrame):
            print(f"Error: Los datos no son un DataFrame válido para {self._fuente}")
            return False
        
        if self._datos.isnull().sum().sum() > 0:
            print("Datos faltantes detectados.")
        if self._datos.duplicated().sum() > 0:
            print("Filas duplicadas detectadas.")
        return True

    def transformar_datos(self):
        if self._datos is not None:
            self._datos.columns = self._datos.columns.str.lower().str.replace(" ", "_")
            self._datos = self._datos.drop_duplicates()
            for col in self._datos.select_dtypes(include="object").columns:
                self._datos[col] = self._datos[col].astype(str).str.strip()
            print("Transformaciones aplicadas")
        else:
            print("No hay datos para transformar.")

    def mostrar_resumen(self):
        if self._datos is not None:
            print(self._datos.describe(include='all'))
        else:
            print("No hay datos")

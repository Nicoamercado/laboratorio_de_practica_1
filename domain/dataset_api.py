import requests
import pandas as pd
from domain.dataset import Dataset


class DatasetAPI(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def _obtener_extensiones_validas(self):
        return ['api']

    def validar_archivo(self):
        return self._fuente.startswith(('http://', 'https://'))

    def cargar_datos(self):
        if not self.validar_archivo():
            print(f"Error: URL no válida {self._fuente}")
            return False
            
        try:
            response = requests.get(self._fuente)
            if response.status_code == 200:
                data = response.json()
                self._datos = pd.json_normalize(data)
                
                for col in self._datos.columns:
                    if self._datos[col].apply(lambda x: isinstance(x, list)).any():
                        self._datos[col] = self._datos[col].apply(
                            lambda x: ', '.join(map(str, x)) if isinstance(x, list) else x
                        )
                
                print(f"API cargada: {self._fuente}")
                
                if self.validar_datos():
                    self.transformar_datos()
                return True
            else:
                print(f"Error API: {response.status_code}")
                return False
        except Exception as e:
            print(f"Error cargando API {self._fuente}: {e}")
            return False
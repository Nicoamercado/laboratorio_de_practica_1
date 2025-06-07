import pandas as pd
from domain.dataset import Dataset


class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def _obtener_extensiones_validas(self):
        return ['csv']

    def cargar_datos(self):
        if not self.validar_archivo():
            return False
            
        try:
            self._datos = pd.read_csv(self._fuente)
            print(f"CSV cargado: {self._fuente}")
            
            if self.validar_datos():
                self.transformar_datos()
            return True
        except Exception as e:
            print(f"Error cargando CSV {self._fuente}: {e}")
            return False
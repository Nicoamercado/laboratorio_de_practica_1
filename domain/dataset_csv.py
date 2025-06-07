import pandas as pd
from domain.dataset import Dataset

class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def _obtener_extensiones_validas(self):
        return ["csv"]
    
    def cargar_datos(self):
        if not self.validar_archivo():
            return False
        
        try:
            self.__datos = pd.read_csv(self.fuente)
            print(f"CSV cargado: {self}")
        
            if self.validar_datos():
                self.transformar_datos()
            return  True
        except Exception as e:
            print(f"Error cargando CSV {self.fuente}: {e}")
            return False
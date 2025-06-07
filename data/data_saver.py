from sqlalchemy import create_engine
import os


class DataSaver:
    def __init__(self, ruta_db):
        directorio = os.path.dirname(ruta_db)
        if directorio:
            os.makedirs(directorio, exist_ok=True)
        
        self._engine = create_engine(f'sqlite:///{ruta_db}')

    def guardar_dataframe(self, dataframe, nombre_tabla):
        try:
            dataframe.to_sql(nombre_tabla, self._engine, if_exists='replace', index=False)
            print(f"Tabla '{nombre_tabla}' guardada exitosamente")
            return True
        except Exception as e:
            print(f"Error guardando tabla '{nombre_tabla}': {e}")
            return False

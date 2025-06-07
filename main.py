from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_api import DatasetAPI
from data.data_saver import DataSaver



print("=== LABORATORIO DE PRÁCTICA 1 ===")

csv_path = path.join(path.dirname(__file__), "files/precios-de-gas-natural-.csv")
excel_path = path.join(path.dirname(__file__), "files/estadisticas_biocombustibles.xls")
api_url = "https://apis.datos.gob.ar/series/api/series/?ids=168.1_T_CAMBIOR_D_0_0_26&start_date=2018-07&limit=5000"

datasets_exitosos = []

csv_dataset = DatasetCSV(csv_path)
if csv_dataset.cargar_datos():
    csv_dataset.mostrar_resumen()
    datasets_exitosos.append(("precios-de-gas-natural_csv", csv_dataset))

excel_dataset = DatasetExcel(excel_path)
if excel_dataset.cargar_datos():
    excel_dataset.mostrar_resumen()
    datasets_exitosos.append(("estadisticas_biocombustibles_xlsx", excel_dataset))

api_dataset = DatasetAPI(api_url)
if api_dataset.cargar_datos():
    api_dataset.mostrar_resumen()
    datasets_exitosos.append(("tipo_de_cambio", api_dataset))

db_saver = DataSaver("db/recoleccion.db")

for nombre_tabla, dataset in datasets_exitosos:
    db_saver.guardar_dataframe(dataset.datos, nombre_tabla)

print(f"\nProceso completado. {len(datasets_exitosos)} datasets guardados.")

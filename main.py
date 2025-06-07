from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_api import DatasertAPI
from domain.dataset_excel import DatasetExcel
from data.data_saver import DataSaver

def main():
    csv_path = path.join(path.dirname(__file__), "files/data.csv")
    excel_path = path.join(path.dirname(__file__), "files/data.xlsx")
    api_url = ""

    datasets_exitosos = []

    csv_dataset = DatasetCSV(csv_path)
    if csv_dataset.cargar_datos():
        csv_dataset.mostrar_resumen()
        datasets_exitosos.append(("csv_data",csv_dataset))
    
    excel_dataset = DatasetExcel(excel_path)
    if excel_dataset.cargar_datos():
        excel_dataset.mostrar_resumen()
        datasets_exitosos.append(("excel_data", excel_dataset))
    
    api_dataset = DatasertAPI(api_url)
    if api_dataset.cargar_datos():
        api_dataset.mostrar_resumen()
        datasets_exitosos.append(("provincias_api", api_dataset))

    db_saver = DataSaver("db/recoleccion.db")

    for nombre_tabla, dataset in datasets_exitosos:
        db_saver.guardar_dataframe(dataset.datos, nombre_tabla)
    
    print(f"Proceso completo. {len(datasets_exitosos)} datasets cargados.")
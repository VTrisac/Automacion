import pandas as pd
import sqlite3 as sql
import os

ruta = os.getcwd() + "\\Documents\\"
excel = pd.read_excel(ruta + "Listados Excel.xlsx",
        sheet_name="Automocion", header=0)

fabric = ["nissan", "toyota", "volvo"]
listado = excel[excel.fabricante.isin(fabric) & excel.tipo_combustible.isin(["gas"])]

tabla_final = listado.pivot_table(index = "carroceria",
             columns = "fabricante",
             values = "consumo_ciudad",
             fill_value = 0).round(2)

print("\nPivot Table resultante de la lectura Excel:\n", tabla_final)

conex = sql.connect(ruta + "automocion_tablas.sqlite")
tabla_final.to_sql("consumos", con = conex, if_exists = "replace", index_label = "carroceria")
print("\nTabla 'consumos' creada.")

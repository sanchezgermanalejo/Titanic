import pandas as pd
import os

# ✅ PASO 1: Verificar la Ubicación del Archivo
print("📂 Directorio actual:", os.getcwd())
print("📜 Archivos en la carpeta:", os.listdir())

# ✅ PASO 2: Inspeccionar las Primeras Líneas del Archivo
print("\n🔍 Inspeccionando las primeras 15 líneas del CSV como texto:")
with open("titanic.csv", "r", encoding="utf-8") as f:
    for i in range(15):
        print(f.readline().strip())  # Mostrar cada línea sin espacios extra

# ✅ PASO 3: Probar Diferentes Separadores Automáticamente
separadores = [",", ";", "\t", "|"]
df = None

for sep in separadores:
    try:
        df = pd.read_csv("titanic.csv", sep=sep)
        print(f"\n✅ CSV leído correctamente con separador: '{sep}'")
        print(df.head())  # Mostrar primeras filas
        break  # Detener el bucle si se carga correctamente
    except pd.errors.ParserError:
        print(f"❌ Error al intentar leer con separador: '{sep}'")

# ✅ PASO 4: Manejo de Líneas Problemáticas
if df is None:  # Si no se pudo cargar con ningún separador
    print("\n⚠️ No se pudo leer el archivo normalmente. Intentando ignorar líneas corruptas...")
    df = pd.read_csv("titanic.csv", on_bad_lines='skip')
    print("\n✅ Archivo cargado ignorando líneas problemáticas.")
    print(df.head())

# ✅ PASO 5: Verificar el DataFrame Cargado
print("\n📊 Información del DataFrame:")
print(df.info())

print("\n📊 Primeras filas del DataFrame:")
print(df.head())


print(df.isnull().sum())  # Ver cuántos valores faltan en cada columna

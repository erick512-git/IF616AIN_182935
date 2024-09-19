# Función para incrementar la versión
def incrementar_version(ultima_version, tipo_incremento):
    major, minor, patch = map(int, ultima_version.split('.'))
    
    if tipo_incremento == 'MAJOR':
        major += 1
        minor = 0
        patch = 0
    elif tipo_incremento == 'MINOR':
        minor += 1
        patch = 0
    elif tipo_incremento == 'PATCH':
        patch += 1
    else:
        raise ValueError("Tipo de incremento no válido. Debe ser MAJOR, MINOR o PATCH.")
    
    return f"{major}.{minor}.{patch}"

# Función para etiquetar la nueva versión en Git
def etiquetar_nueva_version(nueva_version):
    # Aquí iría el código para etiquetar y subir la versión a Git
    # Ejemplo: os.system(f"git tag {nueva_version} && git push --tags")
    print(f"Version {nueva_version} etiquetada y subida a Git.")

# Código principal
ultima_version = "1.0.0"  # Ejemplo de versión actual
nuevo_tipo = input("Indica el tipo de incremento (MAJOR, MINOR, PATCH): ").upper()

nueva_version = incrementar_version(ultima_version, nuevo_tipo)
print("Nueva versión:", nueva_version)

# Etiquetar y empujar nueva versión a Git
etiquetar_nueva_version(nueva_version)
print(f"Versión {nueva_version} etiquetada y subida a Git.")

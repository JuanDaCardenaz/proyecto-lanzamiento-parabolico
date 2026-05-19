# Guia rapida para subir el proyecto a GitHub usando Git Bash

Esta guia es para hacer el proceso paso a paso desde una carpeta local hasta GitHub.

## 1. Crear una carpeta para el proyecto

```bash
mkdir proyecto-lanzamiento-parabolico
cd proyecto-lanzamiento-parabolico
```

Si ya descargaste el paquete del proyecto, solo descomprimelo y entra a la carpeta:

```bash
cd proyecto-lanzamiento-parabolico
```

## 2. Crear el entorno virtual

```bash
python -m venv venv
```

## 3. Activar el entorno virtual en Git Bash

```bash
source venv/Scripts/activate
```

Si estas en PowerShell, usa:

```bash
venv\Scripts\activate
```

## 4. Instalar las librerias

```bash
pip install -r requirements.txt
```

## 5. Probar el programa

```bash
python main.py
```

Debe aparecer primero la informacion en consola y luego la grafica con la animacion.

## 6. Revisar lo instalado

```bash
pip freeze
```

## 7. Regenerar requirements.txt, solo si el profesor lo pide

```bash
pip freeze > requirements.txt
```

## 8. Inicializar Git dentro de la carpeta

```bash
git init
```

## 9. Agregar todos los archivos

```bash
git add .
```

## 10. Hacer el primer commit

```bash
git commit -m "Primer commit del proyecto final"
```

## 11. Crear el repositorio en GitHub

En GitHub:

1. Entrar a github.com.
2. Dar clic en New repository.
3. Poner un nombre, por ejemplo:

```text
proyecto-lanzamiento-parabolico
```

4. Dejarlo publico si el profesor lo pidio publico.
5. No agregar README desde GitHub, porque este proyecto ya tiene README.
6. Crear el repositorio.

## 12. Conectar la carpeta local con GitHub

GitHub te mostrara una URL parecida a esta:

```text
https://github.com/TU-USUARIO/proyecto-lanzamiento-parabolico.git
```

Usa esa URL en este comando:

```bash
git remote add origin https://github.com/TU-USUARIO/proyecto-lanzamiento-parabolico.git
```

## 13. Cambiar la rama principal a main

```bash
git branch -M main
```

## 14. Subir el proyecto

```bash
git push -u origin main
```

Si GitHub pide iniciar sesion, sigue las instrucciones que salgan en la terminal.

## 15. Verificar

Entra al repositorio desde el navegador y revisa que aparezcan:

```text
main.py
README.md
requirements.txt
documento_explicativo_lanzamiento_parabolico_sin_errores_tildes.tex
COMANDOS_GITBASH.md
.gitignore
```

La carpeta `venv` no debe aparecer en GitHub.

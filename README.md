# Simulacion y optimizacion de un lanzamiento parabolico hacia un objetivo

Este repositorio contiene el proyecto final de Programacion. La idea principal es simular un lanzamiento parabolico y encontrar el angulo de lanzamiento que permite que el proyectil pase lo mas cerca posible de un objetivo definido en el plano.

El proyecto usa un modelo fisico ideal: no se considera rozamiento del aire, la gravedad se toma constante y el proyectil parte desde el origen. A partir de las ecuaciones del movimiento parabolico, el programa calcula la trayectoria y usa una funcion de optimizacion para buscar el angulo mas adecuado.

## Planteamiento del problema

Se tiene un proyectil lanzado desde el origen con una velocidad inicial conocida. Tambien se define un objetivo mediante sus coordenadas:

```python
objetivo_x = 5.0
objetivo_y = 14.0
```

La pregunta central del proyecto es:

**Que angulo de lanzamiento permite que el proyectil pase lo mas cerca posible del objetivo?**

Para responder esto, el programa usa las ecuaciones del movimiento parabolico:

```text
x(t) = v0 cos(theta) t
y(t) = v0 sin(theta) t - 1/2 g t^2
```

Despues calcula la altura del proyectil cuando llega a la misma posicion horizontal del objetivo. La diferencia entre esa altura y la altura del objetivo se usa como una medida de cercania. No se interpreta como error experimental, sino como una forma numerica de saber que angulo se ajusta mejor.

## Archivos del repositorio

```text
proyecto-lanzamiento-parabolico/
│
├── main.py
├── requirements.txt
├── README.md
├── documento_explicativo_lanzamiento_parabolico_sin_errores_tildes.tex
├── COMANDOS_GITBASH.md
└── .gitignore
```

## Explicacion general del codigo

El programa esta organizado con programacion orientada a objetos.

### SistemaFisico

Es una clase abstracta. Define que todo sistema fisico debe tener un metodo `simular` y un metodo `resumen`.

### Proyectil

Guarda la velocidad inicial y la gravedad. Estos datos son necesarios para calcular la trayectoria.

### LanzamientoParabolico

Es la clase principal del proyecto. Calcula la posicion del proyectil, busca el angulo optimo y genera los datos simulados de tiempo, posicion horizontal y altura.

### Analizador

Muestra los resultados principales en consola: angulo optimo, desviacion minima, altura maxima y alcance.

### Visualizador

Crea la grafica y la animacion. En la ventana grafica aparece la trayectoria, el objetivo y un punto que representa el proyectil en movimiento.

## Requisitos

Se recomienda usar:

```text
Python 3.12 o superior
```

Librerias necesarias:

```text
numpy
matplotlib
scipy
```

Python ya incluye las librerias `abc` y `venv`, por eso no se instalan aparte.

## Crear el entorno virtual

Desde la carpeta del proyecto se ejecuta:

```bash
python -m venv venv
```

Esto crea una carpeta llamada `venv`, que contiene un entorno virtual independiente para el proyecto.

## Activar el entorno virtual

En PowerShell de Windows:

```bash
venv\Scripts\activate
```

En Git Bash:

```bash
source venv/Scripts/activate
```

Cuando el entorno virtual este activo, la terminal debe mostrar algo parecido a:

```bash
(venv)
```

## Instalar las librerias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

## Crear requirements.txt con pip freeze

Si se quiere generar nuevamente el archivo `requirements.txt`, primero se instalan las librerias:

```bash
pip install numpy matplotlib scipy
```

Luego se ejecuta:

```bash
pip freeze > requirements.txt
```

Este comando guarda en `requirements.txt` las librerias instaladas en el entorno virtual junto con sus versiones.

## Ejecutar el proyecto

Con el entorno virtual activado y las librerias instaladas:

```bash
python main.py
```

Al ejecutar el programa, primero aparecen los resultados en consola:

- velocidad inicial;
- gravedad;
- posicion del objetivo;
- angulo optimo;
- desviacion minima respecto al objetivo;
- altura maxima;
- alcance de la trayectoria.

Luego se abre una ventana con la grafica y la animacion del proyectil.

## Resultado esperado

El programa muestra una trayectoria parabolica optimizada. El objetivo aparece marcado con una equis y el proyectil aparece como un punto animado que se mueve sobre la curva.

La desviacion minima que aparece en consola no representa un error experimental. Es una medida matematica que el programa usa para saber que tan cerca pasa la trayectoria del objetivo.

## Cumplimiento de la rubrica

| Requisito | Como se cumple |
|---|---|
| Al menos 3 clases propias | Proyectil, LanzamientoParabolico, Analizador y Visualizador |
| Clase abstracta | SistemaFisico |
| Herencia | LanzamientoParabolico hereda de SistemaFisico |
| NumPy | Calculos trigonometricos, arreglos y maximos |
| Matplotlib | Grafica y animacion |
| SciPy | Optimizacion del angulo con minimize_scalar |
| Datos simulados | Arreglos t, x, y |
| Visualizacion | Trayectoria, objetivo y proyectil animado |
| Analisis | Resultados en consola e interpretacion en el informe |
| Codigo que compile | Proyecto organizado en un solo archivo main.py |

## Informe del proyecto

El repositorio incluye el documento explicativo en LaTeX:

```text
documento_explicativo_lanzamiento_parabolico_sin_errores_tildes.tex
```

Ese documento explica con mas detalle el planteamiento del problema, el marco teorico, el diseno de la solucion, el codigo usado, los resultados esperados y el cumplimiento de la rubrica.

## Autor

Juan David Cardenas Velez  
Programa de Fisica  
Universidad del Quindio

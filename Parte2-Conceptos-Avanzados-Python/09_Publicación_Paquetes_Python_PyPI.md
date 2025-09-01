# Publicación de Paquetes Python en PyPI

> **Nota:**  
> Los siguientes pasos y explicaciones fueron realizados y documentados por **Cristofer Vargas Morales** en el curso de Python de Platzi.  
> Este contenido no es de mi autoría, solo lo desarrollo y formateo para compartirlo.

---

## Introducción

Me tomó tiempo entender y ver qué pasos son necesarios y cuáles no. Me apoyé con apuntes de esta clase, ChatGPT y consultas a la IA de Platzi.

Al final, les comparto el proyecto que realicé y los pasos:

El proyecto trata de un paquete que contiene un módulo `Calculadora.py`, el cual contiene una clase del mismo nombre y métodos estáticos para suma, resta, división, multiplicación, potencia y radicación.

Iré enumerando los pasos, desde la estructura de la carpeta, la implementación de cada archivo y los pasos para la publicación, hasta finalmente cómo instalarlo y usarlo.

---

## Pre-requisitos

- Tener una cuenta en [PyPI](https://pypi.org/)
- Tener una cuenta en [TestPyPI](https://test.pypi.org/) (opcional, para pruebas)
- Tener una cuenta en [GitHub](https://github.com/) para publicar tu proyecto y colocar la URL en la metadata del archivo `pyproject.toml`
- Recordar que el archivo `setup.py` ya no se usa en proyectos modernos, esto es reemplazado por el archivo `pyproject.toml`

---

## Pasos Realizados

### 1. Estructura Inicial

La carpeta inicial es del proyecto general, que se llama igual a la carpeta del paquete. Por estándar suelen nombrarse igual, pero no es necesario.  
La carpeta del proyecto contiene los archivos como `pyproject.toml`, `LICENSE`, `README.md` y el paquete que contendrá el módulo que se importará y que tiene la lógica que nos interesa.

En el archivo `pyproject.toml` se incluye toda la metadata del proyecto, y entre sus atributos está el `name = <mi_paquete>`, que es el nombre que se da al paquete que se distribuirá, publicará y posteriormente instalará.

```
project-root/
│
├── package_calculator/
│   ├── __init__.py
│   └── Calculadora.py
├── LICENSE
├── pyproject.toml
└── README.md
```
![](https://static.platzi.com/media/user_upload/upload-ca513621-eb39-4623-b90b-87f27de18bea.png)
---

### 2. Implementación

#### Archivo `/package_calculator/__init__.py`
![](https://static.platzi.com/media/user_upload/upload-8719bf51-eae4-4458-9a3d-72228da55052.png)

Esto se realiza para que a la hora de importar el paquete solo coloquemos:

```python
from package_calculator import Calculadora
```

en lugar de:

```python
from package_calculator.Calculadora import Calculadora
```

#### Módulo `/package_calculator/Calculadora.py`

```python
import math

class Calculadora:
    @staticmethod
    def sumar(a: int|float, b: int|float) -> int|float:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            raise ValueError("Debe ingresar valores numéricos enteros o flotantes.")

    @staticmethod
    def restar(a: int|float, b: int|float) -> int|float:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a - b
        else:
            raise ValueError("Debe ingresar valores numéricos enteros o flotantes.")

    @staticmethod
    def multiplicar(a: int|float, b: int|float) -> int|float:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            raise ValueError("Debe ingresar valores numéricos enteros o flotantes.")

    @staticmethod
    def dividir(a: int|float, b: int|float) -> int|float:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if b == 0:
                raise ValueError("No se puede dividir entre 0")
            return a / b
        else:
            raise ValueError("Debe ingresar valores numéricos enteros o flotantes.")

    @staticmethod
    def exponenciar(a: int|float, b: int|float) -> int|float:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return math.pow(a, b)
        else:
            raise ValueError("Debe ingresar valores numéricos enteros o flotantes.")

    @staticmethod
    def obtener_raiz(a: int|float, b: int|float) -> int|float:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return round(math.pow(a, 1/b), 4)
        else:
            raise ValueError("Debe ingresar valores numéricos enteros o flotantes.")
```

#### Archivo LICENSE

Hay varios tipos de licencia, puedes optar por cualquier formato y personalizarlo.  
En este caso se eligió el tipo MIT.
![](https://static.platzi.com/media/user_upload/upload-a60484c2-6e29-4a90-90d4-e531cb8249e9.png)

#### Archivo `pyproject.toml`

En el atributo `name` se le da el nombre al paquete, por ejemplo:  
`name = "package_calculator_zriiman84"`  
Este debe ser único y no debe existir en PYPI.  
Lo único que deberá cambiar en caso vuelva a publicarlo, sería la versión.  
La sección `[build-system]` es importante.
![](https://static.platzi.com/media/user_upload/upload-b5458b51-5067-4889-befb-be96cf2ded64.png)

#### Archivo `README.md`

Incluye la descripción, uso y ejemplos del paquete.
![](https://static.platzi.com/media/user_upload/upload-961a4123-2493-4d46-8d70-cfe13d4d7a9d.png)
---

### 3. Subir a GitHub

Este paso no es obligatorio para que se distribuya tu paquete en PYPI, pero se recomienda tener tu proyecto también subido a Github, ya que es parte de la metadata descrita en el archivo `pyproject.toml`.

Pasos básicos:

1. Crear un repositorio remoto público y vacío llamado “package_calculator”.
2. Desde git, convertir la carpeta del proyecto en un repositorio:
   ```bash
   git init
   git add .
   git commit -m "Primer commit"
   git remote add origin <ruta_remota>
   git remote -v
   git push --set-upstream origin main
   ```
![](https://static.platzi.com/media/user_upload/upload-981ea4f7-8b8d-4d62-912b-357797c46fe8.png)
![](https://static.platzi.com/media/user_upload/upload-333d12c6-3a27-4322-908c-72ef0b55e8c7.png)
---

### 4. Actualizar pip

No es necesario actualizarlo siempre, pero se recomienda ejecutar:

```bash
python3 -m pip install --upgrade pip
```
![](https://static.platzi.com/media/user_upload/upload-5b7032ae-de55-474c-9c5a-51f66f37eaf4.png)
---

### 5. Generar la distribución de paquetes

Ejecutar:

```bash
python3 -m pip install --upgrade build
```
![](https://static.platzi.com/media/user_upload/upload-dddd7516-2e10-4ccf-b47a-27f165c1bc1d.png)
---

### 6. Construir el paquete con build

Este paso es **muy importante**.  
Esto crea un directorio `dist/` con archivos `.tar.gz` y `.whl` en la raíz del proyecto.
![](https://static.platzi.com/media/user_upload/upload-676b6a98-ff76-4a05-97e5-1e36b40caa19.png)
![](https://static.platzi.com/media/user_upload/upload-844c48a1-b2ee-46f4-a882-d272fe092674.png)
![](https://static.platzi.com/media/user_upload/upload-7c4143c1-d72c-4d50-ac4b-69dc6ed9d1bf.png)
---

### 7. Instalar Twine o actualizarlo

Ejecutar:

```bash
python3 -m pip install --upgrade twine
```
![](https://static.platzi.com/media/user_upload/upload-b3856e2d-5db7-47e0-bdce-6341b7d72a6c.png)
![](https://static.platzi.com/media/user_upload/upload-4c3aefca-762a-4c20-b2c2-313ae9380633.png)
---

### 8. Subir el paquete a PyPI con Twine

Ejecutar:

```bash
python3 -m twine upload dist/*
```

**Pre-requisitos:**

- Tener un API TOKEN creado
- Tener el API TOKEN almacenado en el archivo `~/.pypirc`
![](https://static.platzi.com/media/user_upload/upload-85bda86c-2a0e-4c69-a120-1fab8a8752f1.png)
---

### 9. Validar que exista el paquete en PyPI y/o en TestPyPI

Recordar que PyPI y TestPyPI son dos ámbitos distintos.  
TestPyPI requiere de su propio usuario y contraseña.

Para publicar en TestPyPI:

```bash
python3 -m twine upload --repository testpypi dist/*
```
![](https://static.platzi.com/media/user_upload/upload-3a2406e9-857c-4223-8e70-22dea215ec0c.png)
![](https://static.platzi.com/media/user_upload/upload-6c413f3c-d1a9-4ae2-bd3c-6d9c3b5bbb78.png)
---

### 10. Instalar el paquete

Ejecutar:

```bash
pip install package-calculator-zriiman84
```
![](https://static.platzi.com/media/user_upload/upload-3da1bb13-f6e6-4522-9166-56e4067edb3d.png)
> Nótese que el nombre del paquete para la instalación es el que se le asignó en el atributo `name` del archivo `pyproject.toml`.  
> Si bien es cierto se puso con "_", PyPI lo publica con "-" (guión).

---

### 11. Usar el paquete

```python
from package_calculator import Calculadora
```
![](https://static.platzi.com/media/user_upload/upload-8208ee7a-6e63-4ed9-a4c1-655436927978.png)
> Nótese que al realizar la importación se usa el nombre original del paquete, no el nombre o alias que se le puso en el archivo `pyproject.toml`.  
> Por ejemplo, `from package_calculator_zriiman84 import Calculadora` o `from package-calculator-zriiman84 import Calculadora` no funcionarán.

---

## Finalmente

Hay muchos términos y consideraciones, pero los pasos realizados son los más básicos e importantes.  
Se recomienda apoyarse en herramientas como ChatGPT o cualquier otra IA y leer la documentación oficial de PyPI para la publicación:  
[https://packaging.python.org/en/latest/tutorials/packaging-projects/](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

---

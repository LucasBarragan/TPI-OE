# TPI - Organización Empresarial

## Sistema de Gestión de Proveedores

### Descripción del proyecto

Este proyecto fue desarrollado como Trabajo Práctico Integrador (TPI) para la materia Organización Empresarial de la Tecnicatura Universitaria en Programación a Distancia (TUPaD).

El objetivo del trabajo consiste en analizar un proceso administrativo dentro de una organización, modelarlo mediante BPMN 2.0 y desarrollar una solución informática que permita automatizar dicho proceso.

Para este proyecto se seleccionó el proceso de **alta y gestión de proveedores**, permitiendo registrar, consultar, visualizar y eliminar proveedores mediante una aplicación desarrollada en Python.

---

## Objetivo

El sistema busca optimizar la gestión de proveedores mediante la automatización de tareas que normalmente se realizan de forma manual, permitiendo almacenar y consultar información de manera rápida y organizada.

---

## Funcionalidades

El sistema incluye las siguientes operaciones:

* Registrar proveedores.
* Consultar proveedores mediante CUIT.
* Mostrar la lista completa de proveedores registrados.
* Visualizar información detallada de cada proveedor.
* Eliminar proveedores existentes.
* Validar los datos ingresados por el usuario.
* Almacenar la información de manera persistente mediante archivos CSV.

---

## Estructura de datos

Cada proveedor registrado contiene la siguiente información:

* CUIT
* Razón Social
* Rubro
* Correo Electrónico
* Teléfono

Los datos son almacenados en un archivo CSV para garantizar su persistencia entre ejecuciones.

---

## Requisitos

Para ejecutar el proyecto es necesario contar con:

* Python 3 instalado.
* Acceso a los archivos del proyecto.

No se requieren bibliotecas externas.

---

## Ejecución del programa

1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar el archivo principal:

```bash
python python sistema_proveedores.py
```

3. Seleccionar una opción del menú principal.

---

## Menú principal

El sistema presenta las siguientes opciones:

1. Consultar proveedor.
2. Registrar proveedor.
3. Mostrar proveedores.
4. Eliminar proveedor.
5. Salir.

---

## Validaciones implementadas

El sistema contempla distintas validaciones para garantizar la calidad de los datos ingresados:

* Verificación de CUIT vacío.
* Verificación de longitud del CUIT.
* Validación de CUIT numérico.
* Detección de proveedores duplicados.
* Validación de razón social obligatoria.
* Validación de rubro obligatorio.
* Validación de formato básico de correo electrónico.
* Validación de teléfono numérico.
* Verificación de longitud mínima y máxima del teléfono.

---

## Tecnologías utilizadas

* Python
* CSV
* Git
* GitHub
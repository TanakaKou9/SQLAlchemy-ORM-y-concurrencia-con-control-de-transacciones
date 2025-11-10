# 📚 Taller #3 — Sistema de Gestión de Libros (MVC + SQLAlchemy + Concurrencia)

## 👥 Integrantes
- **Nombre 1:** Chica Becerra — 202420200335  
- **Nombre 2:** Daniela Murillo Castañeda — 20241020051  

---

## 🧩 Descripción General

Este proyecto implementa un **sistema de gestión de libros** utilizando el patrón **MVC (Modelo–Vista–Controlador)**, la librería **SQLAlchemy** para la persistencia de datos, y **concurrencia con hilos** para simular operaciones simultáneas en la base de datos.

## Objetivos

1. Aplicar los principios de la arquitectura **MVC** en Python.  
2. Implementar **persistencia de datos** con SQLAlchemy y SQLite.  
3. Demostrar el uso de **hilos (threading)** y **bloqueos (Lock)** para manejar concurrencia.  
4. Cumplir con los estándares de documentación y estilo **PEP 8** y **PEP 257**.  
---
## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.10 o superior  
- Virtualenv (recomendado)  
- SQLAlchemy

---
## 🏗️ Arquitectura del Proyecto

La estructura general del proyecto sigue el patrón **MVC**, separando responsabilidades en carpetas:

```bash
Taller-3/
├── controlador/
│   └── operaciones.py
├── modelo/
│   ├── Categoria.py
│   └── Libro.py
├── vista/
│   └── main.py
├── datos/
│   └── libros.db          # Se genera automáticamente
├── .gitignore
├── requirements.txt
└── README.md
```
---
## Ejecución del Proyecto

Para ejecutar el programa principal:
```bash
python -m vista.main
```

Este comando inicializa la base de datos, crea las tablas categorias y libros (si no existen), y permite realizar operaciones como:
- Agregar libros
- Listar libros
- Asociar libros a categorías

---

## 🏁 Demo de Concurrencia

El proyecto incluye un demo de concurrencia para demostrar cómo varios hilos pueden realizar inserciones en la base de datos de manera segura.

### Objetivo

Simular tres hilos que insertan libros de forma concurrente, utilizando un **Lock** para proteger el tramo crítico (la inserción en la base de datos).

### Funcionamiento

* Se crean tres hilos (`threading.Thread`) que intentan insertar libros simultáneamente.
* Antes de cada inserción, cada hilo adquiere el **Lock** para evitar interferencia entre operaciones.
* Una vez completada la inserción, el **Lock** se libera.
* Al finalizar, se verifica que todos los libros fueron insertados correctamente sin corrupción de datos.
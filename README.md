# IAC
Proyecto para Codigo Limpio

Con este proyecto se busca desarrollar un sistema que optimice la gestión de la empresa IAC, ya que actualmente su base de datos se administra mediante Microsoft Office. Aunque es una herramienta sólida y funcional, su interfaz puede resultar poco intuitiva para usuarios no expertos, lo que dificulta la eficiencia en los procesos diarios.

Esta propuesta tiene como objetivo modernizar y mejorar la gestión interna de la empresa, implementando un sistema más ágil, intuitivo y eficiente, que facilite el trabajo de los usuarios y optimice los procesos administrativos.

# 🚀 Características

- ### *Arquitectura Modular:*
División clara entre modelos de datos, lógica de negocio, almacenamiento y excepciones.
- ### *Persistencia JSON:*
Implementaremos un sistema de guardadp y carga de datos local mediante archivos tipo *.json.*

- ### *Manejo de Errores:*
Usaremos jerarquia de excepciones para hayar errores especificos como *ids duplicados,stock insuficiente, empresa no encontrada, entre otros...*
- ### *Tipado Estático:*
Usamos *dataclasses* y *typing* para hacer el código más legible y menos propenso a errores.

# 🚀 Funcionalidades Principales
El sistema permite realizar las siguientes operaciones a través de una interfaz de línea de comandos (CLI):

- ### Gestión de Empresas: 
Agregar nuevas empresas al sistema.

- ### Gestión de Catálogo: 
Registrar, modificar y eliminar servicios y productos asociados a cada empresa.


- ### Visualización: 
Listar todas las empresas registradas junto con sus respectivos servicios, productos o ventas realizadas.


- ### Persistencia Local: 
Almacenamiento de información en archivos de formato JSON, sin depender de sistemas de bases de datos externos.

# 📁 Estructura de Capas del Código

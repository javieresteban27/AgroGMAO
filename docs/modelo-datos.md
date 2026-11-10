# Modelo de datos

Diagrama entidad-relación de AgroGMAO. El diccionario completo de campos está en el documento 'Modelo de Datos (E/R y diccionario)' del proyecto.

```mermaid
erDiagrama
    Tipos_Equipo ||--o{ Equipos : clasifica
    Tipos_Equipo ||--o{ Sintomas : tiene
    Tipos_Equipo ||--o{ Hojas_Ruta : tiene
    Tipos_Equipo ||--o{ Repuesto_Familia : admite
    Repuestos ||--o{ Repuesto_Familia : sirve_a
    Equipos ||--o{ Lecturas_Horas : registra
    Usuarios ||--o{ Lecturas_Horas : anota
    Categorias_Repuesto ||--o{ Repuestos : agrupa
    Repuestos ||--o{ Movimientos_Stock : mueve
    Usuarios ||--o{ Movimientos_Stock : realiza
    Equipos ||--o{ Incidencias : sufre
    Sintomas |o--o{ Incidencias : describe
    Usuarios |o--o{ Incidencias : asignada_a
    Incidencias |o--o{ Incidencias : duplicada_de
    Incidencias ||--o{ Comentarios_Incidencia : recibe
    Usuarios ||--o{ Comentarios_Incidencia _ escribe
    Equipos ||--o{ Ordenes_Trabajo : repara
    Incidencias |o--o{ Ordenes_Trabajo : origina
    Revisiones |o--o{ Ordenes_Trabajo : origina
    Usuarios |o--o{ Ordenes_Trabajo : responsable
    Campanas |o--o{ Ordenes_Trabajo : en
    Ordenes_Trabajo ||--o{ Imputacion_Horas : carga
    Clases_Actividad ||--o{ Imputacion_Horas : tarifa
    Usuarios ||--o{ Imputacion_Horas : trabaja
    Ordenes_Trabajo ||--o{ Consumo_Materiales : consume
    Repuestos ||--o{ Consumo_Materiales : usa
    Movimientos_Stock ||--o| Consumo_Materiales : descuenta
    Hojas_Ruta ||--o{ Puntos_Control : contiene
    Hojas_Ruta ||--o{ Hoja_Repuesto : requiere
    Repuestos ||--o{ Hoja_Repuesto : requerido_en
    Equipos ||--o{ Plan_Mantenimiento : programa
    Hojas_Ruta ||--o{ Plan_Mantenimiento : aplica
    Equipos ||--o{ Revisiones : pasa
    Hojas_Ruta ||--o{ Revisiones : sigue
    Revisiones ||--o{ Resultados_Control : anota
    Puntos_Control ||--o{ Resultados_Control : evalua
    Usuarios ||--o{ Registro_Actividad : genera
    Parametros {
        texto clave PK
    }
```
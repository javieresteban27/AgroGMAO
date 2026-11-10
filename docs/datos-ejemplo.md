# Datos de ejemplo (ficticios)

Borrador de datos para pruebas y demostraciones. Las marcas y modelos son los típicos del campo español, como referencia. **Los años, las horas y el estado son inventados** y no corresponden a ninguna máquina real ni a ninguna explotación. Es una hipótesis que se contrastará y corregirá en la entrevista familiar, y de aquí saldrán los datos de ejemplo de la aplicación.

| Denominación | Familia | Marca | Modelo | Año | Horas aprox. | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| Tractor grande | Tractor | John Deere | 6400 | 1998 | 9.400 | activo |
| Tractor de la viña | Tractor | Deutz-Fahr | DX 3.60 | 1992 | 6.200 | activo |
| Tractor viejo | Tractor | Ebro | 6100 | 1982 | 11.800 | en_reparacion |
| Tractor mediano | Tractor | New Holland | TM 140 | 2004 | 7.300 | activo |
| Cosechadora | Cosechadora | Claas | Dominator 98 | 1999 | 4.100 | activo |
| Sembradora de 3 metros | Sembradora | Gil | S-300 | 2010 | sin horómetro | activo |
| Pulverizador arrastrado | Pulverizador | Hardi | Commander | 2012 | sin horómetro | activo |
| Remolque basculante | Remolque | Teymo | RB-8 | 1996 | sin horómetro | activo |
| Arado de vertedera | Apero de labranza | Naud | tres rejas | 1992 | sin horómetro | baja |
| Empacadora | Empacadora | John Deere | 342 | 2005 | 1.900 | activo |

## Dudas para contrastar con la familia

- ¿Qué familias de equipo tienen de verdad y cómo las llaman?
- ¿Los aperos y remolques se miden por horas de uso, por superficie, por campaña, o no se mide nada?
- ¿Cómo llaman a cada equipo en el día a día?
- ¿Qué equipos están de baja o son de otro propietario?
- ¿Qué marcas y modelos hay realmente en la finca?

## Síntomas por familia (Sintomas)

Son las opciones que ve el operario al avisar de una avería, en lenguaje de campo.

**Tractor**
- No arranca
- Pierde potencia
- Echa humo negro o azul
- Pierde aceite
- Se calienta
- El embrague patina
- Pierde fuerza el hidráulico

**Cosechadora**
- No arranca
- Se atasca el cabezal
- Pierde grano por la cola
- Patina una correa
- Pierde aceite hidráulico

**Sembradora**
- Falla la distribución de semilla
- Tubos de bajada atascados
- Rodamiento con ruido
- Falta de engrase

**Pulverizador**
- Boquilla obstruida
- Presión baja
- Fuga en la bomba
- La barra no se despliega

**Remolque**
- Neumático pinchado
- Frenos defectuosos
- El basculante no sube
- Pierde aceite hidráulico

**Apero de labranza**
- Reja desgastada
- Punta rota
- Rodamiento con ruido

**Empacadora**
- Se atasca la recogida
- Falla el atado
- Se rompe una correa

## Categorías de repuesto (Categorias_Repuesto)

Filtros, aceites y lubricantes, correas y cadenas, hidráulica, eléctrico, desgaste de labranza, pulverización.

## Repuestos (Repuestos y Repuesto_Familia)

Las referencias y los precios son inventados. La última columna son las familias para las que sirve el repuesto (`Repuesto_Familia`).

| Referencia | Descripción | Categoría | Unidad | Precio (€) | Sirve para |
| --- | --- | --- | --- | --- | --- |
| FIL-ACE-001 | Filtro de aceite de motor | Filtros | unidad | 12,00 | Tractor, cosechadora |
| FIL-GAS-001 | Filtro de gasoil | Filtros | unidad | 15,00 | Tractor, cosechadora |
| FIL-AIR-001 | Filtro de aire | Filtros | unidad | 28,00 | Tractor, cosechadora |
| LUB-MOT-001 | Aceite de motor 15W-40 | Aceites y lubricantes | litro | 5,50 | Tractor, cosechadora |
| LUB-HID-001 | Aceite hidráulico | Aceites y lubricantes | litro | 4,80 | Tractor, cosechadora, remolque |
| LUB-GRA-001 | Grasa de engrase | Aceites y lubricantes | unidad | 3,50 | Todas las familias |
| COR-TRA-001 | Correa de transmisión | Correas y cadenas | unidad | 35,00 | Cosechadora, empacadora |
| CAD-ROD-001 | Cadena de rodillos | Correas y cadenas | metro | 14,00 | Sembradora, empacadora |
| HID-MAN-001 | Manguera hidráulica | Hidráulica | metro | 9,00 | Tractor, cosechadora, remolque |
| ELE-BAT-001 | Batería de 12V | Eléctrico | unidad | 95,00 | Tractor, cosechadora |
| LAB-REJ-001 | Reja de arado | Desgaste de labranza | unidad | 45,00 | Apero de labranza |
| PUL-BOQ-001 | Boquilla de pulverización | Pulverización | unidad | 4,00 | Pulverizador |
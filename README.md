# EDA_Loans_DS
Proyecto EDA Bootcamp DS The Bridge

Con este proyecto hacemos la fase EDA ("Exploratory Data Analysis") de un dataset extraído de la web Amazon Sagemaker.

Los datos de partida vienen de 2 datasets con columnas diferentes: 

Dataset 1:

* id: número de identificación del préstamo
* loan_status: estado actual del préstamo (normalmente 3 estados: fully paid, charged off, current)
* loan_amount: importe concedido del préstamo
* funded_amount_by_investors: monto recibido efectivamente por el prestatario (deducidas las comisiones de apertura)
* loan_term: número de pagos del préstamo en meses (36 o 60)
* interest_rate: tipo de interés del préstamo
* installment: cuota mensual del préstamo
* grade: grado clasificación dado por LC (Lending Club)
* subgrade: subgrado otorgado por LC
* verification_status: indica si los ingresos del prestatario han sido verificados por LC
* issued_on: fecha de emisión del préstamo
* purpose: propósito del préstamo (coche, negocio, tarjeta, etc)
* dti: ratio que divide el pago total de cuotas en préstamos del prestatario sobre el total de ingresos mensuales, excluyendo el pago de la hipoteca.
* inquiries_last_six_months: númeo de consultas del prestatario en los últimos 6 meses
* open_credit_lines: número de préstamos del prestatario abiertas.
* derogatory_public_records: número de registros públicos negativos
* revolving_line_utilization_rate: tasa de uso de crédito en tarjetas revolving
* total_credit_lines: total de créditos del pretatario en la base de datos

Dataset 2:

* id: número de identificación del préstamo
* employment_length: tiempo que el prestario ha estado trabajando en años (entre 0 y 10, si es más se le asigna 10)
* employer_title: nombre del empleo del prestatario
* home_ownership: (own= vivienda en propiedad, rent: alquilada)
* annual_income: ingresos anuales del prestatario

Ambos dataset tienen 39717 filas de datos

En el EDA se llevan a cabo las siguientes fases:

1. Estudio previo de las columnas que lo componen.
2. Limpieza de datos (eliminación de columnas, limpieza de valores Nan y outliers)
3. Análisis univariante
4. Análisis multivariante
5. Contraste de hipótesis
6. Conclusiones

Las hipótesis que tratamos de demostrar es si las siguientes variables tiene incidencia en el impago de un préstamo

1. El importe del préstamo
2. El tipo de interés aplicado
3. El importe de la cuota
4. El ratio dti (cuotas pagadas en préstamo / ingresos totales)
5. El grado de uso del crédito en tarjetas revolving
6. El tiempo que lleva empleado.
7. Si tiene una casa en propiedad o alquilada
8. El propósito para el que se concedió el préstamo
9. Los ingresos anuales del prestatario.
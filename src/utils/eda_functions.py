import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def graficos_var_cont(df, column_df):
      

    # Crear la figura y las subtramas en 1 fila y 2 columnas
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Primer gráfico: histograma con función de densidad usando Seaborn
    sns.histplot(df[column_df], kde=True, bins=20, color='red', ax=ax1)
    ax1.set_xlabel(f'{column_df}')
    ax1.set_ylabel('Density')
    ax1.set_title(f'{column_df} Distribution with Density Function')

    # Segundo gráfico: histograma de 'loan_amount' por 'loan_status'
    status_counts = df['loan_status'].value_counts(normalize=True) * 100

    for status in df['loan_status'].unique():
        loan_amounts = df[df['loan_status'] == status][column_df]
        ax2.hist(loan_amounts, bins=20, alpha=0.5, label=f"{status} ({status_counts[status]:.2f}%)")

    ax2.set_xlabel(f'{column_df}')
    ax2.set_ylabel('Frequency')
    ax2.set_title(f'Histogram of {column_df} by Loan Status')
    ax2.legend()

    # Ajustar espaciado entre subplots
    plt.tight_layout()

    # Mostrar los gráficos combinados
    plt.show()



def mapa_calor(df, col_heatmap):
    
    # Filtrar el DataFrame para 'loan_status' igual a 'charged off'
    charged_off_df = df[df['loan_status'] == 'charged off']

    # Obtener el recuento de combinaciones 'purpose'-'loan_status' igual a 'charged off'
    grouped = charged_off_df.groupby(col_heatmap)['loan_status'].count()

    # Calcular los porcentajes relativos para cada valor de 'purpose'
    relative_percentages = (grouped / df[col_heatmap].value_counts()) * 100

    # Crear un DataFrame con los porcentajes relativos
    relative_percentages_df = pd.DataFrame(relative_percentages, columns=['Charged Off Relative Percentage'])

    # Crear un gráfico de calor
    plt.figure(figsize=(7, 4))
    heatmap = plt.imshow(relative_percentages_df.values.reshape(1, -1), aspect='auto', cmap='Greens')

    # Añadir etiquetas, título y colorbar
    plt.xticks(range(len(relative_percentages_df)), relative_percentages_df.index, rotation=90)
    plt.xlabel(col_heatmap)
    plt.ylabel('')
    plt.title('Charged Off Relative Percentage by Purpose')
    plt.colorbar(heatmap)

    plt.tight_layout()
    plt.show()

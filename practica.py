import pandas as pd
import matplotlib.pyplot as plt

mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ventas = [100, 50, 300, 250, 105, 340, 240, 432, 434, 765, 354, 456]

df = pd.DataFrame({'Mes': mes, 'Ventas': ventas})

plt.barh(df['Mes'], df['Ventas'], color='skyblue')

plt.xlabel('Ventas Totales')
plt.ylabel('Mes')
plt.title('Ventas Mensuales')
plt.show()

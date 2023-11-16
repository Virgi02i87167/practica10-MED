import pandas as pd
import matplotlib.pyplot as plt

Examen1 = [10, 9.5, 5, 7, 2, 8, 7]
Examen2 = [7, 6,3,10, 5, 8, 8.9]
df = pd.DataFrame({'Examen1': Examen1, 'Examen2': Examen2})

plt.stackplot(df['Examen1'], df['Examen2'], labels=['Examen 2'], colors=['skyblue'])

# Etiquetar los ejes y agregar un título al gráfico
plt.xlabel('Puntajes en el Examen 1')
plt.ylabel('Puntajes en el Examen 2')
plt.title('Relación entre Puntajes en los Exámenes')
plt.legend()

# Mostrar el gráfico
plt.show()
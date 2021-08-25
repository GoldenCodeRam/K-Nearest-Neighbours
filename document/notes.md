# k-Nearest-Neighbours

## Resumen

El presente informe estudia la implementación y ejecución del algoritmo _K-Nearest-Neighbours_
sobre un conjunto de datos relacionado con la enfermedad que se presenta en los bobinos, _Neospora_.
Se encontrará la relación existente entre las diferentes variables para determinar si con ellas es
posible detectar con anterioridad si un bobino sufre de esta enfermedad, además de cuáles de estas
variables son las más relevantes a la hora de hacer un análisis.  Y finalmente, se mostraran los
resultados de todo el proceso de investigación y simulación.

## Introducción

(basics) Se definen los métodos supervisados de aprendizaje de máquina como la manera
de aprender modelos funcionales _f_ de observaciones para generar relaciones.
Los métodos supervisados se basan en observar datos y organizarlos haciendo
uso de etiquetas.

(dimensionality) El algoritmo _K-Nearest-Neighbours_, es un tipo de algoritmo simple para
la implementación de un algoritmo de aprendizaje de máquina supervisado, que puede ser usado para
resolver problemas de regresión y clasificación.  Por otra parte (machinelearning1), afirma que
el algoritmo adapta la cantidad de _suavizado_ a una densidad local de datos y esa cantidad de
suavizado viene dada por el término _k_, que es el número de vecinos que se tienen en cuenta para
el cálculo, el cual es mucho menor que la población total.

(basics) En los problemas de clasificación del algoritmo, se requiere predecir
patrones teniendo en cuenta un grupo de observaciones.  Por ejemplo, se tiene
un grupo de observaciones {(x1, y1), ... , (xN, yN)}, siendo X = {x}_i=1^N el
grupo de patrones y Y = {Y_i}_i=1^N el grupo de etiquetas. El objetivo en
los problemas de clasificación es encontrar un modelo funcional _f_ que permita
realizar predicciones sobre una etiqueta y' para un patrón desconocido x'. Los
patrones que no tengan etiquetas deberán ser asignados a patrones con etiquetas
similares; se encuentran relativamente cerca, están en la misma distribución o
se encuentran en el mismo lado de la función separadora.


---
Para el desarrollo y análisis de los datos, se observa que todos los datos pueden
ser únicamente clasificados, al ser datos categóricos.  De manera que se debe
encontrar una manera de convertir los datos categóricos a datos numéricos.  A
este proceso se le suele llamar Label-Encoding o codificación de etiquetas, como
traducción del Inglés. (encoding) Uno de los mayores desafíos es convertir datos
en forma de texto o etiquetas a datos en forma numérica, y lograr ejecutar un
algoritmo o modelo con ellos. El proceso de codificación de etiquetas se lleva
a cabo convirtiendo cada uno de los valores en una columna a un número; el tipo
de números elegidos para cada columna puede variar al, por ejemplo, usar una
secuencia de números.

		AYR	HOR 	JER	NOR
		3	5	7	11
2	13	39	65	91	143
3	17	51	85	119	187
4	19	57	95	133	209

Para la tabla anterior, se puede observar que se tienen 4 etiquetas como columnas
y 3 etiquetas como filas.

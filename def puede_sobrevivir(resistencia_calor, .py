def puede_sobrevivir(resistencia_calor, necesidad_agua, profundidad_raiz, tipo_hoja):
    if resistencia_calor == 'alta':
        if necesidad_agua == 'baja':
            return 'Sí'
        else:
            if tipo_hoja == 'cerosa':
                return 'Sí'
            else:
                return 'No'
    elif resistencia_calor == 'media':
        if profundidad_raiz == 'profunda':
            if tipo_hoja == 'cerosa':
                return 'Sí'
            else:
                return 'No'
        else:
            return 'No'
    else:
        return 'No'
# Entrada de datos del usuario
print("Clasificador de supervivencia de plantas en Arrakis ")
resistencia = input("Resistencia al calor (alta/media/baja): ").strip().lower()
agua = input("Necesidad de agua (alta/media/baja): ").strip().lower()
raiz = input("Profundidad de la raíz (profunda/media/superficial): ").strip().lower()
hoja = input("Tipo de hoja (cerosa/gruesa/fina): ").strip().lower()

# Evaluación
resultado = puede_sobrevivir(resistencia, agua, raiz, hoja)

# Resultado
print("\n¿Puede sobrevivir la planta en un clima seco y caliente?:", resultado)

# Visualización del árbol de decisiones
def mostrar_arbol_decision():
    print("\nÁrbol de decisión para la supervivencia de plantas:")
    print("Resistencia al calor?")
    print("├── Alta")
    print("│   ├── Necesidad de agua?")
    print("│   │   ├── Baja: Sí")
    print("│   │   └── Alta/Media")
    print("│   │       ├── Tipo de hoja?")
    print("│   │       │   ├── Cerosa: Sí")
    print("│   │       │   └── Gruesa/Fina: No")
    print("├── Media")
    print("│   ├── Profundidad de la raíz?")
    print("│   │   ├── Profunda")
    print("│   │   │   ├── Tipo de hoja?")
    print("│   │   │   │   ├── Cerosa: Sí")
    print("│   │   │   │   └── Gruesa/Fina: No")
    print("│   │   └── Media/Superficial: No")
    print("└── Baja: No")

# Mostrar el árbol de decisión
mostrar_arbol_decision()

# Introducción a Entropía e Impureza de Gini
print("\nConceptos básicos de aprendizaje automático:")
print("1. Entropía: Es una medida de incertidumbre o desorden en los datos. En los árboles de decisión, se utiliza para determinar qué característica dividir para reducir la incertidumbre.")
print("2. Impureza de Gini: Es una métrica que mide la probabilidad de clasificar incorrectamente un elemento si se selecciona al azar. Los algoritmos de árboles de decisión intentan minimizar esta impureza al construir el árbol.")

print("\nNota: Los algoritmos de aprendizaje automático, como los árboles de decisión, utilizan estas métricas para dividir los datos de manera automática y eficiente.")


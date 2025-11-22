'''
En este archivo se deben recir los datos entregados
y procesarlo en MATH u ELEMENTS
El cual mostrara las otras secciones.
'''
import streamlit as st
from core.elements.interpretation import Interpretation
from components.design_textual.information import SectionBOX3,SectionBOX4,SectionBOX5,SectionBOX6,SectionBOX7
def Datos():
    # PESTAÑAS
    tab1, tab2 = st.tabs(["Resultados", "Interpretación Automatica"])

    with tab1:
        st.subheader("Resultados econtrados")
        st.write("Aquí va contenido teórico, gráficos, ejemplos, videos, etc.")

        # ===== SECCION 2.Función Matemática =====
        # - Crear exprección, importar proceso matematico
        formula21 = "C(t) = 2t² + 5t + 10"   
        st.markdown(SectionBOX3(formula21), unsafe_allow_html=True) # Posible enviar datos 
        # - Implemetar Grafico

        # ===== SECCION 3.Derivadas ======
        # - Crear exprección, importar proceso matematico
        formula31 = "C'(t) = 4t + 5"
        st.markdown(SectionBOX4(formula31), unsafe_allow_html=True)
        # - Implementar Grafico

        # ===== SECCION 4.Integral =====
        # - Crear exprección, importar proceso matematico
        formula41 = "S(T) = ∫₀ᵀ 12 C(t) dt"
        formula42 = "S(T) = 8T³ + 30T² + 120T"
        st.markdown(SectionBOX5(formula41,formula42), unsafe_allow_html=True)

        # ===== SEccion 5. Tabla =====
        st.markdown(SectionBOX6(), unsafe_allow_html=True)
        # - Crear tabla y mostrar tabla


    with tab2:
        st.subheader("Explicación Desarrollada")
        st.write("Aquí se encuentra una información extra sobre el desarrollo aplicado.")
        # ===== SECCION 6.INTERPRETACIÓN
        st.markdown(SectionBOX7(), unsafe_allow_html=True)
        with st.expander("Ver desarrollo paso a paso"):
            st.write("""
            Desarrollo Matemático Completo \n

            Derivada:\n
            d/dt (2t² + 5t + 10) = 4t + 5 \n

            Integral:\n
            ∫ 1/2 (2t² + 5t + 10) dt = 1/2 [ (2/3)t³ + (5/2)t² + 10t ]
            """)
        # --- Modificar archivo, para que salga el mensaje corresponiente
        # --- Posible q se borre SectionBOX07 ya q no es estatito.
        # --- Y los mensajes deben considir con la interpretación de resultado
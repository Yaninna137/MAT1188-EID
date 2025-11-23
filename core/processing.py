'''
En este archivo se deben recir los datos entregados
y procesarlo en MATH u ELEMENTS
El cual mostrara las otras secciones.
'''
import streamlit as st
from core.elements.interpretation import Interpretation
from components.design_textual.information import SectionBOX3,SectionBOX4,SectionBOX5,SectionBOX6,SectionBOX7
from core.math.Nombre_procesamiento import ModeloCosto
import sympy as sp
from core.elements.graphic import GRAPHIC_A


def Datos():
    # PESTAÑAS
    tab1, tab2 = st.tabs(["Resultados", "Interpretación Automatica"])

    with tab1:
        st.subheader("Resultados econtrados")
        st.write("Aquí va contenido teórico, gráficos, ejemplos, videos, etc.")

       # Recuperar lo ingresado por usuario
        func = st.session_state.get("funcion", "2*t**2 + 5*t + 10")
        T = st.session_state.get("T", 5)

        if func.strip() == "":
            st.error("❌ Primero debes ingresar una función válida.")
            return
        
        # Crear modelo matemático
        modelo = ModeloCosto(func)

        # Expresión bonita en LaTeX
        C_expr = sp.latex(modelo.funcion)

        # Mostrar sección usando tu caja HTML
        st.markdown(SectionBOX3(f"C(t) = {C_expr}"), unsafe_allow_html=True)

        # Gráfico real
        st.pyplot(GRAPHIC_A(modelo, T))

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
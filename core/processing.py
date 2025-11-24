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
from core.elements.graphic import GRAPHIC_A, GRAPHIC_B


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
        derivada = modelo.derivada
        formula31 = f"C'(t) = {sp.latex(derivada)}"
        st.markdown(SectionBOX4(formula31,derivada)[0], unsafe_allow_html=True) # Primera parte del html
        # debajo de la formula, input para evaluar en cierto punto
        punto_eval = st.number_input("Evaluar C'(t) en t =", min_value=0.0, value=1.0)
        valor_derivada = modelo.evaluar_Cp(punto_eval)
        if st.button("Calcular C' en el punto dado"):
            st.session_state['evaluar_derivada'] = valor_derivada
        if 'evaluar_derivada' in st.session_state:
            st.write(f"El valor de C'({punto_eval}) es: {st.session_state['evaluar_derivada']}")

        st.markdown(SectionBOX4(formula31,derivada)[1], unsafe_allow_html=True) # Segunda parte del html
        
        # - Implementar Grafico
        if 'evaluar_derivada' in st.session_state:
            st.pyplot(GRAPHIC_B(modelo, T, xy_evaluado=(punto_eval, st.session_state['evaluar_derivada'])), use_container_width=False)
        else:
            st.pyplot(GRAPHIC_B(modelo, T), use_container_width=False)

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
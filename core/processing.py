'''
En este archivo se deben recir los datos entregados
y procesarlo en MATH u ELEMENTS
El cual mostrara las otras secciones.
'''
import streamlit as st
from core.elements.interpretation import Interpretation
from components.design_textual.information import (
    SectionBOX3, SectionBOX4, SectionBOX5,
    SectionBOX6, SectionBOX7
)
from core.math.Nombre_procesamiento import ModeloCosto
import sympy as sp
from core.elements.graphic import (
    GRAPHIC_A,
    GRAPHIC_B,
    GRAPHIC_C,
    GRAPHIC_D
)


def Datos():
    # PESTAÑAS
    tab1, tab2 = st.tabs(["Resultados", "Interpretación Automatica"])

    # =======================================
    # TAB 1 — RESULTADOS
    # =======================================
    with tab1:
        st.subheader("Resultados encontrados")
        st.write("Aquí va contenido teórico, gráficos, ejemplos, videos, etc.")

        # Recuperar datos ingresados por usuario
        func = st.session_state.get("funcion", "2*t**2 + 5*t + 10")
        T = int(st.session_state.get("T", 5) or 5)

        if func.strip() == "":
            st.error("❌ Primero debes ingresar una función válida.")
            return
        
        # Crear modelo matemático
        modelo = ModeloCosto(func)

        # Expresión bonita en LaTeX
        C_expr = sp.latex(modelo.funcion)

        # Mostrar sección usando tu caja HTML
        st.markdown(SectionBOX3(f"C(t) = {C_expr}"), unsafe_allow_html=True)

        # Mostrar fórmula con Streamlit
        st.latex(rf"C(t) = {C_expr}")

        # Gráfico principal C(t)
        st.pyplot(GRAPHIC_A(modelo, T))

        # =======================================
        # SECCIÓN 3: DERIVADAS
        # =======================================
        derivada = modelo.derivada
        formula31 = f"C'(t) = {sp.latex(derivada)}"

        st.markdown(SectionBOX4(formula31, derivada)[0], unsafe_allow_html=True)

        # Input para evaluar derivada
        punto_eval = st.number_input("Evaluar C'(t) en t =", min_value=0.0, value=1.0)
        valor_derivada = modelo.evaluar_Cp(punto_eval)

        if st.button("Calcular C' en el punto dado"):
            st.session_state['evaluar_derivada'] = valor_derivada

        if 'evaluar_derivada' in st.session_state:
            st.write(f"El valor de C'({punto_eval}) es: {st.session_state['evaluar_derivada']}")

        st.markdown(SectionBOX4(formula31, derivada)[1], unsafe_allow_html=True)

        # Gráfico derivada
        if 'evaluar_derivada' in st.session_state:
            st.pyplot(
                GRAPHIC_B(
                    modelo, T,
                    xy_evaluado=(punto_eval, st.session_state['evaluar_derivada'])
                ),
                use_container_width=False
            )
        else:
            st.pyplot(GRAPHIC_B(modelo, T), use_container_width=False)

        # =======================================
        # SECCIÓN 4: INTEGRAL (NUEVA DE develop)
        # =======================================
        st.markdown("""
            <section class='BOX-4'>
                <h2>4. Integral – Costo Acumulado</h2>
                <p>Para calcular el costo acumulado durante T años se integra:</p>
            </section>
        """, unsafe_allow_html=True)

        st.latex(r"S(T) = 12 \int_{0}^{T} C(t)\, dt")

        S_T = modelo.costo_acumulado(T)

        st.markdown(
            f"<p><b>Solución numérica:</b> S(T) = {S_T:.2f}</p>",
            unsafe_allow_html=True
        )

        # Gráficos nuevos integrales
        st.markdown("<h3>Gráfico de la integral acumulada</h3>", unsafe_allow_html=True)
        st.pyplot(GRAPHIC_C(modelo, T))

        st.markdown("<h3>Área bajo la curva C(t)</h3>", unsafe_allow_html=True)
        st.pyplot(GRAPHIC_D(modelo, T))

        # =======================================
        # SECCIÓN 5: TABLA
        # =======================================
        st.markdown(SectionBOX6(), unsafe_allow_html=True)

    # =======================================
    # TAB 2 — INTERPRETACIÓN AUTOMÁTICA
    # =======================================
    with tab2:
        st.subheader("Explicación Desarrollada")
        st.write("Aquí se encuentra una información extra sobre el desarrollo aplicado.")

        # Datos para interpretación final
        datos_interpretacion = {
            "C0": modelo.evaluar_C(0),
            "CT": modelo.evaluar_C(T),
            "Cp0": modelo.evaluar_Cp(0),
            "CpT": modelo.evaluar_Cp(T),
            "S_T": modelo.costo_acumulado(T),
            "T": T,
            "funcion_latex": sp.latex(modelo.funcion),
            "derivada_latex": sp.latex(modelo.derivada),
        }

        interpretacion_texto = Interpretation(datos_interpretacion)

        st.markdown(f"""
        <section class='BOX-6'>
            <h2>6. Interpretación Automática</h2>
            {interpretacion_texto}
        </section>
        """, unsafe_allow_html=True)

        # =======================================
        # DESARROLLO PASO A PASO
        # =======================================
        with st.expander("Ver desarrollo paso a paso"):

            st.markdown("### Función original")
            st.latex(fr"C(t) = {sp.latex(modelo.funcion)}")

            st.markdown("### Derivada de C(t)")
            st.latex(fr"C'(t) = {sp.latex(modelo.derivada)}")

            st.markdown("### Integral indefinida de C(t)")
            st.latex(fr"\int C(t)\, dt = {sp.latex(modelo.integral_indef)} + C")

            st.markdown(f"### Integral definida en [0, {T}]")
            integral_simbolica = sp.integrate(modelo.funcion, modelo.t)
            st.latex(fr"\int C(t)\, dt = {sp.latex(integral_simbolica)} + C")

            st.markdown("### Cálculo del costo acumulado final")
            st.latex(r"S(T) = 12 \cdot \int_0^T C(t)\, dt")

            try:
                integral_T_simbolica = sp.integrate(modelo.funcion, (modelo.t, 0, T))
                st.latex(fr"\int_0^{T} C(t)\, dt = {sp.latex(integral_T_simbolica)}")
            except:
                st.warning("No se pudo integrar simbólicamente.")

            valor_S = modelo.costo_acumulado(T)
            st.latex(fr"S({T}) = {valor_S:.2f}")

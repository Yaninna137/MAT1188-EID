''''
Archivo HOME
Casi Terminado
Falta el boton de limpiar la pagina, Y saber como ingresar datos
en fomrula, por seccion, etc.
@yaninna173
'''

import streamlit as st

from core.state import inicializar_session_state
from core.processing import Datos
from components.design_textual.information import SectionBOX1, SectionBOX2,SectionBOX0,Header_subheader
from components.design_elements.layout import Desing_CSS

def main():
    st.set_page_config(layout="wide")
    inicializar_session_state()
    st.markdown(Desing_CSS(), unsafe_allow_html=True)
    st.markdown(Header_subheader(), unsafe_allow_html=True)
    Estado = False # Para mostrar las otras paginas

    # ---- Cuerpo Inicial 
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown(SectionBOX1(), unsafe_allow_html=True)
    with col2:
        st.markdown(SectionBOX2(), unsafe_allow_html=True)
        # ---- Posible campos de ediccion, para enviar los datos ---- Mejorar
        func = st.text_input("C(t)", "2*t**2 + 5*t + 10")
        T = st.number_input("Periodo de amortización (años)", min_value=1, value=5)
        r = st.number_input("Tasa de descuento r (opcional)", min_value=0.0, value=0.0)
        K = st.number_input("Costo de reemplazo K (opcional)", min_value=0.0, value=0.0)
        if st.button("Calcular Modelo"):
            st.success("PROXIMENTE ")
            Estado = True # Habilta moratrala
    st.markdown("---")
    if Estado == True:
        Datos()
    # ---- Footer ----
    st.markdown(SectionBOX0(), unsafe_allow_html=True)

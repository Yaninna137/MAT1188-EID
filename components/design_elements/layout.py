'''
Estructura con todos los componentes de la pagina
'''
def Desing_CSS():
    return """
    <style>

    body {
        background: #0f0f17;
        color: #e6e6e6;
    }

    .card {
        background: #1c1f2e;
        padding: 22px;
        border-radius: 14px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.35);
        border: 1px solid rgba(255,255,255,0.07);
        transition: 0.25s;
    }

    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(0,0,0,0.45);
    }

    .card-info {
        border-left: 5px solid #59a9ff;
    }

    .card-secondary {
        border-left: 5px solid #a46bff;
    }

    .h2box1 {
        color: #96BAE0 !important;
        font-weight: 600;
        margin-top: 0.3rem;
        margin-bottom: 0.8rem;
    }
    .h2box2{
        color: #8F72AF !important;
        font-weight: 600;
        margin-top: 0.3rem;
        margin-bottom: 0.8rem;
    }

    ul li {
        margin-bottom: 6px;
    }

    /* Inputs streamlit */
    .stTextInput > div > input,
    .stNumberInput input {
        background: #2a2d3d !important;
        border-radius: 8px;
        border: 1px solid #3b3e55 !important;
        color: white !important;
        padding: 10px !important;
    }

    .stButton > button {
        width: 100%;
        background: #2fdf83 !important;
        color: black !important;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 0;
        border: none;
    }

    .stButton > button:hover {
        background: #26c373 !important;
        transform: scale(1.02);
    }
    .input-card {
        background: rgba(255,255,255,0.03);
        padding: 15px 20px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        margin-bottom: 20px;
    }

    .input-card h4 {
        margin-top: 0;
        text-align: center;
        font-weight: 600;
    }



    </style>
    """


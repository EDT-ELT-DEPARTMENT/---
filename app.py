import streamlit as st
import os

# 1. Configuration de la page
st.set_page_config(page_title="Plateforme - Qissati Dirassati", layout="wide")

# 2. CSS pour le design "Propre et Moderne" (Style de l'image)
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

html, body, [data-testid="stMarkdownContainer"] {
    font-family: 'Cairo', sans-serif !important;
    direction: RTL;
}

/* Fond blanc très léger et propre */
.stApp { background-color: #ffffff; }

/* Style des Cartes (Boutons avec ombre) */
.stButton>button { 
    width: 100% !important; 
    height: 120px !important;
    border-radius: 15px !important; 
    border: 1px solid #e0e0e0 !important;
    background-color: #ffffff !important;
    color: #333 !important;
    font-weight: bold !important;
    font-size: 18px !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    transition: 0.3s !important;
}

.stButton>button:hover { 
    border-color: #2980B9 !important;
    box-shadow: 0 6px 12px rgba(0,0,0,0.1) !important;
}

/* Titre principal */
h1 { color: #2c3e50 !important; text-align: center; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 3. Fonction pour le logo
def afficher_logo():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("logo.jpeg", width=300)

# 4. Logique de navigation
if "page" not in st.session_state:
    st.session_state.page = "accueil"

# 5. Interface Principale
if st.session_state.page == "accueil":
    afficher_logo()
    st.markdown("<h1>قصتي دراستي</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #7f8c8d;'>رحلة النجاح تبدأ هنا</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #27ae60;'>جميع هذه الدروس مطابقة تماماً للمناهج التعليمية الوطنية الجزائرية</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Mise en page en colonnes comme sur votre image
    c1, c2 = st.columns(2)
    
    with c1:
        if st.button("الدروس اليومية\nالمتكاملة من ثنائية"):
            st.session_state.page = "cours"
            st.rerun()
        st.write("")
        if st.button("الدروس\nالمرجعية القدة"):
            st.session_state.page = "referentiel"
            st.rerun()

    with c2:
        if st.button("التقدم الأكاديمي\nمن تمات المنمات الأكاديمي"):
            st.session_state.page = "progres"
            st.rerun()
        st.write("")
        if st.button("الدروس اليومية\nممرات كل طالب من الدروب"):
            st.session_state.page = "quotidien"
            st.rerun()

elif st.session_state.page != "accueil":
    st.title(f"صفحة {st.session_state.page}")
    if st.button("⬅ العودة للرئيسية"):
        st.session_state.page = "accueil"
        st.rerun()

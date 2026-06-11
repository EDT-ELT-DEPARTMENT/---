import streamlit as st

# Configuration de la page
st.set_page_config(page_title="قصتي دراستي", layout="wide")

# CSS pour obtenir le design exact de l'image
st.markdown("""
<style>
    /* Centrage global */
    .block-container { max-width: 1200px; padding-top: 2rem; }
    
    /* Style des boutons rectangulaires blancs avec ombre */
    .stButton > button {
        width: 100%;
        height: 120px;
        border-radius: 15px;
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        color: #333 !important;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton > button:hover {
        border-color: #2e7d32 !important;
        transform: translateY(-5px);
    }
    
    /* Style des boutons supérieurs (المصادر/الصفوف) */
    .top-buttons .stButton > button {
        height: 40px;
        border-radius: 50px;
        background-color: #2e7d32 !important;
        color: white !important;
    }
    
    .center-content { text-align: center; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# 1. En-tête : Boutons supérieurs
c1, c2, c3, c4 = st.columns([2, 1, 1, 2])
with c2: st.markdown('<div class="top-buttons">', unsafe_allow_html=True); st.button("الصفوف ⚙️"); st.markdown('</div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="top-buttons">', unsafe_allow_html=True); st.button("الصفوف ⊞"); st.markdown('</div>', unsafe_allow_html=True)

# 2. Centre : Titre et Logo
st.markdown('<div class="center-content">', unsafe_allow_html=True)
st.title("قصتي دراستي")
st.subheader("رحلة النجاح تبدأ هنا")
# Remplacer par votre logo
st.image("https://via.placeholder.com/200x150?text=LOGO", width=200)
st.markdown('</div>', unsafe_allow_html=True)

# 3. Grille des boutons latéraux (2 à gauche, 2 à droite)
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.button("الدروس\nالمنهجية القمة")
    st.write("")
    st.button("الدروس اليومية\nمسارات كل طالب")

with col2:
    # Espace vide central pour le logo/chemin
    st.write("")

with col3:
    st.button("الدروس اليومية\nالمحاضرة من ثانوية")
    st.write("")
    st.button("التقدم الأكاديمي\nمن سمات المنصات")

# 4. Pied de page
st.markdown("---")
st.markdown("### أرحلة النجاح")

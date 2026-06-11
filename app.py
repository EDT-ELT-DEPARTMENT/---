import streamlit as st
import os

# Configuration de la page de l'application
st.set_page_config(
    page_title="قصتي دراستي - لوحة الإنجازات",
    page_icon="🏆",
    layout="centered"
)

# Injection de style CSS personnalisé pour correspondre aux couleurs chaleureuses de l'image (Thème Crème / Pastel)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* Configuration globale en Arabe / RTL */
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, span {
        font-family: 'Cairo', sans-serif !important;
        direction: RTL;
        text-align: right;
    }
    
    /* Fond de l'application reprenant les tons de l'image */
    .stApp {
        background-color: #FDF6EC;
    }
    
    /* Titre principal stylisé avec des feuilles végétales décoratives */
    .board-title {
        text-align: center;
        color: #5D4037;
        font-size: 36px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 30px;
    }
    
    /* Cadre de style "Dessin Animé" pour les badges */
    .badge-card {
        background-color: #FFFFFF;
        border: 2px solid #FFE0B2;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(93, 64, 55, 0.05);
        margin-bottom: 20px;
        min-height: 280px;
    }
    
    .badge-icon {
        font-size: 60px;
        margin-bottom: 10px;
    }
    
    .badge-name {
        color: #E65100;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 8px;
        text-align: center;
    }
    
    .badge-desc {
        color: #795548;
        font-size: 14px;
        line-height: 1.6;
        text-align: center;
    }
    
    /* Jauge verticale de croissance (Arbre de la connaissance) */
    .gauge-container {
        background-color: #FFFFFF;
        border: 2px solid #FFE0B2;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(93, 64, 55, 0.05);
        height: 100%;
    }
    
    .gauge-title {
        color: #5D4037;
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 15px;
        text-align: center;
    }
    
    /* Message d'accueil en bas de l'écran */
    .welcome-banner {
        background-color: #FFFFFF;
        border: 2px solid #FFCC80;
        border-radius: 30px;
        padding: 12px 30px;
        margin-top: 30px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }
    
    .welcome-text {
        color: #2C3E50;
        font-size: 18px;
        font-weight: bold;
        margin: 0;
        text-align: center;
        width: 100%;
    }
    
    /* Bouton de retour en haut à gauche */
    .stButton>button {
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 20px !important;
        background-color: #FFFFFF;
        border: 2px solid #FFE0B2;
        color: #5D4037;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- BOUTON DE RETOUR (En haut à gauche comme sur la photo) ---
col_back_1, col_back_2 = st.columns([1, 10])
with col_back_1:
    if st.button("❯", key="back_btn"):
        st.write("العودة...") # Redirection vers le menu principal si nécessaire

# --- TITRE PRINCIPAL ---
st.markdown('<div class="board-title">🌿 لَوْحَةُ إِنْجَازَاتِ بَطَلِ العِلْمِ 🌿</div>', unsafe_allow_html=True)

# --- ZONE CENTRALE : BADGES & JAUGE D'AVANCEMENT ---
# Division en colonnes : 3 colonnes pour les badges (à gauche) et 1 colonne large pour la jauge (à droite)
col_badges, col_gauge = st.columns([3, 1])

with col_badges:
    # Sous-colonnes pour aligner horizontalement les 3 médailles
    b_col1, b_col2, b_col3 = st.columns(3)
    
    with b_col1:
        st.markdown("""
        <div class="badge-card">
            <div class="badge-icon">☀️</div>
            <div class="badge-name">وسام الإشراق</div>
            <div class="badge-desc">لتسجيل الدخول 5 أيام متتالية</div>
        </div>
        """, unsafe_allow_html=True)
        
    with b_col2:
        st.markdown("""
        <div class="badge-card">
            <div class="badge-icon">🦉</div>
            <div class="badge-name">وسام الحكيم الصغير</div>
            <div class="badge-desc">لقراءة 10 قصص تعليمية</div>
        </div>
        """, unsafe_allow_html=True)
        
    with b_col3:
        st.markdown("""
        <div class="badge-card">
            <div class="badge-icon">🍃</div>
            <div class="badge-name">وسام الثمرة الأولى</div>
            <div class="badge-desc">لإنهاء أول وحدة دراسية بنجاح</div>
        </div>
        """, unsafe_allow_html=True)

with col_gauge:
    # Construction de la jauge de croissance à 75%
    st.markdown("""
    <div class="gauge-container">
        <div class="gauge-title">شجرة نمو<br>المعرفة</div>
        <div style="margin: 20px 0;">
            🍁<br>🍂<br>🍃<br>🌿
        </div>
        <div style="background-color: #FFF3E0; border-radius: 15px; padding: 10px; font-weight: bold; color: #E65100; font-size: 18px; text-align: center;">
            75%
        </div>
        <div class="badge-desc" style="margin-top: 15px; font-size: 12px;">الشجرة تكبر بمعرفتك!</div>
    </div>
    """, unsafe_allow_html=True)

# --- BANNIÈRE DE BIENVENUE (MESSAGE EN BAS) ---
st.markdown("""
<div class="welcome-banner">
    <p class="welcome-text">
        🦉 أهلاً بك يا <b>أحمد</b>، صديقك بَهِيّ ينتظرك لنكمل قصة اليوم!
    </p>
</div>
""", unsafe_allow_html=True)

# Lancement d'un effet festif discret de ballons pour célébrer les réussites de l'élève
st.balloons()

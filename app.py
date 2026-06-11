import streamlit as st
import os

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="قصتي دراستي - عالم القواعد السحري",
    page_icon="🎨",
    layout="centered"
)

# ==========================================
# 2. DESIGN CSS "SUPER COLORÉ" ET INTERACTIF
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;700;900&display=swap');
    
    /* Configuration globale RTL / Arabe */
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, span, label {
        font-family: 'Cairo', sans-serif !important;
        direction: RTL;
        text-align: right;
    }
    
    /* Fond dégradé magique et joyeux */
    .stApp {
        background: linear-gradient(135deg, #FFF9E6 0%, #E3F2FD 50%, #E8F5E9 100%);
    }
    
    /* Boutons de navigation et de choix */
    .stButton>button {
        width: 100% !important;
        border-radius: 20px !important;
        font-size: 20px !important;
        font-weight: 900 !important;
        padding: 15px !important;
        background: linear-gradient(135deg, #FF7675, #FF4757) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0px 6px 0px rgba(0,0,0,0.1) !important;
        margin-bottom: 10px;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0px 8px 0px rgba(0,0,0,0.15) !important;
    }
    
    /* Boîtes de style BD pour les histoires */
    .cartoon-box {
        background-color: #FFFFFF;
        border: 4px solid #FFCC80;
        padding: 25px;
        border-radius: 25px;
        margin-bottom: 25px;
        box-shadow: 8px 8px 0px #FFE0B2;
    }
    
    .story-title {
        color: #FF6B6B;
        font-weight: 900;
        font-size: 24px;
        text-align: center;
        margin-bottom: 15px;
    }
    
    .story-text {
        font-size: 20px;
        line-height: 1.9;
        color: #2C3E50;
        font-weight: 700;
    }

    /* Tableau d'honneur (Tableau des médailles) */
    .board-title {
        text-align: center;
        color: #FF6B6B;
        font-size: 36px;
        font-weight: 900;
        margin-bottom: 30px;
    }
    
    .badge-card {
        background: white;
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        min-height: 270px;
        border: 3px solid #FFD32A;
    }
    
    .badge-icon { 
        font-size: 65px; 
        margin-bottom: 10px; 
    }
    
    .badge-name { 
        font-size: 22px; 
        font-weight: 900; 
        margin-bottom: 8px; 
        text-align: center; 
        color: #FF9F43; 
    }
    
    .badge-desc { 
        color: #57606F; 
        font-size: 15px; 
        font-weight: 700; 
        text-align: center; 
    }
    
    /* Jauge de progression personnalisée pour l'arbre */
    .gauge-container {
        background: linear-gradient(180deg, #FFFFFF, #E8F5E9);
        border: 3px solid #10AC84;
        border-radius: 25px;
        padding: 20px;
        text-align: center;
    }
    
    /* Grande bannière d'accueil */
    .welcome-banner {
        background: linear-gradient(135deg, #FFF9E6, #FFF2CC);
        border: 3px solid #FFA801;
        border-radius: 35px;
        padding: 15px 30px;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 3. GESTION DE L'ÉTAT ET DES COMPÉTENCES (Session State)
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "menu"

# Variables de réponses (correct / wrong / None)
if "ans_lesson1" not in st.session_state:
    st.session_state.ans_lesson1 = None
if "ans_lesson2" not in st.session_state:
    st.session_state.ans_lesson2 = None
if "ans_lesson3" not in st.session_state:
    st.session_state.ans_lesson3 = None

# Validation définitive des compétences (True / False) pour le calcul du score
if "score_lesson1" not in st.session_state:
    st.session_state.score_lesson1 = False
if "score_lesson2" not in st.session_state:
    st.session_state.score_lesson2 = False
if "score_lesson3" not in st.session_state:
    st.session_state.score_lesson3 = False


# ==========================================
# 4. CALCUL DYNAMIQUE DU POURCENTAGE
# ==========================================
nombre_de_lecons_reussies = 0

if st.session_state.score_lesson1 == True:
    nombre_de_lecons_reussies = nombre_de_lecons_reussies + 1

if st.session_state.score_lesson2 == True:
    nombre_de_lecons_reussies = nombre_de_lecons_reussies + 1

if st.session_state.score_lesson3 == True:
    nombre_de_lecons_reussies = nombre_de_lecons_reussies + 1

# Formule du pourcentage général (3 leçons au total, chacune vaut 33.33%)
if nombre_de_lecons_reussies == 0:
    pourcentage_connaissance = 0
elif nombre_de_lecons_reussies == 1:
    pourcentage_connaissance = 33
elif nombre_de_lecons_reussies == 2:
    pourcentage_connaissance = 66
elif nombre_de_lecons_reussies == 3:
    pourcentage_connaissance = 100


# ==========================================
# 5. FONCTIONS UTILES (Affichage du logo)
# ==========================================
def afficher_logo_haut():
    if os.path.exists("logo.jpeg"):
        col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
        with col_l2:
            st.image("logo.jpeg", use_column_width=True)


# ==========================================
# 6. PAGES DU SYSTÈME ET LOGIQUE REPOUSSÉE
# ==========================================

# ------------------------------------------
# A. MENU PRINCIPAL INTERACTIF
# ------------------------------------------
if st.session_state.page == "menu":
    afficher_logo_haut()
    st.markdown("<h1 style='text-align: center; color: #FF6B6B; font-size: 42px; font-weight: 900;'>🎈 عَالَمُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #57606F; font-weight: bold;'>مرحباً بك يا بطل القواعد! اختر مغامرتك التفاعلية اليوم:</h3>", unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌟 مغامرة أقسام الكلمة\n(مع الأرنب سمسم 🥕)", key="btn_l1"):
            st.session_state.page = "lesson1"
            st.rerun()
            
    with col2:
        if st.button("🏰 حصن الجملة الاسمية والفعلية\n(تحدي حراس القلعة 👑)", key="btn_l2"):
            st.session_state.page = "lesson2"
            st.rerun()
            
    st.write("")
    col3, col4 = st.columns([1.4, 1])
    with col3:
        if st.button("🕵️‍♂️ لغز المفعول به والمنصوبات\n(عدسة المحقق كَانَمُون 🔍)", key="btn_l3"):
            st.session_state.page = "lesson3"
            st.rerun()
            
    with col4:
        if st.button("🏆 لوحة الأوسمة والأرباح", key="btn_rew"):
            st.session_state.page = "لوحة_الإنجازات"
            st.rerun()


# ------------------------------------------
# B. MISSION 1 : أقسام الكلمة
# ------------------------------------------
elif st.session_state.page == "lesson1":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_1"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #FF4757; text-align: center; font-weight: 900;'>🎬 قصة متحركة: الأرنب السريع سمسم</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <div class="story-title">📦 صندوق الكلمات السحري</div>
        <p class="story-text">
        🏃‍♂️ كـان الأرنب الذكي <b>سَمسَم</b> يقفز في الغابة، وفجأة وجد

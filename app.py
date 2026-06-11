import streamlit as st
import os

# 1. Configuration de la page
st.set_page_config(
    page_title="قصتي دراستي - عالم القواعد السحري",
    page_icon="🎨",
    layout="centered"
)

# 2. Design CSS "Super Coloré" et Enfantin
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;700;900&display=swap');
    
    /* Configuration globale Arabe / RTL */
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, span, label {
        font-family: 'Cairo', sans-serif !important;
        direction: RTL;
        text-align: right;
    }
    
    /* Fond dégradé magique et très joyeux */
    .stApp {
        background: linear-gradient(135deg, #FFF9E6 0%, #E3F2FD 50%, #E8F5E9 100%);
    }
    
    /* Boutons Principaux stylisés avec des dégradés de couleurs vifs */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        font-size: 20px !important;
        font-weight: 900;
        padding: 15px;
        color: white !important;
        border: none;
        box-shadow: 0px 6px 0px rgba(0,0,0,0.1);
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 9px 0px rgba(0,0,0,0.15);
    }
    
    /* Attribution des couleurs uniques par type de bouton */
    button[key*="btn_lesson1"] { background: linear-gradient(135deg, #FF7675, #FF4757) !important; }
    button[key*="btn_lesson2"] { background: linear-gradient(135deg, #54A0FF, #2E86DE) !important; }
    button[key*="btn_lesson3"] { background: linear-gradient(135deg, #1DD1A1, #10AC84) !important; }
    button[key*="btn_rewards"] { background: linear-gradient(135deg, #FFC048, #FFA801) !important; }
    button[key*="back_btn"] { background: #57606F !important; border-radius: 50% !important; width: 55px; height: 55px; }
    
    /* Boîtes de texte pour l'histoire (Style Bande Dessinée) */
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

    /* Styles colorés pour la Table des Médailles */
    .board-title {
        text-align: center;
        color: #FF6B6B;
        font-size: 36px;
        font-weight: 900;
        text-shadow: 2px 2px 0px #FFF;
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
        transition: 0.3s;
    }
    
    .badge-card:hover { transform: scale(1.05); }
    
    .card-sun { border: 3px solid #FFD32A; background: #FFFDF0; }
    .card-owl { border: 3px solid #FF9F43; background: #FFF9F2; }
    .card-leaf { border: 3px solid #10AC84; background: #F0FDF4; }
    
    .badge-icon { font-size: 65px; margin-bottom: 10px; }
    .badge-name { font-size: 22px; font-weight: 900; margin-bottom: 8px; text-align: center; }
    .badge-desc { color: #57606F; font-size: 15px; font-weight: 700; text-align: center; }
    
    /* Jauge de l'arbre colorée */
    .gauge-container {
        background: linear-gradient(180deg, #FFFFFF, #E8F5E9);
        border: 3px solid #10AC84;
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.05);
    }
    
    /* Grande bannière de bienvenue jaune */
    .welcome-banner {
        background: linear-gradient(135deg, #FFF9E6, #FFF2CC);
        border: 3px solid #FFA801;
        border-radius: 35px;
        padding: 15px 30px;
        margin-top: 30px;
        box-shadow: 0px 8px 16px rgba(255, 168, 1, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Gestion de l'état (Session State)
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "ans_lesson1" not in st.session_state:
    st.session_state.ans_lesson1 = None
if "ans_lesson2" not in st.session_state:
    st.session_state.ans_lesson2 = None
if "ans_lesson3" not in st.session_state:
    st.session_state.ans_lesson3 = None

# 4. Affichage du Logo unique
def afficher_logo_haut():
    if os.path.exists("logo.jpeg"):
        col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
        with col_l2:
            st.image("logo.jpeg", use_column_width=True)

# --- PAGES ET NAVIGATION ---

# A. MENU PRINCIPAL SANS CATÉGORIES D'ÂGE
if st.session_state.page == "menu":
    afficher_logo_haut()
    st.markdown("<h1 style='text-align: center; color: #FF6B6B; font-size: 42px; font-weight: 900;'>🎈 عَالَمُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #57606F; font-weight: bold;'>مرحباً بك يا بطل القواعد! اختر مغامرتك التفاعلية اليوم:</h3>", unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌟 مغامرة أقسام الكلمة\n(مع الأرنب سمسم 🥕)", key="btn_lesson1"):
            st.session_state.page = "lesson1"
            st.session_state.ans_lesson1 = None
            st.rerun()
            
    with col2:
        if st.button("🏰 حصن الجملة الاسمية والفعلية\n(تحدي حراس القلعة 👑)", key="btn_lesson2"):
            st.session_state.page = "lesson2"
            st.session_state.ans_lesson2 = None
            st.rerun()
            
    st.write("")
    col3, col4 = st.columns([1.4, 1])
    with col3:
        if st.button("🕵️‍♂️ لغز المفعول به والمنصوبات\n(عدسة المحقق كَانَمُون 🔍)", key="btn_lesson3"):
            st.session_state.page = "lesson3"
            st.session_state.ans_lesson3 = None
            st.rerun()
            
    with col4:
        if st.button("🏆 لوحة الأوسمة والأرباح", key="btn_rewards"):
            st.session_state.page = "لوحة_الإنجازات"
            st.rerun()

# B. MAGHREB 1 : أقسام الكلمة
elif st.session_state.page == "lesson1":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_l1"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #FF4757; text-align: center; font-weight: 900;'>🎬 دروس قواعد تفاعلية: الأرنب السريع سمسم</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box" style="border-color: #FF7675; box-shadow: 8px 8px 0px #FFD2D2;">
        <div class="story-title">📦 صندوق الكلمات السحري</div>
        <p class="story-text">
        🏃‍♂️ كـان الأرنب الذكي <b>سَمسَم</b> يقفز في الغابة السحرية، وفجأة وجد صندوقاً ذهبياً كبيراً تتطاير منه الكلمات الملونة في الهواء! <br>
        أسرع الحكيم سُلحوف وقال له: يا سمسم، كل كلمات اللغة العربية تنقسم إلى ثلاثة أنواع رائعة:<br><br>
        🦁 <span style='color: #FF7675;'><b>1. الاسم:</b></span> اسم إنسان أو حيوان أو شيء (مثل: أرنب، شجرة، أحمد).<br>
        🏃‍♂️ <span style='color: #2E86DE;'><b>2. الفعل:</b></span> نشاط وحركة نقوم بها في زمن معين (مثل: يَقْفِزُ، يَأْكُلُ).<br>
        📦 <span style='color: #10AC84;'><b>3. الحرف:</b></span> كلمة صغيرة جداً لا نفهم معناها إلا مع غيرها (مثل: فِي، إِلَى، عَلَى).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🎮 اضغط على نوع الكلمة الصحيح لتطعم سمسم:")
    st.markdown("<h2 style='text-align: center; color: white; background: linear-gradient(135deg, #FF7675, #FF4757); padding: 15px; border-radius: 20px; box-shadow: 0px 5px 0px #C23

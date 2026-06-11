import streamlit as st
import os

# 1. Configuration de la page
st.set_page_config(
    page_title="قصتي دراستي - عالم القواعد السحري",
    page_icon="🎨",
    layout="centered"
)

# 2. Design CSS "Super Coloré" et Enfantin (Thème Parc d'attractions et Magie)
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
    button[key*="btn_6_7"] { background: linear-gradient(135deg, #FF7675, #FF4757) !important; }
    button[key*="btn_8_9"] { background: linear-gradient(135deg, #54A0FF, #2E86DE) !important; }
    button[key*="btn_10_11"] { background: linear-gradient(135deg, #1DD1A1, #10AC84) !important; }
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
    
    /* Grande bannière de bienvenue jaune pétante */
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
if "ans_6_7" not in st.session_state:
    st.session_state.ans_6_7 = None
if "ans_8_9" not in st.session_state:
    st.session_state.ans_8_9 = None
if "ans_10_11" not in st.session_state:
    st.session_state.ans_10_11 = None

# 4. Affichage du Logo unique
def afficher_logo_haut():
    if os.path.exists("logo.jpeg"):
        col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
        with col_l2:
            st.image("logo.jpeg", use_column_width=True)

# --- PAGES ET NAVIGATION ---

# A. LE MENU PRINCIPAL SUPER COLORÉ
if st.session_state.page == "menu":
    afficher_logo_haut()
    st.markdown("<h1 style='text-align: center; color: #FF6B6B; font-size: 42px; font-weight: 900;'>🎈 عَالَمُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #57606F; font-weight: bold;'>مرحباً بك يا بطل القواعد! اختر مغامرتك الملونة اليوم:</h3>", unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧒 فئة 6 - 7 سنوات\n(مغامرة الأرنب سمسم 🥕)", key="btn_6_7"):
            st.session_state.page = "6-7"
            st.session_state.ans_6_7 = None
            st.rerun()
            
    with col2:
        if st.button("👦 فئة 8 - 9 سنوات\n(حصن القلعة السحرية 🏰)", key="btn_8_9"):
            st.session_state.page = "8-9"
            st.session_state.ans_8_9 = None
            st.rerun()
            
    st.write("")
    col3, col4 = st.columns([1.4, 1])
    with col3:
        if st.button("🧑 فئة 10 - 11 سنة\n(عدسة المحقق كَانَمُون 🕵️‍♂️)", key="btn_10_11"):
            st.session_state.page = "10-11"
            st.session_state.ans_10_11 = None
            st.rerun()
            
    with col4:
        if st.button("🏆 لوحة الأوسمة والأرباح", key="btn_rewards"):
            st.session_state.page = "لوحة_الإنجازات"
            st.rerun()

# B. CATEGORIE 6-7 ANS (أقسام الكلمة)
elif st.session_state.page == "6-7":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_6_7"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #FF4757; text-align: center; font-weight: 900;'>🎬 قصة متحركة: الأرنب السريع سمسم</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box" style="border-color: #FF7675; box-shadow: 8px 8px 0px #FFD2D2;">
        <div class="story-title">📦 صندوق الكلمات السحري</div>
        <p class="story-text">
        🏃‍♂️ كـان الأرنب الذكي <b>سَمسَم</b> يقفز في الغابة السحرية، وفجأة وجد صندوقاً ذهبياً كبيراً تتطاير منه الكلمات الملونة في الهواء! <br>
        أسرع الحكيم سُلحوف وقال له: يا سمسم، كل كلمات اللغة العربية تنقسم إلى ثلاثة أنواع رائعة:<br><br>
        🦁 <span style='color: #FF7675;'><b>1. الاسم:</b></span> اسم إنسان أو حيوان أو شيء (مثل: أرنب، شجرة).<br>
        🏃‍♂️ <span style='color: #2E86DE;'><b>2. الفعل:</b></span> نشاط وحركة نقوم بها (مثل: يَقْفِزُ، يَأْكُلُ).<br>
        📦 <span style='color: #10AC84;'><b>3. الحرف:</b></span> كلمة صغيرة جداً (مثل: فِي، إِلَى).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🎮 اضغط على الزر الصحيح لتطعم سمسم:")
    st.markdown("<h2 style='text-align: center; color: white; background: linear-gradient(135deg, #FF7675, #FF4757); padding: 15px; border-radius: 20px; box-shadow: 0px 5px 0px #C23616;'>الكلمة هي: « يَقْفِزُ »</h2>", unsafe_allow_html=True)
    st.write("")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("اسْم 🦁", key="opt_1"): st.session_state.ans_6_7 = "wrong"
    with c2:
        if st.button("فِعْل 🏃‍♂️", key="opt_2"): st.session_state.ans_6_7 = "correct"
    with c3:
        if st.button("حَرْف 📦", key="opt_3"): st.session_state.ans_6_7 = "wrong"
            
    if st.session_state.ans_6_7 == "correct":
        st.success("🎉 ممتاز! (يَقْفِزُ) حركة ونشاط، إذن هي فعل! سمسم سعيد بالجزرة الآن 🥕!")
    elif st.session_state.ans_6_7 == "wrong":
        st.warning("🧐 ركز يا بطل! الأرنب يقوم بحركة ممتعة (القفز)، إذن الكلمة تعبر عن حركة!")

# C. CATEGORIE 8-9 ANS (الجملة الاسمية والفعلية)
elif st.session_state.page == "8-9":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_8_9"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #2E86DE; text-align: center; font-weight: 900;'>🎬 قصة متحركة: حراس قلعة الجمل</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box" style="border-color: #54A0FF; box-shadow: 8px 8px 0px #D2E7FF;">
        <div class="story-title" style="color: #2E86DE;">🏰 بوابات الحصن اللغوي</div>
        <p class="story-text">
        وقف الأبطال أمام قلعة القواعد الضخمة! وعلى البوابة يقف حارسان شجاعان:<br><br>
        👑 <span style='color: #FF9F43;'><b>الحارس الأول (الجملة الاسمية):</b></span> يصرخ ويقول: أنا أبدأ دائماً بـ <b>اسم</b> صريح، وعندي ركنان هما المبتدأ والخبر (مثل: <i>العِلْمُ نُورٌ</i>).<br>
        ⚔️ <span style='color: #2E86DE;'><b>الحارس الثاني (الجملة الفعلية):</b></span> يلوح بسيفه ويقول: أنا أبدأ دائماً بـ <b>فعل</b> قوي يدل على حركة (مثل: <i>تُمطِرُ السَّمَاءُ</i>).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🎮 تحدى حارس البوابة الآن:")
    st.markdown("<h2 style='text-align: center; color: white; background: linear-gradient(135deg, #54A0FF, #2E86DE); padding: 15px; border-radius: 20px; box-shadow: 0px 5px 0px #1B4F72;'>الجملة هي: « تُمطِرُ السَّمَاءُ »</h2>", unsafe_allow_html=True)
    st.write("")

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("جملة اسمية 👑", key="opt_p1"): st.session_state.ans_8_9 = "wrong"
    with col_b2:
        if st.button("جملة فعلية ⚔️", key="opt_p2"): st.session_state.ans_8_9 = "correct"
            
    if st.session_state.ans_8_9 == "correct":
        st.success("🎉 واو! الإجابة صحيحة لأن 'تُمطِرُ' فعل مضارع. انفتحت بوابة القلعة السحرية 🔑!")
    elif st.session_state.ans_8_9 == "wrong":
        st.warning("❌ الحارس يرفض العبور! انظر للكلمة الأولى 'تُمطِرُ'.. هل هي اسم أم شيء يحدث الآن (فعل)؟")

# D. CATEGORIE 10-11 ANS (المفعول به)
elif st.session_state.page == "10-11":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_10_11"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #10AC84; text-align: center; font-weight: 900;'>🎬 قصة متحركة: قضية المحقق كَانَمُون</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box" style="border-color: #1DD1A1; box-shadow: 8px 8px 0px #D1F2E9;">
        <div class="story-title" style="color: #10AC84;">🔍 لغز الكلمة المنصوبة</div>
        <p class="story-text">
        🕵️‍♂️ المحقق الذكي <b>كَانَمُون</b> يمسك بعدسته ويبحث عن سر اختفاء كلمة في الجملة التالية!<br>
        قال: لدينا الفعل (كَتَبَ) والفاعل الذي قام بالعمل وهو (التِّلْمِيذُ).. لكن ماذا كتب؟! <br><br>
        🎯 فجأة ظهر <b>المَفْعُولُ بِهِ</b> وهو يضحك ويقول: أنا الاسم المنصوب بالفتحة، وأنا الذي وقع عليّ فعل الفاعل! لمعرفتي اسألني دائماً بـ: <b>مَاذَا؟</b> (مثل: كَتَبَ التِّلْمِيذُ <u>الدَّرْسَ</u>).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🎮 ساعد المحقق في حل القضية واقبض على المفعول به:")
    st.markdown("<h2 style='text-align: center; color: white; background: linear-gradient(135deg, #1DD1A1, #10AC84); padding: 15px; border-radius: 20px; box-shadow: 0px 5px 0px #065F46;'>الجملة هي: « قَرَأَ الطِّفْلُ قِصَّةً جَمِيلَةً »</h2>", unsafe_allow_html=True)
    st.write("")

    ca1, ca2, ca3 = st.columns(3)
    with ca1:
        if st.button("قَرَأَ 📖", key="ca1"): st.session_state.ans_10_11 = "v"
    with ca2:
        if st.button("الطِّفْلُ 🧒", key="ca2"): st.session_state.ans_10_11 = "f"
    with ca3:
        if st.button("قِصَّةً 📚", key="ca3"): st.session_state.ans_10_11 = "m"
            
    if st.session_state.ans_10_11 == "m":
        st.success("🎯 قضية ناجحة! 'قِصَّةً' هي الإجابة عن سؤال (ماذا قرأ الطفل؟), مفعول به منصوب وعلامة نصبه الفتحة!")
    elif st.session_state.ans_10_11 == "v":
        st.warning("❌ لا يا سيادة المحقق! 'قَرَأَ' هو الفعل الأساسي في القصة وليس المفعول به.")
    elif st.session_state.ans_10_11 == "f":
        st.warning("❌ ركز! 'الطِّفْلُ' هو الفاعل البطل الذي قرأ القصة، وليس المفعول به.")

# E. INTERFACE REPRODUITE DE LA PHOTO (لوحة الإنجازات)
elif st.session_state.page == "لوحة_الإنجازات":
    col_back_1, col_back_2 = st.columns([1, 10])
    with col_back_1:
        if st.button("❯", key="back_btn"):
            st.session_state.page = "menu"
            st.rerun()

    afficher_logo_haut()
    st.markdown('<div class="board-title">🌿 لَوْحَةُ إِنْجَازَاتِ بَطَلِ العِلْمِ 🌿</div>', unsafe_allow_html=True)

    col_badges, col_gauge = st.columns([3, 1])

    with col_badges:
        b_col1, b_col2, b_col3 = st.columns(3)
        with b_col1:
            st.markdown("""
            <div class="badge-card card-sun">
                <div class="badge-icon">☀️</div>
                <div class="badge-name" style="color: #FFB900;">وسام الإشراق</div>
                <div class="badge-desc">لتسجيل الدخول 5 أيام متتالية</div>
            </div>
            """, unsafe_allow_html=True)
        with b_col2:
            st.markdown("""
            <div class="badge-card card-owl">
                <div class="badge-icon">🦉</div>
                <div class="badge-name" style="color: #FF9F43;">وسام الحكيم الصغير</div>
                <div class="badge-desc">لقراءة 10 قصص تعليمية</div>
            </div>
            """, unsafe_allow_html=True)
        with b_col3:
            st.markdown("""
            <div class="badge-card card-leaf">
                <div class="badge-icon">🍃</div>
                <div class="badge-name" style="color: #10AC84;">وسام الثمرة الأولى</div>
                <div class="badge-desc">لإنهاء أول وحدة دراسية بنجاح</div>
            </div>
            """, unsafe_allow_html=True)

    with col_gauge:
        st.markdown("""
        <div class="gauge-container">
            <div style="color: #2F3542; font-size: 16px; font-weight: 900; text-align:center;">شجرة نمو<br>المعرفة</div>
            <div style="margin: 20px 0; font-size: 26px; text-align:center; line-height:1.4;">🍁<br>🍂<br>🍃<br>🌿</div>
            <div style="background-color: #2ED573; border-radius: 15px; padding: 10px; font-weight: 900; color: white; font-size: 20px; text-align: center; box-shadow: 0px 4px 0px #26AF5F;">75%</div>
            <div style="color: #57606F; font-size: 12px; font-weight:bold; text-align: center; margin-top: 12px;">الشجرة تكبر بمعرفتك!</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="welcome-banner">
        <p style="color: #2C3E50; font-size: 20px; font-weight: 900; margin: 0; text-align: center;">
            🦉 أهلاً بك يا <b>أحمد</b>، صديقك بَهِيّ ينتظرك لنكمل قصة اليوم اللغوية!
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

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
        🏃‍♂️ كـان الأرنب الذكي <b>سَمسَم</b> يقفز في الغابة، وفجأة وجد صندوقاً ذهبياً تتطاير منه الكلمات الملونة في الهواء! <br>
        أسرع الحكيم سُلحوف وقال له: يا سمسم، كل كلمات اللغة العربية تنقسم إلى ثلاثة أنواع رائعة:<br><br>
        🦁 <b>1. الاسم:</b> ما نسمي به الإنسان، الحيوان، أو الشيء (مثل: أرنب، شجرة، أحمد).<br>
        🏃‍♂️ <b>2. الفعل:</b> حركة ونشاط نقوم به في زمن معين (مثل: يَقْفِزُ، يَأْكُلُ).<br>
        📦 <b>3. الحرف:</b> كلمة صغيرة لا نفهم معناها إلا مع غيرها (مثل: فِي، إِلَى، عَلَى).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🎮 اضغط على نوع الكلمة الصحيح لتطعم سمسم:")
    st.markdown("<h2 style='text-align: center; color: white; background: #FF4757; padding: 15px; border-radius: 20px;'>الكلمة هي: « يَقْفِزُ »</h2>", unsafe_allow_html=True)
    st.write("")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("اسْم 🦁", key="opt_1"):
            st.session_state.ans_lesson1 = "wrong"
    with c2:
        if st.button("فِعْل 🏃‍♂️", key="opt_2"):
            st.session_state.ans_lesson1 = "correct"
            st.session_state.score_lesson1 = True
    with c3:
        if st.button("حَرْف 📦", key="opt_3"):
            st.session_state.ans_lesson1 = "wrong"
            
    if st.session_state.ans_lesson1 == "correct":
        st.success("🎉 ممتاز يا بطل! (يَقْفِزُ) حركة ونشاط، إذن هي فعل! سمسم سعيد بالجزرة الآن 🥕!")
    elif st.session_state.ans_lesson1 == "wrong":
        st.warning("🧐 ركز جيداً! الأرنب يقوم بحركة ممتعة (القفز)، إذن الكلمة تعبر عن حركة وفعل!")


# ------------------------------------------
# C. MISSION 2 : الجملة الاسمية والفعلية
# ------------------------------------------
elif st.session_state.page == "lesson2":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_2"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #2E86DE; text-align: center; font-weight: 900;'>🎬 قصة متحركة: حراس قلعة الجمل</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <div class="story-title" style="color: #2E86DE;">🏰 بوابات الحصن اللغوي</div>
        <p class="story-text">
        وقف الأبطال أمام قلعة القواعد الضخمة! وعلى البوابة يقف حارسان شجاعان لحمايتها:<br><br>
        👑 <b>الحارس الأول (الجملة الاسمية):</b> يصرخ ويقول: أنا أبدأ دائماً بـ <b>اسم</b> صريح، وعندي ركنان هما المبتدأ والخبر (مثل: <i>العِلْمُ نُورٌ</i>).<br>
        ⚔️ <b>الحارس الثاني (الجملة الفعلية):</b> يلوح بسيفه ويقول: أنا أبدأ دائماً بـ <b>فعل</b> قوي يدل على حركة ونشاط (مثل: <i>تُمطِرُ السَّمَاءُ</i>).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🎮 تحدى حارس البوابة لفتح القلعة:")
    st.markdown("<h2 style='text-align: center; color: white; background: #2E86DE; padding: 15px; border-radius: 20px;'>الجملة هي: « تُمطِرُ السَّمَاءُ »</h2>", unsafe_allow_html=True)
    st.write("")

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("جملة اسمية 👑", key="opt_p1"):
            st.session_state.ans_lesson2 = "wrong"
    with col_b2:
        if st.button("جملة فعلية ⚔️", key="opt_p2"):
            st.session_state.ans_lesson2 = "correct"
            st.session_state.score_lesson2 = True
            
    if st.session_state.ans_lesson2 == "correct":
        st.success("🎉 واو! الإجابة صحيحة لأن جملة 'تُمطِرُ السَّمَاءُ' تبدأ بفعل مضارع. انفتحت بوابة القلعة السحرية 🔑!")
    elif st.session_state.ans_lesson2 == "wrong":
        st.warning("❌ الحارس يرفض العبور! انظر للكلمة الأولى 'تُمطِرُ'.. هل هي اسم أم شيء يحدث الآن (فعل)؟")


# ------------------------------------------
# D. MISSION 3 : المفعول به والمنصوبات
# ------------------------------------------
elif st.session_state.page == "lesson3":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_3"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #10AC84; text-align: center; font-weight: 900;'>🎬 قصة متحركة: قضية المحقق كَانَمُون</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <div class="story-title" style="color: #10AC84;">🔍 لغز الكلمة المفقودة</div>
        <p class="story-text">
        🕵️‍♂️ المحقق الذكي <b>كَانَمُون</b> يمسك بعدسته ويبحث عن سر اختفاء كلمة وقع عليها الفعل المذكور!<br>
        قال: لدينا الفعل (قَرَأَ) والفاعل الذي قام بالعمل وهو (الطِّفْلُ).. لكن ماذا قرأ الطفل؟! <br><br>
        🎯 وفجأة ظهر <b>المَفْعُولُ بِهِ</b> وهو يضحك ويقول: أنا الاسم المنصوب بالفتحة، وأنا الذي وقع عليّ فعل الفاعل! لمعرفتي دائماً اسأل الفاعل بـ: <b>مَاذَا؟</b> (مثل: قَرَأَ الطِّفْلُ <u>قِصَّةً</u>).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🎮 ساعد المحقق في حل القضية واقبض على المفعول به:")
    st.markdown("<h2 style='text-align: center; color: white; background: #10AC84; padding: 15px; border-radius: 20px;'>الجملة هي: « قَرَأَ الطِّفْلُ قِصَّةً جَمِيلَةً »</h2>", unsafe_allow_html=True)
    st.write("")

    ca1, ca2, ca3 = st.columns(3)
    with ca1:
        if st.button("قَرَأَ 📖", key="ca1"):
            st.session_state.ans_lesson3 = "v"
    with ca2:
        if st.button("الطِّفْلُ 🧒", key="ca2"):
            st.session_state.ans_lesson3 = "f"
    with ca3:
        if st.button("قِصَّةً 📚", key="ca3"):
            st.session_state.ans_lesson3 = "m"
            st.session_state.score_lesson3 = True
            
    if st.session_state.ans_lesson3 == "m":
        st.success("🎯 قضية ناجحة! 'قِصَّةً' هي الإجابة عن سؤال (ماذا قرأ الطفل؟)، مفعول به منصوب بالفتحة!")
    elif st.session_state.ans_lesson3 == "v":
        st.warning("❌ لا يا سيادة المحقق! 'قَرَأَ' هو الفعل وعملية القراءة نفسها وليس الركن المنصوب.")
    elif st.session_state.ans_lesson3 == "f":
        st.warning("❌ ركز! 'الطِّفْلُ' هو الفاعل البطل الذي قرأ القصة وليس المفعول به.")


# ------------------------------------------
# E. LOVET AL INJAZAT (TABLEAU DES MÉDAILLES INTERACTIF)
# ------------------------------------------
elif st.session_state.page == "لوحة_الإنجازات":
    if st.button("⬅ العودة للمنزل", key="back_r"):
        st.session_state.page = "menu"
        st.rerun()

    afficher_logo_haut()
    st.markdown('<div class="board-title">🌿 لَوْحَةُ إِنْجَازَاتِ بَطَلِ العِلْمِ 🌿</div>', unsafe_allow_html=True)

    col_badges, col_gauge = st.columns([3, 1])

    with col_badges:
        b_col1, b_col2, b_col3 = st.columns(3)
        
        with b_col1:
            if st.session_state.score_lesson1 == True:
                st.markdown("""
                <div class="badge-card" style="border-color: #FF4757; background-color: #FFF5F5;">
                    <div class="badge-icon">🦁</div>
                    <div class="badge-name" style="color: #FF4757;">وسام بطل الكلمات</div>
                    <div class="badge-desc">مُنح لك لتعرفك على الاسم والفعل والحرف مع سمسم!</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="badge-card" style="border-color: #CCCCCC; opacity: 0.5;">
                    <div class="badge-icon">🔒</div>
                    <div class="badge-name" style="color: #888888;">وسام الكلمات مغلق</div>
                    <div class="badge-desc">أكمل مغامرة الأرنب سمسم لفتح هذا الوسام.</div>
                </div>
                """, unsafe_allow_html=True)
                
        with b_col2:
            if st.session_state.score_lesson2 == True:
                st.markdown("""
                <div class="badge-card" style="border-color: #2E86DE; background-color: #F0F7FF;">
                    <div class="badge-icon">🏰</div>
                    <div class="badge-name" style="color: #2E86DE;">وسام حارس القلعة</div>
                    <div class="badge-desc">مُنح لك لنجاحك في عبور بوابات الجملة الاسمية والفعلية!</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="badge-card" style="border-color: #CCCCCC; opacity: 0.5;">
                    <div class="badge-icon">🔒</div>
                    <div class="badge-name" style="color: #888888;">وسام القلعة مغلق</div>
                    <div class="badge-desc">افتح بوابات القلعة اللغوية لفتح هذا الوسام.</div>
                </div>
                """, unsafe_allow_html=True)
                
        with b_col3:
            if st.session_state.score_lesson3 == True:
                st.markdown("""
                <div class="badge-card" style="border-color: #10AC84; background-color: #F0FDF4;">
                    <div class="badge-icon">🕵️‍♂️</div>
                    <div class="badge-name" style="color: #10AC84;">وسام المحقق الذكي</div>
                    <div class="badge-desc">مُنح لك لمساعدتك المحقق كانمون في حل لغز المفعول به!</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="badge-card" style="border-color: #CCCCCC; opacity: 0.5;">
                    <div class="badge-icon">🔒</div>
                    <div class="badge-name" style="color: #888888;">وسام المحقق مغلق</div>
                    <div class="badge-desc">حل قضية الكلمة المنصوبة لفتح this ونوع الوسام.</div>
                </div>
                """, unsafe_allow_html=True)

    with col_gauge:
        st.markdown(f"""
        <div class="gauge-container">
            <div style="color: #2F3542; font-size: 16px; font-weight: 900; text-align:center;">شجرة نمو<br>المعرفة</div>
            <div style="margin: 20px 0; font-size: 26px; text-align:center; line-height:1.4;">🍁<br>🍂<br>🍃<br>🌿</div>
            <div style="background-color: #2ED573; border-radius: 15px; padding: 10px; font-weight: 900; color: white; font-size: 24px; text-align: center; box-shadow: 0px 4px 0px #26AF5F;">
                {pourcentage_connaissance}%
            </div>
            <div style="color: #57606F; font-size: 13px; font-weight: bold; margin-top: 10px; text-align: center;">
                نجحت في {nombre_de_lecons_reussies} من 3
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="welcome-banner">
        <p style="color: #2C3E50; font-size: 20px; font-weight: 900; margin: 0; text-align: center;">
            🦉 أهلاً بك يا <b>أحمد</b>، صديقك بَهِيّ يتابع نمو شجرة معرفتك الذكية خطوة بخطوة!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if pourcentage_connaissance == 100:
        st.balloons()
        st.success("🏆 أشرقت شجرة معرفتك بالكامل يا بطل القواعد المستقبلي! أنت مذهل!")

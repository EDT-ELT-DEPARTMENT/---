import streamlit as st
import os

# Configuration de la page de l'application
st.set_page_config(
    page_title="قصتي دراستي - منصة تعليمية تفاعلية",
    page_icon="✨",
    layout="centered"
)

# Injection de style CSS personnalisé (Thème ludique et chaleureux)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, span, label {
        font-family: 'Cairo', sans-serif !important;
        direction: RTL;
        text-align: right;
    }
    
    .stApp {
        background-color: #FDF6EC;
    }
    
    /* Boutons de navigation principaux */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-size: 18px !important;
        font-weight: bold;
        padding: 12px;
        transition: 0.3s;
    }
    
    /* Style boîte de dialogue dessin animé */
    .cartoon-box {
        background-color: #FFF9E6;
        border: 3px dashed #FFAAA6;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    
    .story-text {
        font-size: 18px;
        line-height: 1.8;
        color: #2C3E50;
    }

    /* Style pour le tableau des badges */
    .board-title {
        text-align: center;
        color: #5D4037;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 25px;
    }
    
    .badge-card {
        background-color: #FFFFFF;
        border: 2px solid #FFE0B2;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(93, 64, 55, 0.05);
        margin-bottom: 15px;
        min-height: 250px;
    }
    
    .badge-icon {
        font-size: 50px;
        margin-bottom: 8px;
    }
    
    .badge-name {
        color: #E65100;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
        text-align: center;
    }
    
    .badge-desc {
        color: #795548;
        font-size: 13px;
        line-height: 1.5;
        text-align: center;
    }
    
    .gauge-container {
        background-color: #FFFFFF;
        border: 2px solid #FFE0B2;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(93, 64, 55, 0.05);
    }
    
    .welcome-banner {
        background-color: #FFFFFF;
        border: 2px solid #FFCC80;
        border-radius: 30px;
        padding: 12px 30px;
        margin-top: 25px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 1. Initialisation de la variable d'état de navigation
if "page" not in st.session_state:
    st.session_state.page = "menu"

# 2. Fonction utilitaire pour afficher le logo en haut de chaque page
def afficher_logo_haut():
    if os.path.exists("logo.jpeg"):
        col_l1, col_l2, col_l3 = st.columns([1, 1.3, 1])
        with col_l2:
            st.image("logo.jpeg", use_column_width=True)

# --- NAVIGATION ET CONTENU ---

# A. MENU PRINCIPAL
if st.session_state.page == "menu":
    afficher_logo_haut()
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>✨ مَنْصَّةُ قِصَّتِي دِرَاسَتِي ✨</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #7F8C8D;'>مرحباً بك يا بطل! اختر مغامرتك اللغوية لليوم:</h3>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧒 فئة 6 - 7 سنوات\n(مغامرة أقسام الكلمة 🏃‍♂️)"):
            st.session_state.page = "6-7"
            st.rerun()
            
    with col2:
        if st.button("👦 فئة 8 - 9 سنوات\n(مملكة الجملة الاسمية والفعلية 🏰)"):
            st.session_state.page = "8-9"
            st.rerun()
            
    st.write("")
    col3, col4 = st.columns([1.5, 1])
    with col3:
        if st.button("🧑 فئة 10 - 11 سنة\n(محقق القواعد: الصياد والمنصوبات 🕵️‍♂️)"):
            st.session_state.page = "10-11"
            st.rerun()
            
    with col4:
        # Bouton interactif pour ouvrir la page calquée sur votre photo
        if st.button("🏆 لوحة الإنجازات"):
            st.session_state.page = "لوحة_الإنجازات"
            st.rerun()

# B. COURS INTERACTIF : 6-7 ANS (أقسام الكلمة)
elif st.session_state.page == "6-7":
    afficher_logo_haut()
    if st.button("⬅ العودة للقائمة الرئيسية"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #FF7675; text-align: center;'>🎬 رسوم متحركة قواعد: مغامرة الأرنب سمسم</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <p class="story-text">
        🏃‍♂️ كـان الأرنب الذكي <b>سَمسَم</b> يقفز في الغابة السحرية، وفجأة وجد صندوقاً كبيراً تتطاير منه الكلمات! <br>
        قال له الحكيم سُلحوف: يا سمسم، الكلمات في لغتنا العربية ثلاثة أنواع لا رابع لها:<br>
        🦁 <b>الاسم:</b> ما نسمي به الإنسان، الحيوان، أو الأشياء (مثل: أرنب، شجرة).<br>
        🏃‍♂️ <b>الفعل:</b> حركة ونشاط نقوم به في زمن معين (مثل: يقفز، أكلَ).<br>
        📦 <b>الحرف:</b> كلمة صغيرة لا نفهم معناها إلا مع غيرها (مثل: في، إلى، على).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎮 العب وتحدّ سمسم:")
    st.write("ساعد سمسم في تصنيف الكلمة التالية ليحصل على الجَزرة 🥕")
    
    st.markdown("<h2 style='text-align: center; color: #E84393;'>الكلمة هي: « يَقْفِزُ »</h2>", unsafe_allow_html=True)
    choix = st.radio("ما هو نوع هذه الكلمة؟", ["اسْم", "فِعْل", "حَرْف"], index=None)
    
    if st.button("تحقق من الإجابة 🥕"):
        if choix == "فِعْل":
            st.success("🎉 إجابة رائعة! يَقْفِزُ هي حركة، إذن هي فعل! لقد أكل سمسم الجزرة!")
        elif choix is not None:
            st.error("🧐 ركّز جيداً يا بطل! يَقْفِزُ تدل على حركة ونشاط، إذن هي فِعْل.")

# C. COURS INTERACTIF : 8-9 ANS (الجملة الاسمية والفعلية)
elif st.session_state.page == "8-9":
    afficher_logo_haut()
    if st.button("⬅ العودة للقائمة الرئيسية"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #74B9FF; text-align: center;'>🎬 رسوم متحركة قواعد: قلعة الجمل السحرية</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <p class="story-text">
        🏰 وصلنا إلى قلعة القواعد! هناك حارسان على باب القلعة:<br>
        👑 <b>الحارس الأول (الجملة الاسمية):</b> يصرخ ويقول: أنا أبدأ دائماً بـ <b>اسم</b>، وعندي ركنان هما المبتدأ والخبر (مثل: <i>العِلْمُ نُورٌ</i>).<br>
        ⚔️ <b>الحارس الثاني (الجملة الفعلية):</b> يلوح بسيفه ويقول: أنا أبدأ دائماً بـ <b>فعل</b>، وعندي فعل وفاعل (مثل: <i>جَاءَ البَطَلُ</i>).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎮 تحدي حراس القلعة:")
    st.write("الحراس يمنعونك من الدخول حتى تحدد نوع هذه الجملة:")
    
    st.markdown("<h2 style='text-align: center; color: #0984E3;'>الجملة هي: « تُمطِرُ السَّمَاءُ »</h2>", unsafe_allow_html=True)
    choix_phrase = st.radio("ما نوع هذه الجملة؟", ["جملة اسمية", "جملة فعلية"], index=None)
    
    if st.button("فتح باب القلعة 🔑"):
        if choix_phrase == "جملة فعلية":
            st.success("🎉 مذهل! الجملة تبدأ بكلمة 'تُمطِرُ' وهي فعل، إذن هي جملة فعلية! تفضل بالدخول.")
        elif choix_phrase is not None:
            st.error("❌ الحارس يرفض إجابتك! انظر إلى الكلمة الأولى 'تُمطِرُ'.. إنها فعل، إذن الجملة فعلية.")

# D. COURS INTERACTIF : 10-11 ANS (المفعول به والمنصوبات)
elif st.session_state.page == "10-11":
    afficher_logo_haut()
    if st.button("⬅ العودة للقائمة الرئيسية"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #55E6C1; text-align: center;'>🎬 رسوم متحركة قواعد: المحقق كـانَمون ومصيدة المفعول به</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <p class="story-text">
        🕵️‍♂️ المحقق الشهير <b>كَانَمُون</b> يبحث عن ركن مفقود في مسرح الجريمة اللغوية! <br>
        قال المحقق: لدينا فعل (كَتَبَ) ولدينا فاعل قام بالحركة (التِّلْمِيذُ).. لكن ماذا كتب؟! <br>
        🎯 وفجأة ظهر <b>المَفْعُولُ بِهِ</b> ضاحكاً وقال: أنا الاسم المنصوب بالفتحة الذي وقع عليّ فعل الفاعل! (مثل: كَتَبَ التِّلْمِيذُ <u>الدَّرْسَ</u>). أنا دائماً أجيب عن سؤال: <b>مَاذَا؟</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎮 اختبر مهاراتك الإعرابية مع المحقق:")
    st.write("ابحث عن المفعول به المنصوب في الجملة التالية:")
    
    st.markdown("<h2 style='text-align: center; color: #27AE60;'>الجملة هي: « قَرَأَ الطِّفْلُ قِصَّةً جَمِيلَةً »</h2>", unsafe_allow_html=True)
    reponse_inv = st.text_input("اكتب الكلمة التي تمثل المفعول به هنا:").strip()
    
    if st.button("تقديم التقرير للمحقق 🕵️‍♂️"):
        if reponse_inv in ["قصة", "قِصَّةً", "قصةً"]:
            st.success("🎯 أحسنت يا سيادة المحقق! 'قصةً' هي المفعول به منصوب وعلامة نصبه الفتحة!")
        elif reponse_inv != "":
            st.error("❌ المحقق يقول: الإجابة غير دقيقة. اسأل نفسك: ماذا قرأ الطفل؟ الطفل قرأ 'قِصَّةً'.")

# E. L'INTERFACE REPRODUITE DE VOTRE PHOTO (لوحة الإنجازات)
elif st.session_state.page == "لوحة_الإنجازات":
    # Bouton flèche de retour fonctionnel
    col_back_1, col_back_2 = st.columns([1, 10])
    with col_back_1:
        if st.button("❯", key="back_btn"):
            st.session_state.page = "menu"
            st.rerun()

    afficher_logo_haut()
    st.markdown('<div class="board-title">🌿 لَوْحَةُ إِنْجَازَاتِ بَطَلِ العِلْمِ 🌿</div>', unsafe_allow_html=True)

    # Zone centrale : Badges et Jauge
    col_badges, col_gauge = st.columns([3, 1])

    with col_badges:
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
        st.markdown("""
        <div class="gauge-container">
            <div style="color: #5D4037; font-size: 15px; font-weight: bold; text-align:center;">شجرة نمو<br>المعرفة</div>
            <div style="margin: 15px 0; font-size: 22px; text-align:center;">🍁<br>🍂<br>🍃<br>🌿</div>
            <div style="background-color: #FFF3E0; border-radius: 15px; padding: 8px; font-weight: bold; color: #E65100; font-size: 18px; text-align: center;">75%</div>
            <div style="color: #795548; font-size: 11px; text-align: center; margin-top: 10px;">الشجرة تكبر بمعرفتك!</div>
        </div>
        """, unsafe_allow_html=True)

    # Bannière message d'accueil de la photo
    st.markdown("""
    <div class="welcome-banner">
        <p style="color: #2C3E50; font-size: 18px; font-weight: bold; margin: 0; text-align: center;">
            🦉 أهلاً بك يا <b>أحمد</b>، صديقك بَهِيّ ينتظرك لنكمل قصة اليوم!
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

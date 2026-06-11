import streamlit as st
import os

# ==========================================
# 1. تهيئة وإعدادات الصفحة العامة
# ==========================================
st.set_page_config(
    page_title="قصتي دراستي - عالم القواعد السحري",
    page_icon="🎨",
    layout="centered"
)

# ==========================================
# 2. تصميم الـ CSS الخارجي لمنع التداخل اللغوي
# ==========================================
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;700;900&display=swap');

/* تنسيق اتجاه النصوص للغة العربية */
html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, span, label {
    font-family: 'Cairo', sans-serif !important;
    direction: RTL;
    text-align: right;
}

/* خلفية التطبيق الكرتونية الملونة */
.stApp {
    background: linear-gradient(135deg, #FFF9E6 0%, #E3F2FD 50%, #E8F5E9 100%);
}

/* تنسيق أزرار التنقل والاختيارات */
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
    box-shadow: 0px 8px 0px rgba(0,0,0,0.1) !important;
}

/* صناديق عرض القصص الحكواتية */
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

/* تنسيق عناوين لوحات الشرف والأوسمة */
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

/* حاوية شجرة نمو المعرفة الذكية */
.gauge-container {
    background: linear-gradient(180deg, #FFFFFF, #E8F5E9);
    border: 3px solid #10AC84;
    border-radius: 25px;
    padding: 20px;
    text-align: center;
}

/* لافتة الترحيب السفلية */
.welcome-banner {
    background: linear-gradient(135deg, #FFF9E6, #FFF2CC);
    border: 3px solid #FFA801;
    border-radius: 35px;
    padding: 15px 30px;
    margin-top: 30px;
}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)


# ==========================================
# 3. إدارة الجلسة وحفظ الإنجازات (Session State)
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "menu"

if "selected_year" not in st.session_state:
    st.session_state.selected_year = None

# حفظ إجابات الطالب الحالية
if "ans_lesson1" not in st.session_state:
    st.session_state.ans_lesson1 = None
if "ans_lesson2" not in st.session_state:
    st.session_state.ans_lesson2 = None
if "ans_lesson3" not in st.session_state:
    st.session_state.ans_lesson3 = None

# التوثيق والاعتماد الدائم للمهارة بعد الإجابة الصحيحة
if "score_lesson1" not in st.session_state:
    st.session_state.score_lesson1 = False
if "score_lesson2" not in st.session_state:
    st.session_state.score_lesson2 = False
if "score_lesson3" not in st.session_state:
    st.session_state.score_lesson3 = False


# ==========================================
# 4. الحساب الديناميكي لنسبة تقدم المعرفة
# ==========================================
nombre_de_lecons_reussies = 0

if st.session_state.score_lesson1 == True:
    nombre_de_lecons_reussies = nombre_de_lecons_reussies + 1

if st.session_state.score_lesson2 == True:
    nombre_de_lecons_reussies = nombre_de_lecons_reussies + 1

if st.session_state.score_lesson3 == True:
    nombre_de_lecons_reussies = nombre_de_lecons_reussies + 1

if nombre_de_lecons_reussies == 0:
    pourcentage_connaissance = 0
elif nombre_de_lecons_reussies == 1:
    pourcentage_connaissance = 33
elif nombre_de_lecons_reussies == 2:
    pourcentage_connaissance = 66
elif nombre_de_lecons_reussies == 3:
    pourcentage_connaissance = 100


# ==========================================
# 5. دوال مساعدة (عرض شعار المنصة علوياً)
# ==========================================
def afficher_logo_haut():
    if os.path.exists("logo.jpeg"):
        col_l1, col_l2, col_l3 = st.columns([0.5, 2, 0.5])
        with col_l2:
            st.image("logo.jpeg", use_column_width=True)


# ==========================================
# 6. بناء الصفحات البرمجية للنظام التفاعلي المتسلسل
# ==========================================

# ------------------------------------------
# أ. القائمة الرئيسية للمغامرات اللغوية
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
    col3, col4 = st.columns(2)
    with col3:
        if st.button("🕵️‍♂️ لغز المفعول به والمنصوبات\n(عدسة المحقق كَانَمُون 🔍)", key="btn_l3"):
            st.session_state.page = "lesson3"
            st.rerun()
            
    with col4:
        if st.button("🏆 لوحة الأوسمة والأرباح", key="btn_rew"):
            st.session_state.page = "لوحة_الإنجازات"
            st.rerun()
            
    st.write("")
    if st.button("📚 استكشف البرنامج الوطني حسب السنوات الدراسية (من 1 إلى 6)", key="btn_national_prog"):
        st.session_state.page = "البرنامج_الوطني"
        st.rerun()



# ------------------------------------------
# هـ. قسم البرنامج الوطني والسنوات الدراسية
# ------------------------------------------
elif st.session_state.page == "البرنامج_الوطني":
    if st.button("⬅ العودة للمنزل", key="back_program"):
        st.session_state.page = "menu"
        st.rerun()

    afficher_logo_haut()
    st.markdown('<div class="board-title">📚 رِحْلَةُ القَوَاعِدِ حَسَبَ السَّنَواتِ 📚</div>', unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #57606F; font-weight: bold;'>اختر سنتك الدراسية واستكشف مغامرات القواعد المقررة لك:</h4>", unsafe_allow_html=True)
    st.write("")

    col_y1, col_y2, col_y3 = st.columns(3)
    col_y4, col_y5, col_y6 = st.columns(3)

    with col_y1:
        if st.button("🌱 السنة الأولى ابتدائي", key="y1"): st.session_state.selected_year = 1
    with col_y2:
        if st.button("🌿 السنة الثانية ابتدائي", key="y2"): st.session_state.selected_year = 2
    with col_y3:
        if st.button("🍀 السنة الثالثة ابتدائي", key="y3"): st.session_state.selected_year = 3
    with col_y4:
        if st.button("🌳 السنة الرابعة ابتدائي", key="y4"): st.session_state.selected_year = 4
    with col_y5:
        if st.button("🌴 السنة الخامسة ابتدائي", key="y5"): st.session_state.selected_year = 5
    with col_y6:
        if st.button("👑 السنة السادسة ابتدائي", key="y6"): st.session_state.selected_year = 6

    if st.session_state.selected_year is not None:
        st.write("---")
        y = st.session_state.selected_year
        
        if y == 1:
            st.markdown("<h3 style='color: #FF4757; text-align: center;'>🎯 دروس السنة الأولى: عוالم الحروف والكلمات الأولى</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #FF7675;">
                <p class="story-text">
                • <b>اكتشاف الحروف والكلمات:</b> التعرف على شكل الحرف وصوته.<br>
                • <b>الضمائر المنفصلة البسيطة:</b> أنا، أنتَ، أنتِ.<br>
                • <b>أسماء الإشارة للقريب:</b> هَذَا، هَذِهِ.<br>
                • <b>التراكيب الأساسية:</b> تركيب جمل قصيرة جداً (مثل: هَذَا كِتَابٌ).
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 2:
            st.markdown("<h3 style='color: #2E86DE; text-align: center;'>🎯 دروس السنة الثانية: بناء الجملة البسيطة</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #54A0FF;">
                <p class="story-text">
                • <b>ضمائر المتكلم والمخاطب والغائب:</b> (نحن، أنتم، هو، هي...).<br>
                • <b>أسماء الإشارة المتقدمة:</b> هَذَا، هَذِهِ، هَؤُلَاءِ.<br>
                • <b>أدوات الاستفهام المشهورة:</b> مَاذَا، مَنْ، كَيْفَ، أَيْنَ.<br>
                • <b>التحويل الصرفي البسيط:</b> تحويل الفعل مع ضمائر المفرد والجمع في الماضي.
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 3:
            st.markdown("<h3 style='color: #10AC84; text-align: center;'>🎯 دروس السنة الثالثة: مغامرة أقسام الكلمة</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #1DD1A1;">
                <p class="story-text">
                • <b>أقسام الكلمة بالتفصيل:</b> الاسم، الفعل، الحرف.<br>
                • <b>أنواع الفعل:</b> الماضي، المضارع، الأمر.<br>
                • <b>الجملة وعناصرها:</b> الجملة الاسمية والجملة الفعلية.<br>
                • <b>حروف الجر وحروف العطف:</b> (في، إلى، على / و، ف، ثم).
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 4:
            st.markdown("<h3 style='color: #FF9F43; text-align: center;'>🎯 دروس السنة الرابعة: حصن المرفوعات والمنصوبات</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #FECA57;">
                <p class="story-text">
                • <b>أركان الجملة الفِعلية:</b> الفعل والفاعل والمفعول به وعلامات الإعراب.<br>
                • <b>أركان الجملة الاسْمية:</b> المبتدأ والخبر وعلامة الرفع بالضمة.<br>
                • <b>الصفة والموصوف:</b> كيف تتبع الصفة الموصوف في التذكير والتأنيث.<br>
                • <b>المضاف والمضاف إليه:</b> التعرف على الاسم المجرور المضاف.
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 5:
            st.markdown("<h3 style='color: #9B59B6; text-align: center;'>🎯 دروس السنة الخامسة: أسرار النواسخ والمثنى والجمع</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #8E44AD;">
                <p class="story-text">
                • <b>النواسخ الفِعلية والحرفية:</b> كَانَ وأخواتها، إِنَّ وأخواتها وتأثيرها على الجمل.<br>
                • <b>علامات الإعراب الفرعية:</b> المثنى (الألف والياء)، وجمع المذكر السالم (الواو والياء).<br>
                • <b>الأسماء الخمسة:</b> (أبو، أخو...) وعلامات إعرابها الخاصة.<br>
                • <b>المفاعيل:</b> المفعول المطلق، والمفعول لأجله.
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 6:
            st.markdown("<h3 style='color: #D35400; text-align: center;'>🎯 دروس السنة السادسة: إتقان التراكيب والصرف المتقدم</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #E67E22;">
                <p class="story-text">
                • <b>إعراب الفعل المضارع:</b> رفعه، جَزمه (أدوات الجزم)، ونصبه (أدوات النصب).<br>
                • <b>الأفعال الخمسة:</b> ثبوت النون وحذفها.<br>
                • <b>المجرد والمزيد من الأفعال:</b> ميزان الصرف الاستكشافي.<br>
                • <b>المنصوبات المتقدمة:</b> الحال والجملة الحالية، والتمييز (الملفوظ والملحوظ).
                </p>
            </div>
            """, unsafe_allow_html=True)


# ------------------------------------------
# و. لوحة إنجازات بطل العلم (لوحة الأوسمة)
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
                badge_1_html = """
                <div class="badge-card" style="border-color: #FF4757; background-color: #FFF5F5;">
                    <div class="badge-icon">🦁</div>
                    <div class="badge-name" style="color: #FF4757;">وسام بطل الكلمات</div>
                    <div class="badge-desc">مُنح لك لتعرفك على الاسم والفعل والحرف مع سمسم!</div>
                </div>
                """
                st.markdown(badge_1_html, unsafe_allow_html=True)
            else:
                badge_1_lock = """
                <div class="badge-card" style="border-color: #CCCCCC; opacity: 0.5;">
                    <div class="badge-icon">🔒</div>
                    <div class="badge-name" style="color: #888888;">وسام الكلمات مغلق</div>
                    <div class="badge-desc">أكمل مغامرة الأرنب سمسم لفتح هذا الوسام.</div>
                </div>
                """
                st.markdown(badge_1_lock, unsafe_allow_html=True)
                
        with b_col2:
            if st.session_state.score_lesson2 == True:
                badge_2_html = """
                <div class="badge-card" style="border-color: #2E86DE; background-color: #F0F7FF;">
                    <div class="badge-icon">🏰</div>
                    <div class="badge-name" style="color: #2E86DE;">وسام حارس القلعة</div>
                    <div class="badge-desc">مُنح لك لنجاحك في عبور بوابات الجملة الاسمية والفعلية!</div>
                </div>
                """
                st.markdown(badge_2_html, unsafe_allow_html=True)
            else:
                badge_2_lock = """
                <div class="badge-card" style="border-color: #CCCCCC; opacity: 0.5;">
                    <div class="badge-icon">🔒</div>
                    <div class="badge-name" style="color: #888888;">وسام القلعة مغلق</div>
                    <div class="badge-desc">افتح بوابات القلعة اللغوية لفتح هذا الوسام.</div>
                </div>
                """
                st.markdown(badge_2_lock, unsafe_allow_html=True)
                
        with b_col3:
            if st.session_state.score_lesson3 == True:
                badge_3_html = """
                <div class="badge-card" style="border-color: #10AC84; background-color: #F0FDF4;">
                    <div class="badge-icon">🕵️‍♂️</div>
                    <div class="badge-name" style="color: #10AC84;">وسام المحقق الذكي</div>
                    <div class="badge-desc">مُنح لك لمساعدتك المحقق كانمون في حل لغز المفعول به!</div>
                </div>
                """
                st.markdown(badge_3_html, unsafe_allow_html=True)
            else:
                badge_3_lock = """
                <div class="badge-card" style="border-color: #CCCCCC; opacity: 0.5;">
                    <div class="badge-icon">🔒</div>
                    <div class="badge-name" style="color: #888888;">وسام المحقق مغلق</div>
                    <div class="badge-desc">حل قضية الكلمة المنصوبة لفتح هذا الوسام.</div>
                </div>
                """
                st.markdown(badge_3_lock, unsafe_allow_html=True)

    with col_gauge:
        gauge_html = f"""
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
        """
        st.markdown(gauge_html, unsafe_allow_html=True)

    welcome_banner_html = """
    <div class="welcome-banner">
        <p style="color: #2C3E50; font-size: 20px; font-weight: 900; margin: 0; text-align: center;">
            🦉 أهلاً بك يا <b>أحمد</b>، صديقك بَهِيّ يتابع نمو شجرة معرفتك الذكية خطوة بخطوة!
        </p>
    </div>
    """
    st.markdown(welcome_banner_html, unsafe_allow_html=True)
    
    if pourcentage_connaissance == 100:
        st.balloons()
        st.success("🏆 أشرقت شجرة معرفتك بالكامل يا بطل القواعد المستقبلي! أنت مذهل!")

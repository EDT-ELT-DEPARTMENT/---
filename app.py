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
# ب. المغامرة الأولى : أقسام الكلمة
# ------------------------------------------
elif st.session_state.page == "lesson1":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_1"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #FF4757; text-align: center; font-weight: 900;'>🎬 قصة متحركة: الأرنب السريع سمسم</h2>", unsafe_allow_html=True)
    
    html_story_1 = """
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
    """
    st.markdown(html_story_1, unsafe_allow_html=True)
    
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
            
    # عزل مخرجات النصوص لحل مشاكل علامات الاقتباس نهائياً
    txt_success_l1 = "🎉 ممتاز يا بطل! (يَقْفِزُ) حركة ونشاط، إذن هي فعل! سمسم سعيد بالجزرة الآن 🥕!"
    txt_wrong_l1 = "🧐 ركز جيداً! الأرنب يقوم بحركة ممتعة (القفز)، إذن الكلمة تعبر عن حركة وفعل!"

    if st.session_state.ans_lesson1 == "correct":
        st.success(txt_success_l1)
    elif st.session_state.ans_lesson1 == "wrong":
        st.warning(txt_wrong_l1)


# ------------------------------------------
# ج. المغامرة الثانية : الجملة الاسمية والفعلية
# ------------------------------------------
elif st.session_state.page == "lesson2":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_2"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #2E86DE; text-align: center; font-weight: 900;'>🎬 قصة متحركة: حراس قلعة الجمل</h2>", unsafe_allow_html=True)
    
    html_story_2 = """
    <div class="cartoon-box">
        <div class="story-title" style="color: #2E86DE;">🏰 بوابات الحصن اللغوي</div>
        <p class="story-text">
        وقف الأبطال أمام قلعة القواعد الضخمة! وعلى البوابة يقف حارسان شجاعان لحمايتها:<br><br>
        👑 <b>الحارس الأول (الجملة الاسمية):</b> يصرخ ويقول: أنا أبدأ دائماً بـ <b>اسم</b> صريح، وعندي ركنان هما المبتدأ والخبر (مثل: <i>العِلْمُ نُورٌ</i>).<br>
        ⚔️ <b>الحارس الثاني (الجملة الفعلية):</b> يلوح بسيفه ويقول: أنا أبدأ دائماً بـ <b>فعل</b> قوي يدل على حركة ونشاط (مثل: <i>تُمطِرُ السَّمَاءُ</i>).
        </p>
    </div>
    """
    st.markdown(html_story_2, unsafe_allow_html=True)
    
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
            
    txt_success_l2 = "🎉 واو! الإجابة صحيحة لأن جملة 'تُمطِرُ السَّمَاءُ' تبدأ بفعل مضارع. انفتحت بوابة القلعة السحرية 🔑!"
    txt_wrong_l2 = "❌ الحارس يرفض العبور! انظر للكلمة الأولى 'تُمطِرُ'.. هل هي اسم أم شيء يحدث الآن (فعل)؟"

    if st.session_state.ans_lesson2 == "correct":
        st.success(txt_success_l2)
    elif st.session_state.ans_lesson2 == "wrong":
        st.warning(txt_wrong_l2)


# ------------------------------------------
# د. المغامرة الثالثة : لغز المفعول به (تم إصلاح وعزل التنبيهات هنا بالكامل)
# ------------------------------------------
elif st.session_state.page == "lesson3":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_3"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #10AC84; text-align: center; font-weight: 900;'>🎬 قصة متحركة: قضية المحقق كَانَمُون</h2>", unsafe_allow_html=True)
    
    html_story_3 = """
    <div class="cartoon-box">
        <div class="story-title" style="color: #10AC84;">🔍 لغز الكلمة المفقودة</div>
        <p class="story-text">
        🕵️‍♂️ المحقق الذكي <b>كَانَمُون</b> يمسك بعدسته ويبحث عن سر اختفاء كلمة وقع عليها الفعل المذكور!<br>
        قال: لدينا الفعل (قَرَأَ) والفاعل الذي قام بالعمل وهو (الطِّفْلُ).. لكن ماذا قرأ الطفل؟! <br><br>
        🎯 وفجأة ظهر <b>المَفْعُولُ بِهِ</b> وهو يضحك ويقول: أنا الاسم المنصوب بالفتحة، وأنا الذي وقع عليّ فعل الفاعل! لمعرفتي دائماً اسأل الفاعل بـ: <b>مَاذَا؟</b> (مثل: قَرَأَ الطِّفْلُ <u>قِصَّةً</u>).
        </p>
    </div>
    """
    st.markdown(html_story_3, unsafe_allow_html=True)
    
    st.write("### 🎮 ساعد المحقق في حل القضية واقبض على المفعول به:")
    
    texte_phrase_test = "الجملة هي: « قَرَأَ الطِّفْلُ قِصَّةً جَمِيلَةً »"
    st.markdown(f"<h2 style='text-align: center; color: white; background: #10AC84; padding: 15px; border-radius: 20px;'>{texte_phrase_test}</h2>", unsafe_allow_html=True)
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
            
    # الحل الجذري والنهائي هنا: عزل نصوص التنبيهات بالكامل في متغيرات منفصلة
    txt_success_l3 = "🎯 قضية ناجحة! 'قِصَّةً' هي الإجابة عن سؤال (ماذا قرأ الطفل؟)، مفعول به منصوب بالفتحة!"
    txt_wrong_verb_l3 = "❌ لا يا سيادة المحقق! 'قَرَأَ' هو الفعل وعملية القراءة نفسها وليس الركن المنصوب."
    txt_wrong_subj_l3 = "❌ ركز! 'الطِّفْلُ' هو الفاعل البطل الذي قرأ القصة وليس المفعول به."

    if st.session_state.ans_lesson3 == "m":
        st.success(txt_success_l3)
    elif st.session_state.ans_lesson3 == "v":
        st.warning(txt_wrong_verb_l3)
    elif st.session_state.ans_lesson3 == "f":
        st.warning(txt_wrong_subj_l3)


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
                    <div class="badge-

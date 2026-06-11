import streamlit as st
import os

# 1. إعدادات الصفحة العامة للمنصة
st.set_page_config(
    page_title="قصتي دراستي - عالم القواعد السحري",
    page_icon="🎨",
    layout="centered"
)

# 2. تصميم CSS مستقر وتفاعلي (يدعم الرؤية الكاملة واللغة العربية RTL)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* ضبط الخطوط والاتجاه من اليمين إلى اليسار لجميع العناصر */
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, span, label {
        font-family: 'Cairo', sans-serif !important;
        direction: RTL;
        text-align: right;
    }
    
    /* خلفية كرتونية مبهجة ومستقرة */
    .stApp {
        background: linear-gradient(135deg, #FFF9E6 0%, #E3F2FD 50%, #E8F5E9 100%);
    }
    
    /* تصميم الأزرار التفاعلية بشكل بارز ومضمون الظهور */
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
    }
    
    /* إطار القصص والرسوم المتحركة التفاعلية */
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

    /* لوحة الأوسمة والإنجازات */
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
    
    .badge-icon { font-size: 65px; margin-bottom: 10px; }
    .badge-name { font-size: 22px; font-weight: 900; margin-bottom: 8px; text-align: center; color: #FF9F43; }
    .badge-desc { color: #57606F; font-size: 15px; font-weight: 700; text-align: center; }
    
    .gauge-container {
        background: linear-gradient(180deg, #FFFFFF, #E8F5E9);
        border: 3px solid #10AC84;
        border-radius: 25px;
        padding: 20px;
        text-align: center;
    }
    
    .welcome-banner {
        background: linear-gradient(135deg, #FFF9E6, #FFF2CC);
        border: 3px solid #FFA801;
        border-radius: 35px;
        padding: 15px 30px;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة حالة الصفحات (Session State) لضمان التفاعلية وثبات المحتوى
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "ans_lesson1" not in st.session_state:
    st.session_state.ans_lesson1 = None
if "ans_lesson2" not in st.session_state:
    st.session_state.ans_lesson2 = None
if "ans_lesson3" not in st.session_state:
    st.session_state.ans_lesson3 = None

# 4. دالة عرض الشعار في الأعلى
def afficher_logo_haut():
    if os.path.exists("logo.jpeg"):
        col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
        with col_l2:
            st.image("logo.jpeg", use_column_width=True)

# --- نظام التنقل والصفحات التفاعلية ---

# أولاً: القائمة الرئيسية (تظهر الآن فوراً وبشكل ملون كامل)
if st.session_state.page == "menu":
    afficher_logo_haut()
    st.markdown("<h1 style='text-align: center; color: #FF6B6B; font-size: 42px; font-weight: 900;'>🎈 عَالَمُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #57606F; font-weight: bold;'>مرحباً بك يا بطل القواعد! اختر مغامرتك التفاعلية اليوم:</h3>", unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌟 مغامرة أقسام الكلمة\n(مع الأرنب سمسم 🥕)", key="btn_l1"):
            st.session_state.page = "lesson1"
            st.session_state.ans_lesson1 = None
            st.rerun()
            
    with col2:
        if st.button("🏰 حصن الجملة الاسمية والفعلية\n(تحدي حراس القلعة 👑)", key="btn_l2"):
            st.session_state.page = "lesson2"
            st.session_state.ans_lesson2 = None
            st.rerun()
            
    st.write("")
    col3, col4 = st.columns([1.4, 1])
    with col3:
        if st.button("🕵️‍♂️ لغز المفعول به والمنصوبات\n(عدسة المحقق كَانَمُون 🔍)", key="btn_l3"):
            st.session_state.page = "lesson3"
            st.session_state.ans_lesson3 = None
            st.rerun()
            
    with col4:
        if st.button("🏆 لوحة الأوسمة والأرباح", key="btn_rew"):
            st.session_state.page = "لوحة_الإنجازات"
            st.rerun()

# ثانياً: الدرس الأول - أقسام الكلمة
elif st.session_state.page == "lesson1":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_1"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #FF4757; text-align: center; font-weight: 900;'>🎬 دروس قواعد تفاعلية: الأرنب السريع سمسم</h2>", unsafe_allow_html=True)
    
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
        if st.button("اسْم 🦁", key="opt_1"): st.session_state.ans_lesson1 = "wrong"
    with c2:
        if st.button("فِعْل 🏃‍♂️", key="opt_2"): st.session_state.ans_lesson1 = "correct"
    with c3:
        if st.button("حَرْف 📦", key="opt_3"): st.session_state.ans_lesson1 = "wrong"
            
    if st.session_state.ans_lesson1 == "correct":
        st.success("🎉 ممتاز يا بطل! (يَقْفِزُ) حركة ونشاط، إذن هي فعل! سمسم سعيد بالجزرة الآن 🥕!")
    elif st.session_state.ans_lesson1 == "wrong":
        st.warning("🧐 ركز جيداً! الأرنب يقوم بحركة ممتعة (القفز)، إذن الكلمة تعبر عن حركة وفعل!")

# ثالثاً: الدرس الثاني - الجملة الاسمية والفعلية
elif st.session_state.page == "lesson2":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_2"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #2E86DE; text-align: center; font-weight: 900;'>🎬 دروس قواعد تفاعلية: حراس قلعة الجمل</h2>", unsafe_allow_html=True)
    
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
        if st.button("جملة اسمية 👑", key="opt_p1"): st.session_state.ans_lesson2 = "wrong"
    with col_b2:
        if st.button("جملة فعلية ⚔️", key="opt_p2"): st.session_state.ans_lesson2 = "correct"
            
    if st.session_state.ans_lesson2 == "correct":
        st.success("🎉 واو! الإجابة صحيحة لأن جملة 'تُمطِرُ السَّمَاءُ' تبدأ بفعل مضارع. انفتحت بوابة القلعة السحرية 🔑!")
    elif st.session_state.ans_lesson2 == "wrong":
        st.warning("❌ الحارس يرفض العبور! انظر للكلمة الأولى 'تُمطِرُ'.. هل هي اسم أم شيء يحدث الآن (فعل)؟")

# رابعاً: الدرس الثالث - المفعول به والمنصوبات
elif st.session_state.page == "lesson3":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_3"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #10AC84; text-align: center; font-weight: 900;'>🎬 دروس قواعد تفاعلية: قضية المحقق كَانَمُون</h2>", unsafe_allow_html=True)
    
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
        if st.button("قَرَأَ 📖", key="ca1"): st.session_state.ans_lesson3 = "v"
    with ca2:
        if st.button("الطِّفْلُ 🧒", key="ca2"): st.session_state.ans_lesson3 = "f"
    with ca3:
        if st.button("قِصَّةً 📚", key="ca3"): st.session_state.ans_lesson3 = "m"
            
    if st.session_state.ans_lesson3 == "m":
        st.success("🎯 قضية ناجحة! 'قِصَّةً' هي الإجابة عن سؤال (ماذا قرأ الطفل؟)، مفعول به منصوب بالفتحة!")
    elif st.session_state.ans_lesson3 == "v":
        st.warning("❌ لا يا سيادة المحقق! 'قَرَأَ' هو الفعل وعملية القراءة نفسها وليس الركن المنصوب.")
    elif st.session_state.ans_lesson3 == "f":
        st.warning("❌ ركز! 'الطِّفْلُ' هو الفاعل البطل الذي قرأ القصة وليس المفعول به.")

# خامساً: لوحة الإنجازات
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
            <div style="color: #2F3542; font-size: 16px; font-weight: 900; text-align:center;">شجرة نمو<br>المعرفة</div>
            <div style="margin: 20px 0; font-size: 26px; text-align:center; line-height:1.4;">🍁<br>🍂<br>🍃<br>🌿</div>
            <div style="background-color: #2ED573; border-radius: 15px; padding: 10px; font-weight: 900; color: white; font-size: 20px; text-align: center;">75%</div>
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

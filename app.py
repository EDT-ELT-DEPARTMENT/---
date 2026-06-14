import streamlit as st
import os
import sqlite3
import hashlib

# 1. إعداد قاعدة البيانات
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, nom TEXT, prenom TEXT)')
conn.commit()

# وظائف تشفير كلمة المرور
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return True
    return False

# 2. إعداد الصفحة الأساسي
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", layout="wide")

# 3. تهيئة الحالة (Session State)
if "connecte" not in st.session_state:
    st.session_state.connecte = False
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
if "نقاط" not in st.session_state:
    st.session_state.نقاط = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# 4. وظيفة تسجيل الدخول أو إنشاء حساب
def afficher_login():
    st.markdown("<h2 style='text-align: center;'>🔐 الدخول للمنصة</h2>", unsafe_allow_html=True)
    menu = ["دخول", "إنشاء حساب", "استعادة كلمة المرور"]
    choice = st.sidebar.selectbox("العمليات", menu)

    if choice == "دخول":
        email = st.text_input("البريد الإلكتروني:")
        password = st.text_input("كلمة المرور:", type="password")
        
        if st.button("دخول"):
            # منطق دخول الأدمن المباشر
            if email == "abboumajda" and password == "iyed2023":
                st.session_state.connecte = True
                st.session_state.nom_eleve = "الأدمن (المعلم)"
                st.rerun()
            else:
                # التحقق من قاعدة البيانات للتلاميذ
                c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, make_hashes(password)))
                user = c.fetchone()
                if user:
                    st.session_state.connecte = True
                    st.session_state.nom_eleve = f"{user[3]} {user[2]}"
                    st.rerun()
                else:
                    st.error("البريد أو كلمة المرور خطأ!")

    elif choice == "إنشاء حساب":
        nom = st.text_input("الاسم:")
        prenom = st.text_input("اللقب:")
        email = st.text_input("البريد الإلكتروني:")
        password = st.text_input("كلمة المرور:", type="password")
        if st.button("تسجيل"):
            try:
                c.execute('INSERT INTO users VALUES (?,?,?,?)', (email, make_hashes(password), prenom, nom))
                conn.commit()
                st.success("تم إنشاء الحساب بنجاح!")
            except:
                st.error("هذا الإيميل موجود مسبقاً!")

    elif choice == "استعادة كلمة المرور":
        email = st.text_input("أدخل بريدك لاستعادة كلمة المرور:")
        if st.button("استعادة"):
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = c.fetchone()
            if user:
                st.info(f"كلمة المرور المسجلة مرتبطة بحسابك. تواصل مع الإدارة.")
            else:
                st.error("الإيميل غير مسجل.")

# 5. قاموس الألعاب
محتوى_الألعاب = {
    "أقسام الكلمة": {
        1: {"سؤال": "ما هو نوع كلمة 'قلم'؟", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"},
        2: {"سؤال": "ما هو نوع كلمة 'يذهب'؟", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "فعل"}
    },
    "الجملة الاسمية والفعلية": {
        1: {"سؤال": "الجملة الاسمية تبدأ بـ:", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"},
        2: {"سؤال": "الجملة الفعلية تبدأ بـ:", "خيارات": ["اسم", "فعل", "حرف"], "إجابة": "فعل"}
    }
}

# 6. الدوال الوظيفية
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 10, 1])
        with col2:
            st.image("logo.jpeg", width=1000)

def تشغيل_لعبة_الدرس(اسم_الدرس, مستوى_السنة):
    data = محتوى_الألعاب.get(اسم_الدرس, {}).get(مستوى_السنة)
    if data:
        st.markdown(f"### 🎮 تحدي: {data['سؤال']}")
        choix = st.radio("اختر الإجابة:", data['خيارات'], key=f"radio_{اسم_الدرس}_{مستوى_السنة}")
        if st.button("تحقق من إجابتي!", key=f"btn_check_{اسم_الدرس}_{مستوى_السنة}"):
            if choix == data['إجابة']:
                st.session_state.نقاط[مستوى_السنة] += 10
                st.success(f"🎉 إجابة صحيحة!")
                st.balloons()
            else:
                st.error("❌ إجابة خاطئة. حاول مرة أخرى!")
    else:
        st.warning("⚠️ اللعبة لهذا المستوى قيد التطوير.")

def عرض_محتوى_الدرس(اسم_الدرس):
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة", key=f"back_{اسم_الدرس}"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown(f"<h2 style='text-align: center;'>{اسم_الدرس}</h2>", unsafe_allow_html=True)
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5], key=f"select_{اسم_الدرس}")
    تشغيل_لعبة_الدرس(اسم_الدرس, annee)
    st.markdown("</div>", unsafe_allow_html=True)

def afficher_page_hamza():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    head_col1, head_col2 = st.columns([4, 1])
    with head_col1:
        st.markdown("<h2 style='margin-top: 50px;'>✍️ قواعدي في قصتي (الهمزة)</h2>", unsafe_allow_html=True)
    with head_col2:
        st.markdown("<div style='font-size: 70px; text-align: center;'>📝</div>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 قصة صراع الحركات", "✍️ قواعد الهمزة"])
    with tab1:
        st.markdown("<h3 style='text-align: center;'>📖 قصة: صراع الحركات في مدينة الهمزة</h3>", unsafe_allow_html=True)
        st.write("في مدينةِ الحروف، كانت الهمزةُ المتوسطة تعيشُ في حيرةٍ من أمرها، فهي لا تعرفُ أين تجلس! قررَت الحركاتُ أن تقيمَ مسابقةً لتعرفَ من هي الأقوى لتفوز بكرسي الهمزة.")
        st.markdown("### 💡 سلم قوة الحركات (نظام الفوز):")
        st.write("🥇 **الكسرة:** تجلس على النبرة (ئـ)")
        st.write("🥈 **الضمة:** تجلس على الواو (ؤ)")
        st.write("🥉 **الفتحة:** تجلس على الألف (أ)")
        st.write("🏅 **السكون:** تجلس على السطر (ء)")
        st.markdown("---")
        st.write("### 🥊 ابدأ الصراع بنفسك!")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("الكسرة ضد الضمة"):
                st.success("الكسرة (ئـ) تهزم الضمة!")
                st.balloons()
        with col_b:
            if st.button("الفتحة ضد السكون"):
                st.success("الفتحة (أ) تهزم السكون!")
                st.snow()
    with tab2:
        st.markdown("<h3 style='text-align: center;'>✍️ قواعد الهمزة للسنة الرابعة</h3>", unsafe_allow_html=True)
        st.write("✅ **1. الهمزة في أول الكلمة:** وصل (ا) أو قطع (أ).")
        st.write("✅ **2. الهمزة المتوسطة:** حسب قوة الحركات.")
        st.write("✅ **3. الهمزة المتطرفة:** حسب حركة ما قبلها.")
    
    st.markdown("---")
    if st.button("⬅ العودة للقائمة", key="back_hamza_btn"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def عرض_سينما_القواعد():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>🎬 سينما القواعد: حارس غابة الكلمات</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=9_6A_M542u8")
    if st.button("⬅ العودة للقائمة", key="back_cinema"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 7. تنسيق CSS
css_style = """
<style>
    html, body, [data-testid="stAppViewContainer"] { direction: rtl !important; }
    .content-card { background-color: rgba(255,255,255,0.95); padding: 40px; border-radius: 30px; color: #333; text-align: justify !important; }
    h1, h2, h3, h4, p, li, div, .stButton { text-align: right !important; }
    p, li, .stMarkdown { font-size: 22px !important; line-height: 1.6 !important; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 8. المنطق الرئيسي
if not st.session_state.connecte:
    afficher_login()
else:
    st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    st.write(f"### أهلاً بك يا بطل/بطلة: {st.session_state.nom_eleve}")
    
    if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
        عرض_الشعار_الكبير()
        c1, c2, c3, c4, c5 = st.columns(5)
        if c1.button("🌟 دروس", key="b1"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
        if c2.button("🏰 حصن", key="b2"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
        if c3.button("✍️ قواعدي في قصتي", key="b4"): st.session_state.الصفحة_الحالية = "Page_Hamza"; st.rerun()
        if c4.button("🎬 سينما", key="b5"): st.session_state.الصفحة_الحالية = "Cinema_Grammaire"; st.rerun()
        if c5.button("🏆 لوحة", key="b3"): st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"; st.rerun()

    elif st.session_state.الصفحة_الحالية == "الدرس_الأول": عرض_محتوى_الدرس("أقسام الكلمة")
    elif st.session_state.الصفحة_الحالية == "الدرس_الثاني": عرض_محتوى_الدرس("الجملة الاسمية والفعلية")
    elif st.session_state.الصفحة_الحالية == "Page_Hamza": afficher_page_hamza()
    elif st.session_state.الصفحة_الحالية == "Cinema_Grammaire": عرض_سينما_القواعد()
    elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
        st.markdown("<div class='content-card'>", unsafe_allow_html=True)
        st.markdown("<h2>🏆 لوحة الإنجازات</h2>", unsafe_allow_html=True)
        for annee, score in st.session_state.نقاط.items():
            badge = "🌟" if score > 0 else "⏳"
            st.write(f"### السنة {annee}: {score} نقطة {badge}")
        if st.button("⬅ العودة", key="back_final"): st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

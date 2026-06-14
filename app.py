import streamlit as st
import os
import sqlite3
import hashlib

# 1. إعداد قاعدة البيانات والأمان
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

# تهيئة جدول المستخدمين
conn = get_db_connection()
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, nom TEXT)')
conn.commit()
conn.close()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return True
    return False

# 2. إعداد الصفحة
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", layout="wide")

# 3. تهيئة الحالة (Session State)
if "connecte" not in st.session_state:
    st.session_state.connecte = False
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
if "نقاط" not in st.session_state:
    st.session_state.نقاط = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# 4. دالة تسجيل الدخول
def afficher_login():
    st.markdown("<h2 style='text-align: center;'>🔐 الدخول للمنصة</h2>", unsafe_allow_html=True)
    menu = ["دخول", "إنشاء حساب"]
    choice = st.sidebar.selectbox("العمليات", menu)

    if choice == "دخول":
        email = st.text_input("البريد الإلكتروني:")
        password = st.text_input("كلمة المرور:", type="password")
        if st.button("دخول"):
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = c.fetchone()
            conn.close()
            if user and check_hashes(password, user[1]):
                st.session_state.connecte = True
                st.success("تم الدخول بنجاح!")
                st.rerun()
            else:
                st.error("البريد أو كلمة المرور غير صحيحة")

    elif choice == "إنشاء حساب":
        nom = st.text_input("الاسم الكامل:")
        email = st.text_input("البريد الإلكتروني:")
        password = st.text_input("كلمة المرور:", type="password")
        if st.button("تسجيل"):
            try:
                conn = get_db_connection()
                c = conn.cursor()
                c.execute('INSERT INTO users VALUES (?,?,?)', (email, make_hashes(password), nom))
                conn.commit()
                conn.close()
                st.success("تم إنشاء الحساب! يمكنك الدخول الآن.")
            except:
                st.error("هذا البريد موجود مسبقاً!")

# 5. الدوال الأساسية للمنصة
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 10, 1])
        with col2:
            st.image("logo.jpeg", width=1000)

def تشغيل_لعبة_الدرس(اسم_الدرس, مستوى_السنة):
    # محتوى الألعاب (تم وضعه هنا لتقليل التكرار)
    محتوى_الألعاب = {
        "أقسام الكلمة": {1: {"سؤال": "ما هو نوع كلمة 'قلم'؟", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"}},
        "الجملة الاسمية والفعلية": {1: {"سؤال": "الجملة الاسمية تبدأ بـ:", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"}}
    }
    data = محتوى_الألعاب.get(اسم_الدرس, {}).get(مستوى_السنة)
    if data:
        st.markdown(f"### 🎮 تحدي: {data['سؤال']}")
        choix = st.radio("اختر الإجابة:", data['خيارات'], key=f"radio_{اسم_الدرس}_{مستوى_السنة}")
        if st.button("تحقق من إجابتي!", key=f"btn_check_{اسم_الدرس}_{مستوى_السنة}"):
            if choix == data['إجابة']:
                st.session_state.نقاط[مستوى_السنة] += 10
                st.success("🎉 إجابة صحيحة!")
            else:
                st.error("❌ إجابة خاطئة!")

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
    tab1, tab2 = st.tabs(["📖 قصة صراع الحركات", "✍️ قواعد الهمزة"])
    with tab1:
        st.markdown("<h2 style='text-align: center;'>📖 قصة: صراع الحركات في مدينة الهمزة</h2>", unsafe_allow_html=True)
        st.write("قصة الهمزة المتوسطة تعتمد على قوة الحركات: الكسرة ثم الضمة ثم الفتحة.")
    with tab2:
        st.markdown("<h2 style='text-align: center;'>✍️ قواعد الهمزة للسنة الرابعة</h2>", unsafe_allow_html=True)
        st.write("قواعد الهمزة في أول ووسط وآخر الكلمة.")
    
    if st.button("⬅ العودة للقائمة", key="back_hamza_btn"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def عرض_سينما_القواعد():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>🎬 سينما القواعد</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=9_6A_M542u8")
    if st.button("⬅ العودة", key="back_cinema"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 6. التنسيق
css_style = """
<style>
    html, body, [data-testid="stAppViewContainer"] { direction: rtl !important; }
    .content-card { background-color: rgba(255,255,255,0.95); padding: 40px; border-radius: 30px; color: #333; text-align: justify !important; }
    h1, h2, h3, h4, p, li, div, .stButton { text-align: right !important; }
    p, li, .stMarkdown { font-size: 22px !important; line-height: 1.6 !important; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 7. المنطق الرئيسي (حماية المحتوى)
if not st.session_state.connecte:
    afficher_login()
else:
    st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    if st.sidebar.button("تسجيل الخروج"):
        st.session_state.connecte = False
        st.rerun()
        
    if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
        عرض_الشعار_الكبير()
        c1, c2, c3, c4, c5 = st.columns(5)
        if c1.button("🌟 دروس"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
        if c2.button("🏰 حصن"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
        if c3.button("✍️ قواعدي"): st.session_state.الصفحة_الحالية = "Page_Hamza"; st.rerun()
        if c4.button("🎬 سينما"): st.session_state.الصفحة_الحالية = "Cinema_Grammaire"; st.rerun()
        if c5.button("🏆 لوحة"): st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"; st.rerun()
    elif st.session_state.الصفحة_الحالية == "الدرس_الأول": عرض_محتوى_الدرس("أقسام الكلمة")
    elif st.session_state.الصفحة_الحالية == "الدرس_الثاني": عرض_محتوى_الدرس("الجملة الاسمية والفعلية")
    elif st.session_state.الصفحة_الحالية == "Page_Hamza": afficher_page_hamza()
    elif st.session_state.الصفحة_الحالية == "Cinema_Grammaire": عرض_سينما_القواعد()

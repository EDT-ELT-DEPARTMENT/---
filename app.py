import streamlit as st
import os
import sqlite3
import hashlib

# 1. إعداد قاعدة البيانات
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

# تهيئة الجدول عند بداية التشغيل
conn = get_db_connection()
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, nom TEXT, prenom TEXT, paye INTEGER)')
try:
    c.execute('ALTER TABLE users ADD COLUMN paye INTEGER DEFAULT 0')
    conn.commit()
except sqlite3.OperationalError:
    pass
conn.close()

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
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# 4. وظيفة تسجيل الدخول أو إنشاء حساب
def afficher_login():
    st.markdown("<h2 style='text-align: center;'>🔐 الدخول للمنصة</h2>", unsafe_allow_html=True)
    menu = ["دخول", "إنشاء حساب", "استعادة كلمة المرور"]
    choice = st.sidebar.selectbox("العمليات", menu)

    if choice == "دخول":
        email = st.text_input("إسم المستخدم:")
        password = st.text_input("كلمة المرور:", type="password")
        
        if st.button("دخول"):
            if email == "chef.department.elt.fge@gmail.com" and password == "123456":
                st.session_state.connecte = True
                st.session_state.is_admin = True
                st.session_state.nom_eleve = "الأدمن (المعلم)"
                st.rerun()
            else:
                conn = get_db_connection()
                c = conn.cursor()
                c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, make_hashes(password)))
                user = c.fetchone()
                conn.close()
                if user:
                    st.session_state.connecte = True
                    st.session_state.is_admin = False
                    st.session_state.email_user = email
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
                conn = get_db_connection()
                c = conn.cursor()
                c.execute('INSERT INTO users VALUES (?,?,?,?,?)', (email, make_hashes(password), prenom, nom, 0))
                conn.commit()
                conn.close()
                st.success("تم إنشاء الحساب بنجاح! بانتظار تفعيل الإدارة.")
            except:
                st.error("هذا الإيميل موجود مسبقاً!")

    elif choice == "استعادة كلمة المرور":
        email = st.text_input("أدخل بريدك لاستعادة كلمة المرور:")
        if st.button("استعادة"):
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = c.fetchone()
            conn.close()
            if user:
                st.info(f"كلمة المرور المسجلة مرتبطة بحسابك. تواصل مع الإدارة.")
            else:
                st.error("الإيميل غير مسجل.")

# 5. دوال العرض والمنطق (كما هي تماماً)
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 10, 1])
        with col2:
            st.image("logo.jpeg", width=1000)

def admin_panel():
    st.markdown("## 🛠 لوحة تحكم الأدمن")
    email_to_activate = st.text_input("إيميل التلميذ لتفعيله:")
    if st.button("تفعيل الحساب (الدفع)"):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('UPDATE users SET paye = 1 WHERE email = ?', (email_to_activate,))
        conn.commit()
        conn.close()
        st.success(f"تم تفعيل الحساب بنجاح لـ: {email_to_activate}")
    if st.button("خروج من لوحة التحكم"):
        st.session_state.connecte = False
        st.session_state.is_admin = False
        st.rerun()

# 8. تنسيق CSS
css_style = """
<style>
    html, body, [data-testid="stAppViewContainer"] { direction: rtl !important; }
    .content-card { background-color: rgba(255,255,255,0.95); padding: 40px; border-radius: 30px; color: #333; text-align: justify !important; }
    h1, h2, h3, h4, p, li, div, .stButton { text-align: right !important; }
    p, li, .stMarkdown { font-size: 22px !important; line-height: 1.6 !important; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 9. المنطق الرئيسي (بوابة الوصول)
if not st.session_state.connecte:
    afficher_login()
else:
    if st.session_state.is_admin:
        admin_panel()
    else:
        if "email_user" in st.session_state:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('SELECT paye FROM users WHERE email = ?', (st.session_state.email_user,))
            result = c.fetchone()
            conn.close()
            
            if result and result[0] == 1:
                # محتوى المنصة للأعضاء
                st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
                # (أضف هنا بقية محتوى القائمة الرئيسية والدوال...)
                if st.button("🚪 تسجيل الخروج"):
                    st.session_state.connecte = False
                    st.rerun()
            else:
                st.warning("⚠️ حسابك غير مفعل.")
                st.markdown("""
                ### 💳 يرجى إتمام عملية الدفع للوصول إلى الدروس:
                * **الاسم:** Abbou Majda
                * **رقم الحساب (CCP):** 10917874
                * **للتفعيل:** أرسل صورة إيصال الدفع عبر الواتساب إلى 0657012174
                """)
                if st.button("🚪 تسجيل الخروج"):
                    st.session_state.connecte = False
                    st.rerun()

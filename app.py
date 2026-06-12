import streamlit as st
import os
import sqlite3
import hashlib
import pandas as pd

# 1. إعداد قاعدة البيانات
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

# إنشاء الجدول إذا لم يكن موجوداً
conn = get_db_connection()
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, nom TEXT, prenom TEXT, paye INTEGER)')

# محاولة إضافة عمود paye إذا كان الجدول قديماً
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
            conn = get_db_connection()
            c = conn.cursor()
            try:
                c.execute('INSERT INTO users VALUES (?,?,?,?,?)', (email, make_hashes(password), nom, prenom, 0))
                conn.commit()
                st.success("تم إنشاء الحساب بنجاح! بانتظار تفعيل الإدارة.")
            except:
                st.error("هذا الإيميل موجود مسبقاً!")
            conn.close()

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
        st.write("في مدينةِ الحروف، كانت الهمزةُ المتوسطة تعيشُ في حيرةٍ من أمرها.")
        st.markdown("### 💡 سلم قوة الحركات:")
        st.write("🥇 **الكسرة:** تجلس على النبرة (ئـ) | 🥈 **الضمة:** تجلس على الواو (ؤ) | 🥉 **الفتحة:** تجلس على الألف (أ) | 🏅 **السكون:** تجلس على السطر (ء)")
        st.markdown("---")
    with tab2:
        st.markdown("<h3 style='text-align: center;'>✍️ قواعد الهمزة للسنة الرابعة</h3>", unsafe_allow_html=True)
        st.write("✅ 1. الهمزة في أول الكلمة: وصل أو قطع. ✅ 2. المتوسطة: حسب قوة الحركات. ✅ 3. المتطرفة: حسب حركة ما قبلها.")
    
    if st.button("⬅ العودة للقائمة", key="back_hamza_btn"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def عرض_سينما_القواعد():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>🎬 سينما القواعد</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=9_6A_M542u8")
    if st.button("⬅ العودة للقائمة", key="back_cinema"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 7. لوحة تحكم الأدمن
def admin_panel():
    st.markdown("## 🛠 لوحة تحكم الأدمن")
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT email, nom, prenom, paye FROM users", conn)
    st.table(df)
    email_to_activate = st.text_input("إيميل التلميذ لتفعيله:")
    if st.button("تفعيل الحساب (الدفع)"):
        c = conn.cursor()
        c.execute('UPDATE users SET paye = 1 WHERE email = ?', (email_to_activate,))
        conn.commit()
        conn.close()
        st.success(f"تم تفعيل الحساب بنجاح لـ: {email_to_activate}")
        st.rerun()
    conn.close()
    if st.button("خروج"):
        st.session_state.connecte = False
        st.session_state.is_admin = False
        st.rerun()

# 8. تنسيق CSS
css_style = """
<style>
    html, body, [data-testid="stAppViewContainer"] { direction: rtl !important; }
    .content-card { background-color: rgba(255,255,255,0.95); padding: 40px; border-radius: 30px; color: #333; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 9. المنطق الرئيسي
if not st.session_state.connecte:
    afficher_login()
else:
    if st.session_state.is_admin:
        admin_panel()
    else:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT paye FROM users WHERE email = ?', (st.session_state.email_user,))
        result = c.fetchone()
        conn.close()
        
        if result and result[0] == 1:
            st.markdown("<h1 style='text-align: center;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ 🎈</h1>", unsafe_allow_html=True)
            if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
                 عرض_الشعار_الكبير()
                 c1, c2, c3, c4, c5 = st.columns(5)
                 if c1.button("🌟 دروس"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
                 if c2.button("🏰 حصن"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
                 if c3.button("✍️ قواعدي"): st.session_state.الصفحة_الحالية = "Page_Hamza"; st.rerun()
                 if c4.button("🎬 سينما"): st.session_state.الصفحة_الحالية = "Cinema_Grammaire"; st.rerun()
            elif st.session_state.الصفحة_الحالية == "الدرس_الأول": عرض_محتوى_الدرس("أقسام الكلمة")
            elif st.session_state.الصفحة_الحالية == "الدرس_الثاني": عرض_محتوى_الدرس("الجملة الاسمية والفعلية")
            elif st.session_state.الصفحة_الحالية == "Page_Hamza": afficher_page_hamza()
            elif st.session_state.الصفحة_الحالية == "Cinema_Grammaire": عرض_سينما_القواعد()
        else:
            st.warning("⚠️ حسابك غير مفعل. يرجى إتمام الدفع وتفعيل الإدارة.")
            if st.button("🚪 تسجيل الخروج"):
                st.session_state.connecte = False
                st.rerun()

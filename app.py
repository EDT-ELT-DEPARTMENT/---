import streamlit as st
import os
import sqlite3
import hashlib
import pandas as pd

# 1. إعداد قاعدة البيانات
# 1. إعداد قاعدة البيانات
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

# تهيئة الجدول وتحديثه
conn = get_db_connection()
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, nom TEXT, prenom TEXT, paye INTEGER, montant REAL)')

# التحقق من وجود الأعمدة وإضافتها إذا كانت مفقودة
try:
    c.execute('ALTER TABLE users ADD COLUMN paye INTEGER DEFAULT 0')
except:
    pass

try:
    c.execute('ALTER TABLE users ADD COLUMN montant REAL DEFAULT 0')
except:
    pass

conn.commit()
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
            if email == "abboumajda1985@gmail.com" and password == "iyed2023":
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
                c.execute('INSERT INTO users VALUES (?,?,?,?,?,?)', (email, make_hashes(password), prenom, nom, 0, 0.0))
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

# 5. دوال العرض والمنطق
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 10, 1])
        with col2:
            st.image("logo.jpeg", width=1000)

def admin_panel():
    st.markdown("## 🛠 لوحة تحكم الأدمن والمالية")
    
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM users", conn)
    conn.close()
    
    st.write("### 📋 قائمة المستخدمين المسجلين:")
    st.dataframe(df)
    
    # تحضير البيانات للتحميل
    csv = df.to_csv(index=False).encode('utf-8')
    
    import io
    # Excel
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Clients')
    excel_data = buffer.getvalue()
    
    # HTML
    html_data = df.to_html(index=False, classes='table table-striped', border=1)

    # وضع الأزرار بشكل أفقي
    st.write("#### 📥 تحميل البيانات:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.download_button(label="📄 تحميل (CSV)", data=csv, file_name='clients.csv', mime='text/csv', key="csv_btn_admin")
    with col2:
        st.download_button(label="📊 تحميل (Excel)", data=excel_data, file_name="clients.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", key="xlsx_btn_admin")
    with col3:
        st.download_button(label="🌐 تحميل (HTML)", data=html_data, file_name="clients.html", mime="text/html", key="html_btn_admin")
    
    st.markdown("---")
    st.write("### ⚙️ تفعيل حساب وتحديث المبلغ:")
    email_to_act = st.text_input("إيميل التلميذ لتفعيله:", key="email_admin_input")
    montant_paye = st.number_input("المبلغ المدفوع (DA):", min_value=0.0, key="amount_admin_input")
    
    if st.button("✅ تأكيد التفعيل والمبلغ", key="confirm_admin_btn"):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('UPDATE users SET paye = 1, montant = ? WHERE email = ?', (montant_paye, email_to_act))
        conn.commit()
        conn.close()
        st.success(f"تم تحديث بيانات التلميذ: {email_to_act}")
        st.rerun()
        
    if st.button("🚪 خروج", key="logout_admin_btn"):
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

# --- دالة عرض الصفحة ---
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
                # 1. عرض الترحيب والخروج
                col_header, col_logout = st.columns([6, 1])
                with col_header:
                    st.markdown("<h1 style='text-align: center; color: blue;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
                with col_logout:
                    if st.button("🚪 تسجيل الخروج"):
                        st.session_state.connecte = False
                        st.rerun()

                # 2. نظام التنقل بين الصفحات (هذا هو الجزء المسؤول عن عدم ظهور الصفحة فارغة)
                if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
                    st.write(f"### أهلاً بك يا بطل: {st.session_state.nom_eleve}")
                    عرض_الشعار_الكبير() # تأكد من أن هذه الدالة معرفة في كودك
                    
                    # الأزرار التي تنقل العميل للصفحات
                    c1, c2, c3, c4, c5 = st.columns(5)
                    if c1.button("🌟 دروس"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
                    if c2.button("🏰 حصن"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
                    if c3.button("✍️ قواعدي"): st.session_state.الصفحة_الحالية = "Page_Hamza"; st.rerun()
                    if c4.button("🎬 سينما"): st.session_state.الصفحة_الحالية = "Cinema_Grammaire"; st.rerun()
                    if c5.button("🏆 لوحة"): st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"; st.rerun()

                # 3. عرض محتوى الصفحة المختارة
                elif st.session_state.الصفحة_الحالية == "الدرس_الأول":
                    st.write("### محتوى الدرس الأول")
                    # أضف هنا استدعاء دالة الدرس الخاص بك
                
                elif st.session_state.الصفحة_الحالية == "Page_Hamza":
                    afficher_page_hamza() # الدالة التي صححناها سابقاً
                
                # إضافة زر عودة في الصفحات الفرعية
                if st.session_state.الصفحة_الحالية != "القائمة_الرئيسية":
                    if st.button("⬅ العودة للرئيسية"):
                        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
                        st.rerun()
            

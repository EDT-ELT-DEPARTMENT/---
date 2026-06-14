import streamlit as st
import os
import sqlite3
import hashlib
import pandas as pd
import io

# 1. إعداد قاعدة البيانات
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

# تهيئة الجدول وتحديثه
conn = get_db_connection()
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, nom TEXT, prenom TEXT, paye INTEGER, montant REAL)')
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

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# 2. إعداد الصفحة
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", layout="wide")

# 3. تهيئة الحالة
if "connecte" not in st.session_state:
    st.session_state.connecte = False
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# 4. دوال العرض
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

def afficher_page_hamza():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>✍️ قواعدي في قصتي (الهمزة)</h2>", unsafe_allow_html=True)
    st.write("### 📖 قصة: صراع الحركات في مدينة الهمزة")
    st.write("في مدينةِ الحروف، كانت الهمزةُ المتوسطة تعيشُ في حيرةٍ من أمرها...")
    if st.button("⬅ العودة للقائمة", key="back_hamza_btn"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def admin_panel():
    st.markdown("## 🛠 لوحة تحكم الأدمن والمالية")
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM users", conn)
    conn.close()
    st.write("### 📋 قائمة المستخدمين:")
    st.dataframe(df)
    
    csv = df.to_csv(index=False).encode('utf-8')
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Clients')
    excel_data = buffer.getvalue()
    html_data = df.to_html(index=False)
    
    col1, col2, col3 = st.columns(3)
    col1.download_button("📄 CSV", csv, 'c.csv', 'text/csv', key="c1")
    col2.download_button("📊 Excel", excel_data, 'c.xlsx', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', key="c2")
    col3.download_button("🌐 HTML", html_data, 'c.html', 'text/html', key="c3")
    
    email_to_act = st.text_input("إيميل لتفعيله:")
    montant_paye = st.number_input("المبلغ:", min_value=0.0)
    if st.button("✅ تأكيد التفعيل"):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('UPDATE users SET paye = 1, montant = ? WHERE email = ?', (montant_paye, email_to_act))
        conn.commit()
        conn.close()
        st.rerun()

    if st.button("🚪 خروج"):
        st.session_state.connecte = False
        st.session_state.is_admin = False
        st.rerun()

# 9. المنطق الرئيسي
# 9. المنطق الرئيسي
if not st.session_state.connecte:
    afficher_login()
else:
    # --- منطق الأدمن ---
    if st.session_state.is_admin:
        admin_panel()
        
    # --- منطق الطالب ---
    else:
        # تأكد من وجود إيميل الطالب في الجلسة قبل الاستعلام
        if "email_user" in st.session_state:
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('SELECT paye FROM users WHERE email = ?', (st.session_state.email_user,))
            result = c.fetchone()
            conn.close()
            
            # التحقق من حالة الدفع
            if result and result[0] == 1:
                if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
                    st.write(f"### أهلاً بك يا بطل: {st.session_state.nom_eleve}")
                    عرض_الشعار_الكبير()
                    # أزرار التنقل
                    col1, col2, col3, col4, col5 = st.columns(5)
                    if col1.button("✍️ قواعدي"): st.session_state.الصفحة_الحالية = "Page_Hamza"; st.rerun()
                    # ... (بقية الأزرار)
                
                elif st.session_state.الصفحة_الحالية == "Page_Hamza":
                    afficher_page_hamza()
            else:
                st.warning("⚠️ حسابك غير مفعل، يرجى التواصل مع الإدارة.")
        else:
            # إذا حدث خطأ في الجلسة نرجع لشاشة الدخول
            st.session_state.connecte = False
            st.rerun()

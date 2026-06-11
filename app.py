import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", page_icon="🎨", layout="centered")

# CSS المخصص
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, span, label {
    font-family: 'Cairo', sans-serif !important;
    direction: RTL;
    text-align: right;
}
.stApp { background: linear-gradient(135deg, #FFF9E6 0%, #E3F2FD 50%, #E8F5E9 100%); }
.stButton>button { width: 100% !important; border-radius: 20px !important; font-size: 20px !important; font-weight: 900 !important; padding: 15px !important; background: linear-gradient(135deg, #FF7675, #FF4757) !important; color: white !important; border: none !important; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# دالة عرض الشعار
def عرض_الشعار():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("logo.jpeg", use_column_width=True)
    else:
        st.warning("⚠️ يرجى التأكد من وضع ملف 'logo.jpeg' في نفس المجلد")

# 2. إدارة الحالة
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"

# 3. دالة لعرض محتوى الدروس
def عرض_محتوى_الدرس(اسم_الدرس):
    عرض_الشعار() # استدعاء الشعار داخل الصفحات
    st.markdown(f"<h2 style='text-align: center;'>{اسم_الدرس}</h2>", unsafe_allow_html=True)
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5])
    st.markdown(f"### 📖 المادة العلمية للسنة {annee}:")
    # المحتوى بناءً على السنة
    if annee == 1: st.info("الدروس الأساسية للسنة الأولى...")
    elif annee == 2: st.info("الدروس الأساسية للسنة الثانية...")
    # ... إلخ

# 4. بناء الصفحات
if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    عرض_الشعار() # عرض الشعار في القائمة الرئيسية
    st.markdown("<h1 style='text-align: center; color: #FF6B6B;'>🎈 المنصة التعليمية قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    
    if st.button("🌟 دروس مرجعية"):
        st.session_state.الصفحة_الحالية = "الدرس_الأول"
        st.rerun()
    if st.button("🏰 حصن الجملة"):
        st.session_state.الصفحة_الحالية = "الدرس_الثاني"
        st.rerun()
    if st.button("🏆 لوحة الإنجازات"):
        st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"
        st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الأول":
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    عرض_محتوى_الدرس("أقسام الكلمة")

elif st.session_state.الصفحة_الحالية == "الدرس_الثاني":
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    عرض_محتوى_الدرس("الجملة الاسمية والفعلية")

elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    عرض_الشعار()
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("<h2 style='text-align: center;'>🌿 لَوْحَةُ الإِنْجَازَاتِ 🌿</h2>", unsafe_allow_html=True)

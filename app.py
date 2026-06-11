import streamlit as st
import os

# ==========================================
# 1. تهيئة وإعدادات الصفحة
# ==========================================
st.set_page_config(
    page_title="عالم القواعد السحري",
    page_icon="🎨",
    layout="centered"
)

# [CSS المخصص يبقى كما هو لضمان تناسق الخطوط والاتجاهات]
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;700;900&display=swap');
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

# ==========================================
# 2. إدارة الحالة (مع تعريب كامل للمفاتيح)
# ==========================================
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"

# حفظ إجابات الطالب
if "إجابة_الدرس1" not in st.session_state: st.session_state.إجابة_الدرس1 = None
if "إجابة_الدرس2" not in st.session_state: st.session_state.إجابة_الدرس2 = None
if "إجابة_الدرس3" not in st.session_state: st.session_state.إجابة_الدرس3 = None

# حفظ الأوسمة المحققة
if "وسام_الدرس1" not in st.session_state: st.session_state.وسام_الدرس1 = False
if "وسام_الدرس2" not in st.session_state: st.session_state.وسام_الدرس2 = False
if "وسام_الدرس3" not in st.session_state: st.session_state.وسام_الدرس3 = False

# ==========================================
# 3. الدوال المساعدة
# ==========================================
def عرض_الشعار():
    if os.path.exists("logo.jpeg"):
        col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
        with col_l2: st.image("logo.jpeg", use_column_width=True)

# ==========================================
# 4. بناء الصفحات (تعريب كامل للـ Logic)
# ==========================================

# أ. القائمة الرئيسية
if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    عرض_الشعار()
    st.markdown("<h1 style='text-align: center; color: #FF6B6B;'>🎈 عَالَمُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    
    if st.button("🌟 مغامرة أقسام الكلمة"):
        st.session_state.الصفحة_الحالية = "الدرس_الأول"
        st.rerun()
    if st.button("🏰 حصن الجملة الاسمية والفعلية"):
        st.session_state.الصفحة_الحالية = "الدرس_الثاني"
        st.rerun()
    if st.button("🕵️‍♂️ لغز المفعول به والمنصوبات"):
        st.session_state.الصفحة_الحالية = "الدرس_الثالث"
        st.rerun()
    if st.button("🏆 لوحة الأوسمة"):
        st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"
        st.rerun()

# ب. الدرس الأول (أقسام الكلمة)
elif st.session_state.الصفحة_الحالية == "الدرس_الأول":
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("<h2 style='text-align: center;'>درس أقسام الكلمة</h2>", unsafe_allow_html=True)
    # ... (باقي كود المحتوى الخاص بك هنا مع نصوص عربية)
    if st.button("فِعْل"):
        st.session_state.وسام_الدرس1 = True
        st.success("أحسنت! هذا فعل.")

# ج. لوحة الإنجازات
elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("<h2 style='text-align: center;'>🌿 لَوْحَةُ الإِنْجَازَاتِ 🌿</h2>", unsafe_allow_html=True)
    # المنطق هنا يعتمد الآن على مفاتيح عربية (مثل وسام_الدرس1)

import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(
    page_title="قصتي دراستي - عالم القواعد السحري",
    layout="wide"
)

# 2. تصميم CSS المخصص (الأزرار والبطاقات المربعة)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, span, label, button {
        font-family: 'Cairo', sans-serif !important;
        direction: RTL;
        text-align: right;
    }
    
    .stApp {
        background: linear-gradient(135deg, #FFF9E6 0%, #E3F2FD 50%, #E8F5E9 100%);
    }
    
    .card-button {
        width: 100% !important;
        height: 150px !important;
        border-radius: 20px !important;
        background-color: white !important;
        border: 2px solid #e0e0e0 !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
        font-weight: 900 !important;
        color: #333 !important;
        margin-bottom: 20px !important;
    }
    
    .card-button:hover {
        border-color: #2E7D32 !important;
        color: #2E7D32 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. إدارة الجلسة
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"

# 4. دالة عرض الشعار
def عرض_الشعار():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("logo.jpeg", use_column_width=True)

# 5. الهيكل الرئيسي للتنقل
if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    st.markdown("<h1 style='text-align: center;'>قصتي دراستي</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>رحلة النجاح تبدأ هنا</h3>", unsafe_allow_html=True)
    
    col_left, col_mid, col_right = st.columns([1, 1, 1])
    
    with col_left:
        if st.button("الدروس\nالمنهجية القمة", key="b1"):
            st.session_state.الصفحة_الحالية = "الدرس_الأول"
            st.rerun()
        if st.button("الدروس اليومية\nمسارات كل طالب من الدروس", key="b2"):
            st.session_state.الصفحة_الحالية = "الدرس_الثاني"
            st.rerun()
            
    with col_mid:
        عرض_الشعار()
        st.write("")
        if st.button("الذهاب للبرنامج الوطني", key="b_nat"):
            st.session_state.الصفحة_الحالية = "البرنامج_الوطني"
            st.rerun()
            
    with col_right:
        if st.button("الدروس اليومية\nالمحاضرة من ثانوية", key="b3"):
            st.session_state.الصفحة_الحالية = "الدرس_الثالث"
            st.rerun()
        if st.button("التقدم الأكاديمي\nمن سمات المنصات الأكاديمية", key="b4"):
            st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"
            st.rerun()

elif st.session_state.الصفحة_الحالية == "البرنامج_الوطني":
    st.markdown("## 📚 البرنامج الوطني")
    y = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5, 6])
    st.info(f"تمارين مقترحة للسنة {y}")
    if st.button("العودة للقائمة الرئيسية"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الأول":
    st.write("محتوى الدرس الأول...")
    if st.button("العودة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الثاني":
    st.write("محتوى الدرس الثاني...")
    if st.button("العودة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الثالث":
    st.write("محتوى الدرس الثالث...")
    if st.button("العودة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()

elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    st.markdown("## 🏆 لوحة الإنجازات")
    if st.button("العودة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()

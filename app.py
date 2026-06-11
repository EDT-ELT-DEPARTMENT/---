import streamlit as st

# إعداد الصفحة لتكون واسعة وتدعم العربية
st.set_page_config(page_title="منصة قصتي دراستي", layout="wide")

# CSS لجعل الأزرار مربعة وواضحة (بنفس ألوان الشكل الذي طلبته)
st.markdown("""
<style>
    body { direction: rtl; text-align: right; }
    .stButton > button {
        width: 100%;
        height: 120px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 18px;
        background-color: white !important;
        border: 2px solid #2e7d32 !important;
        color: #2e7d32 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background-color: #2e7d32 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'الرئيسية'

def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- الواجهة الرئيسية ---
if st.session_state.page == 'الرئيسية':
    st.markdown("<h1 style='text-align: center;'>قصتي دراستي</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>رحلة النجاح تبدأ هنا</h3>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📚 الدروس المرجعية"): go_to('الدروس')
    with col2:
        if st.button("📝 تمارين مرجعية"): go_to('التمارين')
    with col3:
        if st.button("📑 الامتحانات"): go_to('الامتحانات')
    with col4:
        if st.button("✅ التقييمات"): go_to('التقييمات')

# --- منطق الصفحات الفرعية ---
elif st.session_state.page in ['الدروس', 'التمارين', 'الامتحانات', 'التقييمات']:
    st.title(f"قسم {st.session_state.page}")
    
    # اختيار السنة من 1 إلى 5
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5])
    
    st.write(f"أنت الآن تتصفح محتوى السنة {annee} وفقاً للبرنامج الوطني لوزارة التربية.")
    
    if st.button("⬅ العودة للرئيسية"):
        go_to('الرئيسية')

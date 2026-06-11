import streamlit as st
import os

# إعداد الصفحة
st.set_page_config(page_title="منصة قصتي دراستي", layout="wide")

# CSS المخصص (الألوان، الشعار، الأزرار)
st.markdown("""
<style>
    /* لون الخلفية */
    .stApp { background-color: #f9fdf9; }
    
    /* تصميم الأزرار المربعة الملونة */
    .btn-card {
        width: 100%;
        height: 140px !important;
        border-radius: 25px !important;
        border: 3px solid #2E7D32 !important;
        background-color: white !important;
        font-weight: 900 !important;
        font-size: 20px !important;
        color: #2E7D32 !important;
        transition: 0.3s !important;
    }
    .btn-card:hover {
        background-color: #2E7D32 !important;
        color: white !important;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = 'home'

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # منطقة الشعار
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=200)
        else:
            st.markdown("<h2 style='text-align:center;'> شعار منصتي </h2>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>قصتي دراستي - رحلة النجاح</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # الأزرار الأربعة
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        if st.button("📚 الدروس المرجعية", key="b1", help="المنهج الوطني"):
            st.session_state.page = 'cours'
            st.rerun()
    with c2:
        if st.button("📝 تمارين مرجعية", key="b2"):
            st.session_state.page = 'exercices'
            st.rerun()
    with c3:
        if st.button("📑 الامتحانات", key="b3"):
            st.session_state.page = 'examens'
            st.rerun()
    with c4:
        if st.button("✅ التقييمات", key="b4"):
            st.session_state.page = 'evaluations'
            st.rerun()

# --- صفحات المحتوى ---
else:
    st.title(f"صفحة: {st.session_state.page}")
    annee = st.selectbox("اختر السنة الدراسية (1-5):", [1, 2, 3, 4, 5])
    st.info(f"عرض محتوى {st.session_state.page} للسنة {annee}")
    
    if st.button("⬅ العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()

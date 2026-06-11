import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(layout="wide", page_title="قصتي دراستي")

# 2. تصميم CSS قوي لضمان الألوان والوضوح
st.markdown("""
<style>
    .stApp { background-color: #fcfcfc; }
    
    /* تصميم البطاقات (الأزرار) */
    .button-card {
        background-color: #ffffff !important;
        border: 2px solid #2e7d32 !important;
        border-radius: 20px !important;
        padding: 20px !important;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
        color: #2e7d32 !important;
        font-weight: 900 !important;
        font-size: 18px !important;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# 3. نظام الحالة
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# 4. واجهة الصفحة الرئيسية
if st.session_state.page == 'home':
    # العنوان
    st.markdown("<h1 style='text-align: center; color: #2e7d32;'>قصتي دراستي</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>رحلة النجاح تبدأ هنا</h3>", unsafe_allow_html=True)
    
    # توزيع الأعمدة
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("الدروس - المنهجية القمة", key="d1"):
            st.session_state.page = 'lessons'
            st.rerun()
        st.write("<br>", unsafe_allow_html=True)
        if st.button("الدروس اليومية - مسارات", key="d2"):
            st.session_state.page = 'daily'
            st.rerun()
            
    with col2:
        # هنا الشعار - إذا لم يوجد ملف باسم logo.jpeg سيظهر نص تنبيه
        if os.path.exists("logo.jpeg"):
            st.image("logo.jpeg", use_column_width=True)
        else:
            st.warning("⚠️ ضع صورة باسم 'logo.jpeg' في نفس المجلد")
            
    with col3:
        if st.button("المحاضرات - ثانوية", key="d3"):
            st.session_state.page = 'lectures'
            st.rerun()
        st.write("<br>", unsafe_allow_html=True)
        if st.button("التقدم الأكاديمي", key="d4"):
            st.session_state.page = 'progress'
            st.rerun()

# 5. الصفحات الفرعية
elif st.session_state.page == 'lessons':
    st.title("📚 الدروس")
    if st.button("🏠 العودة"): st.session_state.page = 'home'; st.rerun()

elif st.session_state.page == 'daily':
    st.title("🗓️ الدروس اليومية")
    if st.button("🏠 العودة"): st.session_state.page = 'home'; st.rerun()

elif st.session_state.page == 'lectures':
    st.title("🎥 المحاضرات")
    if st.button("🏠 العودة"): st.session_state.page = 'home'; st.rerun()

elif st.session_state.page == 'progress':
    st.title("📈 التقدم الأكاديمي")
    if st.button("🏠 العودة"): st.session_state.page = 'home'; st.rerun()

import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="قصتي دراستي", layout="wide")

# 2. تصميم CSS (الأزرق والبرتقالي مع البطاقات)
st.markdown("""
<style>
    .stApp { background-color: #F0F4F8; }
    
    /* الأزرار الرئيسية */
    .btn-card { 
        height: 140px !important; border-radius: 20px !important; 
        font-weight: 900 !important; font-size: 18px !important;
        border: none !important; box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    
    /* ألوان الأزرار */
    .blue-btn { background-color: #2980B9 !important; color: white !important; }
    .blue-btn:hover { background-color: #1F618D !important; }
    
    .orange-btn { background-color: #E67E22 !important; color: white !important; }
    .orange-btn:hover { background-color: #CA6F1E !important; }
    
    .content-box { 
        background: white; padding: 25px; border-radius: 20px; 
        border-top: 5px solid #2980B9; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = 'home'

# 4. الواجهة الرئيسية
if st.session_state.page == 'home':
    # عرض الشعار
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if os.path.exists("logo.png"):
            st.image("logo.png", use_column_width=False, width=250)
        else:
            st.markdown("<h2 style='text-align:center; color:#2980B9;'>قصتي دراستي</h2>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>رحلة النجاح تبدأ هنا</h1>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("📚 الدروس المرجعية", key="b1", type="primary"): st.session_state.page = 'cours'; st.rerun()
    with c2:
        if st.button("📝 تمارين مرجعية", key="b2"): st.session_state.page = 'exercices'; st.rerun()
    with c3:
        if st.button("📑 الامتحانات", key="b3"): st.session_state.page = 'examens'; st.rerun()
    with c4:
        if st.button("✅ التقييمات", key="b4"): st.session_state.page = 'evaluations'; st.rerun()

# 5. صفحات المحتوى (الدروس بداخلها)
else:
    st.markdown(f"<div class='content-box'>", unsafe_allow_html=True)
    st.title(f"قسم: {st.session_state.page}")
    
    annee = st.selectbox("اختر السنة الدراسية (البرنامج الوطني):", ["السنة 1", "السنة 2", "السنة 3", "السنة 4", "السنة 5"])
    
    st.write(f"### 📖 محتوى {st.session_state.page} لـ {annee}")
    # عرض دروس تجريبية داخلية
    st.info("💡 الدرس 1: مفاهيم أساسية")
    st.info("💡 الدرس 2: تطبيقات عملية")
    
    if st.button("⬅ العودة للرئيسية"): st.session_state.page = 'home'; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

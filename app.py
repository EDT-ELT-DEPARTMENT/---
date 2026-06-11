import streamlit as st
import os

# 2. تصميم CSS المخصص
st.markdown("""
<style>
    body { direction: rtl; text-align: right; font-family: 'Cairo', sans-serif; }
    .stApp { background-color: #F0F4F8; }
    .btn-card { 
        height: 140px !important; border-radius: 20px !important; 
        font-weight: 900 !important; font-size: 20px !important;
        border: none !important; box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    .blue-btn { background-color: #2980B9 !important; color: white !important; }
    .orange-btn { background-color: #E67E22 !important; color: white !important; }
    .content-box { 
        background: white; padding: 30px; border-radius: 25px; 
        border-right: 8px solid #2980B9; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = 'الرئيسية'
if 'وسام1' not in st.session_state: st.session_state.وسام1 = False

# 4. دالة عرض الشعار
def عرض_الشعار():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2: st.image("logo.jpeg", use_column_width=True)
    else:
        st.error("ملف الشعار (logo.jpeg) غير موجود في المجلد!")

# 5. بناء واجهة التطبيق
if st.session_state.page == 'الرئيسية':
    عرض_الشعار()
    st.markdown("<h1 style='text-align: center; color: #2980B9;'>Plateforme de gestion des EDTs-S2-2026-Département d'Électrotechnique-Faculté de génie électrique-UDL-SBA</h1>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("📚 الدروس المرجعية", key="b1"): st.session_state.page = 'الدروس'; st.rerun()
    with c2:
        if st.button("📝 تمارين مرجعية", key="b2"): st.session_state.page = 'التمارين'; st.rerun()
    with c3:
        if st.button("📑 الامتحانات", key="b3"): st.session_state.page = 'الامتحانات'; st.rerun()
    with c4:
        if st.button("✅ التقييمات", key="b4"): st.session_state.page = 'التقييمات'; st.rerun()

    st.write("<br><br>")
    if st.button("🏆 لوحة الإنجازات"): st.session_state.page = 'لوحة_الإنجازات'; st.rerun()

# 6. منطق الصفحات الفرعية (يحتوي على السنوات 1-5)
else:
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.title(f"قسم: {st.session_state.page}")
    
    if st.session_state.page in ['الدروس', 'التمارين', 'الامتحانات', 'التقييمات']:
        سنة = st.selectbox("اختر السنة الدراسية:", ["السنة 1", "السنة 2", "السنة 3", "السنة 4", "السنة 5"])
        st.write(f"### محتوى {st.session_state.page} لـ {سنة}")
        
        # مثال لمحتوى تفاعلي
        if st.button("أكملت المراجعة لهذا القسم"):
            st.session_state.وسام1 = True
            st.balloons()
            st.success("أحسنت! تم تسجيل إنجازك.")
            
    elif st.session_state.page == 'لوحة_الإنجازات':
        st.write("### أوسمتك المحققة:")
        if st.session_state.وسام1:
            st.success("🌟 وسام الطالب المجتهد")
        else:
            st.info("لا توجد أوسمة بعد، ابدأ المراجعة!")
    
    st.write("<br>")
    if st.button("⬅ العودة للرئيسية"): st.session_state.page = 'الرئيسية'; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

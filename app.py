import streamlit as st

# 1. تهيئة الصفحة
st.set_page_config(page_title="قصتي دراستي", layout="wide")

# 2. CSS للتصميم المماثل للصورة
st.markdown("""
<style>
    .card-btn { width: 100%; height: 120px; border-radius: 20px !important; 
                background: white !important; border: 1px solid #ddd !important;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1); font-weight: bold; }
    .top-btn { border-radius: 50px !important; background: #2e7d32 !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة التنقل (Session State)
if "nav" not in st.session_state:
    st.session_state.nav = "home"

# 4. واجهة الصفحة الرئيسية (التي تشبه صورتك)
if st.session_state.nav == "home":
    # الصف العلوي
    c1, c2, c3, c4 = st.columns([2, 1, 1, 2])
    with c2: st.button("الصفوف ⚙️", key="t1")
    with c3: st.button("الصفوف ⊞", key="t2")
    
    # الوسط
    st.markdown("<h1 style='text-align: center;'>قصتي دراستي</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>رحلة النجاح تبدأ هنا</h3>", unsafe_allow_html=True)
    
    # الأعمدة الجانبية للأزرار
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("الدروس - المنهجية القمة", key="b1"):
            st.session_state.nav = "lessons"
            st.rerun()
        st.write("")
        if st.button("الدروس اليومية - مسارات الطالب", key="b2"):
            st.session_state.nav = "daily"
            st.rerun()
            
    with col2:
        st.image("https://via.placeholder.com/200", caption="الشعار")
        
    with col3:
        if st.button("الدروس اليومية - المحاضرات", key="b3"):
            st.session_state.nav = "lectures"
            st.rerun()
        st.write("")
        if st.button("التقدم الأكاديمي", key="b4"):
            st.session_state.nav = "progress"
            st.rerun()

# 5. صفحات المحتوى (هنا تضع الدروس)
elif st.session_state.nav == "lessons":
    st.title("📚 قسم الدروس")
    st.write("هنا ستظهر قائمة الدروس والمواد الدراسية...")
    if st.button("العودة للرئيسية"):
        st.session_state.nav = "home"
        st.rerun()

elif st.session_state.nav == "daily":
    st.title("🗓️ الدروس اليومية")
    st.write("جدول الحصص اليومي هنا...")
    if st.button("العودة للرئيسية"):
        st.session_state.nav = "home"
        st.rerun()

elif st.session_state.nav == "lectures":
    st.title("🎥 المحاضرات")
    st.write("محتوى المحاضرات هنا...")
    if st.button("العودة للرئيسية"):
        st.session_state.nav = "home"
        st.rerun()

elif st.session_state.nav == "progress":
    st.title("📈 التقدم الأكاديمي")
    st.write("رسوم بيانية لتقدمك الدراسي...")
    if st.button("العودة للرئيسية"):
        st.session_state.nav = "home"
        st.rerun()

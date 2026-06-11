import streamlit as st

# 1. إعداد الصفحة لتكون واسعة (Wide)
st.set_page_config(layout="wide", page_title="قصتي دراستي")

# 2. كود CSS لجعل الأزرار مربعة، بيضاء، وذات ظل، وتظهر بشكل واضح
st.markdown("""
<style>
    /* تنسيق الحاويات */
    .stApp { background-color: #f8f9fa; }
    
    /* جعل الأزرار تبدو كبطاقات مربعة */
    div.stButton > button {
        width: 100%;
        height: 150px !important;
        border-radius: 20px !important;
        background-color: white !important;
        border: 2px solid #e1e1e1 !important;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1) !important;
        font-size: 18px !important;
        font-weight: bold !important;
        color: #2c3e50 !important;
        transition: 0.3s;
    }
    
    /* تأثير عند التحويم */
    div.stButton > button:hover {
        border-color: #28a745 !important;
        color: #28a745 !important;
        transform: translateY(-5px);
    }
</style>
""", unsafe_allow_html=True)

# 3. إدارة التنقل بين الصفحات
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main'

def set_page(page_name):
    st.session_state.current_page = page_name
    st.rerun()

# 4. واجهة الصفحة الرئيسية (Main Interface)
if st.session_state.current_page == 'main':
    # العنوان العلوي
    st.markdown("<h1 style='text-align: center;'>قصتي دراستي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>رحلة النجاح تبدأ هنا</p>", unsafe_allow_html=True)
    
    # الأعمدة لتوزيع الأزرار
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("الدروس\nالمنهجية القمة"): set_page('lessons')
        st.write("") # فراغ
        if st.button("الدروس اليومية\nمسارات كل طالب"): set_page('daily')
        
    with col2:
        # هنا مكان الشعار (ضع مسار صورتك)
        st.image("https://via.placeholder.com/200", use_column_width=False)
        st.markdown("<br>", unsafe_allow_html=True)
    
    with col3:
        if st.button("المحاضرات\nمن ثانوية"): set_page('lectures')
        st.write("") # فراغ
        if st.button("التقدم الأكاديمي\nمن سمات المنصات"): set_page('progress')

# 5. صفحات المحتوى (يتم عرضها عند الضغط على الأزرار)
elif st.session_state.current_page == 'lessons':
    st.title("📚 صفحة الدروس")
    st.write("هنا ستجد المادة العلمية الكاملة لكل سنة.")
    if st.button("العودة للرئيسية"): set_page('main')

elif st.session_state.current_page == 'daily':
    st.title("🗓️ الدروس اليومية")
    st.write("متابعة المسارات اليومية للطلاب.")
    if st.button("العودة للرئيسية"): set_page('main')

elif st.session_state.current_page == 'lectures':
    st.title("🎥 المحاضرات")
    st.write("شرح الفيديو والمحاضرات المسجلة.")
    if st.button("العودة للرئيسية"): set_page('main')

elif st.session_state.current_page == 'progress':
    st.title("📈 التقدم الأكاديمي")
    st.write("عرض الإحصائيات والأوسمة.")
    if st.button("العودة للرئيسية"): set_page('main')

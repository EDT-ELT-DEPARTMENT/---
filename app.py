import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", page_icon="🎈", layout="wide")

# 2. CSS المخصص لتصميم عصري وجذاب
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

html, body, [data-testid="stMarkdownContainer"] {
    font-family: 'Cairo', sans-serif !important;
    direction: RTL;
}

/* خلفية متدرجة جذابة */
.stApp { 
    background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); 
    color: white;
}

/* تنسيق الأزرار الجذابة */
.stButton>button { 
    width: 100% !important; 
    height: 80px !important;
    border-radius: 50px !important; 
    font-size: 24px !important; 
    font-weight: 900 !important; 
    border: none !important;
    background: linear-gradient(45deg, #FF9A9E 0%, #FEC163 99%, #FEC163 100%) !important; 
    color: #333 !important;
    box-shadow: 0px 10px 20px rgba(0,0,0,0.2) !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

.stButton>button:hover { 
    transform: scale(1.05); 
    box-shadow: 0px 15px 30px rgba(0,0,0,0.3) !important;
    background: linear-gradient(45deg, #FEC163 0%, #FF9A9E 100%) !important;
}

/* حاوية المحتوى */
.content-card {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 40px;
    border-radius: 30px;
    color: #333;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 3. دالة عرض الشعار (حجم كبير)
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("logo.jpeg", use_column_width=False, width=400) # تم تكبير العرض لـ 400
    else:
        st.error("⚠️ لم يتم العثور على ملف الشعار 'logo.jpeg'")

# 4. إدارة الحالة
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"

# 5. بناء واجهة الصفحات
# 5. بناء واجهة الصفحات
if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    عرض_الشعار_الكبير()
    st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    
    # الجملة الجديدة المضافة
    st.markdown("<p style='text-align: center; color: #FFD700; font-size: 20px; font-weight: bold;'>جميع هذه الدروس مطابقة تماماً للمناهج التعليمية الوطنية الجزائرية</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True) 
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("🌟 دروس مرجعية"):
            st.session_state.الصفحة_الحالية = "الدرس_الأول"
            st.rerun()
    with c2:
        if st.button("🏰 حصن الجملة"):
            st.session_state.الصفحة_الحالية = "الدرس_الثاني"
            st.rerun()
    with c3:
        if st.button("🏆 لوحة الإنجازات"):
            st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"
            st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الأول":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    
    st.markdown("<h2 style='text-align: center;'>درس أقسام الكلمة</h2>", unsafe_allow_html=True)
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5])
    st.info(f"محتوى تعليمي تفاعلي للسنة الدراسية رقم {annee}")
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.الصفحة_الحالية == "الدرس_الثاني":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("<h2 style='text-align: center;'>الجملة الاسمية والفعلية</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("<h2 style='text-align: center;'>🌿 لَوْحَةُ الإِنْجَازَاتِ 🌿</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

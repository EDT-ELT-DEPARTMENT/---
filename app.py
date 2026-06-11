import streamlit as st
import os

# تأكد من أن ملف الشعار موجود في نفس مجلد ملف الكود (app.py)
# يمكنك تغيير 'logo.png' إلى اسم ملفك الحقيقي (مثلاً logo.jpg أو logo.jpeg)

def عرض_الشعار():
    # إنشاء أعمدة لتوسيط الشعار
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=250, use_column_width=False)
        else:
            # رسالة تنبيه إذا لم يتم العثور على الملف
            st.warning("⚠️ يرجى التأكد من وضع ملف الشعار باسم 'logo.png' في المجلد")

# استدعاء الدالة لعرض الشعار
عرض_الشعار()
import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="قصتي دراستي", layout="wide")

# 2. تصميم CSS (الأزرق والبرتقالي)
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

# 3. إدارة التنقل
if 'page' not in st.session_state: st.session_state.page = 'الرئيسية'

# 4. الواجهة الرئيسية
if st.session_state.page == 'الرئيسية':
    # عرض الشعار
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=250)
        else:
            st.markdown("<h1 style='text-align:center; color:#2980B9;'>قصتي دراستي</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: #34495E;'>رحلة النجاح تبدأ هنا</h2>", unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("📚 الدروس المرجعية", key="b1"): st.session_state.page = 'الدروس'; st.rerun()
    with c2:
        if st.button("📝 تمارين مرجعية", key="b2"): st.session_state.page = 'التمارين'; st.rerun()
    with c3:
        if st.button("📑 الامتحانات", key="b3"): st.session_state.page = 'الامتحانات'; st.rerun()
    with c4:
        if st.button("✅ التقييمات", key="b4"): st.session_state.page = 'التقييمات'; st.rerun()

# 5. صفحات المحتوى
else:
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.title(f"قسم: {st.session_state.page}")
    
    سنة = st.selectbox("اختر السنة الدراسية:", ["السنة 1", "السنة 2", "السنة 3", "السنة 4", "السنة 5"])
    
    st.write(f"### 📖 محتوى {st.session_state.page} لـ {سنة}")
    st.info("💡 الدرس الأول: مفاهيم أساسية في البرنامج الوطني")
    st.info("💡 الدرس الثاني: تطبيقات وتدريبات عملية")
    st.info("💡 الدرس الثالث: مراجعة شاملة")
    
    st.write("<br>", unsafe_allow_html=True)
    if st.button("⬅ العودة للرئيسية"): st.session_state.page = 'الرئيسية'; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

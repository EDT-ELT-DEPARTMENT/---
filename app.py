import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(
    page_title="Plateforme de gestion des EDTs-S2-2026-Département d'Électrotechnique-Faculté de génie électrique-UDL-SBA", 
    layout="wide"
)

# 2. تنسيق CSS للأزرار والواجهة (مطابق للتصميم المرفق)
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 140px;
        border-radius: 20px;
        background-color: #ffffff;
        border: 2px solid #e0e0e0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        font-weight: bold;
        color: #333;
        transition: 0.3s;
        text-align: center;
    }
    .stButton>button:hover {
        border-color: #2e7d32;
        color: #2e7d32;
    }
    .center-text { text-align: center; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "score_lesson1" not in st.session_state: st.session_state.score_lesson1 = False
if "score_lesson2" not in st.session_state: st.session_state.score_lesson2 = False
if "score_lesson3" not in st.session_state: st.session_state.score_lesson3 = False

# 4. الهيكل الرئيسي (if / elif)
if st.session_state.page == "menu":
    st.markdown("<h1 class='center-text'>Plateforme de gestion des EDTs-S2-2026-Département d'Électrotechnique-Faculté de génie électrique-UDL-SBA</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='center-text'>رحلة النجاح تبدأ هنا</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.button("الدروس\nالمنهجية القمة")
        st.write("")
        st.button("الدروس اليومية\nمسارات كل طالب من الدروس")
        
    with col2:
        # هنا يمكن وضع الشعار (logo.jpeg)
        st.markdown("<div style='text-align: center; padding-top: 50px;'><h3>[شعار المنصة]</h3></div>", unsafe_allow_html=True)
        st.write("")
        if st.button("الذهاب للبرنامج الوطني"):
            st.session_state.page = "البرنامج_الوطني"
            st.rerun()
            
    with col3:
        st.button("الدروس اليومية\nالمحاضرة من ثانوية")
        st.write("")
        st.button("التقدم الأكاديمي\nمن سمات المنصات الأكاديمية")

elif st.session_state.page == "البرنامج_الوطني":
    st.markdown("## 📚 البرنامج الوطني والتمارين")
    
    y = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5, 6])
    
    exercices = {
        1: "تمرين: صل الكلمة بالصورة (أسد، قلم، كرة).",
        2: "تمرين: حول الجملة إلى صيغة الجمع: (هو يكتب الدرس).",
        3: "تمرين: حدد نوع الكلمة في الجملة: (سافرَ محمدٌ إلى مكةَ).",
        4: "تمرين: أعرب ما تحته خط: (يأكلُ الولدُ التفاحةَ).",
        5: "تمرين: أدخل (كان) على الجملة التالية: (السماءُ صافيةٌ).",
        6: "تمرين: حول الأفعال التالية إلى المضارع (قرأ، كتب، جلس)."
    }
    
    st.info(f"تمارين مقترحة للسنة {y}: {exercices.get(y)}")
    
    # حساب التقييم
    nombre_de_lecons_reussies = (1 if st.session_state.score_lesson1 else 0) + \
                               (1 if st.session_state.score_lesson2 else 0) + \
                               (1 if st.session_state.score_lesson3 else 0)
    pourcentage_connaissance = (nombre_de_lecons_reussies / 3) * 100
    
    st.write("---")
    st.metric("نسبة التقدم في Plateforme de gestion des EDTs-S2-2026-Département d'Électrotechnique-Faculté de génie électrique-UDL-SBA", f"{int(pourcentage_connaissance)}%")
    
    if st.button("العودة للقائمة الرئيسية"):
        st.session_state.page = "menu"
        st.rerun()

import streamlit as st
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="Plateforme de gestion des EDTs-S2-2026-Département d'Électrotechnique-Faculté de génie électrique-UDL-SBA", layout="centered")

# 2. إدارة الحالة
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "score_lesson1" not in st.session_state: st.session_state.score_lesson1 = False
if "score_lesson2" not in st.session_state: st.session_state.score_lesson2 = False
if "score_lesson3" not in st.session_state: st.session_state.score_lesson3 = False

def afficher_logo_haut():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("logo.jpeg", use_column_width=True)

# 3. الهيكل الرئيسي (if / elif)
if st.session_state.page == "menu":
    afficher_logo_haut()
    st.title("Plateforme de gestion des EDTs-S2-2026-Département d'Électrotechnique-Faculté de génie électrique-UDL-SBA")
    if st.button("الذهاب للبرنامج الوطني"):
        st.session_state.page = "البرنامج_الوطني"
        st.rerun()

elif st.session_state.page == "البرنامج_الوطني":
    afficher_logo_haut()
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
    
    # حساب التقييم قبل العودة للقائمة
    nombre_de_lecons_reussies = (1 if st.session_state.score_lesson1 else 0) + \
                               (1 if st.session_state.score_lesson2 else 0) + \
                               (1 if st.session_state.score_lesson3 else 0)
    pourcentage_connaissance = (nombre_de_lecons_reussies / 3) * 100
    
    st.write("---")
    st.metric("نسبة التقدم في Plateforme de gestion des EDTs-S2-2026-Département d'Électrotechnique-Faculté de génie électrique-UDL-SBA", f"{int(pourcentage_connaissance)}%")
    
    if st.button("العودة للقائمة الرئيسية"):
        st.session_state.page = "menu"
        st.rerun()

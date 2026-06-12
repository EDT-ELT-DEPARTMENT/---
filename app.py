import streamlit as st
import os

# 1. إعداد الصفحة
st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FFD700; font-size: 20px; font-weight: withe;'>جميع هذه الدروس مطابقة تماماً للمناهج التعليمية الوطنية الجزائرية</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# 2. تهيئة الحالة (Session State)
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
if "نقاط" not in st.session_state:
    st.session_state.نقاط = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# 3. قاموس الألعاب
محتوى_الألعاب = {
    "أقسام الكلمة": {
        1: {"سؤال": "ما هو نوع كلمة 'قلم'؟", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"},
        2: {"سؤال": "ما هو نوع كلمة 'يذهب'؟", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "فعل"},
        3: {"سؤال": "ما نوع كلمة 'في'؟", "خيارات": ["اسم", "فعل", "حرف"], "إجابة": "حرف"},
        4: {"سؤال": "أي مما يلي اسم إنسان؟", "خيارات": ["شجرة", "محمد", "يقرأ"], "إجابة": "محمد"},
        5: {"سؤال": "كلمة 'مدرسة' تدل على:", "خيارات": ["مكان", "زمان", "فعل"], "إجابة": "مكان"}
    },
    "الجملة الاسمية والفعلية": {
        1: {"سؤال": "الجملة الاسمية تبدأ بـ:", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"},
        2: {"سؤال": "الجملة الفعلية تبدأ بـ:", "خيارات": ["اسم", "فعل", "حرف"], "إجابة": "فعل"},
        3: {"سؤال": "حول 'يلعبُ الولدُ' لجملة اسمية:", "خيارات": ["الولدُ يلعبُ", "يلعبُ الولدُ", "الولدُ يلعبُ في البيت"], "إجابة": "الولدُ يلعبُ"},
        4: {"سؤال": "ما ركن الجملة الاسمية الأساسي؟", "خيارات": ["المبتدأ والخبر", "الفعل والفاعل", "الحرف والاسم"], "إجابة": "المبتدأ والخبر"},
        5: {"سؤال": "في 'الطالبُ يدرسُ'، ما هو الخبر؟", "خيارات": ["الطالبُ", "يدرسُ", "لا يوجد"], "إجابة": "يدرسُ"}
    }
}

# 4. الدوال الأساسية
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 10, 1])
        with col2:
            st.image("logo.jpeg", width=1000)

def تشغيل_لعبة_الدرس(اسم_الدرس, مستوى_السنة):
    data = محتوى_الألعاب.get(اسم_الدرس, {}).get(مستوى_السنة)
    if data:
        st.markdown(f"### 🎮 تحدي: {data['سؤال']}")
        choix = st.radio("اختر الإجابة:", data['خيارات'], key=f"radio_{اسم_الدرس}_{مستوى_السنة}")
        
        if st.button("تحقق من إجابتي!", key=f"btn_check_{اسم_الدرس}_{مستوى_السنة}"):
            if choix == data['إجابة']:
                st.session_state.نقاط[مستوى_السنة] += 10
                st.success(f"🎉 إجابة صحيحة! نقاط المستوى {مستوى_السنة} هي: {st.session_state.نقاط[مستوى_السنة]}")
                st.balloons()
            else:
                st.error("❌ إجابة خاطئة. حاول مرة أخرى!")
    else:
        st.warning("⚠️ اللعبة لهذا المستوى قيد التطوير.")

def عرض_محتوى_الدرس(اسم_الدرس):
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة", key=f"back_{اسم_الدرس}"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown(f"<h2 style='text-align: center;'>{اسم_الدرس}</h2>", unsafe_allow_html=True)
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5], key=f"select_{اسم_الدرس}")
    تشغيل_لعبة_الدرس(اسم_الدرس, annee)
    st.markdown("</div>", unsafe_allow_html=True)
def afficher_fiche_interactive():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>📖 رحلة القلم الصغير</h2>", unsafe_allow_html=True)
    st.write("""
    كان يا مكان، في عالم الكلمات الملون، التقى القلم بـ 'يذهب' (الفعل) 
    الذي كان يجري بسرعة! ثم التقى بـ 'مدرسة' (الاسم) التي علمته الثبات.
    """)
    if st.button("⬅ العودة للقائمة", key="back_fiche"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 5. التنسيق
css_style = "<style>.content-card { background-color: rgba(255,255,255,0.95); padding: 40px; border-radius: 30px; color: #333; }</style>"
st.markdown(css_style, unsafe_allow_html=True)

# 6. منطق التنقل
if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    عرض_الشعار_الكبير()
    st.title("🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈")
    c1, c2, c3, c4 = st.columns(4) # Ajout d'une 4ème colonne
    if c1.button("🌟 دروس", key="b1"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
    if c2.button("🏰 حصن", key="b2"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
    if c3.button("📜 قصة", key="b4"): st.session_state.الصفحة_الحالية = "Fiche_Vocabulaire"; st.rerun()
    if c4.button("🏆 لوحة", key="b3"): st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"; st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الأول":
    عرض_محتوى_الدرس("أقسام الكلمة")

elif st.session_state.الصفحة_الحالية == "الدرس_الثاني":
    عرض_محتوى_الدرس("الجملة الاسمية والفعلية")

elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2>🏆 لوحة الإنجازات حسب المستوى</h2>", unsafe_allow_html=True)
    for annee, score in st.session_state.نقاط.items():
        st.write(f"### السنة {annee}: {score} نقطة")
    total = sum(st.session_state.نقاط.values())
elif st.session_state.الصفحة_الحالية == "Fiche_Vocabulaire":
    afficher_fiche_interactive()
    st.markdown(f"--- \n ### 🌟 المجموع الكلي: {total} نقطة")
    if st.button("⬅ العودة للقائمة", key="back_final"): st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


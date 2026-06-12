import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", page_icon="🎈", layout="wide")

# 2. قاموس الألعاب المتكامل
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

# 3. CSS المخصص
css_style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
html, body, [data-testid="stMarkdownContainer"] { font-family: 'Cairo', sans-serif !important; direction: RTL; }
.stApp { background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); color: white; }
.stButton>button { width: 100% !important; height: 80px !important; border-radius: 50px !important; font-size: 20px !important; background: linear-gradient(45deg, #FF9A9E 0%, #FEC163 99%) !important; color: #333 !important; }
.content-card { background-color: rgba(255, 255, 255, 0.95); padding: 40px; border-radius: 30px; color: #333; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 4. الدوال الأساسية
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("logo.jpeg", width=400)

def تشغيل_لعبة_الدرس(اسم_الدرس, مستوى_السنة):
    data = محتوى_الألعاب.get(اسم_الدرس, {}).get(مستوى_السنة)
    if data:
        st.markdown(f"### 🎮 تحدي: {data['سؤال']}")
        choix = st.radio("اختر الإجابة:", data['خيارات'], key=f"radio_{اسم_الدرس}_{مستوى_السنة}")
        if st.button("تحقق من إجابتي!", key=f"btn_check_{اسم_الدرس}_{مستوى_السنة}"):
            if choix == data['إجابة']:
                st.session_state.نقاط += 10
                st.success(f"🎉 إجابة صحيحة! نقاطك الآن: {st.session_state.نقاط}")
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

# 5. منطق الحالة
if "الصفحة_الحالية" not in st.session_state: st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
if "نقاط" not in st.session_state: st.session_state.نقاط = 0

# 6. الواجهة الرئيسية
if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    عرض_الشعار_الكبير()
    st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FFD700; font-size: 20px; font-weight: bold;'>جميع هذه الدروس مطابقة تماماً للمناهج التعليمية الوطنية الجزائرية</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    if c1.button("🌟 دروس مرجعية", key="btn_1"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
    if c2.button("🏰 حصن الجملة", key="btn_2"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
    if c3.button("🏆 لوحة الإنجازات", key="btn_3"): st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"; st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الأول": عرض_محتوى_الدرس("أقسام الكلمة")
elif st.session_state.الصفحة_الحالية == "الدرس_الثاني": عرض_محتوى_الدرس("الجملة الاسمية والفعلية")
elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    st.markdown(f"<div class='content-card'><h2>مجموع نقاطك: {st.session_state.نقاط} 🏆</h2></div>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة", key="back_main"): st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"; st.rerun()

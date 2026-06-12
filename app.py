import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", layout="wide")
st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FFD700; font-size: 20px; font-weight: bold;'>جميع هذه الدروس مطابقة تماماً للمناهج التعليمية الوطنية الجزائرية</p>", unsafe_allow_html=True)
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
        2: {"سؤال": "ما هو نوع كلمة 'يذهب'؟", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "فعل"}
    },
    "الجملة الاسمية والفعلية": {
        1: {"سؤال": "الجملة الاسمية تبدأ بـ:", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"},
        2: {"سؤال": "الجملة الفعلية تبدأ بـ:", "خيارات": ["اسم", "فعل", "حرف"], "إجابة": "فعل"}
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
                st.success(f"🎉 إجابة صحيحة!")
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

def afficher_page_hamza():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #2c3e50;'>✍️ قواعد الهمزة للسنة الرابعة ابتدائي</h2>", unsafe_allow_html=True)
    
    st.write("### 1. الهمزة في أول الكلمة:")
    st.write("- **همزة الوصل (ا):** تظهر في بداية الكلمة ولا تُنطق في وسط الكلام مثل: (اِسْتَغْفَرَ، اِبْن، اِسْم، القلم).")
    st.write("- **همزة القطع (أ / إ):** همزة تُكتب وتُنطق بوضوح مثل: (أَحْمَدَ، إِسْلام، أُسْتَاذ).")
    
    st.write("### 2. الهمزة المتوسطة:")
    st.write("تعتمد كتابة الهمزة المتوسطة على **أقوى الحركات**.")
    
    st.write("### 3. الهمزة المتطرفة:")
    st.write("تكتب الهمزة المتطرفة حسب حركة الحرف الذي **قبلها فقط**.")
    
    st.markdown("---")
    c1, c2 = st.columns(2)
    if c1.button("⬅ العودة للقائمة", key="back_hamza_btn"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    if c2.button("🎬 الانتقال للسينما ➔", key="go_cinema_hamza"):
        st.session_state.الصفحة_الحالية = "Cinema_Grammaire"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def عرض_سينما_القواعد():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>🎬 سينما القواعد: حارس غابة الكلمات</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=9_6A_M542u8")
    if st.button("⬅ العودة", key="back_cinema"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 5. التنسيق
css_style = """
<style>
    html, body, [data-testid="stAppViewContainer"] { direction: rtl !important; text-align: right !important; }
    .content-card { background-color: rgba(255,255,255,0.95); padding: 40px; border-radius: 30px; color: #333; }
    h1, h2, h3, h4, p, div { text-align: right !important; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 6. منطق التنقل
if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    عرض_الشعار_الكبير()
    c1, c2, c3, c4, c5 = st.columns(5)
    if c1.button("🌟 دروس", key="b1"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
    if c2.button("🏰 حصن", key="b2"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
    # تم تغيير اسم الزر هنا
    if c3.button("✍️ قواعدي في قصتي", key="b4"): st.session_state.الصفحة_الحالية = "Page_Hamza"; st.rerun()
    if c4.button("🎬 سينما", key="b5"): st.session_state.الصفحة_الحالية = "Cinema_Grammaire"; st.rerun()
    if c5.button("🏆 لوحة", key="b3"): st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"; st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الأول": عرض_محتوى_الدرس("أقسام الكلمة")
elif st.session_state.الصفحة_الحالية == "الدرس_الثاني": عرض_محتوى_الدرس("الجملة الاسمية والفعلية")
elif st.session_state.الصفحة_الحالية == "Page_Hamza": afficher_page_hamza()
elif st.session_state.الصفحة_الحالية == "Cinema_Grammaire": عرض_سينما_القواعد()
elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2>🏆 لوحة الإنجازات</h2>", unsafe_allow_html=True)
    for annee, score in st.session_state.نقاط.items(): st.write(f"### السنة {annee}: {score} نقطة")
    if st.button("⬅ العودة", key="back_final"): st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"; st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

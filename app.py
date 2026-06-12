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
.stButton>button { width: 100% !important; height: 60px !important; border-radius: 30px !important; font-size: 18px !important; background: #FFD700 !important; color: #333 !important; font-weight: bold; }
.content-card { background-color: white; padding: 30px; border-radius: 20px; color: #333; box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 4. تهيئة الحالة (Session State)
if "الصفحة_الحالية" not in st.session_state: st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
if "نقاط" not in st.session_state: st.session_state.نقاط = 0

# 5. دوال العرض
def تشغيل_لعبة_الدرس(اسم_الدرس, مستوى_السنة):
    data = محتوى_الألعاب.get(اسم_الدرس, {}).get(مستوى_السنة)
    if data:
        st.markdown(f"### 🎮 تحدي: {data['سؤال']}")
        choix = st.radio("اختر الإجابة:", data['خيارات'])
        if st.button("تحقق من إجابتي!"):
            if choix == data['إجابة']:
                st.session_state.نقاط += 10
                st.success(f"🎉 إجابة صحيحة! نقاطك الآن: {st.session_state.نقاط}")
                st.balloons()
            else:
                st.error("❌ إجابة خاطئة. حاول مرة أخرى!")
    else:
        st.warning("⚠️ اللعبة قيد التطوير لهذا المستوى.")

def عرض_محتوى_الدرس(اسم_الدرس):
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    
    # إضافة مفتاح فريد (key) للزر لمنع تكرار المعرف
    if st.button("⬅ العودة للقائمة", key=f"btn_retour_{اسم_الدرس}"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    
    st.markdown(f"<h2 style='text-align: center;'>{اسم_الدرس}</h2>", unsafe_allow_html=True)
    
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5], key=f"select_{اسم_الدرس}")
    
    if اسم_الدرس in محتوى_الألعاب:
        تشغيل_لعبة_الدرس(اسم_الدرس, annee)
    else:
        st.warning("⚠️ عذراً، لا توجد دروس لهذا العنوان حالياً.")
        
    st.markdown("</div>", unsafe_allow_html=True)
# 6. التنقل
if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    if col1.button("🌟 دروس مرجعية"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
    if col2.button("🏰 حصن الجملة"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
    if col3.button("🏆 لوحة الإنجازات"): st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"; st.rerun()
elif st.session_state.الصفحة_الحالية == "الدرس_الأول": عرض_محتوى_الدرس("أقسام الكلمة")
elif st.session_state.الصفحة_الحالية == "الدرس_الثاني": عرض_محتوى_الدرس("الجملة الاسمية والفعلية")
elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    st.markdown(f"<div class='content-card'><h2>مجموع نقاطك: {st.session_state.نقاط} 🏆</h2></div>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة"): st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"; st.rerun()
# 4. دالة اللعبة (المحدثة)
def تشغيل_لعبة_الدرس(اسم_الدرس, مستوى_السنة):
    # محاولة الحصول على اللعبة من القاموس
    data = محتوى_الألعاب.get(اسم_الدرس, {}).get(مستوى_السنة)
    
    if data:
        st.markdown(f"### 🎮 تحدي: {data['سؤال']}")
        choix = st.radio("اختر الإجابة الصحيحة:", data['خيارات'])
        
        if st.button("تحقق من إجابتي!"):
            if choix == data['إجابة']:
                st.success("🎉 إجابة صحيحة! أحسنت يا بطل.")
                st.balloons()
            else:
                st.error("❌ إجابة خاطئة. حاول مجدداً!")
    else:
        st.warning("⚠️ اللعبة لهذا المستوى قيد التطوير...")

# 5. دالة عرض محتوى الدرس المحدثة
def عرض_محتوى_الدرس(اسم_الدرس):
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    
    st.markdown(f"<h2 style='text-align: center;'>{اسم_الدرس}</h2>", unsafe_allow_html=True)
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5])
    
    # عرض اللعبة
    تشغيل_لعبة_الدرس(اسم_الدرس, annee)
        
    st.markdown("</div>", unsafe_allow_html=True)

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

# 4. دالة عرض الشعار
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("logo.jpeg", width=1000)
    else:
        st.warning("⚠️ يرجى التأكد من وضع ملف 'logo.jpeg' في نفس المجلد")

# 5. دالة عرض محتوى الدرس
def عرض_محتوى_الدرس(اسم_الدرس):
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    
    st.markdown(f"<h2 style='text-align: center;'>{اسم_الدرس}</h2>", unsafe_allow_html=True)
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5])
    
    st.write(f"### 📖 دروس السنة {annee}:")
    
    liste_cours = محتوى_الدروس.get(اسم_الدرس, {}).get(annee, ["لا يوجد محتوى حالي لهذه السنة"])
    
    for cours in liste_cours:
        st.success(f"✅ {cours}")
        
    st.markdown("</div>", unsafe_allow_html=True)

# 6. منطق التنقل بين الصفحات
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"

if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    عرض_الشعار_الكبير()
    st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FFD700; font-size: 20px; font-weight: bold;'>جميع هذه الدروس مطابقة تماماً للمناهج التعليمية الوطنية الجزائرية</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
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
    عرض_محتوى_الدرس("أقسام الكلمة")

elif st.session_state.الصفحة_الحالية == "الدرس_الثاني":
    عرض_محتوى_الدرس("الجملة الاسمية والفعلية")

elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("<h2 style='text-align: center;'>🌿 لَوْحَةُ الإِنْجَازَاتِ 🌿</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

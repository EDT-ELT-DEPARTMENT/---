import streamlit as st
import os

# 1. إعداد الصفحة
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", page_icon="🎈", layout="wide")

# 2. هيكلة الدروس (يمكنك إضافة أي دروس هنا)
محتوى_الدروس = {
    "أقسام الكلمة": {
        1: ["الكلمة والحرف", "أشكال الحروف"],
        2: ["الاسم والفعل والحرف", "علامات الرفع"],
        3: ["أنواع الكلمة بالتفصيل", "تدريبات إعرابية"],
        4: ["الاسم المذكر والمؤنث", "المفرد والمثنى والجمع"],
        5: ["قواعد متقدمة في الكلمة", "إعراب شامل"]
    },
    "الجملة الاسمية والفعلية": {
        1: ["جملة بسيطة", "تكوين الجملة"],
        2: ["أركان الجملة الاسمية", "أركان الجملة الفعلية"],
        3: ["الخبر وأنواعه", "الفاعل والمفعول به"],
        4: ["النواسخ (كان وأخواتها)", "الجملة الخبرية"],
        5: ["التقديم والتأخير في الجملة", "تدريبات معقدة"]
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

# 4. دالة عرض محتوى الدرس
def عرض_محتوى_الدرس(اسم_الدرس):
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if st.button("⬅ العودة للقائمة"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    
    st.markdown(f"<h2 style='text-align: center;'>{اسم_الدرس}</h2>", unsafe_allow_html=True)
    annee = st.selectbox("اختر السنة الدراسية:", [1, 2, 3, 4, 5])
    
    st.write(f"### 📖 دروس السنة {annee}:")
    
    # جلب الدروس من القاموس أعلاه
    liste_cours = محتوى_الدروس.get(اسم_الدرس, {}).get(annee, ["لا يوجد محتوى حالي لهذه السنة"])
    
    for cours in liste_cours:
        st.success(f"✅ {cours}")
        
    st.markdown("</div>", unsafe_allow_html=True)

# 5. منطق الصفحات
if "الصفحة_الحالية" not in st.session_state: st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"

if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
    st.markdown("<h1 style='text-align: center; color: white;'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ قِصَّتِي دِرَاسَتِي 🎈</h1>", unsafe_allow_html=True)
    # [باقي أزرار القائمة الرئيسية كما هي...]
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🌟 دروس مرجعية"): st.session_state.الصفحة_الحالية = "الدرس_الأول"; st.rerun()
    with c2:
        if st.button("🏰 حصن الجملة"): st.session_state.الصفحة_الحالية = "الدرس_الثاني"; st.rerun()
    with c3:
        if st.button("🏆 لوحة الإنجازات"): st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"; st.rerun()

elif st.session_state.الصفحة_الحالية == "الدرس_الأول":
    عرض_محتوى_الدرس("أقسام الكلمة")

elif st.session_state.الصفحة_الحالية == "الدرس_الثاني":
    عرض_محتوى_الدرس("الجملة الاسمية والفعلية")

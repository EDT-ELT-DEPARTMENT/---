import streamlit as st

# إعداد الصفحة لملء العرض بالكامل
st.set_page_config(page_title="قصتي دراستي", layout="wide")

# CSS المخصص للمطابقة التامة مع الشكل
st.markdown("""
<style>
    /* تنسيق الحاويات لتكون متناسقة */
    .block-container { padding: 1rem; }
    
    /* تصميم الأزرار المربعة (البطاقات) */
    div.stButton > button {
        width: 100%;
        height: 110px;
        border-radius: 20px;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        font-family: 'Cairo', sans-serif;
        font-weight: bold;
        color: #333;
        text-align: right;
        padding-right: 20px;
        display: block;
    }
    
    /* تصميم الأزرار العلوية الصغيرة */
    .top-btns div.stButton > button {
        height: 40px;
        border-radius: 50px;
        background-color: #2e7d32;
        color: white;
        text-align: center;
        padding: 0;
    }
</style>
""", unsafe_allow_html=True)

# 1. الصف العلوي (المصادر والصفوف)
col_top1, col_top2, col_top3, col_top4 = st.columns([2, 1, 1, 2])
with col_top2:
    st.markdown('<div class="top-btns">', unsafe_allow_html=True)
    st.button("الصفوف ⚙️")
    st.markdown('</div>', unsafe_allow_html=True)
with col_top3:
    st.markdown('<div class="top-btns">', unsafe_allow_html=True)
    st.button("الصفوف ⊞")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. الوسط (الشعار والعنوان)
st.markdown("<h1 style='text-align: center;'>قصتي دراستي</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>رحلة النجاح تبدأ هنا</h3>", unsafe_allow_html=True)

# 3. توزيع 3 أعمدة (الأزرار على الجوانب، والوسط للشعار والطريق)
main_col1, main_col2, main_col3 = st.columns([1, 1, 1])

with main_col1:
    st.button("الدروس\nالمنهجية القمة")
    st.write("<br>", unsafe_allow_html=True)
    st.button("الدروس اليومية\nمسارات كل طالب من الدروس")

with main_col2:
    # هنا يتم وضع الشعار وصورة الطفل في الطريق
    st.image("https://via.placeholder.com/200x250?text=LOGO+CENTER", use_column_width=False)

with main_col3:
    st.button("الدروس اليومية\nالمحاضرة من ثانوية")
    st.write("<br>", unsafe_allow_html=True)
    st.button("التقدم الأكاديمي\nمن سمات المنصات الأكاديمية")

# 4. الجزء السفلي
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("### أرحلة النجاح")

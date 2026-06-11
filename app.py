import streamlit as st
import random

# Configuration de la page de l'application
st.set_page_config(
    page_title="قصتي دراستي - منصة تعليمية",
    page_icon="✨",
    layout="centered"
)

# Injection de style CSS pour forcer l'affichage de droite à gauche (RTL) et personnaliser le design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [data-testid="stMarkdownContainer"], h1, h2, h3, h4, p, button {
        font-family: 'Cairo', sans-serif !important;
        direction: RTL;
        text-align: right;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-size: 18px !important;
        font-weight: bold;
        padding: 15px;
        transition: 0.3s;
    }
    div[data-testid="stBlock"] {
        direction: RTL;
    }
    .cartoon-box {
        background-color: #FFF9E6;
        border: 3px dashed #FFAAA6;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .story-text {
        font-size: 18px;
        line-height: 1.8;
        color: #2C3E50;
    }
    </style>
""", unsafe_allow_html=True)

# Initialisation des variables d'état (Session State)
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "score" not in st.session_state:
    st.session_state.score = 0

# --- MENU PRINCIPAL ---
if st.session_state.page == "menu":
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>✨ قِصَّتِي دِرَاسَتِي ✨</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #7F8C8D;'>مرحباً بك يا بطل! اختر مغامرتك اللغوية لليوم:</h3>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧒 فئة 6 - 7 سنوات\n(مغامرة أقسام الكلمة 🏃‍♂️)", key="b1"):
            st.session_state.page = "6-7"
            st.rerun()
    with col2:
        if st.button("👦 فئة 8 - 9 سنوات\n(مملكة الجملة الاسمية والفعلية 🏰)", key="b2"):
            st.session_state.page = "8-9"
            st.rerun()
            
    st.write("")
    if st.button("🧑 فئة 10 - 11 سنة\n(محقق القواعد: الصياد والمنصوبات 🕵️‍♂️)", key="b3"):
        st.session_state.page = "10-11"
        st.rerun()

# --- CATÉGORIE 6-7 ANS : أقسام الكلمة ---
elif st.session_state.page == "6-7":
    if st.button("⬅ العودة للقائمة الرئيسية"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #FF7675;'>🎬 رسوم متحركة: مغامرة الأرنب سمسم</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <p class="story-text">
        🏃‍♂️ كـان الأرنب الذكي <b>سَمسَم</b> يقفز في الغابة السحرية، وفجأة وجد صندوقاً كبيراً تتطاير منه الكلمات! <br>
        قال له الحكيم سُلحوف: يا سمسم، الكلمات في لغتنا العربية ثلاثة أنواع لا رابع لها:<br>
        🦁 <b>الاسم:</b> ما نسمي به الإنسان، الحيوان، أو الأشياء (مثل: أرنب، شجرة).<br>
        🏃‍♂️ <b>الفعل:</b> حركة نقوم بها في زمن معين (مثل: يقفز، أكلَ).<br>
        📦 <b>الحرف:</b> كلمة صغيرة لا نفهم معناها إلا مع غيرها (مثل: في، إلى، على).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎮 العب وتحدّ سمسم:")
    st.write("ساعد سمسم في تصنيف الكلمة التالية ليحصل على الجَزرة 🥕")
    
    mot_test = "يَقْفِزُ"
    st.markdown(f"<h2 style='text-align: center; color: #E84393;'>الكلمة هي: {mot_test}</h2>", unsafe_allow_html=True)
    
    choix = st.radio("ما هو نوع هذه الكلمة؟", ["اسْم", "فِعْل", "حَرْف"], index=None, key="rad_6_7")
    
    if st.button("إرسال الإجابة 🥕"):
        if choix == "فِعْل":
            st.success("🎉 إجابة رائعة! يَقْفِزُ هي حركة، إذن هي فعل! لقد أكل سمسم الجزرة!")
        else:
            st.error("🧐 ركّز جيداً يا بطل! يَقْفِزُ تدل على حركة ونشاط، إذن هي فِعْل وليست اسماً أو حرفاً.")

# --- CATÉGORIE 8-9 ANS : الجملة الاسمية والفعلية ---
elif st.session_state.page == "8-9":
    if st.button("⬅ العودة للقائمة الرئيسية"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #74B9FF;'>🎬 رسوم متحركة: قلعة الجمل السحرية</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <p class="story-text">
        🏰 وصلنا إلى قلعة القواعد! هناك حارسان على باب القلعة:<br>
        👑 <b>الحارس الأول (الجملة الاسمية):</b> يصرخ ويقول: أنا تبدأ دائماً بـ <b>اسم</b>، وعندي ركنان هما المبتدأ والخبر (مثل: <i>العِلْمُ نُورٌ</i>).<br>
        ⚔️ <b>الحارس الثاني (الجملة الفعلية):</b> يلوح بسيفه ويقول: أنا أبدأ دائماً بـ <b>فعل</b>، وعندي فعل وفاعل (مثل: <i>جَاءَ البَطَلُ</i>).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎮 تحدي حراس القلعة:")
    st.write("الحراس يمنعونك من الدخول حتى تحدد نوع هذه الجملة:")
    
    phrase_test = "تُمطِرُ السَّمَاءُ"
    st.markdown(f"<h2 style='text-align: center; color: #0984E3;'>الجملة هي: « {phrase_test} »</h2>", unsafe_allow_html=True)
    
    choix_phrase = st.radio("ما نوع هذه الجملة؟", ["جملة اسمية", "جملة فعلية"], index=None, key="rad_8_9")
    
    if st.button("فتح باب القلعة 🔑"):
        if choix_phrase == "جملة فعلية":
            st.success("🎉 مذهل! الجملة تبدأ بكلمة 'تُمطِرُ' وهي فعل، إذن هي جملة فعلية! تفضل بالدخول للقلعة.")
        else:
            st.error("❌ الحارس يرفض إجابتك! انظر إلى الكلمة الأولى 'تُمطِرُ'، هل هي اسم أم فعل؟ إنها فعل، إذن الجملة فعلية.")

# --- CATÉGORIE 10-11 ANS : المفعول به والمنصوبات ---
elif st.session_state.page == "10-11":
    if st.button("⬅ العودة للقائمة الرئيسية"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #55E6C1;'>🎬 رسوم متحركة: المحقق كـانَمون ومصيدة المفعول به</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cartoon-box">
        <p class="story-text">
        🕵️‍♂️ المحقق الشهير <b>كَانَمُون</b> يبحث عن ركن مفقود في مسرح الجريمة اللغوية! <br>
        قال المحقق: لدينا فعل (كَتَبَ) ولدينا فاعل قام بالحركة (التِّلْمِيذُ).. لكن ماذا كتب؟! <br>
        🎯 وفجأة ظهر <b>المَفْعُولُ بِهِ</b> ضاحكاً وقال: أنا الاسم المنصوب بالفتحة الذي وقع عليّ فعل الفاعل! (مثل: كَتَبَ التِّلْمِيذُ <u>الدَّرْسَ</u>). أنا دائماً أجيب عن سؤال: <b>مَاذَا؟</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎮 اختبر مهاراتك الإعرابية مع المحقق:")
    st.write("ابحث عن المفعول به المنصوب في الجملة التالية واقبض عليه:")
    
    phrase_adv = "قَرَأَ الطِّفْلُ قِصَّةً جَمِيلَةً"
    st.markdown(f"<h2 style='text-align: center; color: #27AE60;'>الجملة هي: « {phrase_adv} »</h2>", unsafe_allow_html=True)
    
    reponse_inv = st.text_input("اكتب الكلمة التي تمثل المفعول به هنا:", key="input_10_11").strip()
    
    if st.button("تقديم التقرير للمحقق 🕵️‍♂️"):
        if reponse_inv == "قصة" or reponse_inv == "قِصَّةً" or reponse_inv == "قصةً":
            st.success("🎯 أحسنت يا سيادة المحقق! 'قصةً' هي الإجابة عن سؤال: ماذا قرأ الطفل؟ وهي مفعول به منصوب وعلامة نصبه الفتحة!")
        else:
            st.error("❌ المحقق يقول: الإجابة غير دقيقة. اسأل نفسك: ماذا قرأ الطفل؟ الطفل قرأ 'قِصَّةً'. إذن 'قصةً' هي المفعول به!")

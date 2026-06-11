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
    </style>
""", unsafe_index=True)

# Initialisation des variables d'état (Session State) pour garder les scores et les questions
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "score" not in st.session_state:
    st.session_state.score = 0
if "calcul" not in st.session_state:
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    op = random.choice(['+', '-'])
    if op == '-' and n1 < n2: n1, n2 = n2, n1
    st.session_state.calcul = {"n1": n1, "n2": n2, "op": op, "res": n1+n2 if op=='+' else n1-n2}
if "mot" not in st.session_state:
    mots = [("مدرسة", "د"), ("قلم", "ل"), ("كتاب", "ت"), ("تفاحة", "ف"), ("بيت", "ي")]
    choisi, cache = random.choice(mots)
    st.session_state.mot = {"affiche": choisi.replace(cache, " _ ", 1), "lettre": cache, "complet": choisi}
if "culture" not in st.session_state:
    questions = [
        {"q": "ما هي عاصمة الجزائر؟", "r": "الجزائر"},
        {"q": "ما هو أكبر محيط في العالم؟", "r": "الهادي"},
        {"q": "كم عدد كواكب المجموعة الشمسية؟", "r": "8"},
        {"q": "ما هو الحيوان الذي يلقب بسفينة الصحراء؟", "r": "الجمل"}
    ]
    st.session_state.culture = random.choice(questions)

def changer_page(nom_page):
    st.session_state.page = nom_page

def generer_nouveau_calcul():
    n1, n2 = random.randint(1, 10), random.randint(1, 10)
    op = random.choice(['+', '-'])
    if op == '-' and n1 < n2: n1, n2 = n2, n1
    st.session_state.calcul = {"n1": n1, "n2": n2, "op": op, "res": n1+n2 if op=='+' else n1-n2}

def generer_nouveau_mot():
    mots = [("مدرسة", "د"), ("قلم", "ل"), ("كتاب", "ت"), ("تفاحة", "ف"), ("بيت", "ي")]
    choisi, cache = random.choice(mots)
    st.session_state.mot = {"affiche": choisi.replace(cache, " _ ", 1), "lettre": cache, "complet": choisi}

def generer_nouvelle_culture():
    questions = [
        {"q": "ما هي عاصمة الجزائر؟", "r": "الجزائر"},
        {"q": "ما هو أكبر محيط في العالم؟", "r": "الهادي"},
        {"q": "كم عدد كواكب المجموعة الشمسية؟", "r": "8"},
        {"q": "ما هو الحيوان الذي يلقب بسفينة الصحراء؟", "r": "الجمل"}
    ]
    st.session_state.culture = random.choice(questions)

# --- MENU PRINCIPAL ---
if st.session_state.page == "menu":
    st.markdown("<h1 style='text-align: center; color: #2C3E50;'>✨ قِصَّتِي دِرَاسَتِي ✨</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #7F8C8D;'>مرحباً بك يا بطل! اختر فئتك العمرية لنبدأ المغامرة:</h3>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧒 من 6 إلى 7 سنوات\n(حساب ومرح)", key="b1"):
            changer_page("6-7")
            st.rerun()
    with col2:
        if st.button("👦 من 8 إلى 9 سنوات\n(لغتي الجميلة)", key="b2"):
            changer_page("8-9")
            st.rerun()
            
    st.write("")
    if st.button("🧑 من 10 إلى 11 سنة\n(ذكاء وتحدي)", key="b3"):
        changer_page("10-11")
        st.rerun()

# --- CATÉGORIE 6-7 ANS ---
elif st.session_state.page == "6-7":
    if st.button("⬅ العودة للقائمة الرئيسية"):
        changer_page("menu")
        st.rerun()
        
    st.markdown("<h2 style='color: #FF7675;'>🧮 تحدي الحساب السريع</h2>", unsafe_allow_html=True)
    c = st.session_state.calcul
    st.write(f"### كم يساوي : {c['n1']} {c['op']} {c['n2']} ؟")
    
    reponse = st.text_input("أدخل إجابتك هنا :", key="input_6_7")
    if st.button("تحقق من الإجابة ✔️"):
        if reponse.strip() == str(c['res']):
            st.success("ممتاز ! 🎉 إجابة صحيحة يا بطل ! واصل هكذا .")
            generer_nouveau_calcul()
        else:
            st.error(f"خطأ ❌ الإجابة الصحيحة هي : {c['res']}")
            generer_nouveau_calcul()

# --- CATÉGORIE 8-9 ANS ---
elif st.session_state.page == "8-9":
    if st.button("⬅ العودة للقائمة الرئيسية"):
        changer_page("menu")
        st.rerun()
        
    st.markdown("<h2 style='color: #74B9FF;'>🔤 ابحث عن الحرف الناقص</h2>", unsafe_allow_html=True)
    m = st.session_state.mot
    st.write("### ما هو الحرف الناقص في الكلمة التالية :")
    st.markdown(f"<h1 style='text-align:center; color:#2980B9;'>{m['affiche']}</h1>", unsafe_allow_html=True)
    
    reponse = st.text_input("الحرف الناقص هو :", key="input_8_9")
    if st.button("تأكيد الحرف"):
        if reponse.strip() == m['lettre']:
            st.success(f"رائع ! 🌟 صحيح ! الكلمة هي : {m['complet']}")
            generer_nouveau_mot()
        else:
            st.error(f"حاول مجدداً 🧐 الكلمة الصحيحة هي : {m['complet']}")
            generer_nouveau_mot()

# --- CATÉGORIE 10-11 ANS ---
elif st.session_state.page == "10-11":
    if st.button("⬅ العودة للقائمة الرئيسية"):
        changer_page("menu")
        st.rerun()
        
    st.markdown("<h2 style='color: #55E6C1;'>🌍 بنك المعلومات والذكاء</h2>", unsafe_allow_html=True)
    q = st.session_state.culture
    st.write(f"### {q['q']}")
    
    reponse = st.text_input("إجابتك :", key="input_10_11")
    if st.button("إرسال الإجابة"):
        if reponse.strip() == q['r']:
            st.success("عبقري ! 🧠 إجابتك صحيحة وممتازة !")
            generer_nouvelle_culture()
        else:
            st.error(f"للأسف إجابة خاطئة. الإجابة الصحيحة هي : {q['r']}")
            generer_nouvelle_culture()

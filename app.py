import streamlit as st
import os
import sqlite3
import hashlib

# 1. إعداد قاعدة البيانات (مع إضافة تفادي مشاكل الخيوط المتعددة في Streamlit)
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, nom TEXT, prenom TEXT)')
conn.commit()

# وظائف تشفير كلمة المرور
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return True
    return False

# 2. إعداد الصفحة الأساسي بتصميم مريح
st.set_page_config(page_title="المنصة التعليمية قِصَّتِي دِرَاسَتِي", layout="wide")

# 3. تهيئة الحالة (Session State)
if "connecte" not in st.session_state:
    st.session_state.connecte = False
if "الصفحة_الحالية" not in st.session_state:
    st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
if "نقاط" not in st.session_state:
    st.session_state.نقاط = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
if "nom_eleve" not in st.session_state:
    st.session_state.nom_eleve = ""

# 4. وظيفة تسجيل الدخول أو إنشاء حساب بتصميم ملون
def afficher_login():
    st.markdown("<div class='login-header'>🔐 الدخول للمنصة التعليمية</div>", unsafe_allow_html=True)
    
    menu = ["💥 تسجيل الدخول", "✨ إنشاء حساب جديد", "🔑 استعادة كلمة المرور"]
    choice = st.sidebar.selectbox("📋 العمليات المتاحة", menu)

    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    if choice == "💥 تسجيل الدخول":
        st.markdown("<h3 style='color: #2E4057;'>👋 مرحباً بك مجدداً! سجل دخولك وابدأ المغامرة</h3>", unsafe_allow_html=True)
        email = st.text_input("👤 اسم المستخدم (الإيميل):")
        password = st.text_input("🔒 كلمة المرور:", type="password")
        
        if st.button("🚀 انطلق الآن"):
            # منطق دخول الأدمن المباشر
            if email == "abboumajda" and password == "iyed2023":
                st.session_state.connecte = True
                st.session_state.nom_eleve = "الأدمن (المعلم)"
                st.rerun()
            else:
                # التحقق من قاعدة البيانات للتلاميذ
                c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, make_hashes(password)))
                user = c.fetchone()
                if user:
                    st.session_state.connecte = True
                    st.session_state.nom_eleve = f"{user[3]} {user[2]}"
                    st.rerun()
                else:
                    st.error("❌ البريد أو كلمة المرور غير صحيحة، حاول مجدداً يا بطل!")

    elif choice == "✨ إنشاء حساب جديد":
        st.markdown("<h3 style='color: #2E4057;'>📝 انضم إلينا وأنشئ حسابك الخاص</h3>", unsafe_allow_html=True)
        nom = st.text_input("✍️ الاسم:")
        prenom = st.text_input("✍️ اللقب:")
        email = st.text_input("👤 اسم المستخدم المفضل:")
        password = st.text_input("🔒 اختر كلمة مرور قوية:", type="password")
        
        if st.button("🎉 تسجيل الحساب الجديد"):
            if nom and prenom and email and password:
                try:
                    c.execute('INSERT INTO users VALUES (?,?,?,?)', (email, make_hashes(password), prenom, nom))
                    conn.commit()
                    st.success("🎯 ممتاز! تم إنشاء حسابك بنجاح. يمكنك الآن الانتقال لخيار تسجيل الدخول.")
                except:
                    st.error("⚠️ اسم المستخدم هذا مسجل مسبقاً! اختر اسماً آخر.")
            else:
                st.warning("❗ يرجى ملء جميع الحقول أولاً.")

    elif choice == "🔑 استعادة كلمة المرور":
        st.markdown("<h3 style='color: #2E4057;'>🔍 استعادة الحساب</h3>", unsafe_allow_html=True)
        email = st.text_input("📧 أدخل بريدك الإلكتروني المسجل:")
        if st.button("🔍 تحقق من الحساب"):
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = c.fetchone()
            if user:
                st.info(f"ℹ️ تم العثور على حسابك بنجاح! يرجى التواصل مع إدارة المدرسة أو المعلم لاستلام كلمة المرور الخاصة بك.")
            else:
                st.error("❌ هذا الإيميل غير مسجل في المنصة.")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. قاموس الألعاب والأسئلة لجميع المستويات
محتوى_الألعاب = {
    "أقسام الكلمة": {
        1: {"سؤال": "ما هو نوع كلمة 'قلم'؟", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"},
        2: {"سؤال": "ما هو نوع كلمة 'يذهب'؟", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "فعل"},
        3: {"سؤال": "ما هو نوع الكلمة 'في'؟", "خيارات": ["اسم", "فعل", "حرف"], "إجابة": "حرف"},
        4: {"سؤال": "حدد الكلمة التي تمثل (فعلاً ماضياً):", "خيارات": ["كتبَ", "يكتبُ", "اكتبْ"], "إجابة": "كتبَ"},
        5: {"سؤال": "الاسم في الجملة التالية هو: (قَرَأَ الطَّالِبُ القِصَّةَ)", "خيارات": ["قرأ", "الطالب", "في"], "إجابة": "الطالب"}
    },
    "الجملة الاسمية والفعلية": {
        1: {"سؤال": "الجملة الاسمية تبدأ بـ:", "خيارات": ["فعل", "اسم", "حرف"], "إجابة": "اسم"},
        2: {"سؤال": "الجملة الفعلية تبدأ بـ:", "خيارات": ["اسم", "فعل", "حرف"], "إجابة": "فعل"},
        3: {"سؤال": "جملة (الْوَلَدُ نَشِيطٌ) هي جملة:", "خيارات": ["اسمية", "فعلية"], "إجابة": "اسمية"},
        4: {"سؤال": "جملة (يَشْرَحُ المُعَلِّمُ الدَّرْسَ) هي جملة:", "خيارات": ["اسمية", "فعلية"], "إجابة": "فعلية"},
        5: {"سؤال": "ما هو الركن الأول في الجملة الاسمية؟", "خيارات": ["الفاعل", "المبتدأ", "الخبر"], "إجابة": "المبتدأ"}
    }
}

# 6. الدوال الوظيفية وعرض الدروس المدعومة بالفيديو والأنيميشن
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 10, 1])
        with col2:
            st.image("logo.jpeg", width=1000)

def تشغيل_لعبة_الدرس(اسم_الدرس, مستوى_السنة):
    data = محتوى_الألعاب.get(اسم_الدرس, {}).get(مستوى_السنة)
    if data:
        st.markdown(f"<div style='background-color: #E8F5E9; padding: 20px; border-radius: 15px; border-right: 5px solid #4CAF50; margin-top: 20px;'>"
                    f"<h3 style='color: #2E7D32;'>🎮 تحدي الأبطال للمستوى {مستوى_السنة}:</h3>"
                    f"<p style='font-weight: bold; color: #1B5E20;'>{data['سؤال']}</p></div>", unsafe_allow_html=True)
        
        choix = st.radio("اختر إجابتك الصحيحة الذكية:", data['خيارات'], key=f"radio_{اسم_الدرس}_{مستوى_السنة}")
        
        if st.button("🎯 تحقق من إجابتي الحاسمة!", key=f"btn_check_{اسم_الدرس}_{مستوى_السنة}"):
            if choix == data['إجابة']:
                st.session_state.نقاط[مستوى_السنة] += 10
                st.success(f"🎉 ممتاز جداً! إجابة صحيحة وعبقرية.. حصلت على +10 نقاط!")
                st.balloons()
            else:
                st.error("❌ أوه! الإجابة غير صحيحة بالكامل. حاول مجدداً وركز جيدا يا بطل!")
    else:
        st.warning("⚠️ التحدي الخاص بهذا المستوى قيد التطوير والتحضير الفني حالياً.")

def عرض_محتوى_الدرس(اسم_الدرس):
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ قائمة الدروس", key=f"back_{اسم_الدرس}"):
            st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
            st.rerun()
            
    st.markdown(f"<h1 style='text-align: center; color: #4A90E2; background-color: #F0F4F8; padding: 15px; border-radius: 20px;'>📖 درس: {اسم_الدرس}</h1>", unsafe_allow_html=True)
    
    # إضافة الفيديوهات الكرتونية والأنيميشن التعليمية التفاعلية حسب نوع الدرس المطروح
    st.markdown("<h3 style='color: #D32F2F;'>🎬 شاهد الفيديو التعليمي والأنيميشن لتفهم درسك بذكاء:</h3>", unsafe_allow_html=True)
    if اسم_الدرس == "أقسام الكلمة":
        st.video("https://www.youtube.com/watch?v=CvTvx1TRYw4")
    elif اسم_الدرس == "الجملة الاسمية والفعلية":
        st.video("https://www.youtube.com/watch?v=IZ9Zq8CLdLU")
        
    st.markdown("<hr style='border: 1px dashed #4A90E2;'>", unsafe_allow_html=True)
    
    # اختيار المستوى وتجربة اللعبة التفاعلية
    annee = st.selectbox("🎯 اختر سنتك الدراسية الحالية لتجربة التحدي:", [1, 2, 3, 4, 5], key=f"select_{اسم_الدرس}")
    تشغيل_لعبة_الدرس(اسم_الدرس, annee)
    st.markdown("</div>", unsafe_allow_html=True)

def afficher_page_hamza():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    head_col1, head_col2 = st.columns([5, 1])
    with head_col1:
        st.markdown("<h1 style='color: #FF6F61; margin-top: 20px;'>✍️ قواعدي في قصتي الممتعة (قواعد الهمزة)</h1>", unsafe_allow_html=True)
    with head_col2:
        st.markdown("<div style='font-size: 80px; text-align: center;'>📝</div>", unsafe_allow_html=True)
    
    # إضافة أنيميشن لدرس الهمزة المتوسطة لتوضيح قوة الحركات للأطفال
    st.markdown("<h3 style='color: #D32F2F;'>🎬 أنيميشن كرتوني لدرس الهمزة وقوة الحركات:</h3>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=8bebUGwsYvw")
    
    tab1, tab2 = st.tabs(["📖 قصة صراع الحركات المشوقة", "✍️ ملخص قواعد الهمزة"])
    with tab1:
        st.markdown("<h3 style='text-align: center; color: #E67E22;'>📖 قصة: صراع الحركات في مدينة الهمزة السحرية</h3>", unsafe_allow_html=True)
        st.write("في مدينةِ الحروف والكلمات الجميلة، كانت الهمزةُ المتوسطة تعيشُ في حيرةٍ شديدة من أمرها، فهي لا تعرفُ فوق أي كرسي تجلس لترتاح! قررَت الحركات الأربع أن تقيمَ مسابقةً حماسية كبرى لتعرفَ من هي الحركة الأقوى والأجدر لتفوز بكرسي الهمزة وتحدد شكل جلوسها.")
        st.markdown("<div style='background-color: #FFF3E0; padding: 20px; border-radius: 15px; border-left: 5px solid #FF9800;'> "
                    "<h3>💡 سلم قوة الحركات الذهبي ونوع الكرسي المخصص:</h3>"
                    "<p>🥇 <b>الكسرة القوية جداً:</b> تجلس وتأمر بالجلوس على النبرة (ئـ)</p>"
                    "<p>🥈 <b>الضمة الشجاعة:</b> تجلس وتأمر بالجلوس على الواو (ؤ)</p>"
                    "<p>🥉 <b>الفتحة اللطيفة:</b> تجلس وتأمر بالجلوس على الألف (أ)</p>"
                    "<p>🏅 <b>السكون الهادئ والضعيف:</b> يجلس على السطر بكل هدوء (ء)</p></div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("### 🥊 جرب وبدأ التحدي والصراع بنفسك لترى القوة والانتصار:")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("💥 الكسرة ضد الضمة"):
                st.success("👑 الكسرة القوية الماهرة (ئـ) تهزم وتكسر الضمة وتجلس على النبرة!")
                st.balloons()
        with col_b:
            if st.button("💥 الفتحة ضد السكون"):
                st.success("👑 الفتحة اللطيفة (أ) تهزم السكون الضعيف وتجلس شموخاً على الألف!")
                st.snow()
    with tab2:
        st.markdown("<h3 style='text-align: center; color: #2ECC71;'>✍️ قواعد الهمزة الأساسية للسنة الرابعة والخامسة</h3>", unsafe_allow_html=True)
        st.markdown("<div style='line-height: 2;'>", unsafe_allow_html=True)
        st.write("✅ **1. الهمزة في أول الكلمة:** تكون إما همزة وصل مثل (ا) أو همزة قطع مثل (أ).")
        st.write("✅ **2. الهمزة المتوسطة:** نحددها بمقارنة حركتها مع حركة الحرف الذي يسبقها مباشرة ونختار الكرسي المناسب للحركة الأقوى.")
        st.write("✅ **3. الهمزة المتطرفة في آخر الكلمة:** تكتب مباشرة حسب الحركة الخاصة بالحرف الذي يسبقها فقط دون النظر لحركتها هي.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    if st.button("⬅️ العودة للقائمة الرئيسية للألعاب", key="back_hamza_btn"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def عرض_القواعد():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #E74C3C;'>🎬 سينما القواعد: مغامرة حارس غابة الكلمات</h2>", unsafe_allow_html=True)
    st.write("استمتع بمشاهدة العرض الكرتوني الشيق لتتعلم كيف تحمي الكلمات من الأخطاء اللغوية الإملائية والنحوية بكل سهولة:")
    st.video("https://www.youtube.com/watch?v=9_6A_M542u8")
    if st.button("⬅️ العودة للقائمة السابقة", key="back_cinema"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 7. تنسيق CSS المطور والمعدل بالألوان الزاهية لجذب اهتمام الأطفال والطلاب
css_style = """
<style>
    html, body, [data-testid="stAppViewContainer"] { 
        direction: rtl !important; 
        background-color: #F4F7F9;
    }
    .main-title {
        text-align: center; 
        color: #FFFFFF; 
        background: linear-gradient(45deg, #FF6F61, #4A90E2); 
        padding: 25px; 
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .login-header {
        text-align: center; 
        color: #FFFFFF; 
        background: linear-gradient(45deg, #2E4057, #1A252F); 
        padding: 15px; 
        border-radius: 15px;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .content-card { 
        background-color: #FFFFFF; 
        padding: 40px; 
        border-radius: 30px; 
        color: #333333; 
        text-align: justify !important; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 2px solid #EBF0F5;
    }
    h1, h2, h3, h4, p, li, div { 
        text-align: right !important; 
    }
    p, li, .stMarkdown { 
        font-size: 22px !important; 
        line-height: 1.8 !important; 
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        font-size: 18px !important;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF6F61;
        color: white;
        transform: scale(1.05);
    }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 8. المنطق الرئيسي للتحكم بالصفحات وتوجيه الطالب
if not st.session_state.connecte:
    afficher_login()
else:
    # إضافة زر تسجيل الخروج والترهيب في الأعلى بتصميم أنيق ومميز
    col_header, col_logout = st.columns([6, 1.5])
    with col_header:
        st.markdown("<div class='main-title'>🎈 المَنْصَةُ التَّعْلِيمِيَّةُ الرَّائِعَةُ: قِصَّتِي دِرَاسَتِي 🎈</div>", unsafe_allow_html=True)
    with col_logout:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚪 مغادرة وتسجيل الخروج"):
            st.session_state.connecte = False
            st.session_state.nom_eleve = ""
            st.rerun()

    st.markdown(f"<div style='background-color: #E3F2FD; padding: 15px; border-radius: 12px; border-right: 5px solid #2196F3; margin-bottom: 20px;'>"
                f"<h3 style='margin: 0; color: #0D47A1;'>🌟 أهلاً بك يا بطل/بطلة المستقبل العبقري: {st.session_state.nom_eleve}</h3></div>", unsafe_allow_html=True)
    
    if st.session_state.網絡_الحالية == "القائمة_الرئيسية":
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية" # لتفادي أي تعارض في الحالات

    if st.session_state.الصفحة_الحالية == "القائمة_الرئيسية":
        عرض_الشعار_الكبير()
        st.markdown("<h3 style='text-align: center; color: #7F8C8D;'>👇 اختر محطتك التعليمية التفاعلية وابدأ باللعب والتعلم:</h3>", unsafe_allow_html=True)
        
        c1, c2, c3, c4, c5 = st.columns(5)
        if c1.button("📚 درس أقسام الكلمة", key="b1"): 
            st.session_state.الصفحة_الحالية = "الدرس_الأول"
            st.rerun()
        if c2.button("🏰 الجملة الاسمية والفعلية", key="b2"): 
            st.session_state.الصفحة_الحالية = "الدرس_الثاني"
            st.rerun()
        if c3.button("✍️ قواعد الهمزة العجيبة", key="b4"): 
            st.session_state.الصفحة_الحالية = "Page_Hamza"
            st.rerun()
        if c4.button("🎬 حارس غابة الكلمات", key="b5"): 
            st.session_state.الصفحة_الحالية = "Cinema_Grammaire"
            st.rerun()
        if c5.button("🏆 لوحة أوسمة الإنجازات", key="b3"): 
            st.session_state.الصفحة_الحالية = "لوحة_الإنجازات"
            st.rerun()

    elif st.session_state.الصفحة_الحالية == "الدرس_الأول": 
        عرض_محتوى_الدرس("أقسام الكلمة")
    elif st.session_state.الصفحة_الحالية == "الدرس_الثاني": 
        عرض_محتوى_الدرس("الجملة الاسمية والفعلية")
    elif st.session_state.الصفحة_الحالية == "Page_Hamza": 
        afficher_page_hamza()
    elif st.session_state.الصفحة_الحالية == "Cinema_Grammaire": 
        عرض_القواعد()
    elif st.session_state.الصفحة_الحالية == "لوحة_الإنجازات":
        st.markdown("<div class='content-card'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #8E44AD;'>🏆 لوحة الأبطال وأوسمة الإنجازات المحققة</h2>", unsafe_allow_html=True)
        st.write("تابع عدد النقاط والنجاحات التي جمعتها في كل مستوى دراسي بفضل ذكائك:")
        
        for annee, score in st.session_state.نقاط.items():
            badge = "🌟 متميز ومتفوق!" if score > 0 else "⏳ بانتظار التحدي الأول"
            st.markdown(f"<div style='background-color: #F9F1FC; padding: 10px; margin: 5px 0; border-radius: 8px; border-right: 4px solid #9B59B6;'>"
                        f"<b>السنة الدراسية {annee}:</b> {score} نقطة مجتمعة {badge}</div>", unsafe_allow_html=True)
                        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⬅️ عودة إلى الشاشة الرئيسية", key="back_final"): 
            st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

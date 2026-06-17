import streamlit as st
import os
import sqlite3
import hashlib

# 1. إعداد قاعدة البيانات (تفادي مشاكل الخيوط المتعددة)
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

# 2. إعداد الصفحة الأساسي بتصميم مريح للأطفال
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
            if email == "abboumajda" and password == "iyed2023":
                st.session_state.connecte = True
                st.session_state.nom_eleve = "الأدمن (المعلم)"
                st.rerun()
            else:
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

# 6. الدوال الوظيفية وعرض الدروس المدعومة بالرسوم المتحركة التفاعلية
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
    
    # رسوم متحركة تفاعلية بديلة للفيديوهات الكلاسيكية
    st.markdown("<h3 style='color: #D32F2F;'>✨ تفاعل مع الكرتون المتحرك أدناه واكتشف السر:</h3>", unsafe_allow_html=True)
    
    if اسم_الدرس == "أقسام الكلمة":
        # تصميم رسم كرتوني متحرك لأقسام الكلمة يتفاعل عند مرور الفأرة
        cartoon_html = """
        <div style="display: flex; justify-content: space-around; align-items: center; background: #FFF9E6; padding: 30px; border-radius: 20px; border: 3px dashed #FFB300; margin-bottom: 20px;">
            <div class="cartoon-char character-noun">
                <div style="font-size: 50px;">🏷️</div>
                <div style="font-weight: bold; color: #E67E22; font-size: 24px;">أنا الاسْمُ</div>
                <div style="font-size: 14px; color: #555;">أدل على إنسان، حيوان أو شيء!</div>
            </div>
            <div class="cartoon-char character-verb">
                <div style="font-size: 50px;">🏃</div>
                <div style="font-weight: bold; color: #2ECC71; font-size: 24px;">أنا الفِعْلُ</div>
                <div style="font-size: 14px; color: #555;">أتحرك دائماً وأدل على عمل!</div>
            </div>
            <div class="cartoon-char character-particle">
                <div style="font-size: 50px;">🔗</div>
                <div style="font-weight: bold; color: #9B59B6; font-size: 24px;">أنا الحَرْفُ</div>
                <div style="font-size: 14px; color: #555;">أربط بين الإخوة الكلمات!</div>
            </div>
        </div>
        """
        st.markdown(cartoon_html, unsafe_allow_html=True)
        
    elif اسم_الدرس == "الجملة الاسمية والفعلية":
        # تصميم قطار كرتوني متحرك لتركيب الجمل
        cartoon_html = """
        <div style="background: #E0F7FA; padding: 30px; border-radius: 20px; border: 3px dashed #00ACC1; text-align: center; margin-bottom: 20px;">
            <div style="font-size: 28px; font-weight: bold; color: #006064; margin-bottom: 15px;">🚂 قطار الجمل السحري متحرك!</div>
            <div style="display: flex; justify-content: center; gap: 10px;">
                <div class="train-wagon wagon-blue">🏠 المبتدأ + 🌸 الخبر = 📜 جملة اسمية</div>
                <div style="font-size: 30px; linear-height: 50px;">↔️</div>
                <div class="train-wagon wagon-green">⚔️ الفعل + 🧑 الفاعل = 🎬 جملة فعلية</div>
            </div>
        </div>
        """
        st.markdown(cartoon_html, unsafe_allow_html=True)
        
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
    
    # لوحة كرتونية متحركة تفاعلية لقوة الحركات (بدل الفيديو)
    st.markdown("<h3 style='color: #D32F2F;'>👑 حلبة صراع الحركات الكرتونية - مرر الفأرة لترى البطل المكتسح:</h3>", unsafe_allow_html=True)
    
    hamza_cartoon = """
    <div style="display: flex; flex-direction: column; gap: 10px; background: #FFF3E0; padding: 25px; border-radius: 20px; border: 3px dashed #E67E22; margin-bottom: 20px;">
        <div class="rank-card rank-1">🥇 الحركة الأقوى: الكسرة ──> تجلس على النبرة (ئـ) 🔥</div>
        <div class="rank-card rank-2">🥈 المرتبة الثانية: الضمة ──> تجلس على الواو (ؤ) 💪</div>
        <div class="rank-card rank-3">🥉 المرتبة الثالثة: الفتحة ──> تجلس على الألف (أ) ✨</div>
        <div class="rank-card rank-4">🏅 المرتبة الأخيرة: السكون ──> يجلس المسكين على السطر (ء) 💤</div>
    </div>
    """
    st.markdown(hamza_cartoon, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 قصة صراع الحركات المشوقة", "✍️ ملخص قواعد الهمزة"])
    with tab1:
        st.markdown("<h3 style='text-align: center; color: #E67E22;'>📖 قصة: صراع الحركات في مدينة الهمزة السحرية</h3>", unsafe_allow_html=True)
        st.write("في مدينةِ الحروف والكلمات الجميلة، كانت الهمزةُ المتوسطة تعيشُ في حيرةٍ شديدة من أمرها، فهي لا تعرفُ فوق أي كرسي تجلس لترتاح! قررَت الحركات الأربع أن تقيمَ مسابقةً حماسية كبرى لتعرفَ من هي الحركة الأقوى والأجدر لتفوز بكرسي الهمزة وتحدد شكل جلوسها.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("### 🥊 اضغط على الأزرار لتبدأ الصراع الكرتوني التفاعلي مباشرة أمامك:")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("💥 الكسرة ضد الضمة"):
                st.success("👑 الكسرة القوية الماهرة (ئـ) تهزم وتكسر الضمة وتجلس شموخاً على النبرة!")
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
    st.markdown("<h2 style='text-align: center; color: #E74C3C;'>🎬 مسرح الكرتون التفاعلي: حارس غابة الكلمات</h2>", unsafe_allow_html=True)
    
    # تحويل السينما التقليدية لرسوم متحركة إبداعية كرتونية بالـ CSS
    cinema_html = """
    <div style="background: radial-gradient(circle, #34495e, #2c3e50); padding: 40px; border-radius: 25px; text-align: center; color: white; border: 4px solid #F1C40F;">
        <div style="font-size: 60px; animation: pulse 1s infinite alternate;">🕵️‍♂️🌳📜</div>
        <h3 style='color: #F1C40F; text-align: center !important;'>مرحباً بك في غابة الكلمات التفاعلية!</h3>
        <p style="color: #ECF0F1; text-align: center !important;">قوانين الحارس ذكي لحماية الحروف من الضياع:</p>
        <div style="display: inline-block; text-align: right; background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin-top: 10px;">
            ⭐ الحفاظ على الضوابط الإعرابية <br>
            ⭐ مراقبة الحركات الإملائية السليمة <br>
            ⭐ مساعدة التلميذ البطل في تجميع النقاط والbadges
        </div>
    </div>
    """
    st.markdown(cinema_html, unsafe_allow_html=True)
    
    if st.button("⬅️ العودة للقائمة السابقة", key="back_cinema"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 7. تنسيق CSS المطور لتشغيل رسوم كرتونية متحركة (Animations CSS)
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

    /* تأثيرات الرسوم المتحركة والرسومات الكرتونية التفاعلية */
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.03); }
    }
    
    .cartoon-char {
        background: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        cursor: pointer;
        animation: bounce 3s infinite ease-in-out;
    }
    .cartoon-char:hover {
        transform: scale(1.1) rotate(2deg);
        box-shadow: 0 12px 20px rgba(0,0,0,0.15);
    }
    
    .train-wagon {
        background: white;
        padding: 15px 30px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        animation: pulse 1.5s infinite alternate;
    }
    .wagon-blue { border-bottom: 5px solid #2196F3; color: #1565C0; }
    .wagon-green { border-bottom: 5px solid #4CAF50; color: #2E7D32; }

    .rank-card {
        padding: 15px;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        font-size: 20px;
        transition: transform 0.2s;
    }
    .rank-card:hover { transform: translateX(-10px); }
    .rank-1 { background: #E74C3C; }
    .rank-2 { background: #E67E22; }
    .rank-3 { background: #F1C40F; color: #333; }
    .rank-4 { background: #95A5A6; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 8. المنطق الرئيسي للتحكم بالصفحات وتوجيه الطالب
if not st.session_state.connecte:
    afficher_login()
else:
    # إضافة زر تسجيل الخروج بتصميم أنيق ومميز
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

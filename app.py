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

# 4. وظيفة تسجيل الدخول أو إنشاء حساب بتصميم ملون مبهج
def afficher_login():
    st.markdown("<div class='login-header'>🔐 الدخول للمنصة التعليمية مدرسة الأبطال</div>", unsafe_allow_html=True)
    
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

# 5. قاموس الألعاب والأسئلة لجميع المستويات الدراسية
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

# 6. الدوال الوظيفية وعرض الدروس المدعومة بالرسوم المتحركة التفاعلية السريعة
def عرض_الشعار_الكبير():
    if os.path.exists("logo.jpeg"):
        col1, col2, col3 = st.columns([1, 10, 1])
        with col2:
            st.image("logo.jpeg", width=1000)

def تشغيل_لعبة_الدرس(اسم_الدرس, مستوى_السنة):
    data = محتوى_الألعاب.get(اسم_الدرس, {}).get(مستوى_السنة)
    if data:
        st.markdown(f"<div class='question-box'>"
                    f"<h3 style='color: #1B5E20;'>🎮 تحدي الأبطال الذكي للمستوى {مستوى_السنة}:</h3>"
                    f"<p style='font-weight: bold; color: #2E7D32;'>{data['سؤال']}</p></div>", unsafe_allow_html=True)
        
        choix = st.radio("اختر إجابتك الصحيحة الفائزة:", data['خيارات'], key=f"radio_{اسم_الدرس}_{مستوى_السنة}")
        
        if st.button("🎯 تحقق من إجابتي الحاسمة!", key=f"btn_check_{اسم_الدرس}_{مستوى_السنة}"):
            if choix == data['إجابة']:
                st.session_state.نقاط[مستوى_السنة] += 10
                st.success(f"🎉 ممتاز جداً! إجابة صحيحة وعبقرية.. حصلت على +10 نقاط!")
                st.balloons()
            else:
                st.error("❌ أوه! الإجابة غير صحيحة بالكامل. حاول مجدداً وركز جيداً يا بطل غابة الكلمات!")
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
    
    if اسم_الدرس == "أقسام الكلمة":
        st.markdown("<h3 style='color: #D32F2F;'>✨ كرتون متحرك تفاعلي (مرر الفأرة فوق الحروف لرؤية الدوران والاهتزاز!):</h3>", unsafe_allow_html=True)
        # تصميم كرتوني متحرك مع تأثير دوران واهتزاز جذاب للغاية عند تمرير الماوس
        cartoon_html = """
        <div style="display: flex; justify-content: space-around; align-items: center; background: linear-gradient(135deg, #FFF9E6, #FFF0C2); padding: 30px; border-radius: 20px; border: 3px dashed #FFB300; margin-bottom: 25px; overflow: hidden;">
            <div class="cartoon-char character-noun animated-rotation">
                <div style="font-size: 60px; animation: bounce 2s infinite;">🏷️</div>
                <div style="font-weight: bold; color: #E67E22; font-size: 26px;">أنا الاسْمُ</div>
                <div style="font-size: 15px; color: #333; font-weight: bold;">أدل على إنسان، حيوان أو شيء!</div>
            </div>
            <div class="cartoon-char character-verb animated-vibrate">
                <div style="font-size: 60px; animation: bounce 1.5s infinite;">🏃</div>
                <div style="font-weight: bold; color: #2ECC71; font-size: 26px;">أنا الفِعْلُ</div>
                <div style="font-size: 15px; color: #333; font-weight: bold;">أتحرك دائماً ولا أتوقف أبداً!</div>
            </div>
            <div class="cartoon-char character-particle animated-rotation">
                <div style="font-size: 60px; animation: bounce 2.5s infinite;">🔗</div>
                <div style="font-weight: bold; color: #9B59B6; font-size: 26px;">أنا الحَرْفُ</div>
                <div style="font-size: 15px; color: #333; font-weight: bold;">أربط بين الإخوة الكلمات السحرية!</div>
            </div>
        </div>
        """
        st.markdown(cartoon_html, unsafe_allow_html=True)
        
    elif اسم_الدرس == "الجملة الاسمية والفعلية":
        st.markdown("<h3 style='color: #00ACC1;'>🚂 أنيميشن كرتوني سحري: شاهد قطار الجمل السريع وهو يسير!</h3>", unsafe_allow_html=True)
        # قطار حقيقي متحرك بالكامل يسير أفقياً من اليمين إلى اليسار بشكل تكراري ممتع للغاية
        cartoon_html = """
        <div class="train-track-container">
            <div class="moving-train-simulation">
                <span style="font-size: 50px;">🚂</span>
                <span class="train-wagon wagon-blue">🏠 المبتدأ + 🌸 الخبر = الجملة الاسمية</span>
                <span style="font-size: 40px;">🔗</span>
                <span class="train-wagon wagon-green">⚔️ الفعل + 🧑 الفاعل = الجملة الفعلية</span>
                <span style="font-size: 50px;">🚃💨</span>
            </div>
        </div>
        """
        st.markdown(cartoon_html, unsafe_allow_html=True)
        
    st.markdown("<hr style='border: 1px dashed #4A90E2;'>", unsafe_allow_html=True)
    
    # اختيار المستوى وتجربة اللعبة التفاعلية
    annee = st.selectbox("🎯 اختر سنتك الدراسية الحالية لتجربة التحدي المثير:", [1, 2, 3, 4, 5], key=f"select_{اسم_الدرس}")
    تشغيل_لعبة_الدرس(اسم_الدرس, annee)
    st.markdown("</div>", unsafe_allow_html=True)

def afficher_page_hamza():
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    head_col1, head_col2 = st.columns([5, 1])
    with head_col1:
        st.markdown("<h1 style='color: #FF6F61; margin-top: 20px;'>✍️ قواعدي في قصتي الممتعة (معركة الهمزة الكبرى)</h1>", unsafe_allow_html=True)
    with head_col2:
        st.markdown("<div style='font-size: 80px; text-align: center; animation: vibrate 0.5s infinite;'>📝</div>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: #D32F2F;'>👑 حلبة صراع الحركات الكرتونية - انزلاق الحركات عند مرور الفأرة واهتزاز الأبطال:</h3>", unsafe_allow_html=True)
    
    # لوحة كرتونية تفاعلية بحركات انزلاقية واهتزازية فريدة للأطفال
    hamza_cartoon = """
    <div style="display: flex; flex-direction: column; gap: 12px; background: #FFF3E0; padding: 25px; border-radius: 20px; border: 3px dashed #E67E22; margin-bottom: 25px; overflow: hidden;">
        <div class="rank-card rank-1 sliding-card">🥇 الحركة المكتسحة والأقوى: الكسرة ──> تجلس بقوة على النبرة (ئـ) 🔥</div>
        <div class="rank-card rank-2 sliding-card" style="animation-delay: 0.2s;">🥈 المرتبة الثانية الشجاعة: الضمة ──> تجلس ببطولة على الواو (ؤ) 💪</div>
        <div class="rank-card rank-3 sliding-card" style="animation-delay: 0.4s;">🥉 المرتبة الثالثة اللطيفة: الفتحة ──> تجلس بشموخ على الألف (أ) ✨</div>
        <div class="rank-card rank-4 sliding-card" style="animation-delay: 0.6s;">🏅 المرتبة الأخيرة الضعيفة: السكون ──> يجلس بهدوء على السطر (ء) 💤</div>
    </div>
    """
    st.markdown(hamza_cartoon, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📖 قصة صراع الحركات المشوقة", "✍️ ملخص قواعد الهمزة"])
    with tab1:
        st.markdown("<h3 style='text-align: center; color: #E67E22;'>📖 قصة: صراع الحركات في مدينة الهمزة السحرية</h3>", unsafe_allow_html=True)
        st.write("في مدينةِ الحروف والكلمات الجميلة، كانت الهمزةُ المتوسطة تعيشُ في حيرةٍ شديدة من أمرها، فهي لا تعرفُ فوق أي كرسي تجلس لترتاح! قررَت الحركات الأربع أن تقيمَ مسابقةً حماسية كبرى لتعرفَ من هي الحركة الأقوى والأجدر لتفوز بكرسي الهمزة وتحدد شكل جلوسها.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("### 🥊 اضغط على قفازات الملاكمة المهتزة لتبدأ الصراع الكرتوني التفاعلي فوراً:")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🥊 الكسرة ضد الضمة", key="fight1"):
                st.success("👑 الكسرة القوية الماهرة (ئـ) تهزم وتكسر الضمة تماماً وتستولي على كرسي النبرة!")
                st.balloons()
        with col_b:
            if st.button("🥊 الفتحة ضد السكون", key="fight2"):
                st.success("👑 الفتحة اللطيفة (أ) تسحق السكون الضعيف وتجلس بانتصار فوق الألف!")
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
    st.markdown("<h2 style='text-align: center; color: #E74C3C;'>🎬 مسرح الكرتون والسيارات السريعة: حارس غابة الكلمات</h2>", unsafe_allow_html=True)
    st.write("راقب الطريق غابة الكلمات التفاعلية السحرية وشاهد سيارة الحارس الذكي وهي تمر مسرعة لحماية القواعد لغوياً:")
    
    # سيارة كرتونية متحركة بالكامل تسير بشكل لامتناهي عبر الشاشة لتجسيد طلب المستخدم
    cinema_html = """
    <div style="background: radial-gradient(circle, #2c3e50, #1a252f); padding: 40px; border-radius: 25px; text-align: center; color: white; border: 4px solid #F1C40F; overflow: hidden; position: relative;">
        <div class="road-simulation-container">
            <div class="moving-car-simulation">🚗💨 🚙💨</div>
        </div>
        <h3 style='color: #F1C40F; text-align: center !important; margin-top: 20px;'>مرحباً بك في غابة الكلمات التفاعلية الآمنة!</h3>
        <p style="color: #ECF0F1; text-align: center !important;">قوانين سيارة حراسة الحروف لمنع الضياع والخطأ:</p>
        <div style="display: inline-block; text-align: right; background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin-top: 10px;">
            ⭐ الحفاظ على الضوابط الإعرابية النحوية السليمة <br>
            ⭐ مراقبة جودة الحركات الإملائية والهمزات بدون أخطاء <br>
            ⭐ قيادة سيارة المعرفة لجمع الأوسمة والنقاط المرتفعة
        </div>
    </div>
    """
    st.markdown(cinema_html, unsafe_allow_html=True)
    
    if st.button("⬅️ العودة للقائمة السابقة", key="back_cinema"):
        st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 7. التنسيق البرمجي الشامل لأقوى محرك رسوم متحركة (CSS Animation Engine) مخصص للطفل
css_style = """
<style>
    html, body, [data-testid="stAppViewContainer"] { 
        direction: rtl !important; 
        background-color: #F0F4F8;
    }
    .main-title {
        text-align: center; 
        color: #FFFFFF; 
        background: linear-gradient(45deg, #FF6F61, #4A90E2); 
        padding: 25px; 
        border-radius: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        margin-bottom: 25px;
        animation: pulse 2s infinite alternate;
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
        box-shadow: 0 12px 30px rgba(0,0,0,0.08);
        border: 2px solid #E6EEF4;
    }
    .question-box {
        background-color: #E8F5E9; 
        padding: 20px; 
        border-radius: 15px; 
        border-right: 6px solid #4CAF50; 
        margin-top: 20px;
        animation: pulse 1.5s infinite alternate;
    }
    h1, h2, h3, h4, p, li, div { 
        text-align: right !important; 
    }
    p, li, .stMarkdown { 
        font-size: 22px !important; 
        line-height: 1.8 !important; 
    }
    
    /* أزرار تفاعلية تهتز وتكبر بشكل رائع عند اللمس */
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        font-size: 19px !important;
        border-radius: 15px;
        padding: 12px 28px;
        border: none;
        box-shadow: 0 4px 10px rgba(74,144,226,0.3);
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .stButton>button:hover {
        background-color: #FF6F61;
        color: white;
        transform: scale(1.1) rotate(-1deg);
        box-shadow: 0 6px 15px rgba(255,111,97,0.4);
        animation: vibrate 0.2s infinite;
    }

    /* كود ومحركات الـ Keyframes للحركات والاهتزاز والقطار والسيارات */
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.02); }
    }
    @keyframes vibrate {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
    @keyframes continuousRotation {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    @keyframes trainMove {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    @keyframes carDrive {
        0% { transform: translateX(120%); }
        100% { transform: translateX(-120%); }
    }
    @keyframes slideIn {
        from { transform: translateX(100px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    /* الرسوم الكرتونية لأقسام الكلمة */
    .cartoon-char {
        background: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center !important;
        box-shadow: 0 8px 16px rgba(0,0,0,0.06);
        transition: all 0.4s ease;
        cursor: pointer;
    }
    .animated-rotation:hover {
        transform: scale(1.15) rotate(15deg);
        background: #FFF3E0;
    }
    .animated-vibrate:hover {
        animation: vibrate 0.15s infinite;
        transform: scale(1.15);
        background: #E8F5E9;
    }
    
    /* محاكاة مضمار القطار المتحرك السريع */
    .train-track-container {
        background: #E0F7FA; 
        padding: 25px; 
        border-radius: 20px; 
        border: 3px dashed #00ACC1; 
        position: relative; 
        overflow: hidden; 
        height: 110px;
        margin-bottom: 20px;
    }
    .moving-train-simulation {
        display: flex;
        align-items: center;
        gap: 15px;
        position: absolute;
        white-space: nowrap;
        animation: trainMove 12s linear infinite;
    }
    .train-wagon {
        background: white;
        padding: 12px 25px;
        border-radius: 15px;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 5px 10px rgba(0,0,0,0.05);
    }
    .wagon-blue { border-bottom: 6px solid #2196F3; color: #1565C0; }
    .wagon-green { border-bottom: 6px solid #4CAF50; color: #2E7D32; }

    /* محاكاة مضمار سيارة الشرطة والحراسة اللغوية */
    .road-simulation-container {
        background: #34495e;
        height: 60px;
        border-radius: 10px;
        position: relative;
        overflow: hidden;
        border-top: 3px dashed #f1c40f;
        border-bottom: 3px dashed #f1c40f;
        margin-bottom: 15px;
    }
    .moving-car-simulation {
        font-size: 35px;
        position: absolute;
        animation: carDrive 8s linear infinite;
        line-height: 55px;
    }

    /* انزلاقات أوراق تحدي الهمزة */
    .sliding-card {
        animation: slideIn 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
    }
    .rank-card {
        padding: 18px;
        border-radius: 12px;
        color: white;
        font-weight: bold;
        font-size: 21px;
        transition: all 0.3s ease;
    }
    .rank-card:hover { 
        transform: translateX(-15px) scale(1.02); 
        box-shadow: 0 5px 15px rgba(0,0,0,0.15);
    }
    .rank-1 { background: #E74C3C; border-left: 8px solid #C0392B; }
    .rank-2 { background: #E67E22; border-left: 8px solid #D35400; }
    .rank-3 { background: #F1C40F; color: #333; border-left: 8px solid #F39C12; }
    .rank-4 { background: #95A5A6; border-left: 8px solid #7F8C8D; }
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# 8. المنطق الرئيسي للتحكم بالصفحات وتوجيه الطالب الذكي بكل دقة
if not st.session_state.connecte:
    afficher_login()
else:
    # زر مغادرة المنصة والتسجيل للخروج في الأعلى
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

    # تصحيح السطر المطلوب وضمان ثبات الحالة
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
        st.write("تابع عدد النقاط والنجاحات التي جمعتها في كل مستوى دراسي بفضل ذكائك وجدارتك:")
        
        for annee, score in st.session_state.نقاط.items():
            badge = "🌟 متميز ومتفوق للغاية!" if score > 0 else "⏳ بانتظار التحدي الأول"
            st.markdown(f"<div style='background-color: #F9F1FC; padding: 10px; margin: 5px 0; border-radius: 8px; border-right: 4px solid #9B59B6;'>"
                        f"<b>السنة الدراسية {annee}:</b> {score} نقطة مجتمعة {badge}</div>", unsafe_allow_html=True)
                        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⬅️ عودة إلى الشاشة الرئيسية", key="back_final"): 
            st.session_state.الصفحة_الحالية = "القائمة_الرئيسية"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

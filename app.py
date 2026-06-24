import streamlit as st
import os
import sqlite3
import hashlib

# Masquer les éléments du menu supérieur (Share, Star, Edit, etc.)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .stAppDeployButton {display:none;}
            #stDecoration {display:none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 1. إعداد قاعدة البيانات (تفادي مشاكل الخيوط المتعددة) مع إضافة التفعيل
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT, nom TEXT, prenom TEXT, active INTEGER DEFAULT 0)')
# محاولة إضافة عمود التفعيل إذا كانت قاعدة البيانات القديمة موجودة
try:
    c.execute('ALTER TABLE users ADD COLUMN active INTEGER DEFAULT 0')
    conn.commit()
except:
    pass # العمود موجود مسبقاً
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

# 4. وظيفة تسجيل الدخول أو إنشاء حساب بتصميم ملون فائق البهجة والألوان
def afficher_login():
    # عنوان ملون بألوان قوس قزح الكرتونية المتدرجة المضيئة
    st.markdown("<div class='login-header'>✨ 🔐 بَوَّابَةُ الأَبْطَالِ: الدُّخُولُ إِلَى المَنَصَّةِ التَّعْلِيمِيَّةِ 🔐 ✨</div>", unsafe_allow_html=True)
    
    # خيارات القائمة الجانبية بتنسيق ملون
    menu = ["💥 تسجيل الدخول للمغامرة", "✨ إنشاء حساب بطل جديد", "🔑 استعادة كلمة المرور المفقودة"]
    choice = st.sidebar.selectbox("📋 اختر وجهتك السحرية اليوم:", menu)

    # كرت استقبال ملون للغاية وخلفية مبهجة للأطفال
    st.markdown("<div class='login-card-colorful'>", unsafe_allow_html=True)
    
    if choice == "💥 تسجيل الدخول للمغامرة":
        st.markdown("<h2 class='colorful-text-blue'>👋 مَرْحَباً بِكَ يَا بَطَلُ مُجَدَّداً!</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #4A5568; font-weight: bold;'>سجّل دخولك الآن وافتح صندوق المفاجآت والدروس المتحركة:</p>", unsafe_allow_html=True)
        
        email = st.text_input("👤 اسم المستخدم الخاص بك (الإيميل):", placeholder="أدخل اسمك هنا يا بطل...")
        password = st.text_input("🔒 كلمة المرور السرية العجيبة:", type="password", placeholder="أدخل رمزك السري هنا...")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 انْطَلِقْ فِي المَغَامَرَةِ الآنَ"):
            if email == "عبو" and password == "00":
                st.session_state.connecte = True
                st.session_state.nom_eleve = "الأدمن (المعلم)"
                st.rerun()
            else:
                c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, make_hashes(password)))
                user = c.fetchone()
                if user:
                    is_active = user[4]
                    if is_active == 1:
                        st.session_state.connecte = True
                        st.session_state.nom_eleve = f"{user[3]} {user[2]}"
                        st.rerun()
                    else:
                        st.warning("⚠️ حسابك مسجل ولكنه **غير مفعل بعد**! \n\nيرجى دفع رسوم التفعيل في حساب الـ CCP الخاص بالمعلم، ثم إرسال وصل الدفع عبر واتساب أو SMS إلى الرقم **0657011874** ليتم تفعيل حسابك فوراً.")
                else:
                    st.error("❌ أوه! البريد أو كلمة المرور غير صحيحة، حاول مجدداً وستنجح بالتأكيد يا بطل!")

    elif choice == "✨ إنشاء حساب بطل جديد":
        st.markdown("<h2 class='colorful-text-pink'>📝 صَنَاعَةُ حِسَابِ بَطَلٍ جَدِيدٍ</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #4A5568; font-weight: bold;'>انضم إلى أصدقائك الرائعين في غابة الكلمات التفاعلية:</p>", unsafe_allow_html=True)
        
        nom = st.text_input("✍️ اسمك الجميل:")
        prenom = st.text_input("✍️ لقبتك العائلي المتميز:")
        email = st.text_input("👤 اختر اسم مستخدم فريد (إيميل):")
        password = st.text_input("🔒 اختر كلمة مرور قوية وسهلة الحفظ بالنسبة لك:", type="password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🎉 تَسْجِيلُ الحِسَابِ الجَدِيدِ وَالِانْضِمَامُ"):
            if nom and prenom and email and password:
                try:
                    # إضافة الحساب مع حالة active = 0 (غير مفعل)
                    c.execute('INSERT INTO users VALUES (?,?,?,?,?)', (email, make_hashes(password), prenom, nom, 0))
                    conn.commit()
                    st.success("🎯 مذهل! تم إنشاء حسابك بنجاح، لكنه **يحتاج إلى تفعيل**.\n\n📱 يرجى دفع رسوم التفعيل (CCP)، ثم إرسال وصل الدفع عبر رسالة واتساب أو SMS إلى الرقم: **0657011874**.\n\nبمجرد التحقق، سيقوم المعلم بفتح أبواب المنصة لك!")
                except:
                    st.error("⚠️ اسم المستخدم هذا مأخوذ ومسجل مسبقاً! جرب إضافة رقم أو تغيير الاسم قليلاً.")
            else:
                st.warning("❗ يرجى ملء جميع الحقول والبيانات أولاً لتكتمل لوحة تسجيلك.")

    elif choice == "🔑 استعادة كلمة المرور المفقودة":
        st.markdown("<h2 class='colorful-text-orange'>🔍 المُحَقِّقُ الذَّكِيُّ: اِسْتِعَادَةُ الحِسَابِ</h2>", unsafe_allow_html=True)
        email = st.text_input("📧 أدخل بريدك الإلكتروني الذي سجلت به سابقاً:")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 بَدْءُ التَّحَقُّقِ السِّحْرِيِّ"):
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = c.fetchone()
            if user:
                st.info(f"ℹ️ وجدنا حسابك يا بطل! يرجى إخبار المعلم أو إدارة المدرسة لتزويدك بكلمة المرور الخاصة بك مباشرة.")
            else:
                st.error("❌ لم نجد هذا الإيميل مسجلاً لدينا في المنصة التعليمية الكرتونية.")
                
    st.markdown("</div>", unsafe_allow_html=True)
    
    # تذكير دائم بعنوان المنصة الإدارية الداعمة خلف الكواليس أسفل شاشة التسجيل
    st.markdown("<div style='text-align: center; color: #7F8C8D; font-size: 14px; margin-top: 30px; font-weight: bold;'>"
                ""
                "</div>", unsafe_allow_html=True)

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
    st.write("راقب طريق غابة الكلمات التفاعلية السحرية وشاهد سيارة الحارس الذكي وهي تمر مسرعة لحماية القواعد لغوياً:")
    
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

# 7. التنسيق البرمجي الشامل لأقوى محرك رسوم متحركة (CSS Animation Engine) مع تلوين فائق لصفحة التسجيل
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
    
    /* تصميم رأس صفحة الدخول والتسجيل بألوان قوس قزح الكرتونية المتدرجة والمتحركة */
    .login-header {
        text-align: center; 
        color: #FFFFFF; 
        background: linear-gradient(45deg, #FF1493, #FF4500, #FFD700, #32CD32, #00BFFF, #9370DB);
        background-size: 400% 400%;
        animation: rainbowGradient 8s ease infinite;
        padding: 20px; 
        border-radius: 25px;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 25px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* تصميم كرت التسجيل والاستقبال بألوان مبهجة وخلفية كرتونية جذابة للغاية */
    .login-card-colorful {
        background: linear-gradient(135deg, #FFF0F5 0%, #E6F2FF 100%);
        padding: 45px; 
        border-radius: 35px; 
        color: #333333; 
        text-align: right !important; 
        box-shadow: 0 15px 35px rgba(255, 105, 180, 0.15);
        border: 4px solid #FFB6C1;
        animation: cardFloat 4s ease-in-out infinite alternate;
    }
    
    /* نصوص ملونة وعناوين جذابة داخل صفحة التسجيل */
    .colorful-text-blue {
        color: #0080FF !important;
        background: linear-gradient(to left, #0052D4, #4364F7, #6FB1FC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
    }
    .colorful-text-pink {
        color: #FF007F !important;
        background: linear-gradient(to left, #FF007F, #FF4500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
    }
    .colorful-text-orange {
        color: #FF7F00 !important;
        background: linear-gradient(to left, #F857A6, #FF5858);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
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

    /* كود ومحركات الـ Keyframes للحركات والاهتزاز والقطار والسيارات وقوس قزح */
    @keyframes rainbowGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes cardFloat {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-10px); }
    }
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

    st.markdown(f"<div style='background-color: #E3F2FD; padding: 15px; border-radius: 12px; border-right: 5px solid #21

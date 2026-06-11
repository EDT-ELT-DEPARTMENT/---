# ==========================================
# 7. قسم السنوات الدراسية والبرنامج الوطني
# ==========================================
elif st.session_state.page == "البرنامج_الوطني":
    if st.button("⬅ العودة للمنزل", key="back_program"):
        st.session_state.page = "menu"
        st.rerun()

    afficher_logo_haut()
    st.markdown('<div class="board-title">📚 رِحْلَةُ القَوَاعِدِ حَسَبَ السَّنَوَاتِ 📚</div>', unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #57606F; font-weight: bold;'>اختر سنتك الدراسية واستكشف مغامرات القواعد المقررة لك:</h4>", unsafe_allow_html=True)
    st.write("")

    # إنشاء الأزرار التفاعلية للسنوات من 1 إلى 6
    col_y1, col_y2, col_y3 = st.columns(3)
    col_y4, col_y5, col_y6 = st.columns(3)

    with col_y1:
        year_1 = st.button("🌱 السنة الأولى ابتدائي", key="y1")
    with col_y2:
        year_2 = st.button("🌿 السنة الثانية ابتدائي", key="y2")
    with col_y3:
        year_3 = st.button("🍀 السنة الثالثة ابتدائي", key="y3")
    with col_y4:
        year_4 = st.button("🌳 السنة الرابعة ابتدائي", key="y4")
    with col_y5:
        year_5 = st.button("🌴 السنة الخامسة ابتدائي", key="y5")
    with col_y6:
        year_6 = st.button("👑 السنة السادسة ابتدائي", key="y6")

    # تهيئة متغير في الجلسة لتذكر السنة المختارة
    if "selected_year" not in st.session_state:
        st.session_state.selected_year = None

    if year_1: st.session_state.selected_year = 1
    if year_2: st.session_state.selected_year = 2
    if year_3: st.session_state.selected_year = 3
    if year_4: st.session_state.selected_year = 4
    if year_5: st.session_state.selected_year = 5
    if year_6: st.session_state.selected_year = 6

    # عرض الدروس ديناميكياً حسب السنة المختارة
    if st.session_state.selected_year is not None:
        st.write("---")
        y = st.session_state.selected_year
        
        if y == 1:
            st.markdown("<h3 style='color: #FF4757; text-align: center;'>🎯 دروس السنة الأولى: عوالم الحروف والكلمات الأولى</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #FF7675;">
                <p class="story-text">
                • <b>اكتشاف الحروف والكلمات:</b> التعرف على شكل الحرف وصوته.<br>
                • <b>الضمائر المنفصلة البسيطة:</b> أنا، أنتَ، أنتِ.<br>
                • <b>أسماء الإشارة للقريب:</b> هَذَا، هَذِهِ.<br>
                • <b>التراكيب الأساسية:</b> تركيب جمل قصيرة جداً (مثل: هَذَا كِتَابٌ).
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 2:
            st.markdown("<h3 style='color: #2E86DE; text-align: center;'>🎯 دروس السنة الثانية: بناء الجملة البسيطة</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #54A0FF;">
                <p class="story-text">
                • <b>ضمائر المتكلم والمخاطب والغائب:</b> (نحن، أنتم، هو، هي...).<br>
                • <b>أسماء الإشارة المتقدمة:</b> هَذَا، هَذِهِ، هَؤُلَاءِ.<br>
                • <b>أدوات الاستفهام المشهورة:</b> مَاذَا، مَنْ، كَيْفَ، أَيْنَ.<br>
                • <b>التحويل الصرفي البسيط:</b> تحويل الفعل مع ضمائر المفرد والجمع في الماضي.
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 3:
            st.markdown("<h3 style='color: #10AC84; text-align: center;'>🎯 دروس السنة الثالثة: مغامرة أقسام الكلمة</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #1DD1A1;">
                <p class="story-text">
                • <b>أقسام الكلمة بالتفصيل:</b> الاسم، الفعل، الحرف.<br>
                • <b>أنواع الفعل:</b> الماضي، المضارع، الأمر.<br>
                • <b>الجملة وعناصرها:</b> الجملة الاسمية والجملة الفعلية.<br>
                • <b>حروف الجر وحروف العطف:</b> (في، إلى، على / و، ف، ثم).
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 4:
            st.markdown("<h3 style='color: #FF9F43; text-align: center;'>🎯 دروس السنة الرابعة: حصن المرفوعات والمنصوبات</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #FECA57;">
                <p class="story-text">
                • <b>أركان الجملة الفِعلية:</b> الفعل والفاعل والمفعول به وعلامات الإعراب.<br>
                • <b>أركان الجملة الاسْمية:</b> المبتدأ والخبر وعلامة الرفع بالضمة.<br>
                • <b>الصفة والموصوف:</b> كيف تتبع الصفة الموصوف في التذكير والتأنيث.<br>
                • <b>المضاف والمضاف إليه:</b> التعرف على الاسم المجرور المضاف.
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 5:
            st.markdown("<h3 style='color: #9B59B6; text-align: center;'>🎯 دروس السنة الخامسة: أسرار النواسخ والمثنى والجمع</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #8E44AD;">
                <p class="story-text">
                • <b>النواسخ الفِعلية والحرفية:</b> كَانَ وأخواتها، إِنَّ وأخواتها وتأثيرها على الجمل.<br>
                • <b>علامات الإعراب الفرعية:</b> المثنى (الألف والياء)، وجمع المذكر السالم (الواو والياء).<br>
                • <b>الأسماء الخمسة:</b> (أبو، أخو...) وعلامات إعرابها الخاصة.<br>
                • <b>المفاعيل:</b> المفعول المطلق، والمفعول لأجله.
                </p>
            </div>
            """, unsafe_allow_html=True)

        elif y == 6:
            st.markdown("<h3 style='color: #D35400; text-align: center;'>🎯 دروس السنة السادسة: إتقان التراكيب والصرف المتقدم</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="cartoon-box" style="border-color: #E67E22;">
                <p class="story-text">
                • <b>إعراب الفعل المضارع:</b> رفعه، جَزمه (أدوات الجزم)، ونصبه (أدوات النصب).<br>
                • <b>الأفعال الخمسة:</b> ثبوت النون وحذفها.<br>
                • <b>المجرد والمزيد من الأفعال:</b> ميزان الصرف الاستكشافي.<br>
                • <b>المنصوبات المتقدمة:</b> الحال والجملة الحالية، والتمييز (الملفوظ والملحوظ).
                </p>
            </div>
            """, unsafe_allow_html=True)

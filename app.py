# ------------------------------------------
# د. المغامرة الثالثة : لغز المفعول به (كود مصحح)
# ------------------------------------------
elif st.session_state.page == "lesson3":
    afficher_logo_haut()
    if st.button("⬅ العودة للمنزل", key="back_3"):
        st.session_state.page = "menu"
        st.rerun()
        
    st.markdown("<h2 style='color: #10AC84; text-align: center; font-weight: 900;'>🎬 قصة متحركة: قضية المحقق كَانَمُون</h2>", unsafe_allow_html=True)
    
    html_story_3 = """
    <div class="cartoon-box">
        <div class="story-title" style="color: #10AC84;">🔍 لغز الكلمة المفقودة</div>
        <p class="story-text">
        🕵️‍♂️ المحقق الذكي <b>كَانَمُون</b> يمسك بعدسته ويبحث عن سر اختفاء كلمة وقع عليها الفعل المذكور!<br>
        قال: لدينا الفعل (قَرَأَ) والفاعل الذي قام بالعمل وهو (الطِّفْلُ).. لكن ماذا قرأ الطفل؟! <br><br>
        🎯 وفجأة ظهر <b>المَفْعُولُ بِهِ</b> وهو يضحك ويقول: أنا الاسم المنصوب بالفتحة، وأنا الذي وقع عليّ فعل الفاعل! لمعرفتي دائماً اسأل الفاعل بـ: <b>مَاذَا؟</b>
        </p>
    </div>
    """
    st.markdown(html_story_3, unsafe_allow_html=True)
    
    st.write("### 🎮 ساعد المحقق في حل القضية:")
    st.markdown("<h2 style='text-align: center; color: white; background: #10AC84; padding: 15px; border-radius: 20px;'>الجملة: « قَرَأَ الطِّفْلُ قِصَّةً جَمِيلَةً »</h2>", unsafe_allow_html=True)
    st.write("")

    ca1, ca2, ca3 = st.columns(3)
    with ca1:
        if st.button("قَرَأَ 📖", key="ca1"): st.session_state.ans_lesson3 = "v"
    with ca2:
        if st.button("الطِّفْلُ 🧒", key="ca2"): st.session_state.ans_lesson3 = "f"
    with ca3:
        if st.button("قِصَّةً 📚", key="ca3"):
            st.session_state.ans_lesson3 = "m"
            st.session_state.score_lesson3 = True
            
    # استخدام Triple Quotes للنصوص الطويلة لتجنب خطأ SyntaxError
    if st.session_state.ans_lesson3 == "m":
        st.success("""🎯 قضية ناجحة! 'قِصَّةً' هي الإجابة عن سؤال (ماذا قرأ الطفل؟)، مفعول به منصوب بالفتحة!""")
    elif st.session_state.ans_lesson3 == "v":
        st.warning("""❌ لا يا سيادة المحقق! 'قَرَأَ' هو الفعل وعملية القراءة نفسها وليس الركن المنصوب.""")
    elif st.session_state.ans_lesson3 == "f":
        st.warning("""❌ ركز! 'الطِّفْلُ' هو الفاعل البطل الذي قرأ القصة وليس المفعول به.""")

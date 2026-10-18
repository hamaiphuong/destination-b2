import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Destination C1 & C2 Self-Study Hub",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        color: #1E3A8A;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 1.8rem;
    }
    .card {
        background-color: #F8FAFC;
        padding: 1.2rem;
        border-radius: 0.6rem;
        border-left: 5px solid #2563EB;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .watchout-box {
        background-color: #FEF2F2;
        border: 1px solid #FCA5A5;
        border-left: 5px solid #EF4444;
        padding: 1.2rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .tip-box {
        background-color: #F0FDF4;
        border: 1px solid #86EFAC;
        border-left: 5px solid #22C55E;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .badge-grammar {
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 0.2rem 0.6rem;
        border-radius: 0.3rem;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .badge-vocab {
        background-color: #FCE7F3;
        color: #9D174D;
        padding: 0.2rem 0.6rem;
        border-radius: 0.3rem;
        font-size: 0.85rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">📘 DESTINATION C1 & C2: LEARNING HUB</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Hệ thống Tự học Ngữ pháp & Từ vựng Nâng cao (Advanced C1 & C2 Proficiency)</div>', unsafe_allow_html=True)

st.sidebar.title("📌 MENU CHÍNH")
menu_option = st.sidebar.radio(
    "Chọn chức năng:",
    [
        "📌 Tổng quan & Lộ trình tự học",
        "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)",
        "✍️ Bài tập Tương tác & Chấm điểm tự động",
        "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)",
        "⚠️ Góc lưu ý (Watch Out! Corner)",
        "📊 Báo cáo Tiến độ Học tập"
    ]
)

if menu_option == "📌 Tổng quan & Lộ trình tự học":
    st.header("📌 Tổng quan Sách & Lộ trình Tự học")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### 📚 Cấu trúc bộ sách Destination C1 & C2
        Sách gồm **26 Units** đan xen giữa Ngữ pháp và Từ vựng nâng cao, đáp ứng chuẩn đầu ra kỳ thi **Cambridge CAE (C1)** & **CPE (C2)**:
        
        * **13 Unit Ngữ pháp (Grammar Units)**: Hệ thống quy tắc chuyên sâu, cấu trúc câu nâng cao và các ngoại lệ.
        * **13 Unit Từ vựng (Vocabulary Units)**: Phân loại từ vựng theo chủ đề (*Topic Vocabulary*), Cụm động từ (*Phrasal Verbs*), Thành ngữ (*Idioms*), Cụm từ cố định (*Collocations*) và Cấu tạo từ (*Word Formation*).
        * **13 Bài Ôn tập (Reviews)**: Ôn tập định kỳ sau mỗi 2 Units.
        * **Bài kiểm tra Tiến độ & Tổng hợp**: 2 bài *Progress Tests* và 6 bài *Revision Tests* hệ thống lại kiến thức.
        """)
        
        st.markdown("""
        ### 🗺️ Lộ trình 4 bước tự học thẩm thấu kiến thức
        1. **Bước 1 (Theory Hub)**: Nắm vững bảng lý thuyết ngữ pháp và danh mục từ vựng chuẩn Cambridge.
        2. **Bước 2 (Watch Out! Corner)**: Điểm lại các bẫy ngữ pháp và lỗi sai phổ biến mà thí sinh C1/C2 thường mắc phải.
        3. **Bước 3 (Interactive Quiz)**: Luyện tập bài tập tương tác, kiểm tra đáp án tự động và đọc giải thích chi tiết.
        4. **Bước 4 (Flashcards)**: Ôn luyện phản xạ từ vựng hàng ngày bằng thẻ ghi nhớ thông minh.
        """)

    with col2:
        st.info("📋 **SƠ ĐỒ 26 UNITS TRONG SÁCH**")
        
        units_data = [
            {"Unit": "Unit 1", "Type": "Grammar", "Topic": "Present time"},
            {"Unit": "Unit 2", "Type": "Vocabulary", "Topic": "Thinking and learning"},
            {"Unit": "Unit 3", "Type": "Grammar", "Topic": "Past time"},
            {"Unit": "Unit 4", "Type": "Vocabulary", "Topic": "Change and technology"},
            {"Unit": "Unit 5", "Type": "Grammar", "Topic": "Future time"},
            {"Unit": "Unit 6", "Type": "Vocabulary", "Topic": "Time and work"},
            {"Unit": "Unit 7", "Type": "Grammar", "Topic": "Passives and causatives"},
            {"Unit": "Unit 8", "Type": "Vocabulary", "Topic": "Movement and transport"},
            {"Unit": "Unit 9", "Type": "Grammar", "Topic": "Modals and semi-modals"},
            {"Unit": "Unit 10", "Type": "Vocabulary", "Topic": "Communication and the media"},
            {"Unit": "Unit 11", "Type": "Grammar", "Topic": "Conditionals"},
            {"Unit": "Unit 12", "Type": "Vocabulary", "Topic": "Chance and nature"},
            {"Unit": "Unit 13", "Type": "Grammar", "Topic": "Unreal time"},
            {"Unit": "Unit 14", "Type": "Vocabulary", "Topic": "Quantity and money"}
        ]
        df_units = pd.DataFrame(units_data)
        st.dataframe(df_units, use_container_width=True, height=380)

elif menu_option == "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)":
    st.header("📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)")
    
    selected_unit = st.selectbox(
        "🎯 Chọn Unit cần tra cứu:",
        [
            "Unit 1: Grammar - Present time",
            "Unit 2: Vocabulary - Thinking and learning",
            "Unit 3: Grammar - Past time (Đang cập nhật)",
            "Unit 4: Vocabulary - Change and technology (Đang cập nhật)"
        ]
    )
    
    if "Unit 1" in selected_unit:
        st.subheader("Unit 1: Present time (Các thì Hiện tại)")
        
        tab_g1, tab_g2, tab_g3, tab_g4, tab_stative = st.tabs([
            "1. Present Simple & Emphatic",
            "2. Present Continuous",
            "3. Present Perfect Simple",
            "4. Present Perfect Continuous",
            "5. Stative Verbs & US/UK Notes"
        ])
        
        with tab_g1:
            st.markdown("#### 🔹 Present Simple (Thì Hiện tại Đơn)")
            g1_data = [
                {"Cách dùng": "General truths (Sự thật hiển nhiên)", "Ví dụ minh họa": "The left-hand side of the brain controls the right-hand side of the body."},
                {"Cách dùng": "Current habits (Thói quen hiện tại)", "Ví dụ minh họa": "I don't always go to lectures that are early in the morning!"},
                {"Cách dùng": "Permanent situations & states (Tình trạng lâu dài)", "Ví dụ minh họa": "Angie teaches French at a local adult education centre."},
                {"Cách dùng": "Telling jokes & informal stories (Kể chuyện phiếm)", "Ví dụ minh họa": "So, a man goes to see his psychiatrist..."},
                {"Cách dùng": "Live sports commentary (Bình luận trực tiếp)", "Ví dụ minh họa": "Adams passes to Kareshi. It's a goal!"},
                {"Cách dùng": "Newspaper headlines (Tiêu đề báo chí)", "Ví dụ minh họa": "HAWKING WINS NOBEL PRIZE"},
                {"Cách dùng": "Reviews & summaries (Tóm tắt phim/sách)", "Ví dụ minh họa": "The film ends with us not knowing whether they survived."},
                {"Cách dùng": "Instructions & directions (Hướng dẫn chỉ đường)", "Ví dụ minh họa": "You turn left at the end of the road."},
                {"Cách dùng": "Proverbs & sayings (Tục ngữ, thành ngữ)", "Ví dụ minh họa": "Too many cooks spoil the broth."},
                {"Cách dùng": "Fixed future events (Lịch trình cố định)", "Ví dụ minh họa": "Term ends on 21st December."}
            ]
            st.table(pd.DataFrame(g1_data))
            
            st.markdown("""
            <div class="tip-box">
            <b>💡 Emphatic Present Simple (Hiện tại đơn nhấn mạnh):</b><br>
            Sử dụng <code>do / does + V-bare</code> để nhấn mạnh sự tương phản hoặc cảm xúc mạnh mẽ:<br>
            • <i>Adam doesn't know much about psychiatry but he <b>does know</b> quite a lot about psychology.</i><br>
            • <i>I <b>do like</b> playing word games!</i>
            </div>
            """, unsafe_allow_html=True)
            
            st.caption("Từ/Cụm từ hay đi kèm: always, usually, generally, often, sometimes, rarely, seldom, never, whenever, nowadays, these days, from time to time, every now and then, most/much of the time.")

        with tab_g2:
            st.markdown("#### 🔹 Present Continuous (Thì Hiện tại Tiếp diễn)")
            g2_data = [
                {"Cách dùng": "Actions happening now (Hành động đang diễn ra)", "Ví dụ minh họa": "The boys are doing their homework right now."},
                {"Cách dùng": "Actions happening around now (Hành động xung quanh hiện tại)", "Ví dụ minh họa": "What book are you doing in English at the moment?"},
                {"Cách dùng": "Temporary situations (Tình huống tạm thời)", "Ví dụ minh họa": "We aren't having any exams while the lecturers are on strike."},
                {"Cách dùng": "Changing & developing situations (Sự thay đổi phát triển)", "Ví dụ minh họa": "More and more people are recognising the advantages of learning languages."},
                {"Cách dùng": "Annoying / amusing habits with 'always' (Thói quen gây phiền phức)", "Ví dụ minh họa": "Dan's always coming up with the craziest ideas!"},
                {"Cách dùng": "Future arrangements (Kế hoạch tương lai đã sắp xếp)", "Ví dụ minh họa": "When are you taking your driving test?"}
            ]
            st.table(pd.DataFrame(g2_data))

        with tab_g3:
            st.markdown("#### 🔹 Present Perfect Simple (Thì Hiện tại Hoàn thành Đơn)")
            g3_data = [
                {"Cách dùng": "Situations/states started in past & still true (Kéo dài đến hiện tại)", "Ví dụ minh họa": "I've been a member of MENSA for over five years."},
                {"Cách dùng": "Series of actions continuing up to now (Chuỗi hành động)", "Ví dụ minh họa": "She's done a BA, an MA and a PhD so far."},
                {"Cách dùng": "Completed actions at unspecified past time (Đã xong, không rõ thời gian)", "Ví dụ minh họa": "Have you ever read any books by Edward De Bono?"},
                {"Cách dùng": "Completed actions with important present result (Kết quả ở hiện tại)", "Ví dụ minh họa": "She's been awarded a scholarship to study at Harvard."},
                {"Cách dùng": "Actions completed recently (Vừa mới hoàn thành)", "Ví dụ minh họa": "I've just received my exam results."}
            ]
            st.table(pd.DataFrame(g3_data))

        with tab_g4:
            st.markdown("#### 🔹 Present Perfect Continuous (Thì Hiện tại Hoàn thành Tiếp diễn)")
            g4_data = [
                {"Cách dùng": "Actions continuing up to present / just before present (Nhấn mạnh tính liên tục/thời lượng)", "Ví dụ minh họa": "We've all been wondering what to get Tony for his birthday."},
                {"Cách dùng": "Future in time clauses (Hành động hoàn thành trong mệnh đề thời gian)", "Ví dụ minh họa": "I won't take my driving test until I've been having lessons for two months."}
            ]
            st.table(pd.DataFrame(g4_data))

        with tab_stative:
            st.markdown("#### 🔹 Stative Verbs (Động từ Chỉ Trạng thái)")
            st.write("Động từ chỉ trạng thái thường **không** dùng ở thì tiếp diễn:")
            
            st.markdown("""
            * **Communication**: agree, deny, disagree
            * **Thinking**: believe, consider, doubt, expect, imagine, know, mean, realise, suppose, suspect, think, understand
            * **Existence**: be, exist
            * **Emotions**: adore, appeal, appreciate, desire, despise, detest, dislike, envy, fear, feel, forgive, hate, like, love, mind, need, pity, prefer, satisfy, trust, want, wish
            * **Perception**: appear, hear, look, notice, recognise, resemble, see, seem, smell, sound, taste
            * **Possession**: belong, concern, consist, contain, cost, depend, equal, fit, have, include, lack, measure, owe, own, possess, suit, weigh
            * **Other**: deserve, matter
            """)
            
            st.markdown("""
            <div class="watchout-box">
            <b>⚠️ Động từ vừa là Stative vừa là Dynamic (Action):</b><br>
            Các động từ như <i>appeal, be, consider, depend, feel, have, include, look, mean, mind, see, smell, taste, think, weigh</i> có thể dùng ở thì tiếp diễn khi diễn tả <b>hành động</b> thay vì trạng thái:<br>
            • <i>I <b>think</b> it's important to know how to use a computer.</i> (Trạng thái: think = believe)<br>
            • <i>I'm <b>thinking</b> about going on a computer course.</i> (Hành động: think = consider)
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("#### 🇺🇸 US vs 🇬🇧 UK Grammar Differences")
            st.info("""
            * Trong tiếng Anh-Mỹ (US), Thì Quá khứ đơn thường được dùng thay cho Hiện tại hoàn thành:
              * US: Did you find the answer yet? | UK: Have you found the answer yet?
            * Trong tiếng Anh-Mỹ thân mật, **gotten** được dùng làm quá khứ phân từ của *get* (nghĩa là obtain/become/move):
              * US: I haven't gotten the books yet. | UK: I haven't got the books yet.
            """)

    elif "Unit 2" in selected_unit:
        st.subheader("Unit 2: Vocabulary - Thinking and learning")
        st.write("Danh mục từ vựng, Phrasal Verbs, Idioms, Word Formation kèm phiên âm IPA, Định nghĩa tiếng Anh & Nghĩa tiếng Việt (Tra cứu cuối sách):")
        
        vocab_list = [
            {"Word": "assess (v)", "IPA": "/əˈses/", "Definition": "to carefully consider a situation, person or problem in order to make a judgment", "Vietnamese": "đánh giá, định giá", "Example": "We need to assess the impact of the new policy."},
            {"Word": "baffle (v)", "IPA": "/ˈbæf.əl/", "Definition": "if a problem or someone's behaviour baffles you, it is so confused or strange that you cannot understand it", "Vietnamese": "làm cản trở, gây khó hiểu", "Example": "His sudden decision to quit baffled everyone."},
            {"Word": "cynical (adj)", "IPA": "/ˈsɪn.ɪ.kəl/", "Definition": "believing that people are only interested in themselves and are not honest or sincere", "Vietnamese": "hoài nghi, nhạo đời", "Example": "I'm a bit cynical about their motives."},
            {"Word": "deduce (v)", "IPA": "/dɪˈdjuːs/", "Definition": "to know something by considering the information or evidence that you have", "Vietnamese": "suy luận, suy ra", "Example": "Finding the bloody weapon allowed the police to deduce that a murder had occurred."},
            {"Word": "dubious (adj)", "IPA": "/ˈdʒuː.bi.əs/", "Definition": "thought not to be completely true or not able to be trusted", "Vietnamese": "mơ hồ, đáng nghi ngờ", "Example": "The story was dynamic, but its authenticity remained dubious."},
            {"Word": "mull over (phr v)", "IPA": "/mʌl ˈəʊ.vər/", "Definition": "to think carefully about something for a long time", "Vietnamese": "suy ngẫm, cân nhắc kỹ", "Example": "I'll mull over your proposal this weekend."},
            {"Word": "ring a bell (idiom)", "IPA": "/rɪŋ ə bel/", "Definition": "sounds familiar, but you cannot remember the exact details", "Vietnamese": "nghe quen thuộc", "Example": "Her name rings a bell, but I can't place her."}
        ]
        st.table(pd.DataFrame(vocab_list))

elif menu_option == "✍️ Bài tập Tương tác & Chấm điểm tự động":
    st.header("✍️ Bài tập Tương tác Unit 1: Present time")
    st.write("Trích lọc hệ thống câu hỏi bài tập từ Unit 1 với đáp án chuẩn cuối sách và lời giải thích chi tiết.")
    
    with st.form("quiz_unit1_form"):
        st.markdown("#### 📝 Exercise A: Write the verb in brackets in the correct form (Present Simple or Present Continuous)")
        
        q1 = st.text_input("1. My brother ________ (do) a degree at university so I don't see him very often, unfortunately.", key="q1")
        q2 = st.text_input("2. Darren usually ________ (get) home until about eight o'clock.", key="q2")
        q3 = st.radio("3. Why ________ ice ________ (float)?", ["does / float", "is / floating", "do / floats"], key="q3")
        q4 = st.radio("4. I think I ________ (recognise) that woman over there. Wasn't she on that quiz show?", ["recognise", "am recognising", "recognised"], key="q4")
        q5 = st.radio("5. Could you explain what 'antidisestablishmentarianism' ________ (mean), please?", ["means", "is meaning", "mean"], key="q5")
        
        st.markdown("#### 📝 Exercise G: Circle the correct word or phrase (Present Perfect Simple vs Continuous)")
        q6 = st.radio("6. They ________ six bags with rubbish from the beach already.", ["have filled", "have been filling", "fill"], key="q6")
        q7 = st.radio("7. I ________ up all day and my feet are killing me!", ["have been standing", "have stood", "am standing"], key="q7")

        submit_quiz = st.form_submit_button("🚀 Nộp bài & Kiểm tra Đáp án")

    if submit_quiz:
        score = 0
        total = 7
        st.subheader("📊 Kết quả & Giải thích Đáp án (Answer Key)")
        
        if q1.strip().lower() in ["is doing", "'s doing"]:
            score += 1
            st.success("✅ Câu 1 đúng! (is doing)")
        else:
            st.error("❌ Câu 1 sai! Đáp án đúng: **is doing**. (Giải thích: Tình huống học tập tạm thời kéo dài xung quanh hiện tại).")
            
        if q2.strip().lower() in ["doesn't get", "does not get", "doesn't usually get", "does not usually get"]:
            score += 1
            st.success("✅ Câu 2 đúng! (doesn't usually get)")
        else:
            st.error("❌ Câu 2 sai! Đáp án đúng: **doesn't usually get**. (Giải thích: Thói quen sinh hoạt lặp đi lặp lại).")
            
        if q3 == "does / float":
            score += 1
            st.success("✅ Câu 3 đúng! (does / float)")
        else:
            st.error("❌ Câu 3 sai! Đáp án đúng: **does / float**. (Giải thích: Sự thật khoa học hiển nhiên).")

        if q4 == "recognise":
            score += 1
            st.success("✅ Câu 4 đúng! (recognise)")
        else:
            st.error("❌ Câu 4 sai! Đáp án đúng: **recognise**. (Giải thích: Động từ nhận thức stative verb không dùng tiếp diễn).")

        if q5 == "means":
            score += 1
            st.success("✅ Câu 5 đúng! (means)")
        else:
            st.error("❌ Câu 5 sai! Đáp án đúng: **means**. (Giải thích: Động từ chỉ ý nghĩa stative verb).")

        if q6 == "have filled":
            score += 1
            st.success("✅ Câu 6 đúng! (have filled)")
        else:
            st.error("❌ Câu 6 sai! Đáp án đúng: **have filled**. (Giải thích: Nhấn mạnh kết quả con số cụ thể 'six bags').")

        if q7 == "have been standing":
            score += 1
            st.success("✅ Câu 7 đúng! (have been standing)")
        else:
            st.error("❌ Câu 7 sai! Đáp án đúng: **have been standing**. (Giải thích: Nhấn mạnh tính liên tục của hành động kéo dài 'all day').")

        percent = int((score / total) * 100)
        st.info(f"🏆 Điểm số của bạn: **{score}/{total}** ({percent}%)")
        if percent == 100:
            st.balloons()

elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng C1/C2 (Vocabulary Flashcards)")
    st.write("Lật thẻ để ghi nhớ Từ vựng, Phiên âm IPA, Định nghĩa tiếng Anh, Nghĩa tiếng Việt và Ví dụ ngữ cảnh.")
    
    flashcards_data = [
        {
            "word": "Antidisestablishmentarianism",
            "ipa": "/ˌæn.ti.dɪs.ɪˌstæb.lɪʃ.mənˈteə.ri.ə.nɪ.zəm/",
            "type": "Noun",
            "def": "Opposition to the disestablishment of the Church of England",
            "vietnamese": "Chủ nghĩa chống bãi bỏ giáo hội nhà nước (từ dài nổi tiếng trong Unit 1)",
            "example": "Could you explain what 'antidisestablishmentarianism' means, please?"
        },
        {
            "word": "Brush up on",
            "ipa": "/brʌʃ ʌp ɒn/",
            "type": "Phrasal Verb",
            "def": "To practice and improve your skills or knowledge of something you learned in the past",
            "vietnamese": "Ôn tập lại, trau dồi lại kiến thức cũ",
            "example": "I'm going to have to brush up on my German before I go to Munich."
        },
        {
            "word": "Piece together",
            "ipa": "/piːs təˈɡeð.ər/",
            "type": "Phrasal Verb",
            "def": "To create or understand something by joining its different parts together",
            "vietnamese": "Xâu chuỗi, xâu kết lại các dữ kiện",
            "example": "Detectives are still trying to piece together exactly what happened that evening."
        },
        {
            "word": "Mull over",
            "ipa": "/mʌl ˈəʊ.vər/",
            "type": "Phrasal Verb",
            "def": "To think carefully about something for a long time",
            "vietnamese": "Suy ngẫm, cân nhắc kỹ lưỡng trong thời gian dài",
            "example": "I'm going to have to mull this proposal over for a while before making a decision."
        },
        {
            "word": "Ring a bell",
            "ipa": "/rɪŋ ə bel/",
            "type": "Idiom",
            "def": "Sounds familiar, but you cannot remember the exact details",
            "vietnamese": "Nghe quen quen nhưng không nhớ rõ chi tiết",
            "example": "The name rings a bell, but I can't remember where I've heard it before."
        }
    ]
    
    card_index = st.slider("🎯 Chọn thẻ từ vựng:", 1, len(flashcards_data), 1) - 1
    card = flashcards_data[card_index]
    
    st.markdown(f"""
    <div class="card" style="text-align: center; padding: 2rem;">
        <span class="badge-vocab">{card['type']}</span>
        <h2 style="color: #1E3A8A; margin-top: 0.5rem;">{card['word']}</h2>
        <p style="color: #6B7280; font-size: 1.1rem; font-weight: 500;">🔊 {card['ipa']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔍 LẬT THẺ ĐỂ XEM NGHĨA & VÍ DỤ"):
        st.markdown(f"**📖 Định nghĩa Tiếng Anh:** {card['def']}")
        st.markdown(f"**🇻🇳 Nghĩa Tiếng Việt:** {card['vietnamese']}")
        st.markdown(f"**💬 Ví dụ ngữ cảnh:** *"" + card['example'] + ""*")

elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý C1/C2 (Watch Out! Corner)")
    st.write("Tổng hợp các bẫy ngữ pháp và từ vựng nâng cao đặc biệt (Watch out!) từ sách Destination C1 & C2.")
    
    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #1: Present Perfect Simple vs Present Perfect Continuous</h4>
    <b>Quy tắc quan trọng:</b><br>
    • Sử dụng <b>Present Perfect Simple</b> khi nhấn mạnh <u>số lượng / số lần hoàn thành</u>:<br>
    &nbsp;&nbsp;<i>✔ I've written <b>two essays</b> this week.</i><br>
    • Sử dụng <b>Present Perfect Continuous</b> khi nhấn mạnh <u>thời lượng / tính liên tục</u> của hành động:<br>
    &nbsp;&nbsp;<i>✔ I've been working here for <b>five years</b>.</i> (nhấn mạnh thời lượng kéo dài)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #2: Stative Verbs in Continuous Tenses</h4>
    <b>Quy tắc quan trọng:</b><br>
    Nhiều động từ trạng thái có thể dùng ở thì tiếp diễn khi mô tả <b>HÀNH ĐỘNG</b> thay vì TRẠNG THÁI:<br>
    • <i>I <b>think</b> it's important to use computers.</i> (State: think = believe)<br>
    • <i>I'm <b>thinking</b> about going on a computer course.</i> (Action: think = consider/cân nhắc)<br>
    • <i>This soup <b>tastes</b> delicious.</i> (State: vị ngon)<br>
    • <i>The chef is <b>tasting</b> the soup.</i> (Action: nếm thử)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #3: Thói quen phiền phức với 'Always'</h4>
    Khi kết hợp <b>Present Continuous + always / continually</b> để diễn tả thói quen lập đi lặp lại gây bực mình hoặc phiền phức:<br>
    • <i>✔ Dan is <b>always coming up</b> with the craziest ideas!</i>
    </div>
    """, unsafe_allow_html=True)

elif menu_option == "📊 Báo cáo Tiến độ Học tập":
    st.header("📊 Báo cáo Tiến độ Học tập")
    st.write("Đánh dấu các Unit bạn đã hoàn thành để theo dõi tỷ lệ tiến độ toàn khóa học.")
    
    units = [f"Unit {i}: " + ("Grammar" if i%2!=0 else "Vocabulary") for i in range(1, 27)]
    
    completed_units = []
    st.subheader("✅ Danh sách 26 Units:")
    
    cols = st.columns(3)
    for idx, u in enumerate(units):
        col = cols[idx % 3]
        checked = col.checkbox(u, key=f"unit_chk_{idx}", value=(idx==0))
        if checked:
            completed_units.append(u)
            
    progress = len(completed_units) / 26
    st.markdown("---")
    st.subheader("📈 Tiến độ hoàn thành toàn bộ khóa học:")
    st.progress(progress)
    st.info(f"🎉 Bạn đã hoàn thành **{len(completed_units)}/26 Units** ({int(progress*100)}%)")

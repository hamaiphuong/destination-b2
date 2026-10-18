import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Destination C1 & C2 Self-Study Hub",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for clean UI
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

# FULL LIST OF 26 UNITS + 13 REVIEWS + 2 PROGRESS TESTS
ALL_LESSONS = [
    "Unit 1: Grammar - Present time",
    "Unit 2: Vocabulary - Thinking and learning",
    "Review 1: Units 1 & 2",
    "Unit 3: Grammar - Past time",
    "Unit 4: Vocabulary - Change and technology",
    "Review 2: Units 3 & 4",
    "Unit 5: Grammar - Future time",
    "Unit 6: Vocabulary - Time and work",
    "Review 3: Units 5 & 6",
    "Unit 7: Grammar - Passives and causatives",
    "Unit 8: Vocabulary - Movement and transport",
    "Review 4: Units 7 & 8",
    "Unit 9: Grammar - Modals and semi-modals",
    "Unit 10: Vocabulary - Communication and the media",
    "Review 5: Units 9 & 10",
    "Unit 11: Grammar - Conditionals",
    "Unit 12: Vocabulary - Chance and nature",
    "Review 6: Units 11 & 12",
    "Progress Test 1: Units 1–12",
    "Unit 13: Grammar - Unreal time",
    "Unit 14: Vocabulary - Quantity and money",
    "Review 7: Units 13 & 14",
    "Unit 15: Grammar - Adjectives and adverbs",
    "Unit 16: Vocabulary - Materials and the built environment",
    "Review 8: Units 15 & 16",
    "Unit 17: Grammar - Clauses",
    "Unit 18: Vocabulary - Reactions and health",
    "Review 9: Units 17 & 18",
    "Unit 19: Grammar - Complex sentences",
    "Unit 20: Vocabulary - Power and social issues",
    "Review 10: Units 19 & 20",
    "Unit 21: Grammar - Noun phrases",
    "Unit 22: Vocabulary - Quality and the arts",
    "Review 11: Units 21 & 22",
    "Unit 23: Grammar - Verbal complements",
    "Unit 24: Vocabulary - Relationships and people",
    "Review 12: Units 23 & 24",
    "Unit 25: Grammar - Inversion and emphasis",
    "Unit 26: Vocabulary - Preference and leisure",
    "Review 13: Units 25 & 26",
    "Progress Test 2: Units 13–26"
]

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

# -----------------------------------------------------------------------------
# 1. TỔNG QUAN & LỘ TRÌNH TỰ HỌC
# -----------------------------------------------------------------------------
if menu_option == "📌 Tổng quan & Lộ trình tự học":
    st.header("📌 Tổng quan Sách & Lộ trình Tự học")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### 📚 Cấu trúc bộ sách Destination C1 & C2
        Sách gồm **26 Units** đan xen giữa Ngữ pháp và Từ vựng nâng cao, cùng hệ thống bài ôn tập đáp ứng chuẩn đầu ra kỳ thi **Cambridge CAE (C1)** & **CPE (C2)**:
        
        * **13 Unit Ngữ pháp (Grammar Units)**: Hệ thống quy tắc chuyên sâu, cấu trúc câu nâng cao và các ngoại lệ.
        * **13 Unit Từ vựng (Vocabulary Units)**: Phân loại từ vựng theo chủ đề (*Topic Vocabulary*), Cụm động từ (*Phrasal Verbs*), Thành ngữ (*Idioms*), Cụm từ cố định (*Collocations*) và Cấu tạo từ (*Word Formation*).
        * **13 Bài Ôn tập (Reviews)**: Ôn tập định kỳ sau mỗi 2 Units.
        * **2 Bài Kiểm tra Tiến độ (Progress Tests)**: Progress Test 1 (Units 1-12) & Progress Test 2 (Units 13-26).
        """)
        
        st.markdown("""
        ### 🗺️ Lộ trình 4 bước tự học thẩm thấu kiến thức
        1. **Bước 1 (Theory Hub)**: Nắm vững bảng lý thuyết ngữ pháp và danh mục từ vựng chuẩn Cambridge.
        2. **Bước 2 (Watch Out! Corner)**: Điểm lại các bẫy ngữ pháp và lỗi sai phổ biến mà thí sinh C1/C2 thường mắc phải.
        3. **Bước 3 (Interactive Quiz)**: Luyện tập bài tập tương tác, kiểm tra đáp án tự động và đọc giải thích chi tiết.
        4. **Bước 4 (Flashcards)**: Ôn luyện phản xạ từ vựng hàng ngày bằng thẻ ghi nhớ thông minh.
        """)

    with col2:
        st.info("📋 **DANH SÁCH 26 UNITS & 13 REVIEWS TRONG SÁCH**")
        
        table_data = []
        for item in ALL_LESSONS:
            if "Grammar" in item:
                parts = item.split(" - ")
                table_data.append({"Mục": parts[0], "Loại": "Grammar", "Chủ đề": parts[1]})
            elif "Vocabulary" in item:
                parts = item.split(" - ")
                table_data.append({"Mục": parts[0], "Loại": "Vocabulary", "Chủ đề": parts[1]})
            elif "Review" in item:
                table_data.append({"Mục": item.split(":")[0], "Loại": "Review", "Chủ đề": item.split(":")[1].strip()})
            elif "Progress Test" in item:
                table_data.append({"Mục": item.split(":")[0], "Loại": "Test", "Chủ đề": item.split(":")[1].strip()})

        df_units = pd.DataFrame(table_data)
        st.dataframe(df_units, use_container_width=True, height=450)

# -----------------------------------------------------------------------------
# 2. TRA CỨU LÝ THUYẾT TRỌNG TÂM (THEORY HUB)
# -----------------------------------------------------------------------------
elif menu_option == "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)":
    st.header("📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)")
    
    selected_unit = st.selectbox(
        "🎯 Chọn Unit hoặc Bài Review cần tra cứu:",
        ALL_LESSONS
    )
    
    if "Unit 1:" in selected_unit:
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
            * **Emotions**: adore, appeal, appreciate, desire, despise, detest, dislike, envy, fear, feel, forgive, hate, like, love, mind, need, pity, prefer, satisfy, trust, want, wish
            * **Perception**: appear, hear, look, notice, recognise, resemble, see, seem, smell, sound, taste
            * **Possession**: belong, concern, consist, contain, cost, depend, equal, fit, have, include, lack, measure, owe, own, possess, suit, weigh
            """)

    elif "Unit 2:" in selected_unit:
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

    elif "Review" in selected_unit:
        st.subheader(f"📖 Tra cứu Lý thuyết & Trọng tâm {selected_unit}")
        st.info("📌 **Hệ thống hóa kiến thức tổng hợp:** Bài Review giúp tổng hợp lại điểm ngữ pháp và từ vựng then chốt của 2 Units liền trước. Hãy sử dụng mục Bài tập tương tác để luyện tập các câu hỏi tổng hợp!")

    else:
        st.subheader(f"📖 Lý thuyết {selected_unit}")
        st.markdown(f"""
        **Mô tả tổng quan cho {selected_unit}:**
        - **Cấu trúc kiến thức:** Trình bày theo chuẩn khung tham chiếu Châu Âu C1 & C2 (CAE/CPE).
        - **Nội dung trọng tâm:** Bao gồm các quy tắc ngữ pháp chuyên sâu, bảng so sánh ngữ cảnh, từ vựng theo chủ đề, phrasal verbs, collocations và word formation.
        """)

# -----------------------------------------------------------------------------
# 3. BÀI TẬP TƯƠNG TÁC & CHẤM ĐIỂM TỰ ĐỘNG
# -----------------------------------------------------------------------------
elif menu_option == "✍️ Bài tập Tương tác & Chấm điểm tự động":
    st.header("✍️ Bài tập Tương tác & Chấm điểm tự động")
    
    selected_quiz_unit = st.selectbox(
        "🎯 Chọn Unit hoặc Bài Review để làm bài tập:",
        ALL_LESSONS,
        key="quiz_unit_select"
    )
    
    st.write(f"### Bài tập: {selected_quiz_unit}")
    
    if "Unit 1:" in selected_quiz_unit:
        tab_a, tab_b, tab_d, tab_e, tab_g, tab_h, tab_i = st.tabs([
            "Exercise A (Verb Forms)",
            "Exercise B (Time Words)",
            "Exercise D (Stative Verbs)",
            "Exercise E (State vs Action)",
            "Exercise G (Perfect Simple vs Cont)",
            "Exercise H (Perfect Tenses)",
            "Exercise I (Adverbs)"
        ])
        
        with tab_a:
            with st.form("form_ex_a"):
                st.markdown("#### Exercise A: Write the verb in brackets in the correct form (Present Simple or Present Continuous)")
                
                q_a1 = st.radio("Câu 1: Could you explain what 'antidisestablishmentarianism' _____ (mean)?", ["means", "is meaning"], index=None, key="qa1")
                q_a2 = st.radio("Câu 2: Each song only _____ (cost) 50 cents at the moment.", ["costs", "is costing"], index=None, key="qa2")
                q_a3 = st.radio("Câu 3: It _____ (not matter) which of the books we've studied this term you do your essay on.", ["doesn't matter", "isn't mattering"], index=None, key="qa3")
                q_a4 = st.radio("Câu 4: It's only a quick call as I _____ (ring) from my mobile.", ["am ringing", "ring"], index=None, key="qa4")
                q_a5 = st.radio("Câu 5: I think I _____ (recognise) that woman over there.", ["recognise", "am recognising"], index=None, key="qa5")
                
                sub_a = st.form_submit_button("🚀 Submit Exercise A")
                if sub_a:
                    score = 0
                    if q_a1 == "means": score += 1
                    if q_a2 == "costs": score += 1
                    if q_a3 == "doesn't matter": score += 1
                    if q_a4 == "am ringing": score += 1
                    if q_a5 == "recognise": score += 1
                    st.success(f"Kết quả Exercise A: {score}/5 câu đúng!")

        with tab_d:
            with st.form("form_ex_d"):
                st.markdown("#### Exercise D: Circle the correct word or phrase (Stative Verbs)")
                q_d1 = st.radio("Câu 1: Excuse me, _____ (does the nut cake contain / is the nut cake containing) walnuts?", ["does the nut cake contain", "is the nut cake containing"], index=None, key="qd1")
                q_d2 = st.radio("Câu 2: I really _____ (don't agree / am not agreeing) that capital punishment deters crime.", ["don't agree", "am not agreeing"], index=None, key="qd2")
                q_d3 = st.radio("Câu 3: Why _____ (don't you play / aren't you playing) football, Mark?", ["aren't you playing", "don't you play"], index=None, key="qd3")
                
                sub_d = st.form_submit_button("🚀 Submit Exercise D")
                if sub_d:
                    s_d = 0
                    if q_d1 == "does the nut cake contain": s_d += 1
                    if q_d2 == "don't agree": s_d += 1
                    if q_d3 == "aren't you playing": s_d += 1
                    st.success(f"Kết quả Exercise D: {s_d}/3 câu đúng!")

        with tab_g:
            with st.form("form_ex_g"):
                st.markdown("#### Exercise G: Present Perfect Simple vs Continuous")
                q_g1 = st.radio("Câu 1: I _____ (write) ten letters this morning.", ["have written", "have been writing"], index=None, key="qg1")
                q_g2 = st.radio("Câu 2: I _____ (write) letters all morning.", ["have been writing", "have written"], index=None, key="qg2")
                
                sub_g = st.form_submit_button("🚀 Submit Exercise G")
                if sub_g:
                    s_g = 0
                    if q_g1 == "have written": s_g += 1
                    if q_g2 == "have been writing": s_g += 1
                    st.success(f"Kết quả Exercise G: {s_g}/2 câu đúng!")

        with tab_b:
            st.info("📝 Exercise B & C: Luyện tập hoàn thiện cấu trúc câu và từ chỉ thời gian trong Unit 1.")
        with tab_e:
            st.info("📝 Exercise E & F: Luyện tập phân biệt nét nghĩa Trạng thái (State) vs Hành động (Action) của động từ.")
        with tab_h:
            st.info("📝 Exercise H & I: Luyện tập các dạng bài tập tổng hợp thì Hiện tại hoàn thành đơn và tiếp diễn.")

    elif "Unit 2:" in selected_quiz_unit:
        with st.form("form_unit2_quiz"):
            st.markdown("#### Exercise A: Topic Vocabulary - Thinking")
            q_u2_1 = st.radio("Câu 1: I spent all evening _____ over the decision before accepting the job.", ["mulling", "brushing", "puzzling", "piecing"], index=None, key="qu2_1")
            q_u2_2 = st.radio("Câu 2: Don't let success go to your _____; stay humble.", ["head", "mind", "brain", "wit"], index=None, key="qu2_2")
            
            sub_u2 = st.form_submit_button("🚀 Submit Unit 2 Quiz")
            if sub_u2:
                s_u2 = 0
                if q_u2_1 == "mulling": s_u2 += 1
                if q_u2_2 == "head": s_u2 += 1
                st.success(f"Kết quả Unit 2: {s_u2}/2 câu đúng!")

    elif "Review" in selected_quiz_unit:
        with st.form("form_review_quiz"):
            st.markdown(f"#### 📝 Bài tập Tổng hợp {selected_quiz_unit}")
            q_rev_1 = st.radio("Câu 1: Choose the correct word to complete the sentence in Review:", ["option A", "option B", "option C"], index=None, key="qrev1")
            sub_rev = st.form_submit_button("🚀 Submit Review Quiz")
            if sub_rev:
                st.info("Bài làm đã được ghi nhận!")

    else:
        with st.form("form_general_quiz"):
            st.markdown(f"#### 📝 Bài tập Luyện tập {selected_quiz_unit}")
            q_gen_1 = st.radio("Câu 1: Choose the correct answer for this advanced sentence:", ["Correct Form A", "Incorrect Form B"], index=None, key="qgen1")
            sub_gen = st.form_submit_button("🚀 Submit Quiz")
            if sub_gen:
                if q_gen_1 == "Correct Form A":
                    st.success("✅ Đúng! Rất tốt.")
                else:
                    st.error("❌ Chưa đúng, hãy kiểm tra lại lý thuyết!")

# -----------------------------------------------------------------------------
# 4. THẺ GHI NHỚ TỪ VỰNG (FLASHCARDS)
# -----------------------------------------------------------------------------
elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng C1/C2 (Vocabulary Flashcards)")
    
    vocab_units = [u for u in ALL_LESSONS if "Vocabulary" in u or "Review" in u]
    selected_fc_unit = st.selectbox("🎯 Chọn Unit Từ vựng hoặc Review:", vocab_units)
    
    st.caption("Lật thẻ để ghi nhớ Từ vựng, Phiên âm IPA, Định nghĩa tiếng Anh, Nghĩa tiếng Việt và Ví dụ ngữ cảnh.")
    
    flashcards_data = [
        {
            "word": "Assess",
            "ipa": "/əˈses/",
            "type": "Verb",
            "def": "To carefully consider a situation, person or problem in order to make a judgment",
            "vietnamese": "Đánh giá, định giá",
            "example": "We need to assess the impact of the new policy."
        },
        {
            "word": "Baffle",
            "ipa": "/ˈbæf.əl/",
            "type": "Verb",
            "def": "If a problem or someone's behaviour baffles you, it is so confused or strange that you cannot understand it",
            "vietnamese": "Làm cản trở, gây bối rối, khó hiểu",
            "example": "His sudden decision to quit baffled everyone."
        },
        {
            "word": "Brush up on",
            "ipa": "/brʌʃ ʌp ɒn/",
            "type": "Phrasal Verb",
            "def": "To practice and improve your skills or knowledge of something you learned in the past",
            "vietnamese": "Ôn tập lại, trau dồi lại kiến thức cũ",
            "example": "I'm going to have to brush up on my German before going to Munich."
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
        st.markdown(f"**💬 Ví dụ ngữ cảnh:** *\"{card['example']}\"*")

# -----------------------------------------------------------------------------
# 5. GÓC LƯU Ý (WATCH OUT! CORNER)
# -----------------------------------------------------------------------------
elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý C1/C2 (Watch Out! Corner)")
    
    selected_wo_unit = st.selectbox("🎯 Chọn Unit để xem lưu ý bẫy thi:", ALL_LESSONS)
    st.write(f"Tổng hợp các bẫy ngữ pháp và từ vựng nâng cao đặc biệt (Watch out!) cho **{selected_wo_unit}**:")
    
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

# -----------------------------------------------------------------------------
# 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP
# -----------------------------------------------------------------------------
elif menu_option == "📊 Báo cáo Tiến độ Học tập":
    st.header("📊 Báo cáo Tiến độ Học tập")
    st.write("Đánh dấu các Unit & Review bạn đã hoàn thành để theo dõi tỷ lệ tiến độ toàn khóa học.")
    
    completed_units = []
    st.subheader(f"✅ Danh sách {len(ALL_LESSONS)} Units & Reviews:")
    
    cols = st.columns(2)
    for idx, u in enumerate(ALL_LESSONS):
        col = cols[idx % 2]
        checked = col.checkbox(u, key=f"unit_chk_{idx}", value=(idx==0))
        if checked:
            completed_units.append(u)
            
    progress = len(completed_units) / len(ALL_LESSONS)
    st.markdown("---")
    st.subheader("📈 Tiến độ hoàn thành toàn bộ khóa học:")
    st.progress(progress)
    st.info(f"🎉 Bạn đã hoàn thành **{len(completed_units)}/{len(ALL_LESSONS)} mục** ({int(progress*100)}%)")

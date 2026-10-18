import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Destination B2 Self-Study Hub",
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

st.markdown('<div class="main-header">📘 DESTINATION B2: LEARNING HUB</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Hệ thống Tự học Ngữ pháp & Từ vựng - Cấp độ B2</div>', unsafe_allow_html=True)

st.sidebar.title("📌 MENU CHÍNH")
menu_option = st.sidebar.radio(
    "Chọn chức năng:",
    [
        "📌 Tổng quan & Lộ trình tự học",
        "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)",
        "✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)",
        "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)",
        "⚠️ Góc lưu ý (Watch Out! Corner)",
        "📊 Báo cáo Tiến độ Học tập (Progress Report)"
    ]
)

# LIST OF ALL 28 UNITS & 14 REVIEWS
ALL_UNITS_LIST = [
    "Unit 1: Grammar - Present time",
    "Unit 2: Vocabulary - Travel and transport",
    "Review 1: Units 1 and 2",
    "Unit 3: Grammar - Past time",
    "Unit 4: Vocabulary - Hobbies, sport and games",
    "Review 2: Units 3 and 4",
    "Unit 5: Grammar - Future time / present tenses in time clauses",
    "Unit 6: Vocabulary - Science and technology",
    "Review 3: Units 5 and 6",
    "Unit 7: Grammar - Articles / countable & uncountable nouns / quantifiers",
    "Unit 8: Vocabulary - The media",
    "Review 4: Units 7 and 8",
    "Unit 9: Grammar - Conditionals: zero, first, second, third, mixed, inverted",
    "Unit 10: Vocabulary - People and society",
    "Review 5: Units 9 and 10",
    "Unit 11: Grammar - Comparatives and superlatives / so, such, enough, too",
    "Unit 12: Vocabulary - The law and crime",
    "Review 6: Units 11 and 12",
    "Unit 13: Grammar - Modals: ability, permission, advice, obligation, certainty",
    "Unit 14: Vocabulary - Health and fitness",
    "Review 7: Units 13 and 14",
    "Progress Test 1: Units 1 - 14",
    "Unit 15: Grammar - The passive / the causative / direct & indirect objects",
    "Unit 16: Vocabulary - Food and drink",
    "Review 8: Units 15 and 16",
    "Unit 17: Grammar - -ing form or infinitive / prefer, would rather, had better",
    "Unit 18: Vocabulary - Education and learning",
    "Review 9: Units 17 and 18",
    "Unit 19: Grammar - Questions / question tags / indirect questions",
    "Unit 20: Vocabulary - Weather and the environment",
    "Review 10: Units 19 and 20",
    "Unit 21: Grammar - Reported speech / reported questions / reporting verbs",
    "Unit 22: Vocabulary - Money and shopping",
    "Review 11: Units 21 and 22",
    "Unit 23: Grammar - Relative clauses / participles",
    "Unit 24: Vocabulary - Entertainment",
    "Review 12: Units 23 and 24",
    "Unit 25: Grammar - Unreal past, wishes / contrast",
    "Unit 26: Vocabulary - Fashion and design",
    "Review 13: Units 25 and 26",
    "Unit 27: Grammar - Inversions / possessives",
    "Unit 28: Vocabulary - Work and business",
    "Review 14: Units 27 and 28",
    "Progress Test 2: Units 15 - 28"
]

VOCAB_UNITS = [u for u in ALL_UNITS_LIST if "Vocabulary" in u or "Review" in u]

# --- 1. TỔNG QUAN & LỘ TRÌNH TỰ HỌC ---
if menu_option == "📌 Tổng quan & Lộ trình tự học":
    st.header("📌 Tổng quan Sách & Lộ trình Tự học")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### 📚 Cấu trúc bộ sách Destination B2
        Sách gồm **28 Units** đan xen giữa Ngữ pháp và Từ vựng, cùng hệ thống bài ôn tập đáp ứng chuẩn đầu ra **FCE (B2)**:
        * **14 Unit Ngữ pháp (Grammar Units)**: Hệ thống quy tắc chuyên sâu, cấu trúc câu nâng cao và các ngoại lệ.
        * **14 Unit Từ vựng (Vocabulary Units)**: Phân loại từ vựng theo chủ đề (*Topic Vocabulary in contrast*), Cụm động từ (*Phrasal Verbs*), Cụm từ cố định (*Phrases and Collocations*), Cấu trúc từ (*Word Patterns*) và Cấu tạo từ (*Word Formation*).
        * **14 Bài Ôn tập (Reviews)**: Ôn tập định kỳ sau mỗi 2 Units.
        * **2 Bài Kiểm tra Tiến độ (Progress Tests)**: Progress Test 1 (Units 1–14) & Progress Test 2 (Units 15–28).
        """)
        
        st.markdown("""
        ### 🗺️ Lộ trình tự học:
        * **Bước 1 (Theory Hub)**: Nắm vững bảng lý thuyết ngữ pháp và danh mục từ vựng chuẩn Cambridge B2.
        * **Bước 2 (Watch Out! Corner)**: Điểm lại các bẫy ngữ pháp và lỗi sai phổ biến mà thí sinh B2 thường mắc phải.
        * **Bước 3 (Interactive Quiz)**: Luyện tập bài tập tương tác, kiểm tra đáp án tự động và đọc giải thích chi tiết.
        * **Bước 4 (Flashcards)**: Ôn luyện phản xạ từ vựng hàng ngày bằng thẻ ghi nhớ thông minh.
        """)

    with col2:
        st.info("📋 **DANH SÁCH 28 UNITS & 14 REVIEWS**")
        
        units_table_data = []
        for item in ALL_UNITS_LIST:
            if "Grammar" in item:
                u_parts = item.split(" - ")
                units_table_data.append({"Unit": u_parts[0], "Loại": "Grammar", "Chủ đề": u_parts[1] if len(u_parts)>1 else ""})
            elif "Vocabulary" in item:
                u_parts = item.split(" - ")
                units_table_data.append({"Unit": u_parts[0], "Loại": "Vocabulary", "Chủ đề": u_parts[1] if len(u_parts)>1 else ""})
            elif "Review" in item or "Progress Test" in item:
                units_table_data.append({"Unit": item.split(":")[0], "Loại": "Review/Test", "Chủ đề": item})
                
        df_units = pd.DataFrame(units_table_data)
        st.dataframe(df_units, use_container_width=True, height=420)

# --- 2. TRA CỨU LÝ THUYẾT TRỌNG TÂM (THEORY HUB) ---
elif menu_option == "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)":
    st.header("📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)")
    
    selected_unit = st.selectbox("🎯 Chọn Unit / Bài Ôn tập cần tra cứu:", ALL_UNITS_LIST)
    
    if "Unit 1" in selected_unit:
        st.subheader("Unit 1: Grammar - Present time (Các thì Hiện tại B2)")
        
        tab_g1, tab_g2, tab_g3, tab_g4, tab_stative = st.tabs([
            "1. Present Simple",
            "2. Present Continuous",
            "3. Present Perfect Simple",
            "4. Present Perfect Continuous",
            "5. Stative Verbs & US/UK Grammar"
        ])
        
        with tab_g1:
            st.markdown("#### 🔹 Present Simple (Thì Hiện tại Đơn)")
            g1_data = [
                {"Cách dùng B2": "General truths (Sự thật hiển nhiên)", "Ví dụ minh họa": "The left-hand side of the brain controls the right-hand side of the body."},
                {"Cách dùng B2": "Current habits (Thói quen hiện tại)", "Ví dụ minh họa": "I don't always go to lectures that are early in the morning!"},
                {"Cách dùng B2": "Permanent situations & states (Tình huống lâu dài)", "Ví dụ minh họa": "Angie teaches French at a local adult education centre."},
                {"Cách dùng B2": "Timetables & fixed future events (Lịch trình cố định)", "Ví dụ minh họa": "Term ends on 21st December."},
                {"Cách dùng B2": "Plots of stories, films & reviews (Tóm tắt cốt truyện)", "Ví dụ minh họa": "The film ends with us not knowing whether they survived."}
            ]
            st.table(pd.DataFrame(g1_data))
            
            st.markdown("""
            <div class="tip-box">
            <b>💡 Emphatic Present Simple (Hiện tại đơn nhấn mạnh):</b><br>
            Sử dụng <code>do / does + V-bare</code> trong câu khẳng định để nhấn mạnh sự tương phản hoặc cảm xúc:<br>
            • <i>Adam doesn't know much about psychiatry but he <b>does know</b> quite a lot about psychology.</i>
            </div>
            """, unsafe_allow_html=True)

        with tab_g2:
            st.markdown("#### 🔹 Present Continuous (Thì Hiện tại Tiếp diễn)")
            g2_data = [
                {"Cách dùng B2": "Actions happening now (Hành động đang diễn ra)", "Ví dụ minh họa": "The boys are doing their homework right now."},
                {"Cách dùng B2": "Actions happening around now (Hành động xung quanh hiện tại)", "Ví dụ minh họa": "What book are you doing in English at the moment?"},
                {"Cách dùng B2": "Temporary situations (Tình huống tạm thời)", "Ví dụ minh họa": "We aren't having any exams while the lecturers are on strike."},
                {"Cách dùng B2": "Changing & developing situations (Sự thay đổi phát triển)", "Ví dụ minh họa": "More and more people are recognising the advantages of learning languages."},
                {"Cách dùng B2": "Annoying habits with 'always' (Thói quen phiền phức)", "Ví dụ minh họa": "Dan's always coming up with the craziest ideas!"}
            ]
            st.table(pd.DataFrame(g2_data))

        with tab_g3:
            st.markdown("#### 🔹 Present Perfect Simple (Thì Hiện tại Hoàn thành Đơn)")
            g3_data = [
                {"Cách dùng B2": "Situations started in past & still true (Kéo dài đến hiện tại)", "Ví dụ minh họa": "I've been a member of MENSA for over five years."},
                {"Cách dùng B2": "Completed actions at unspecified past time (Đã xong, không rõ thời điểm)", "Ví dụ minh họa": "Have you ever read any books by Edward De Bono?"},
                {"Cách dùng B2": "Completed actions with important present result (Kết quả ở hiện tại)", "Ví dụ minh họa": "She's been awarded a scholarship to study at Harvard."},
                {"Cách dùng B2": "Cấu trúc với số lần / thứ tự", "Ví dụ minh họa": "It's the second time I've been on a plane."}
            ]
            st.table(pd.DataFrame(g3_data))

        with tab_g4:
            st.markdown("#### 🔹 Present Perfect Continuous (Thì Hiện tại Hoàn thành Tiếp diễn)")
            g4_data = [
                {"Cách dùng B2": "Actions continuing up to present moment (Nhấn mạnh thời lượng kéo dài)", "Ví dụ minh họa": "We've been driving for hours. Can't we have a break soon?"},
                {"Cách dùng B2": "Actions stopping just before present moment (Vừa mới dừng, có dấu vết)", "Ví dụ minh họa": "I'm out of breath because I've been running to get here in time."}
            ]
            st.table(pd.DataFrame(g4_data))

        with tab_stative:
            st.markdown("#### 🔹 Stative Verbs (Động từ Chỉ Trạng thái B2)")
            st.markdown("""
            Động từ trạng thái không thường dùng ở thì tiếp diễn. Các nhóm chính:
            * **Thinking**: *believe, imagine, know, mean, think, understand*
            * **Existence**: *be, exist*
            * **Emotions**: *hate, like, love, need, prefer, satisfy, want*
            * **Human Senses**: *hear, see, smell, sound, taste*
            * **Appearance**: *appear, look, resemble, seem*
            * **Possession**: *belong to, consist of, have, include, involve, own*
            """)
            
            st.markdown("""
            <div class="watchout-box">
            <b>⚠️ Watch Out! Stative vs Dynamic (Action) Verbs:</b><br>
            Một số động từ có thể dùng ở thì tiếp diễn khi mang nghĩa hành động:<br>
            • <i>Do you <b>have</b> your plane ticket with you?</i> (Trạng thái: sở hữu)<br>
            • <i>Are you <b>having</b> lunch at the moment?</i> (Hành động: ăn uống)
            </div>
            """, unsafe_allow_html=True)

    elif "Unit 2" in selected_unit:
        st.subheader("Unit 2: Vocabulary - Travel and transport")
        st.write("Từ vựng phân biệt, Phrasal Verbs, Phrases & Collocations, Word Patterns và Word Formation từ Macmillan Essential Dictionary (cuối sách Destination B2):")
        
        vocab_b2_list = [
            {"Từ vựng / Cụm từ": "voyage (n)", "IPA": "/ˈvɔɪ.ɪdʒ/", "Định nghĩa Tiếng Anh": "a long journey, especially on a ship", "Nghĩa Tiếng Việt": "chuyến đi dài bằng đường biển", "Ví dụ": "It was a long voyage from London to New York."},
            {"Từ vựng / Cụm từ": "journey (n)", "IPA": "/ˈdʒɜː.ni/", "Định nghĩa Tiếng Anh": "an occasion when you travel from one place to another", "Nghĩa Tiếng Việt": "chuyến đi, hành trình", "Ví dụ": "We had a long journey ahead of us."},
            {"Từ vựng / Cụm từ": "trip (n)", "IPA": "/trɪp/", "Định nghĩa Tiếng Anh": "an occasion when you go somewhere and come back again", "Nghĩa Tiếng Việt": "chuyến đi ngắn (đi rồi về)", "Ví dụ": "The whole family went on a trip to Florida."},
            {"Từ vựng / Cụm từ": "excursion (n)", "IPA": "/ɪkˈskɜː.ʃən/", "Định nghĩa Tiếng Anh": "a short journey that you make for pleasure", "Nghĩa Tiếng Việt": "chuyến tham quan, dã ngoại", "Ví dụ": "My grandmother often talks about excursions to the sea."},
            {"Từ vựng / Cụm từ": "catch up with (phr v)", "IPA": "/kætʃ ʌp wɪð/", "Định nghĩa Tiếng Anh": "reach the same point/level as someone", "Nghĩa Tiếng Việt": "theo kịp, đuổi kịp", "Ví dụ": "Run fast to catch up with the group."},
            {"Từ vựng / Cụm từ": "check in (phr v)", "IPA": "/tʃek ɪn/", "Định nghĩa Tiếng Anh": "register at a hotel or an airport", "Nghĩa Tiếng Việt": "làm thủ tục nhận phòng/lên máy bay", "Ví dụ": "We checked in at the airport two hours before the flight."}
        ]
        st.table(pd.DataFrame(vocab_b2_list))
        
    else:
        st.info(f"Nội dung lý thuyết chi tiết cho **{selected_unit}** đang được hoàn thiện dữ liệu từ sách Destination B2.")

# --- 3. BÀI TẬP TƯƠNG TÁC & CHẤM ĐIỂM TỰ ĐỘNG ---
elif menu_option == "✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)":
    st.header("✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)")
    selected_quiz_unit = st.selectbox("🎯 Chọn Unit / Bài Ôn tập làm bài:", ALL_UNITS_LIST)
    
    if "Unit 1" in selected_quiz_unit:
        st.subheader("✍️ Unit 1: Present time - Full Practice Exercises")
        st.info("Hãy hoàn thành các bài tập bên dưới. Tất cả các câu hỏi trắc nghiệm đều được **bỏ trống ban đầu**, hãy tự chọn đáp án đúng trước khi nhấp nút **Kiểm tra Đáp án**.")
        
        tab_a, tab_d, tab_e, tab_g, tab_i = st.tabs([
            "Exercise A (Present Simple vs Continuous)",
            "Exercise D (Time Words & Adverbs)",
            "Exercise E (Multiple Choice Questions)",
            "Exercise G (Present Perfect Simple vs Continuous)",
            "Exercise I (Holiday Blues Gap-Fill)"
        ])
        
        with st.form("unit1_b2_full_form"):
            with tab_a:
                st.markdown("#### Exercise A: Write the correct form of the verb in brackets")
                qa1 = st.text_input("Câu 1: Ian ________ (take) a shower at the moment, so could you call back in about half an hour?", key="qa1")
                qa2 = st.text_input("Câu 2: ________ (you / ever / go) to Ipswich before?", key="qa2")
                qa3 = st.text_input("Câu 3: I ________ (write) to all the local newspapers to complain about the noise.", key="qa3")
                qa4 = st.text_input("Câu 4: Eric ________ (play) hockey competitively or just for fun?", key="qa4")

            with tab_d:
                st.markdown("#### Exercise D: Complete using words from the box (already, before, ever, for, just, rarely, since, so, still, yet)")
                qd1 = st.radio("Câu 5: Have you ________ dreamt of winning the lottery?", [None, "already", "ever", "never", "yet"], key="qd1")
                qd2 = st.radio("Câu 6: I haven't worked out how to set the timer on the video ________.", [None, "already", "still", "yet", "since"], key="qd2")
                qd3 = st.radio("Câu 7: My dad's lived in the same house ________ he was born.", [None, "for", "since", "from", "ever"], key="qd3")

            with tab_e:
                st.markdown("#### Exercise E: Choose the correct answer")
                qe1 = st.radio("Câu 8: That's the first time I ________ an answer right today!", [None, "A. I get", "B. I am getting", "C. I have got", "D. I have been getting"], key="qe1")
                qe2 = st.radio("Câu 9: Jessica ________ left, I'm afraid.", [None, "A. already", "B. has already", "C. is already", "D. still"], key="qe2")
                qe3 = qe2 # dummy mapping

            with tab_g:
                st.markdown("#### Exercise G: Present Perfect Simple or Continuous")
                qg1 = st.radio("Câu 10: We ________ for over an hour when the train finally arrived.", [None, "A. have waited", "B. have been waiting", "C. are waiting"], key="qg1")
                qg2 = st.radio("Câu 11: I ________ three letters so far this morning.", [None, "A. have written", "B. have been writing", "C. write"], key="qg2")

            with tab_i:
                st.markdown("#### Exercise I: Write one word in each gap (Holiday Blues)")
                qi1 = st.text_input("Câu 12: You've been looking at that timetable ________ the last ten minutes.", key="qi1")
                qi2 = st.text_input("Câu 13: There is ________ point at all in blaming each other.", key="qi2")

            submit_b2_quiz = st.form_submit_button("🚀 Nộp bài & Kiểm tra Đáp án (Submit Answers)")

        if submit_b2_quiz:
            score = 0
            total_qs = 10
            st.markdown("### 📊 Kết quả Bài làm & Giải thích Chi tiết (Answer Key)")
            
            # QA1
            if qa1.strip().lower() in ["is taking", "'s taking"]:
                score += 1
                st.success("✅ Câu 1 đúng! (is taking) - Hành động đang diễn ra tại thời điểm nói ('at the moment').")
            else:
                st.error("❌ Câu 1 sai! Đáp án đúng: **is taking**.")
                
            # QA2
            if qa2.strip().lower() in ["have you ever been", "have you ever gone"]:
                score += 1
                st.success("✅ Câu 2 đúng! (Have you ever been) - Hỏi về trải nghiệm ở thời điểm không xác định.")
            else:
                st.error("❌ Câu 2 sai! Đáp án đúng: **Have you ever been**.")

            # QD1
            if qd1 == "ever":
                score += 1
                st.success("✅ Câu 5 đúng! (ever) - 'Have you ever dreamt...' hỏi trải nghiệm.")
            else:
                st.error(f"❌ Câu 5 sai! Đáp án đúng: **ever** (Bạn chọn: {qd1}).")

            # QD2
            if qd2 == "yet":
                score += 1
                st.success("✅ Câu 6 đúng! (yet) - Dùng ở cuối câu phủ định 'haven't worked out... yet'.")
            else:
                st.error(f"❌ Câu 6 sai! Đáp án đúng: **yet**.")

            # QD3
            if qd3 == "since":
                score += 1
                st.success("✅ Câu 7 đúng! (since) - Đi kèm mốc thời gian 'he was born'.")
            else:
                st.error(f"❌ Câu 7 sai! Đáp án đúng: **since**.")

            # QE1
            if qe1 == "C. I have got":
                score += 1
                st.success("✅ Câu 8 đúng! (C. I have got) - Cấu trúc 'It's/That's the first time + Present Perfect'.")
            else:
                st.error(f"❌ Câu 8 sai! Đáp án đúng: **C. I have got**.")

            # QE2
            if qe2 == "B. has already":
                score += 1
                st.success("✅ Câu 9 đúng! (B. has already) - Vị trí trạng từ 'already' đứng giữa 'has' và V3/ed.")
            else:
                st.error(f"❌ Câu 9 sai! Đáp án đúng: **B. has already**.")

            # QG1
            if qg1 == "B. have been waiting":
                score += 1
                st.success("✅ Câu 10 đúng! (B. have been waiting) - Nhấn mạnh thời lượng tính liên tục 'for over an hour'.")
            else:
                st.error(f"❌ Câu 10 sai! Đáp án đúng: **B. have been waiting**.")

            # QG2
            if qg2 == "A. have written":
                score += 1
                st.success("✅ Câu 11 đúng! (A. have written) - Nhấn mạnh kết quả con số cụ thể 'three letters'.")
            else:
                st.error(f"❌ Câu 11 sai! Đáp án đúng: **A. have written**.")

            # QI1
            if qi1.strip().lower() == "for":
                score += 1
                st.success("✅ Câu 12 đúng! (for) - 'for the last ten minutes' chỉ khoảng thời gian.")
            else:
                st.error("❌ Câu 12 sai! Đáp án đúng: **for**.")

            pct = int((score / total_qs) * 100)
            st.info(f"🏆 Điểm số của bạn: **{score}/{total_qs}** ({pct}%)")
            if pct == 100:
                st.balloons()
    else:
        st.info(f"Bài tập trắc nghiệm & điền từ tương tác cho **{selected_quiz_unit}** đang được xây dựng theo đáp án chuẩn sách B2.")

# --- 4. THẺ GHI NHỚ TỪ VỰNG (FLASHCARDS) ---
elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng (Flashcards)")
    
    selected_fc_unit = st.selectbox("🎯 Chọn Unit Từ vựng để ôn Flashcards:", VOCAB_UNITS)
    
    if "Grammar" in selected_fc_unit:
        st.warning("⚠️ Thẻ ghi nhớ (Flashcards) chỉ dành riêng cho các Unit Từ vựng. Các Unit Ngữ pháp tập trung vào Lý thuyết và Bài tập Tương tác.")
    else:
        flashcards_b2 = [
            {"word": "voyage (n)", "ipa": "/ˈvɔɪ.ɪdʒ/", "type": "Topic Vocabulary", "def": "a long journey, especially on a ship or in space", "vi": "chuyến đi dài bằng đường biển / vũ trụ", "ex": "The voyage across the Atlantic took three weeks."},
            {"word": "catch up with", "ipa": "/kætʃ ʌp wɪð/", "type": "Phrasal Verb", "def": "reach the same point or level as someone who is ahead", "vi": "theo kịp, đuổi kịp", "ex": "I had to run to catch up with the rest of the class."},
            {"word": "check in", "ipa": "/tʃek ɪn/", "type": "Phrasal Verb", "def": "arrive and register at a hotel or airport", "vi": "làm thủ tục nhận phòng / nhận chỗ", "ex": "Please check in at least two hours before departure."},
            {"word": "drop off", "ipa": "/drɒp ɒf/", "type": "Phrasal Verb", "def": "let someone get out of a vehicle; fall asleep", "vi": "cho ai xuống xe; ngủ gật", "ex": "I can drop you off at the station on my way to work."},
            {"word": "on holiday", "ipa": "/ɒn ˈhɒl.ə.deɪ/", "type": "Phrase & Collocation", "def": "taking a period of rest away from work or school", "vi": "đang trong kỳ nghỉ", "ex": "They are currently on holiday in Spain."}
        ]
        
        card_idx = st.slider("🎯 Chọn thẻ từ vựng:", 1, len(flashcards_b2), 1) - 1
        c = flashcards_b2[card_idx]
        
        st.markdown(f"""
        <div class="card" style="text-align: center; padding: 2rem;">
            <span class="badge-vocab">{c['type']}</span>
            <h2 style="color: #1E3A8A; margin-top: 0.5rem;">{c['word']}</h2>
            <p style="color: #6B7280; font-size: 1.1rem; font-weight: 500;">🔊 {c['ipa']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🔍 LẬT THẺ ĐỂ XEM NGHĨA & VÍ DỤ"):
            st.markdown(f"**📖 Định nghĩa Tiếng Anh:** {c['def']}")
            st.markdown(f"**🇻🇳 Nghĩa Tiếng Việt:** {c['vi']}")
            st.markdown(f"**💬 Ví dụ ngữ cảnh:** *\"{c['ex']}\"*")

# --- 5. GÓC LƯU Ý (WATCH OUT! CORNER) ---
elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý B2 (Watch Out! Corner)")
    st.write("Tổng hợp các bẫy ngữ pháp và từ vựng nâng cao đặc biệt (Watch out!) từ sách Destination B2:")
    
    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #1: Present Perfect Simple vs Continuous (Numbers vs Duration)</h4>
    <b>Quy tắc B2:</b><br>
    • Sử dụng <b>Present Perfect Simple</b> khi đề cập đến <u>số lượng / số lần hoàn thành cụ thể</u>:<br>
    &nbsp;&nbsp;<i>✔ I've written <b>three essays</b> this morning.</i> (KHÔNG dùng Present Perfect Continuous)<br>
    • Sử dụng <b>Present Perfect Continuous</b> khi nhấn mạnh <u>thời lượng / tính liên tục kéo dài</u>:<br>
    &nbsp;&nbsp;<i>✔ I've been writing essays <b>all morning</b>.</i>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #2: Stative Verbs in Continuous Tenses</h4>
    <b>Quy tắc B2:</b><br>
    Các động từ chỉ trạng thái (stative verbs) như <i>think, have, feel, look, smell, taste</i> có thể dùng ở thì tiếp diễn khi mang nghĩa <b>hành động / quá trình</b>:<br>
    • <i>I <b>think</b> you're right.</i> (State: think = believe)<br>
    • <i>I'm <b>thinking</b> about buying a new car.</i> (Action: think = consider)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #3: Annoying Habits with 'Always'</h4>
    Khi diễn tả thói quen lặp đi lặp lại gây phiền phức hoặc bực mình, sử dụng <b>Present Continuous + always / continually</b>:<br>
    • <i>✔ You're <b>always leaving</b> your dirty socks on the floor!</i>
    </div>
    """, unsafe_allow_html=True)

# --- 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập (Progress Report)")
    st.write("Đánh dấu các Unit hoặc bài Ôn tập bạn đã hoàn thành để theo dõi tỷ lệ phần trăm tiến độ học tập toàn cuốn sách Destination B2.")
    
    completed_b2 = []
    st.subheader("✅ Danh sách 28 Units & 14 Reviews:")
    
    cols = st.columns(3)
    for idx, unit_item in enumerate(ALL_UNITS_LIST):
        col = cols[idx % 3]
        checked = col.checkbox(unit_item, key=f"chk_b2_{idx}", value=(idx==0))
        if checked:
            completed_b2.append(unit_item)
            
    total_b2_items = len(ALL_UNITS_LIST)
    progress_pct = len(completed_b2) / total_b2_items
    st.markdown("---")
    st.subheader("📈 Tiến độ hoàn thành toàn bộ khóa học B2:")
    st.progress(progress_pct)
    st.info(f"🎉 Bạn đã hoàn thành **{len(completed_b2)}/{total_b2_items} bài** ({int(progress_pct*100)}%)")

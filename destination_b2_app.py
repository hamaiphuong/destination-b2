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
    .explain-box {
        background-color: #F8FAFC;
        border-left: 4px solid #3B82F6;
        padding: 0.8rem;
        margin-top: 0.4rem;
        margin-bottom: 0.8rem;
        border-radius: 4px;
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
        Sách gồm **28 Units** đan xen giữa Ngữ pháp và Từ vựng, cùng hệ thống bài ôn tập đáp ứng chuẩn đầu ra FCE (B2):
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
                {"Cách dùng B2": "Current habits (Thói quen hiện tại)", "Ví dụ minh họa": "Toby walks to work."},
                {"Cách dùng B2": "To talk about how often things happen (Mức độ thường xuyên)", "Ví dụ minh họa": "Angela doesn't visit us very often."},
                {"Cách dùng B2": "Permanent situations (Tình huống lâu dài)", "Ví dụ minh họa": "Carlo works in a travel agent's."},
                {"Cách dùng B2": "States (Trạng thái ở hiện tại)", "Ví dụ minh họa": "Do you have an up-to-date passport?"},
                {"Cách dùng B2": "General truths and facts (Sự thật hiển nhiên/Chân lý)", "Ví dụ minh họa": "Poland is in the European Union."}
            ]
            st.table(pd.DataFrame(g1_data))
            
            st.markdown("""
            <div class="tip-box">
            <b>💡 Watch out! Emphatic Present Simple (Hiện tại đơn nhấn mạnh):</b><br>
            Sử dụng <code>do / does + V-bare</code> trong câu khẳng định để nhấn mạnh sự tương phản hoặc cảm xúc:<br>
            • <i>'You don't like going by bus, do you?' - 'Actually, I <b>do like</b> going by bus for short distances.'</i><br>
            • <i>The bus isn't quicker than the train but it <b>does stop</b> right outside the factory.</i>
            </div>
            """, unsafe_allow_html=True)

        with tab_g2:
            st.markdown("#### 🔹 Present Continuous (Thì Hiện tại Tiếp diễn)")
            g2_data = [
                {"Cách dùng B2": "Actions happening now (Hành động đang diễn ra tại thời điểm nói)", "Ví dụ minh họa": "Mike is driving to work at the moment."},
                {"Cách dùng B2": "Temporary series of actions (Chuỗi hành động tạm thời)", "Ví dụ minh họa": "Taxi drivers aren't stopping at the train station because of the roadworks."},
                {"Cách dùng B2": "Temporary situations (Tình huống tạm thời)", "Ví dụ minh họa": "Are they staying in a hotel near the Olympic stadium?"},
                {"Cách dùng B2": "Changing and developing situations (Sự thay đổi và phát triển)", "Ví dụ minh họa": "Holidays abroad are becoming increasingly popular."},
                {"Cách dùng B2": "Annoying habits (usually with always) (Thói quen phiền phức với 'always')", "Ví dụ minh họa": "Dad is always cleaning the car when I want to use it!"}
            ]
            st.table(pd.DataFrame(g2_data))

        with tab_g3:
            st.markdown("#### 🔹 Present Perfect Simple (Thì Hiện tại Hoàn thành Đơn)")
            g3_data = [
                {"Cách dùng B2": "Situations and states that started in the past and are still true (Bắt đầu ở quá khứ & vẫn đúng ở hiện tại)", "Ví dụ minh họa": "She's had her motorbike for over six years."},
                {"Cách dùng B2": "A series of actions continuing up to now (Chuỗi hành động tiếp diễn đến hiện tại)", "Ví dụ minh họa": "We've travelled by taxi, bus, plane and train - all in the last twenty-four hours!"},
                {"Cách dùng B2": "Completed actions at a time in the past which is not mentioned (Hành động hoàn thành không ghi rõ thời gian)", "Ví dụ minh họa": "Have you ever flown in a helicopter?"},
                {"Cách dùng B2": "Completed actions where the important thing is the present result (Hành động xong có kết quả ở hiện tại)", "Ví dụ minh họa": "I've booked the coach tickets."}
            ]
            st.table(pd.DataFrame(g3_data))
            
            st.markdown("""
            <div class="tip-box">
            <b>💡 Watch out!</b> Phrases such as <i>It's the first / second / etc. time...</i> are followed by the present perfect simple:<br>
            • <i>✔ It's the second time I've been on a plane.</i>
            </div>
            """, unsafe_allow_html=True)

        with tab_g4:
            st.markdown("#### 🔹 Present Perfect Continuous (Thì Hiện tại Hoàn thành Tiếp diễn)")
            g4_data = [
                {"Cách dùng B2": "Actions continuing up to the present moment (Hành động kéo dài liên tục tới hiện tại)", "Ví dụ minh họa": "We have been driving for hours. Can't we have a break soon?"},
                {"Cách dùng B2": "Actions stopping just before the present moment (Hành động dừng ngay trước thời điểm hiện tại)", "Ví dụ minh họa": "I'm out of breath because I've been running to get here in time."}
            ]
            st.table(pd.DataFrame(g4_data))

        with tab_stative:
            st.markdown("#### 🔹 Stative Verbs (Động từ Chỉ Trạng thái B2)")
            st.markdown("""
            Động từ trạng thái không thường dùng ở thì tiếp diễn vì chúng không diễn tả hành động. Các nhóm chính:
            * **Thinking**: *believe, imagine, know, mean, think, understand*
            * **Existence**: *be, exist*
            * **Emotions**: *hate, like, love, need, prefer, satisfy, want*
            * **The human senses**: *hear, see, smell, sound, taste*
            * **Appearance**: *appear, look, resemble, seem*
            * **Possession and relationships between things**: *belong to, consist of, have, include, involve, own*
            """)
            
            st.markdown("""
            <div class="watchout-box">
            <b>⚠️ Watch Out! Stative vs Dynamic (Non-stative) Verbs:</b><br>
            Một số động từ (be, have, imagine, look, see, smell, taste, think) là stative với nét nghĩa này nhưng lại là dynamic với nét nghĩa khác:<br>
            • <i>Do you <b>have</b> your plane ticket with you?</i> (Trạng thái: sở hữu - possession)<br>
            • <i>Are you <b>having</b> lunch at the moment?</i> (Hành động: ăn uống - eating)
            </div>
            """, unsafe_allow_html=True)

    elif "Unit 2" in selected_unit:
        st.subheader("Unit 2: Vocabulary - Travel and transport")
        st.write("Từ vựng phân biệt, Phrasal Verbs, Phrases & Collocations, Word Patterns và Word Formation từ Destination B2:")
        
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
        st.info("Hãy hoàn thành các bài tập bên dưới.")
        
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
                qd1 = st.radio("Câu 5: Have you ________ dreamt of winning the lottery?", ["already", "ever", "never", "yet"], index=None, key="qd1")
                qd2 = st.radio("Câu 6: I haven't worked out how to set the timer on the video ________.", ["already", "still", "yet", "since"], index=None, key="qd2")
                qd3 = st.radio("Câu 7: My dad's lived in the same house ________ he was born.", ["for", "since", "from", "ever"], index=None, key="qd3")

            with tab_e:
                st.markdown("#### Exercise E: Choose the correct answer")
                qe1 = st.radio("Câu 8: That's the first time I ________ an answer right today!", ["A. I get", "B. I am getting", "C. I have got", "D. I have been getting"], index=None, key="qe1")
                qe2 = st.radio("Câu 9: Jessica ________ left, I'm afraid.", ["A. already", "B. has already", "C. is already", "D. still"], index=None, key="qe2")

            with tab_g:
                st.markdown("#### Exercise G: Present Perfect Simple or Continuous")
                qg1 = st.radio("Câu 10: We ________ for over an hour when the train finally arrived.", ["A. have waited", "B. have been waiting", "C. are waiting"], index=None, key="qg1")
                qg2 = st.radio("Câu 11: I ________ three letters so far this morning.", ["A. have written", "B. have been writing", "C. write"], index=None, key="qg2")

            with tab_i:
                st.markdown("#### Exercise I: Write one word in each gap (Holiday Blues)")
                qi1 = st.text_input("Câu 12: You've been looking at that timetable ________ the last ten minutes.", key="qi1")
                qi2 = st.text_input("Câu 13: There is ________ point at all in blaming each other.", key="qi2")

            submit_b2_quiz = st.form_submit_button("🚀 Nộp bài & Kiểm tra Đáp án (Submit Answers)")

        if submit_b2_quiz:
            score = 0
            total_qs = 13
            st.markdown("### 📊 Kết quả Bài làm & Giải thích Chi tiết (Answer Key)")
            
            # QA1
            user_qa1 = qa1.strip().lower() if qa1 else ""
            if user_qa1 in ["is taking", "'s taking"]:
                score += 1
                st.success("✅ **Câu 1 đúng!** (is taking)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Hành động đang diễn ra tại thời điểm nói ('at the moment') ➔ Dùng Present Continuous.</div>", unsafe_allow_html=True)
            elif user_qa1 == "":
                st.warning("⚠️ **Câu 1: Chưa trả lời / Bỏ trống.** Đáp án đúng: **is taking**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Cụm từ 'at the moment' (ngay lúc này) diễn tả hành động đang xảy ra xung quanh thời điểm nói, do đó dùng thì Hiện tại tiếp diễn (Present Continuous) <code>is taking</code>.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 1: Chưa chính xác.** (Bạn nhập: <code>{qa1}</code>) ➔ Đáp án đúng: **is taking**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Cụm từ 'at the moment' diễn tả hành động đang diễn ra ngay lúc nói. Do đó động từ 'take' phải chia ở thì Hiện tại tiếp diễn <code>is taking</code>.</div>", unsafe_allow_html=True)

            # QA2
            user_qa2 = qa2.strip().lower() if qa2 else ""
            if user_qa2 in ["have you ever been", "have you ever gone"]:
                score += 1
                st.success("✅ **Câu 2 đúng!** (Have you ever been)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Hỏi về trải nghiệm cá nhân tính đến thời điểm hiện tại ('ever', 'before') ➔ Dùng Present Perfect.</div>", unsafe_allow_html=True)
            elif user_qa2 == "":
                st.warning("⚠️ **Câu 2: Chưa trả lời / Bỏ trống.** Đáp án đúng: **Have you ever been**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Khi hỏi ai đó đã từng đi đâu hay có trải nghiệm gì trước đây ('before', 'ever'), ta dùng thì Hiện tại hoàn thành (Present Perfect Simple): <code>Have you ever been...</code></div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 2: Chưa chính xác.** (Bạn nhập: <code>{qa2}</code>) ➔ Đáp án đúng: **Have you ever been**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Câu hỏi trải nghiệm trong quá khứ kéo dài đến hiện tại có từ nhận biết 'ever' và 'before', phải chia ở thì Hiện tại hoàn thành câu hỏi: <code>Have you ever been</code>.</div>", unsafe_allow_html=True)

            # QA3
            user_qa3 = qa3.strip().lower() if qa3 else ""
            if user_qa3 in ["have written", "have already written", "'ve written"]:
                score += 1
                st.success("✅ **Câu 3 đúng!** (have written)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Hành động đã hoàn thành có kết quả ở hiện tại ➔ Present Perfect Simple.</div>", unsafe_allow_html=True)
            elif user_qa3 == "":
                st.warning("⚠️ **Câu 3: Chưa trả lời / Bỏ trống.** Đáp án đúng: **have written**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Hành động viết thư phàn nàn đã hoàn thành và kết quả ảnh hưởng đến hiện tại, dùng Present Perfect Simple <code>have written</code>.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 3: Chưa chính xác.** (Bạn nhập: <code>{qa3}</code>) ➔ Đáp án đúng: **have written**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Diễn tả hành động vừa hoàn thành có kết quả ở hiện tại, không rõ thời gian cụ thể ➔ Chia ở thì Hiện tại hoàn thành <code>have written</code>.</div>", unsafe_allow_html=True)

            # QA4
            user_qa4 = qa4.strip().lower() if qa4 else ""
            if user_qa4 in ["does eric play", "does eric usually play"]:
                score += 1
                st.success("✅ **Câu 4 đúng!** (Does Eric play)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Hỏi về thói quen/sở thích lâu dài ➔ Present Simple.</div>", unsafe_allow_html=True)
            elif user_qa4 == "":
                st.warning("⚠️ **Câu 4: Chưa trả lời / Bỏ trống.** Đáp án đúng: **Does Eric play**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Câu hỏi thói quen hoặc sở thích lâu dài ở hiện tại ➔ Dùng Present Simple <code>Does Eric play</code>.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 4: Chưa chính xác.** (Bạn nhập: <code>{qa4}</code>) ➔ Đáp án đúng: **Does Eric play**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Hỏi về thói quen thường xuyên của một cá nhân, dùng thì Hiện tại đơn ở dạng câu hỏi: <code>Does Eric play</code>.</div>", unsafe_allow_html=True)

            # QD1
            if qd1 == "ever":
                score += 1
                st.success("✅ **Câu 5 đúng!** (ever)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'ever' dùng trong câu hỏi Present Perfect để hỏi 'đã từng... chưa'.</div>", unsafe_allow_html=True)
            elif qd1 is None:
                st.warning("⚠️ **Câu 5: Chưa trả lời / Bỏ trống.** Đáp án đúng: **ever**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Trạng từ 'ever' (đã từng) đứng giữa trợ động từ 'Have' và động từ cột 3 'dreamt' trong câu hỏi thì Hiện tại hoàn thành.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 5: Chưa chính xác.** (Bạn chọn: <code>{qd1}</code>) ➔ Đáp án đúng: **ever**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> 'ever' là trạng từ duy nhất phù hợp trong câu hỏi nghi vấn trải nghiệm 'Have you ever dreamt...?'.</div>", unsafe_allow_html=True)

            # QD2
            if qd2 == "yet":
                score += 1
                st.success("✅ **Câu 6 đúng!** (yet)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'yet' dùng ở cuối câu phủ định thì Hiện tại hoàn thành.</div>", unsafe_allow_html=True)
            elif qd2 is None:
                st.warning("⚠️ **Câu 6: Chưa trả lời / Bỏ trống.** Đáp án đúng: **yet**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> 'yet' (chưa) thường đứng cuối câu phủ định ở thì Hiện tại hoàn thành (<code>haven't worked out... yet</code>).</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 6: Chưa chính xác.** (Bạn chọn: <code>{qd2}</code>) ➔ Đáp án đúng: **yet**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Vị trí cuối câu phủ định thì Hiện tại hoàn thành chỉ đi kèm với 'yet'.</div>", unsafe_allow_html=True)

            # QD3
            if qd3 == "since":
                score += 1
                st.success("✅ **Câu 7 đúng!** (since)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'since' chỉ mốc thời gian 'he was born'.</div>", unsafe_allow_html=True)
            elif qd3 is None:
                st.warning("⚠️ **Câu 7: Chưa trả lời / Bỏ trống.** Đáp án đúng: **since**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> 'since' đi kèm với mệnh đề chỉ mốc thời gian quá khứ ('he was born').</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 7: Chưa chính xác.** (Bạn chọn: <code>{qd3}</code>) ➔ Đáp án đúng: **since**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Để chỉ mốc thời gian bắt đầu một hành động trong quá khứ kéo dài đến hiện tại ('he was born'), ta dùng 'since' chứ không dùng 'for'.</div>", unsafe_allow_html=True)

            # QE1
            if qe1 == "C. I have got":
                score += 1
                st.success("✅ **Câu 8 đúng!** (C. I have got)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Sau 'That's the first time...' bắt buộc dùng Present Perfect.</div>", unsafe_allow_html=True)
            elif qe1 is None:
                st.warning("⚠️ **Câu 8: Chưa trả lời / Bỏ trống.** Đáp án đúng: **C. I have got**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Sau cấu trúc nhấn mạnh lần đầu/lần thứ n 'That's the first time...', mệnh đề đằng sau bắt buộc dùng thì Hiện tại hoàn thành (Present Perfect Simple: <code>I have got</code>).</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 8: Chưa chính xác.** (Bạn chọn: <code>{qe1}</code>) ➔ Đáp án đúng: **C. I have got**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Cấu trúc chuẩn: 'It's / That's the first/second... time + Present Perfect'. Do đó phương án đúng duy nhất là C.</div>", unsafe_allow_html=True)

            # QE2
            if qe2 == "B. has already":
                score += 1
                st.success("✅ **Câu 9 đúng!** (B. has already)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'already' đứng giữa 'has' và V3 ('left').</div>", unsafe_allow_html=True)
            elif qe2 is None:
                st.warning("⚠️ **Câu 9: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. has already**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Trạng từ 'already' (đã... rồi) đứng giữa trợ động từ 'has' và động từ phân từ hai 'left' (<code>has already left</code>).</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 9: Chưa chính xác.** (Bạn chọn: <code>{qe2}</code>) ➔ Đáp án đúng: **B. has already**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Vị trí đúng của trạng từ 'already' trong thì Hiện tại hoàn thành khẳng định là đứng sau trợ động từ 'has/have' và trước V3 ('left').</div>", unsafe_allow_html=True)

            # QG1
            if qg1 == "B. have been waiting":
                score += 1
                st.success("✅ **Câu 10 đúng!** (B. have been waiting)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Nhấn mạnh tính liên tục của hành động kéo dài 'for over an hour'.</div>", unsafe_allow_html=True)
            elif qg1 is None:
                st.warning("⚠️ **Câu 10: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. have been waiting**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Hành động chờ đợi kéo dài liên tục có cụm từ chỉ thời lượng 'for over an hour' ➔ Dùng thì Hiện tại hoàn thành tiếp diễn (Present Perfect Continuous) <code>have been waiting</code>.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 10: Chưa chính xác.** (Bạn chọn: <code>{qg1}</code>) ➔ Đáp án đúng: **B. have been waiting**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Để nhấn mạnh tính liên tục và độ dài của hành động kéo dài tới thời điểm nói ('for over an hour'), ta chọn thì Present Perfect Continuous <code>have been waiting</code>.</div>", unsafe_allow_html=True)

            # QG2
            if qg2 == "A. have written":
                score += 1
                st.success("✅ **Câu 11 đúng!** (A. have written)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Nhấn mạnh con số kết quả 'three letters' ➔ Present Perfect Simple.</div>", unsafe_allow_html=True)
            elif qg2 is None:
                st.warning("⚠️ **Câu 11: Chưa trả lời / Bỏ trống.** Đáp án đúng: **A. have written**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Khi nhấn mạnh kết quả với con số cụ thể ('three letters') và từ nhận biết 'so far', ta bắt buộc dùng Present Perfect Simple <code>have written</code> chứ không dùng dạng tiếp diễn.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 11: Chưa chính xác.** (Bạn chọn: <code>{qg2}</code>) ➔ Đáp án đúng: **A. have written**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Khi nhắc đến số lượng kết quả đã hoàn thành ('three letters'), quy tắc trong sách Destination B2 nêu rõ dùng Present Perfect Simple.</div>", unsafe_allow_html=True)

            # QI1
            user_qi1 = qi1.strip().lower() if qi1 else ""
            if user_qi1 == "for":
                score += 1
                st.success("✅ **Câu 12 đúng!** (for)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'for' + khoảng thời gian ('the last ten minutes').</div>", unsafe_allow_html=True)
            elif user_qi1 == "":
                st.warning("⚠️ **Câu 12: Chưa trả lời / Bỏ trống.** Đáp án đúng: **for**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Cụm chỉ khoảng thời gian kéo dài 'the last ten minutes' đi với giới từ 'for' (<code>for the last ten minutes</code>).</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 12: Chưa chính xác.** (Bạn nhập: <code>{qi1}</code>) ➔ Đáp án đúng: **for**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Đi trước khoảng thời gian 'the last ten minutes' ta chọn giới từ 'for' chỉ độ dài thời gian.</div>", unsafe_allow_html=True)

            # QI2
            user_qi2 = qi2.strip().lower() if qi2 else ""
            if user_qi2 == "no":
                score += 1
                st.success("✅ **Câu 13 đúng!** (no)")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Cấu trúc 'There is no point in doing sth'.</div>", unsafe_allow_html=True)
            elif user_qi2 == "":
                st.warning("⚠️ **Câu 13: Chưa trả lời / Bỏ trống.** Đáp án đúng: **no**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Thành ngữ 'There is no point (in doing sth)' nghĩa là không có lý do/không có ích gì khi làm việc gì.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 13: Chưa chính xác.** (Bạn nhập: <code>{qi2}</code>) ➔ Đáp án đúng: **no**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích chi tiết:</i> Cấu trúc cố định 'There is no point at all in...' (Chẳng có ích gì chút nào khi...).</div>", unsafe_allow_html=True)

            pct = int((score / total_qs) * 100)
            st.info(f"🏆 Điểm số của bạn: **{score}/{total_qs}** ({pct}%)")
            if pct == 100:
                st.balloons()
    else:
        st.info(f"Bài tập trắc nghiệm & điền từ tương tác cho **{selected_quiz_unit}** đang được xây dựng theo đáp án chuẩn sách B2.")

# --- 4. THẺ GHI NHỚ TỪ VỰNG (FLASHCARDS) ---
elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng (Flashcards)")
    selected_fc_unit = st.selectbox("🎯 Chọn Unit Từ vựng để ôn tập thẻ:", VOCAB_UNITS)
    
    if "Grammar" in selected_fc_unit:
        st.warning("⚠️ Unit này là Unit Ngữ pháp. Vui lòng chọn Unit Từ vựng (Vocabulary Unit) để học Flashcards.")
    else:
        flashcards_data = [
            {
                "word": "Voyage",
                "ipa": "/ˈvɔɪ.ɪdʒ/",
                "type": "Noun",
                "def": "a long journey, especially on a ship",
                "vietnamese": "Chuyến đi dài bằng đường biển",
                "example": "It was a long voyage from London to New York."
            },
            {
                "word": "Catch up with",
                "ipa": "/kætʃ ʌp wɪð/",
                "type": "Phrasal Verb",
                "def": "reach the same point/level as someone",
                "vietnamese": "Theo kịp, đuổi kịp ai đó",
                "example": "Run fast to catch up with the group."
            },
            {
                "word": "Check in",
                "ipa": "/tʃek ɪn/",
                "type": "Phrasal Verb",
                "def": "register at a hotel or an airport",
                "vietnamese": "Làm thủ tục nhận phòng / lên máy bay",
                "example": "We checked in at the airport two hours before the flight."
            },
            {
                "word": "Drop off",
                "ipa": "/drɒp ɒf/",
                "type": "Phrasal Verb",
                "def": "let someone get out of a vehicle; fall asleep",
                "vietnamese": "Cho ai xuống xe; thiếp đi",
                "example": "I can drop you off at the station on my way to work."
            },
            {
                "word": "Unrecognisable",
                "ipa": "/ˌʌn.rek.əɡˈnaɪ.zə.bəl/",
                "type": "Adjective",
                "def": "so changed that you cannot recognise it",
                "vietnamese": "Không thể nhận ra được (biến đổi từ recognise)",
                "example": "The city has changed so much it is almost unrecognisable."
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
            st.markdown(f"**💬 Ví dụ ngữ cảnh:** *'{card["example"]}'* ")

# --- 5. GÓC LƯU Ý (WATCH OUT! CORNER) ---
elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý B2 (Watch Out! Corner)")
    st.write("Tổng hợp các bẫy ngữ pháp và từ vựng nâng cao đặc biệt (Watch out!) từ sách Destination B2.")
    
    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #1: Present Perfect Simple vs Present Perfect Continuous</h4>
    <b>Quy tắc quan trọng:</b><br>
    • Sử dụng <b>Present Perfect Simple</b> khi nhấn mạnh <u>kết quả / số lượng hoàn thành</u>:<br>
    &nbsp;&nbsp;<i>✔ I've written <b>three letters</b> this morning.</i><br>
    • Sử dụng <b>Present Perfect Continuous</b> khi nhấn mạnh <u>thời lượng / tính liên tục</u> của hành động:<br>
    &nbsp;&nbsp;<i>✔ We've been driving for <b>hours</b>.</i> (nhấn mạnh thời lượng kéo dài)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #2: Stative Verbs in Continuous Tenses</h4>
    <b>Quy tắc quan trọng:</b><br>
    Các động từ như <i>be, have, imagine, look, see, smell, taste, think</i> mang nghĩa trạng thái thì không dùng tiếp diễn, nhưng dùng ở tiếp diễn khi mô tả <b>HÀNH ĐỘNG</b>:<br>
    • <i>Do you <b>have</b> your plane ticket with you?</i> (Trạng thái: sở hữu)<br>
    • <i>Are you <b>having</b> lunch at the moment?</i> (Hành động: ăn uống)<br>
    • <i>I <b>think</b> Poland is in the EU.</i> (Trạng thái: tin/nghĩ là)<br>
    • <i>I'm <b>thinking</b> about going on holiday.</i> (Hành động: cân nhắc)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #3: Emphatic Present Simple với 'do/does'</h4>
    Khi muốn nhấn mạnh sự tương phản hoặc cảm xúc mạnh trong câu khẳng định hiện tại đơn:<br>
    • <i>✔ Actually, I <b>do like</b> going by bus for short distances!</i><br>
    • <i>✔ The bus isn't quicker than the train but it <b>does stop</b> right outside the factory.</i>
    </div>
    """, unsafe_allow_html=True)

# --- 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập (Progress Report)")
    st.write("Đánh dấu các Unit bạn đã hoàn thành để theo dõi tỷ lệ tiến độ toàn khóa học B2.")
    
    completed_units = []
    st.subheader("✅ Danh sách 28 Units & 14 Reviews:")
    
    cols = st.columns(3)
    for idx, u in enumerate(ALL_UNITS_LIST):
        col = cols[idx % 3]
        checked = col.checkbox(u, key=f"unit_chk_{idx}", value=(idx==0))
        if checked:
            completed_units.append(u)
            
    progress = len(completed_units) / len(ALL_UNITS_LIST)
    st.markdown("---")
    st.subheader("📈 Tiến độ hoàn thành toàn bộ khóa học B2:")
    st.progress(progress)
    st.info(f"🎉 Bạn đã hoàn thành **{len(completed_units)}/{len(ALL_UNITS_LIST)} mục** ({int(progress*100)}%)")
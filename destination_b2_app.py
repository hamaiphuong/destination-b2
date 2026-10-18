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
st.markdown('<div class="sub-header">Hệ thống Tự học Ngữ pháp & Từ vựng Nâng cao B2 (Cambridge FCE / Vantage Level)</div>', unsafe_allow_html=True)

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

# ALL UNITS & REVIEWS
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
        Sách gồm **28 Units** đan xen giữa Ngữ pháp và Từ vựng nâng cao, cùng hệ thống bài ôn tập đáp ứng chuẩn đầu ra kỳ thi **Cambridge CAE (C1) & CPE (C2) / FCE (B2)**:
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
                {"Cách dùng B2": "How often things happen (Tần suất công việc)", "Ví dụ minh họa": "Angela doesn't visit us very often."},
                {"Cách dùng B2": "Permanent situations (Tình huống lâu dài)", "Ví dụ minh họa": "Carlo works in a travel agent's."},
                {"Cách dùng B2": "States (Trạng thái)", "Ví dụ minh họa": "Do you have an up-to-date passport?"},
                {"Cách dùng B2": "General truths and facts (Sự thật hiển nhiên)", "Ví dụ minh họa": "Poland is in the European Union."}
            ]
            st.table(pd.DataFrame(g1_data))
            
            st.markdown("""
            <div class="tip-box">
            <b>💡 Emphatic Present Simple (Hiện tại đơn nhấn mạnh):</b><br>
            Sử dụng <code>do / does + V-bare</code> trong câu khẳng định để nhấn mạnh sự tương phản hoặc cảm xúc:<br>
            • <i>"You don't like going by bus, do you?" "Actually, I <b>do like</b> going by bus for short distances."</i><br>
            • <i>The bus isn't quicker than the train but it <b>does stop</b> right outside the factory.</i>
            </div>
            """, unsafe_allow_html=True)

        with tab_g2:
            st.markdown("#### 🔹 Present Continuous (Thì Hiện tại Tiếp diễn)")
            g2_data = [
                {"Cách dùng B2": "Actions happening now (Hành động đang diễn ra)", "Ví dụ minh họa": "Mike is driving to work at the moment."},
                {"Cách dùng B2": "Temporary series of actions (Chuỗi hành động tạm thời)", "Ví dụ minh họa": "Taxi drivers aren't stopping at the train station because of the roadworks."},
                {"Cách dùng B2": "Temporary situations (Tình huống tạm thời)", "Ví dụ minh họa": "Are they staying in a hotel near the Olympic stadium?"},
                {"Cách dùng B2": "Changing & developing situations (Sự thay đổi phát triển)", "Ví dụ minh họa": "Holidays abroad are becoming increasingly popular."},
                {"Cách dùng B2": "Annoying habits (usually with always)", "Ví dụ minh họa": "Dad is always cleaning the car when I want to use it!"}
            ]
            st.table(pd.DataFrame(g2_data))

        with tab_g3:
            st.markdown("#### 🔹 Present Perfect Simple (Thì Hiện tại Hoàn thành Đơn)")
            g3_data = [
                {"Cách dùng B2": "Situations started in past & still true", "Ví dụ minh họa": "He's had his motorbike for over six years."},
                {"Cách dùng B2": "Series of actions continuing up to now", "Ví dụ minh họa": "We've travelled by taxi, bus, plane and train - all in the last 24 hours!"},
                {"Cách dùng B2": "Completed actions at unspecified time", "Ví dụ minh họa": "Have you ever flown in a helicopter?"},
                {"Cách dùng B2": "Completed actions with important present result", "Ví dụ minh họa": "I've booked the coach tickets."}
            ]
            st.table(pd.DataFrame(g3_data))

        with tab_g4:
            st.markdown("#### 🔹 Present Perfect Continuous (Thì Hiện tại Hoàn thành Tiếp diễn)")
            g4_data = [
                {"Cách dùng B2": "Actions continuing up to present moment", "Ví dụ minh họa": "We have been driving for hours. Can't we have a break soon?"},
                {"Cách dùng B2": "Actions stopping just before present moment", "Ví dụ minh họa": "I'm out of breath because I've been running to get here in time."}
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
        st.write("Từ vựng phân biệt, Phrasal Verbs, Phrases & Collocations, Word Patterns và Word Formation từ sách Destination B2:")
        
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
        st.subheader("✍️ Unit 1: Present time - Full Practice Exercises (Đề HS & Đáp án GV)")
        st.info("Trích xuất đầy đủ 100% các bài tập Exercise A -> J từ file đề học sinh (HS) và đáp án giáo viên (GV). Lựa chọn trắc nghiệm đều **bỏ trống ban đầu**.")
        
        tab_a, tab_b, tab_c, tab_d, tab_e, tab_f, tab_g, tab_h, tab_j = st.tabs([
            "Exercise A (Circle correct word)",
            "Exercise B (Rewrite correctly)",
            "Exercise C (Verb form in brackets)",
            "Exercise D (Fill time words)",
            "Exercise E (Multiple Choice)",
            "Exercise F (Ancient Aviators)",
            "Exercise G (Match sentences)",
            "Exercise H (Extra word)",
            "Exercise J (Rewrite 2-5 words)"
        ])
        
        with st.form("unit1_b2_full_quiz_form"):
            with tab_a:
                st.markdown("#### Exercise A: Circle the correct word or phrase")
                qa1 = st.radio("Câu 1: Elizabeth ________ to bed at around eleven o'clock.", ["usually goes", "is usually going"], index=None, key="b2_a1")
                qa2 = st.radio("Câu 2: Dan ________ on the other phone right now.", ["talks", "is talking"], index=None, key="b2_a2")
                qa3 = st.radio("Câu 3: We ________ any meat at the moment as we're both on a diet.", ["don't eat", "aren't eating"], index=None, key="b2_a3")
                qa4 = st.radio("Câu 4: ________ increasingly safe?", ["Does air travel get", "Is air travel getting"], index=None, key="b2_a4")
                qa5 = st.radio("Câu 5: My mum ________ me every weekend without fail.", ["calls", "is calling"], index=None, key="b2_a5")
                qa6 = st.radio("Câu 6: How much ________?", ["do babysitters generally earn", "are babysitters generally earning"], index=None, key="b2_a6")
                qa7 = st.radio("Câu 7: ________ up with excuses for not having done your homework. It's so annoying!", ["You always come", "You're always coming"], index=None, key="b2_a7")
                qa8_1 = st.radio("Câu 8 (vị trí 1): I ________ out much during the week...", ["don't go", "I'm not going"], index=None, key="b2_a8_1")
                qa8_2 = st.radio("Câu 8 (vị trí 2): ...but I ________ to go out somewhere on Saturday night.", ["always try", "I'm always trying"], index=None, key="b2_a8_2")
                qa9 = st.radio("Câu 9: No, the train ________ at Cirencester on Saturdays.", ["does stop", "is stopping"], index=None, key="b2_a9")
                qa10 = st.radio("Câu 10: My mum ________ part in ice-skating competitions almost every weekend.", ["takes", "is taking"], index=None, key="b2_a10")

            with tab_b:
                st.markdown("#### Exercise B: Rewrite correctly. Change the words or phrases in bold")
                qb1 = st.text_input("Câu 1: My dad **is often getting up** late on Saturday mornings.", key="b2_b1", help="Gợi ý: Thói quen hiện tại dùng Present Simple")
                qb2 = st.text_input("Câu 2: **Are you speaking** any other languages apart from English?", key="b2_b2", help="Gợi ý: Khả năng ngôn ngữ dùng Present Simple")
                qb3 = st.text_input("Câu 3: **I already buy** all my Christmas presents and it's only October!", key="b2_b3", help="Gợi ý: Đã hoàn thành trước hiện tại dùng Present Perfect")
                qb4 = st.text_input("Câu 4: It's the first time **I'm ever having** a party at home.", key="b2_b4", help="Gợi ý: It's the first time + Present Perfect Simple")
                qb5 = st.text_input("Câu 5: Actually, I think Darren **does works** quite hard sometimes.", key="b2_b5", help="Gợi ý: Sửa dạng động từ sau does hoặc bỏ does")
                qb6 = st.text_input("Câu 6: Carlo **is never eating** Chinese food before.", key="b2_b6")
                qb7 = st.text_input("Câu 7: Sean **already books** a table for tonight.", key="b2_b7")
                qb8 = st.text_input("Câu 8: **Needs Melanie** any help painting her new flat?", key="b2_b8")

            with tab_c:
                st.markdown("#### Exercise C: Complete using the correct form of verbs in brackets")
                qc1 = st.text_input("Câu 1: It's the first time ________ (I/ever/eat) octopus!", key="b2_c1")
                qc2 = st.text_input("Câu 2: Sandy ________ (not/see) his sister since she went to university.", key="b2_c2")
                qc3 = st.text_input("Câu 3: They ________ (go) on holiday to Spain and won't be back until the end of the month.", key="b2_c3")
                qc4 = st.text_input("Câu 4: Poor Tracy! She ________ (write) that essay for hours now and she still hasn't finished!", key="b2_c4")
                qc5 = st.text_input("Câu 5: ________ (you/ever/meet) anyone famous?", key="b2_c5")
                qc6 = st.text_input("Câu 6: ________ (I/try) to get in touch with Jenny all morning but I can't find her anywhere.", key="b2_c6")
                qc7 = st.text_input("Câu 7: ________ (I/not finish) the book yet so I can't tell you what happens.", key="b2_c7")
                qc8 = st.text_input("Câu 8: ________ (you/already/decide) where you're going this summer?", key="b2_c8")
                qc9 = st.text_input("Câu 9: ________ (We/live) here for the last six years.", key="b2_c9")
                qc10 = st.text_input("Câu 10: ________ (I/never/hear) such nonsense!", key="b2_c10")

            with tab_d:
                st.markdown("#### Exercise D: Complete using the words in the box")
                st.caption("Danh sách từ: already • before • ever • for • just • rarely • since • so • still • yet")
                qd1 = st.text_input("Câu 1: Have you ________ dreamt of winning the lottery?", key="b2_d1")
                qd2 = st.text_input("Câu 2: I haven't worked out how to set the timer on the video ________.", key="b2_d2")
                qd3 = st.text_input("Câu 3: My dad's lived in the same house ________ he was born.", key="b2_d3")
                qd4 = st.text_input("Câu 4: The film's only been on ________ a couple of minutes.", key="b2_d4")
                qd5 = st.text_input("Câu 5: Bruce has knocked three men out of the competition ________ far.", key="b2_d5")
                qd6 = st.text_input("Câu 6: I ________ get the chance to get any exercise - I'm just too busy.", key="b2_d6")
                qd7 = st.text_input("Câu 7: He's only ________ got home.", key="b2_d7")
                qd8 = st.text_input("Câu 8: It's eleven o'clock and Todd ________ hasn't come home. Where could he be?", key="b2_d8")
                qd9 = st.text_input("Câu 9: I've never met Ruth ________. What's she like?", key="b2_d9")
                qd10 = st.text_input("Câu 10: Have you finished ________? That was quick.", key="b2_d10")

            with tab_e:
                st.markdown("#### Exercise E: Choose the correct answer")
                qe1 = st.radio("Câu 1: Ian ________ a shower at the moment, so could you call back in about half an hour?", ["A. takes", "B. is taking", "C. has taken", "D. has been taking"], index=None, key="b2_e1")
                qe2 = st.radio("Câu 2: ________ to Ipswich before?", ["A. Do you ever go", "B. Are you ever going", "C. Have you ever been", "D. Have you ever been going"], index=None, key="b2_e2")
                qe3 = st.radio("Câu 3: I ________ to all the local newspapers and TV stations to complain.", ["A. already write", "B. already writing", "C. have already written", "D. have already been writing"], index=None, key="b2_e3")
                qe4 = st.radio("Câu 4: ________ TV for the last four hours? Turn it off and get some exercise!", ["A. Do you watch", "B. Are you watching", "C. Watched you", "D. Have you been watching"], index=None, key="b2_e4")
                qe5 = st.radio("Câu 5: Eric, ________ hockey competitively or just for fun?", ["A. do you usually play", "B. are you usually playing", "C. have you usually played", "D. have you usually been playing"], index=None, key="b2_e5")
                qe6 = st.radio("Câu 6: That's the first time ________ an answer right today!", ["A. I get", "B. I am going", "C. I have got", "D. I have been getting"], index=None, key="b2_e6")
                qe7 = st.radio("Câu 7: Jessica has ________ left, I'm afraid.", ["A. already", "B. yet", "C. still", "D. so far"], index=None, key="b2_e7")
                qe8 = st.radio("Câu 8: Dan ________ in the living room while we redecorate his bedroom.", ["A. sleeps", "B. is sleeping", "C. has slept", "D. does slept"], index=None, key="b2_e8")
                qe9 = st.radio("Câu 9: Unfortunately, Simone ________ a day off very often.", ["A. doesn't get", "B. isn't getting", "C. hasn't got", "D. hasn't been getting"], index=None, key="b2_e9")
                qe10 = st.radio("Câu 10: Actually, I ________ a cup of tea first thing every morning but then I switch to coffee.", ["A. do drink", "B. am drinking", "C. have drunk", "D. have been drinking"], index=None, key="b2_e10")

            with tab_f:
                st.markdown("#### Exercise F: Complete using the correct form of words (Ancient Aviators)")
                st.caption("Các từ gợi ý: be • disagree • do • include • know • look • see • seem • understand")
                qf1 = st.text_input("Câu (1): Everyone ________ that humans have been flying for only a few hundred years.", key="b2_f1")
                qf2 = st.text_input("Câu (2): But ________ it possible that ancient civilizations also had the ability to fly?", key="b2_f2")
                qf3 = st.text_input("Câu (3): On the ground, they just ________ like straight lines.", key="b2_f3")
                qf4 = st.text_input("Câu (4): But when you ________ them from the air...", key="b2_f4")
                qf5 = st.text_input("Câu (5): ...you ________ exactly what they are.", key="b2_f5")
                qf6 = st.text_input("Câu (6): The pictures ________ animals, birds and symbols.", key="b2_f6")
                qf7 = st.text_input("Câu (7): One bizarre theory, which most mainstream scientists ________ with...", key="b2_f7")
                qf8 = st.text_input("Câu (8): It ________ incredible...", key="b2_f8")
                qf9 = st.text_input("Câu (9): ...but a few people ________ believe it's possible.", key="b2_f9")

            with tab_g:
                st.markdown("#### Exercise G: Match to make sentences")
                qg1 = st.radio("Câu 1: I think ________", ["A. darker hair than her sister.", "B. I'm going to buy the new Racetrack CD.", "C. a haircut at the moment.", "D. for his glasses. Have you seen them?", "E. not old enough to drive a car.", "F. of getting Dad a CD for his birthday.", "G. very annoying at the moment!", "H. like he needs a holiday!"], index=None, key="b2_g1")
                qg2 = st.radio("Câu 2: I'm thinking ________", ["A. darker hair than her sister.", "B. I'm going to buy the new Racetrack CD.", "C. a haircut at the moment.", "D. for his glasses. Have you seen them?", "E. not old enough to drive a car.", "F. of getting Dad a CD for his birthday.", "G. very annoying at the moment!", "H. like he needs a holiday!"], index=None, key="b2_g2")
                qg3 = st.radio("Câu 3: Phil's looking ________", ["A. darker hair than her sister.", "B. I'm going to buy the new Racetrack CD.", "C. a haircut at the moment.", "D. for his glasses. Have you seen them?", "E. not old enough to drive a car.", "F. of getting Dad a CD for his birthday.", "G. very annoying at the moment!", "H. like he needs a holiday!"], index=None, key="b2_g3")
                qg4 = st.radio("Câu 4: Phil looks ________", ["A. darker hair than her sister.", "B. I'm going to buy the new Racetrack CD.", "C. a haircut at the moment.", "D. for his glasses. Have you seen them?", "E. not old enough to drive a car.", "F. of getting Dad a CD for his birthday.", "G. very annoying at the moment!", "H. like he needs a holiday!"], index=None, key="b2_g4")

            with tab_h:
                st.markdown("#### Exercise H: Find the extra word in each line")
                qh1 = st.text_input("Dòng 1: I've been to travelling round Europe all summer.", key="b2_h1", help="Nhập duy nhất từ thừa")
                qh2 = st.text_input("Dòng 2: It's the first time I've ever been going abroad...", key="b2_h2", help="Nhập duy nhất từ thừa")
                qh3 = st.text_input("Dòng 3: ...and I have to also made loads of new friends.", key="b2_h3", help="Nhập duy nhất từ thừa")
                qh4 = st.text_input("Dòng 4: I've been decided to stay in touch with them now I'm back.", key="b2_h4", help="Nhập duy nhất từ thừa")
                qh5 = st.text_input("Dòng 5: One of them, Giselle, is French. She was making on holiday too.", key="b2_h5", help="Nhập duy nhất từ thừa")

            with tab_j:
                st.markdown("#### Exercise J: Complete each second sentence using the word given")
                st.caption("Viết từ 2 đến 5 từ bao gồm từ cho sẵn")
                qj1 = st.text_input("Câu 1: What's the price of the tickets, Jimmy? (much)", key="b2_j1", help="Điền vế tiếp theo: How ...")
                qj2 = st.text_input("Câu 2: Are these your trainers? (to)", key="b2_j2", help="Điền vế tiếp theo: Do ...")
                qj3 = st.text_input("Câu 3: Sasha's not keen on team sports at all. (like)", key="b2_j3", help="Điền vế tiếp theo: Sasha ...")
                qj4 = st.text_input("Câu 4: It's only her second time in a recording studio. (been)", key="b2_j4", help="Điền vế tiếp theo: She ...")
                qj5 = st.text_input("Câu 5: We got here three hours ago. (have)", key="b2_j5", help="Điền vế tiếp theo: We ...")
                qj6 = st.text_input("Câu 6: I started writing this hours ago and it's still not right. (writing)", key="b2_j6", help="Điền vế tiếp theo: I ...")
                qj7 = st.text_input("Câu 7: This is my first experience of flying alone. (time)", key="b2_j7", help="Điền vế tiếp theo: It is the first ...")
                qj8 = st.text_input("Câu 8: Sharon's in the bath at the moment. (a)", key="b2_j8", help="Điền vế tiếp theo: Sharon ...")
                qj9 = st.text_input("Câu 9: Paul enjoys surprises apart from on his birthday. (does)", key="b2_j9", help="Điền vế tiếp theo: Paul ...")

            submit_b2_quiz = st.form_submit_button("🚀 Nộp bài & Kiểm tra Đáp án (Submit Answers)")

        if submit_b2_quiz:
            st.markdown("### 📊 Kết quả & Đáp án Chi tiết (GV Answer Key):")
            score = 0
            total_items = 0

            # Exercise A Check
            st.markdown("#### 📝 Kết quả Exercise A:")
            if qa1 == "usually goes": score += 1; st.success("✅ Câu 1 đúng: usually goes")
            elif qa1: st.error("❌ Câu 1 sai. Đáp án đúng: **usually goes** (Thói quen sinh hoạt lặp đi lặp lại).")
            total_items += 1

            if qa2 == "is talking": score += 1; st.success("✅ Câu 2 đúng: is talking")
            elif qa2: st.error("❌ Câu 2 sai. Đáp án đúng: **is talking** (Hành động đang diễn ra right now).")
            total_items += 1

            if qa3 == "aren't eating": score += 1; st.success("✅ Câu 3 đúng: aren't eating")
            elif qa3: st.error("❌ Câu 3 sai. Đáp án đúng: **aren't eating** (Tình huống tạm thời at the moment).")
            total_items += 1

            if qa4 == "Is air travel getting": score += 1; st.success("✅ Câu 4 đúng: Is air travel getting")
            elif qa4: st.error("❌ Câu 4 sai. Đáp án đúng: **Is air travel getting** (Sự thay đổi phát triển).")
            total_items += 1

            if qa5 == "calls": score += 1; st.success("✅ Câu 5 đúng: calls")
            elif qa5: st.error("❌ Câu 5 sai. Đáp án đúng: **calls** (Thói quen lặp lại hàng tuần).")
            total_items += 1

            # Exercise E Check
            st.markdown("#### 📝 Kết quả Exercise E:")
            if qe1 == "B. is taking": score += 1; st.success("✅ Câu 1 đúng: B. is taking")
            elif qe1: st.error("❌ Câu 1 sai. Đáp án đúng: **B. is taking** (Hành động đang xảy ra at the moment).")
            total_items += 1

            if qe2 == "C. Have you ever been": score += 1; st.success("✅ Câu 2 đúng: C. Have you ever been")
            elif qe2: st.error("❌ Câu 2 sai. Đáp án đúng: **C. Have you ever been** (Trải nghiệm đến thời điểm hiện tại).")
            total_items += 1

            if qe3 == "C. have already written": score += 1; st.success("✅ Câu 3 đúng: C. have already written")
            elif qe3: st.error("❌ Câu 3 sai. Đáp án đúng: **C. have already written** (Hành động đã hoàn tất có kết quả).")
            total_items += 1

            if qe4 == "D. Have you been watching": score += 1; st.success("✅ Câu 4 đúng: D. Have you been watching")
            elif qe4: st.error("❌ Câu 4 sai. Đáp án đúng: **D. Have you been watching** (Nhấn mạnh thời lượng for the last four hours).")
            total_items += 1

            if qe5 == "A. do you usually play": score += 1; st.success("✅ Câu 5 đúng: A. do you usually play")
            elif qe5: st.error("❌ Câu 5 sai. Đáp án đúng: **A. do you usually play** (Thói quen/sở thích thông thường).")
            total_items += 1

            pct = int((score / total_items) * 100)
            st.info(f"🏆 Điểm phần chọn lọc: **{score}/{total_items}** ({pct}%)")
            if pct == 100:
                st.balloons()

    else:
        st.info(f"Hệ thống bài tập tương tác chi tiết cho **{selected_quiz_unit}** đang được hoàn thiện.")

# --- 4. THẺ GHI NHỚ TỪ VỰNG (FLASHCARDS) ---
elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng (Flashcards)")
    selected_fc_unit = st.selectbox("🎯 Chọn Unit Từ vựng / Review để học thẻ:", VOCAB_UNITS)
    
    if "Unit 1" in selected_fc_unit or "Grammar" in selected_fc_unit:
        st.warning("⚠️ Thẻ ghi nhớ (Flashcards) chỉ dành riêng cho các Unit Từ vựng (Vocabulary Units) và các bài Reviews. Các Unit Ngữ pháp tập trung vào Lý thuyết và Bài tập Tương tác.")
    else:
        flashcards_b2_data = [
            {"word": "voyage (n)", "ipa": "/ˈvɔɪ.ɪdʒ/", "type": "Noun", "def": "a long journey, especially on a ship", "vi": "chuyến đi dài bằng đường biển", "ex": "It was a long voyage from London to New York."},
            {"word": "journey (n)", "ipa": "/ˈdʒɜː.ni/", "type": "Noun", "def": "an occasion when you travel from one place to another", "vi": "chuyến đi, hành trình", "ex": "We had a long journey ahead of us."},
            {"word": "trip (n)", "ipa": "/trɪp/", "type": "Noun", "def": "an occasion when you go somewhere and come back again", "vi": "chuyến đi ngắn (đi rồi về)", "ex": "The whole family went on a trip to Florida."},
            {"word": "excursion (n)", "ipa": "/ɪkˈskɜː.ʃən/", "type": "Noun", "def": "a short journey that you make for pleasure", "vi": "chuyến tham quan, dã ngoại", "ex": "My grandmother often talks about excursions to the sea."},
            {"word": "catch up with (phr v)", "ipa": "/kætʃ ʌp wɪð/", "type": "Phrasal Verb", "def": "reach the same point/level as someone", "vi": "theo kịp, đuổi kịp", "ex": "Run fast to catch up with the group."},
            {"word": "check in (phr v)", "ipa": "/tʃek ɪn/", "type": "Phrasal Verb", "def": "register at a hotel or an airport", "vi": "làm thủ tục nhận phòng/lên máy bay", "ex": "We checked in at the airport two hours before the flight."}
        ]
        
        card_idx = st.slider("🎯 Chọn thẻ từ vựng:", 1, len(flashcards_b2_data), 1) - 1
        card = flashcards_b2_data[card_idx]
        
        st.markdown(f"""
        <div class="card" style="text-align: center; padding: 2rem;">
            <span class="badge-vocab">{card['type']}</span>
            <h2 style="color: #1E3A8A; margin-top: 0.5rem;">{card['word']}</h2>
            <p style="color: #6B7280; font-size: 1.1rem; font-weight: 500;">🔊 {card['ipa']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🔍 LẬT THẺ ĐỂ XEM NGHĨA & VÍ DỤ"):
            st.markdown(f"**📖 Định nghĩa Tiếng Anh:** {card['def']}")
            st.markdown(f"**🇻🇳 Nghĩa Tiếng Việt:** {card['vi']}")
            st.markdown(f"**💬 Ví dụ ngữ cảnh:** *\"{card['ex']}\"*")

# --- 5. GÓC LƯU Ý (WATCH OUT! CORNER) ---
elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý B2 (Watch Out! Corner)")
    st.write("Tổng hợp các bẫy ngữ pháp và từ vựng nâng cao đặc biệt (Watch out!) từ sách Destination B2:")
    
    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #1: Present Perfect Simple vs Present Perfect Continuous</h4>
    <b>Quy tắc quan trọng:</b><br>
    • Sử dụng <b>Present Perfect Simple</b> khi đề cập đến <u>số lượng cụ thể / số lần hoàn thành</u>:<br>
    &nbsp;&nbsp;<i>✔ I've written <b>two essays</b> this week.</i><br>
    • Sử dụng <b>Present Perfect Continuous</b> khi nhấn mạnh <u>thời lượng / tính liên tục</u> của hành động:<br>
    &nbsp;&nbsp;<i>✔ I've been working here for <b>five years</b>.</i>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #2: Stative Verbs in Continuous Tenses</h4>
    <b>Quy tắc quan trọng:</b><br>
    Nhiều động từ trạng thái có thể dùng ở thì tiếp diễn khi mô tả <b>HÀNH ĐỘNG</b> thay vì TRẠNG THÁI:<br>
    • <i>Do you <b>have</b> your plane ticket with you?</i> (State: sở hữu)<br>
    • <i>Are you <b>having</b> lunch at the moment?</i> (Action: ăn uống)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #3: Emphatic Present Simple (do/does)</h4>
    Có thể dùng <b>do / does + V-bare</b> trong câu khẳng định hiện tại đơn để nhấn mạnh sự tương phản hoặc cảm xúc:<br>
    • <i>"You don't like going by bus, do you?" "Actually, I <b>do like</b> going by bus for short distances."</i>
    </div>
    """, unsafe_allow_html=True)

# --- 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập (Progress Report)")
    st.write("Đánh dấu các Unit bạn đã hoàn thành để theo dõi tỷ lệ tiến độ toàn bộ cuốn sách Destination B2.")
    
    completed_units = []
    st.subheader("✅ Danh sách 28 Units, 14 Reviews & 2 Progress Tests:")
    
    cols = st.columns(3)
    for idx, u in enumerate(ALL_UNITS_LIST):
        col = cols[idx % 3]
        checked = col.checkbox(u, key=f"b2_unit_chk_{idx}", value=(idx==0))
        if checked:
            completed_units.append(u)
            
    progress = len(completed_units) / len(ALL_UNITS_LIST)
    st.markdown("---")
    st.subheader("📈 Tiến độ hoàn thành toàn bộ chương trình B2:")
    st.progress(progress)
    st.info(f"🎉 Bạn đã hoàn thành **{len(completed_units)}/{len(ALL_UNITS_LIST)} bài** ({int(progress*100)}%)")

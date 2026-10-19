import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Destination B2 Self-Study Hub",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header { font-size: 2.2rem; color: #1E3A8A; font-weight: 800; text-align: center; margin-bottom: 0.2rem; }
    .sub-header { font-size: 1.1rem; color: #4B5563; text-align: center; margin-bottom: 1.5rem; }
    .explain-box { background-color: #F8FAFC; border-left: 4px solid #3B82F6; padding: 0.8rem; margin-top: 0.4rem; border-radius: 4px; font-size: 0.95rem; }
    .badge-grammar { background-color: #DBEAFE; color: #1E40AF; padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
    .badge-vocab { background-color: #FCE7F3; color: #9D174D; padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">📘 DESTINATION B2: LEARNING HUB</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Hệ thống Tự học Ngữ pháp & Từ vựng - Cấp độ B2</div>', unsafe_allow_html=True)

# Navigation
st.sidebar.title("📌 MENU CHÍNH")
menu_option = st.sidebar.radio(
    "Chọn chức năng:",
    [
        "📌 Tổng quan & Lộ trình tự học",
        "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)",
        "✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)",
        "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)",
        "📊 Báo cáo Tiến độ Học tập (Progress Report)"
    ]
)

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

# --- 1. TỔNG QUAN & LỘ TRÌNH TỰ HỌC ---
if menu_option == "📌 Tổng quan & Lộ trình tự học":
    st.header("📌 Tổng quan Sách & Lộ trình Tự học")
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        ### 📚 Cấu trúc bộ sách Destination B2
        Sách gồm **28 Units** đan xen giữa Ngữ pháp và Từ vựng, cùng hệ thống bài ôn tập đáp ứng chuẩn đầu ra FCE (B2):
        * **14 Unit Ngữ pháp (Grammar Units)**: Hệ thống quy tắc chuyên sâu, cấu trúc câu nâng cao và các ngoại lệ.
        * **14 Unit Từ vựng (Vocabulary Units)**: Topic vocabulary in contrast, Phrasal verbs, Phrases & Collocations, Word patterns, Word formation.
        * **14 Bài Ôn tập (Reviews)**: Ôn tập định kỳ sau mỗi 2 Units.
        * **2 Bài Kiểm tra Tiến độ (Progress Tests)**: Progress Test 1 (Units 1–14) & Progress Test 2 (Units 15–28).
        """)
        st.markdown("""
        ### 🗺️ Lộ trình tự học 4 bước:
        1. **Bước 1 (Theory Hub)**: Nắm vững bảng lý thuyết ngữ pháp và danh mục từ vựng chuẩn Cambridge B2.
        2. **Bước 2 (Interactive Quiz)**: Luyện tập bài tập tương tác, kiểm tra đáp án tự động và đọc giải thích chi tiết.
        3. **Bước 3 (Flashcards)**: Ôn luyện phản xạ từ vựng hàng ngày bằng thẻ ghi nhớ thông minh.
        4. **Bước 4 (Progress Report)**: Đánh dấu tiến độ và theo dõi sự phát triển.
        """)
    with col2:
        st.info("📋 **DANH SÁCH 28 UNITS & 14 REVIEWS**")
        df_units = pd.DataFrame([{"STT": i+1, "Tên bài học": u} for i, u in enumerate(ALL_UNITS_LIST)])
        st.dataframe(df_units, use_container_width=True, height=400)

# --- 2. TRA CỨU LÝ THUYẾT TRỌNG TÂM (THEORY HUB) ---
elif menu_option == "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)":
    st.header("📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)")
    selected_unit = st.selectbox("🎯 Chọn Unit / Bài Ôn tập cần tra cứu:", ALL_UNITS_LIST)
    
    if "Unit 1" in selected_unit:
        st.subheader("Unit 1: Grammar - Present time (Các thì Hiện tại B2)")
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "1. Present Simple", 
            "2. Present Continuous", 
            "3. Present Perfect Simple", 
            "4. Present Perfect Continuous", 
            "5. Stative Verbs"
        ])
        
        with tab1:
            st.markdown("#### 🔹 Present Simple (Thì Hiện tại Đơn)")
            g1_data = [
                {"Use (Cách dùng)": "Current habits (Thói quen hiện tại)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Toby works to work."},
                {"Use (Cách dùng)": "To talk about how often things happen (Tần suất sự việc)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Angela doesn't visit us very often."},
                {"Use (Cách dùng)": "Permanent situations (Tình huống lâu dài)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Carlo walks in a travel agent's."},
                {"Use (Cách dùng)": "States (Trạng thái)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Do you have an up-to-date passport?"},
                {"Use (Cách dùng)": "General truths and facts (Sự thật hiển nhiên & Chân lý)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Poland is in the European Union."}
            ]
            st.table(pd.DataFrame(g1_data))
            st.info("💡 **Watch out! Emphatic Present Simple (Hiện tại đơn nhấn mạnh):**\n"
                    "We can also use *do/does* in present simple statements for emphasis:\n"
                    "- *'You don't like going by bus, do you?' 'Actually, I do like going by bus for short distances.'*\n"
                    "- *The bus isn't quicker than the train, but it does stop right outside the factory.*")

        with tab2:
            st.markdown("#### 🔹 Present Continuous (Thì Hiện tại Tiếp diễn)")
            g2_data = [
                {"Use (Cách dùng)": "Actions happening now (Hành động đang diễn ra lúc nói)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Mike is driving to work at the moment."},
                {"Use (Cách dùng)": "Temporary series of actions (Chuỗi hành động tạm thời)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Taxi drivers aren't stopping at the train station because of the roadworks."},
                {"Use (Cách dùng)": "Temporary situations (Tình huống tạm thời)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Are they staying in a hotel near the Olympic stadium?"},
                {"Use (Cách dùng)": "Changing and developing situations (Sự thay đổi & Phát triển)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Holidays abroad are becoming increasingly popular."},
                {"Use (Cách dùng)": "Annoying habits (usually with always) (Thói quen gây phiền phức)", "Example in Textbook (Ví dụ chuẩn trong sách)": "Dad is always cleaning the car when I want to use it!"}
            ]
            st.table(pd.DataFrame(g2_data))

        with tab3:
            st.markdown("#### 🔹 Present Perfect Simple (Thì Hiện tại Hoàn thành Đơn)")
            g3_data = [
                {"Use (Cách dùng)": "Situations and states that started in the past and are still true", "Example in Textbook (Ví dụ chuẩn trong sách)": "He's had his motorbike for over six years."},
                {"Use (Cách dùng)": "A series of actions continuing up to now", "Example in Textbook (Ví dụ chuẩn trong sách)": "We've travelled by taxi, bus, plane and train - all in the last twenty-four hours!"},
                {"Use (Cách dùng)": "Completed actions at a time in the past which is not mentioned", "Example in Textbook (Ví dụ chuẩn trong sách)": "Have you ever flown in a helicopter?"},
                {"Use (Cách dùng)": "Completed actions where the important thing is the present result", "Example in Textbook (Ví dụ chuẩn trong sách)": "I've booked the coach tickets."}
            ]
            st.table(pd.DataFrame(g3_data))
            st.warning("⚠️ **Watch out!** Phrases such as *It's the first/second/etc time...* are followed by the present perfect simple:\n"
                       "- *It's the second time I've been on a plane.*")

        with tab4:
            st.markdown("#### 🔹 Present Perfect Continuous (Thì Hiện tại Hoàn thành Tiếp diễn)")
            g4_data = [
                {"Use (Cách dùng)": "Actions continuing up to the present moment (Nhấn mạnh thời lượng tính liên tục)", "Example in Textbook (Ví dụ chuẩn trong sách)": "We have been driving for hours. Can't we have a break soon?"},
                {"Use (Cách dùng)": "Actions stopping just before the present moment (Mới dừng lại, có dấu vết ở hiện tại)", "Example in Textbook (Ví dụ chuẩn trong sách)": "I'm out of breath because I've been running to get here in time."}
            ]
            st.table(pd.DataFrame(g4_data))
            st.info("💡 **Watch out!**\n"
                    "- Often used with *all day/week/year, for, since, just, etc.*: *We've been walking for hours and I need a rest.*\n"
                    "- NOT normally used with *ever* and *never*: *Have you ever flown in a helicopter before?*\n"
                    "- Comparison: *I have read that book (I have finished it)* vs *I have been reading that book (I have not finished it)*.")

        with tab5:
            st.markdown("#### 🔹 Stative Verbs (Động từ Chỉ Trạng thái)")
            st.markdown("Stative verbs are not normally used in continuous tenses because they don't describe actions.\n"
                        "✔ *I see what you mean.* (NOT ✖ *I am seeing what you mean.*)")
            st.markdown("""
            - **Thinking**: *believe, imagine, know, mean, think, understand*
            - **Existence**: *be, exist*
            - **Emotions**: *hate, like, love, need, prefer, satisfy, want*
            - **Human Senses**: *hear, see, smell, sound, taste*
            - **Appearance**: *appear, look, resemble, seem*
            - **Possession & Relationships**: *belong to, consist of, have, include, involve, own*
            """)
            st.warning("⚠️ **Watch out! Stative vs Dynamic Meaning:**\n"
                       "- *Do you have your plane ticket with you?* (state: possession)\n"
                       "- *Are you having lunch at the moment?* (action: eating)")

    else:
        st.info(f"Nội dung lý thuyết cho **{selected_unit}** đang được phát triển theo giáo trình Destination B2.")

# --- 3. BÀI TẬP TƯƠNG TÁC & CHẤM ĐIỂM TỰ ĐỘNG (INTERACTIVE QUIZ) ---
elif menu_option == "✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)":
    st.header("✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)")
    selected_quiz_unit = st.selectbox("🎯 Chọn Unit / Bài Ôn tập làm bài:", ALL_UNITS_LIST)
    
    if "Unit 1" in selected_quiz_unit:
        st.subheader("✍️ Unit 1: Present time - Full Practice Exercises")
        st.info("Hãy hoàn thành các bài tập bên dưới.")
        
        tab_a, tab_b, tab_c, tab_d, tab_e, tab_f, tab_g, tab_h, tab_i, tab_j = st.tabs([
            "Ex A (Choose)", "Ex B (Rewrite)", "Ex C (Verb Form)", "Ex D (Gap Fill)", 
            "Ex E (MCQ)", "Ex F (Cloze)", "Ex G (Match)", "Ex H (Extra Word)", "Ex I (Holiday Blues)", "Ex J (Key Word Transformation)"
        ])
        
        with st.form("u1_full_practice_form"):
            # --- EXERCISE A ---
            with tab_a:
                st.markdown("#### Exercise A: Circle the correct word or phrase")
                u1_qa1 = st.radio("Câu 1: Elizabeth usually goes / is usually going to bed at around eleven o'clock.", [None, "usually goes", "is usually going"], key="u1_qa1")
                u1_qa2 = st.radio("Câu 2: Dan talks / is talking on the other phone right now.", [None, "talks", "is talking"], key="u1_qa2")
                u1_qa3 = st.radio("Câu 3: We don't eat / aren't eating any meat at the moment as we're both on a diet.", [None, "don't eat", "aren't eating"], key="u1_qa3")
                u1_qa4 = st.radio("Câu 4: Does air travel get / Is air travel getting increasingly safe?", [None, "Does air travel get", "Is air travel getting"], key="u1_qa4")
                u1_qa5 = st.radio("Câu 5: My mum calls / is calling me every weekend without fail.", [None, "calls", "is calling"], key="u1_qa5")
                u1_qa6 = st.radio("Câu 6: How much do babysitters generally earn / are babysitters generally earning?", [None, "do babysitters generally earn", "are babysitters generally earning"], key="u1_qa6")
                u1_qa7 = st.radio("Câu 7: You always come / You're always coming up with excuses for not having done your homework. It's so annoying!", [None, "You always come", "You're always coming"], key="u1_qa7")
                u1_qa8_1 = st.radio("Câu 8 (vế 1): I don't go / I'm not going out much during the week...", [None, "don't go", "am not going"], key="u1_qa8_1")
                u1_qa8_2 = st.radio("Câu 8 (vế 2): ...but I always try / I'm always trying to go out somewhere on Saturday night.", [None, "always try", "am always trying"], key="u1_qa8_2")
                u1_qa9 = st.radio("Câu 9: No, the train does stop / is stopping at Cirencester on Saturdays.", [None, "does stop", "is stopping"], key="u1_qa9")
                u1_qa10 = st.radio("Câu 10: My mum takes / is taking part in ice-skating competitions almost every weekend.", [None, "takes", "is taking"], key="u1_qa10")

            # --- EXERCISE B ---
            with tab_b:
                st.markdown("#### Exercise B: Rewrite correctly. Change the words or phrases in bold")
                u1_qb1 = st.text_input("Câu 1: My dad **is often getting up** late on Saturday mornings.", key="u1_qb1")
                u1_qb2 = st.text_input("Câu 2: **Are you speaking** any other languages apart from English?", key="u1_qb2")
                u1_qb3 = st.text_input("Câu 3: **I already buy** all my Christmas presents and it's only October!", key="u1_qb3")
                u1_qb4 = st.text_input("Câu 4: It's the first time **I'm ever having** a party at home.", key="u1_qb4")
                u1_qb5 = st.text_input("Câu 5: Actually, I think Darren **does works** quite hard sometimes.", key="u1_qb5")
                u1_qb6 = st.text_input("Câu 6: Carlo **is never eating** Chinese food before.", key="u1_qb6")
                u1_qb7 = st.text_input("Câu 7: Sean **already books** a table for tonight.", key="u1_qb7")
                u1_qb8 = st.text_input("Câu 8: **Needs Melanie** any help painting her new flat?", key="u1_qb8")

            # --- EXERCISE C ---
            with tab_c:
                st.markdown("#### Exercise C: Complete using the correct form of the verb in brackets")
                u1_qc1 = st.text_input("Câu 1: It's the first time ________ (I / ever / eat) octopus!", key="u1_qc1")
                u1_qc2 = st.text_input("Câu 2: Sandy ________ (not / see) his sister since she went to university.", key="u1_qc2")
                u1_qc3 = st.text_input("Câu 3: They ________ (go) on holiday to Spain and won't be back until the end of the month.", key="u1_qc3")
                u1_qc4 = st.text_input("Câu 4: Poor Tracy! She ________ (write) that essay for hours now and she still hasn't finished!", key="u1_qc4")
                u1_qc5 = st.text_input("Câu 5: ________ (you / ever / meet) anyone famous?", key="u1_qc5")
                u1_qc6 = st.text_input("Câu 6: ________ (I / try) to get in touch with Jenny all morning but I can't find her anywhere.", key="u1_qc6")
                u1_qc7 = st.text_input("Câu 7: ________ (I / not finish) the book yet so I can't tell you what happens.", key="u1_qc7")
                u1_qc8 = st.text_input("Câu 8: ________ (you / already / decide) where you're going this summer?", key="u1_qc8")
                u1_qc9 = st.text_input("Câu 9: ________ (We / live) here for the last six years.", key="u1_qc9")
                u1_qc10 = st.text_input("Câu 10: ________ (I / never / hear) such nonsense!", key="u1_qc10")

            # --- EXERCISE D ---
            with tab_d:
                st.markdown("#### Exercise D: Complete using the words in the box (already, before, ever, for, just, rarely, since, so, still, yet)")
                box_words = [None, "already", "before", "ever", "for", "just", "rarely", "since", "so", "still", "yet"]
                u1_qd1 = st.radio("Câu 1: Have you ________ dreamt of winning the lottery?", box_words, key="u1_qd1")
                u1_qd2 = st.radio("Câu 2: I haven't worked out how to set the timer on the video ________.", box_words, key="u1_qd2")
                u1_qd3 = st.radio("Câu 3: My dad's lived in the same house ________ he was born.", box_words, key="u1_qd3")
                u1_qd4 = st.radio("Câu 4: The film's only been on ________ a couple of minutes.", box_words, key="u1_qd4")
                u1_qd5 = st.radio("Câu 5: Bruce has knocked three men out of the competition ________ far.", box_words, key="u1_qd5")
                u1_qd6 = st.radio("Câu 6: I ________ get the chance to get any exercise - I'm just too busy.", box_words, key="u1_qd6")
                u1_qd7 = st.radio("Câu 7: He's only ________ got home.", box_words, key="u1_qd7")
                u1_qd8 = st.radio("Câu 8: It's eleven o'clock and Todd ________ hasn't come home. Where could he be?", box_words, key="u1_qd8")
                u1_qd9 = st.radio("Câu 9: I've never met Ruth ________. What's she like?", box_words, key="u1_qd9")
                u1_qd10 = st.radio("Câu 10: Have you finished ________? That was quick.", box_words, key="u1_qd10")

            # --- EXERCISE E ---
            with tab_e:
                st.markdown("#### Exercise E: Choose the correct answer")
                u1_qe1 = st.radio("Câu 1: Ian ________ a shower at the moment, so could you call back in about half an hour?", [None, "A. takes", "B. is taking", "C. has taken", "D. has been taking"], key="u1_qe1")
                u1_qe2 = st.radio("Câu 2: ________ to Ipswich before?", [None, "A. Do you ever go", "B. Are you ever going", "C. Have you ever been", "D. Have you ever been going"], key="u1_qe2")
                u1_qe3 = st.radio("Câu 3: I ________ to all the local newspapers and TV stations to complain.", [None, "A. already write", "B. already writing", "C. have already written", "D. have already been writing"], key="u1_qe3")
                u1_qe4 = st.radio("Câu 4: ________ TV for the last four hours? Turn it off and get some exercise!", [None, "A. Do you watch", "B. Are you watching", "C. Watched you", "D. Have you been watching"], key="u1_qe4")
                u1_qe5 = st.radio("Câu 5: Eric, ________ hockey competitively or just for fun?", [None, "A. do you usually play", "B. are you usually playing", "C. have you usually played", "D. have you usually been playing"], key="u1_qe5")
                u1_qe6 = st.radio("Câu 6: That's the first time ________ an answer right today!", [None, "A. I get", "B. I am getting", "C. I have got", "D. I have been getting"], key="u1_qe6")
                u1_qe7 = st.radio("Câu 7: Jessica has ________ left, I'm afraid.", [None, "A. already", "B. yet", "C. still", "D. so far"], key="u1_qe7")
                u1_qe8 = st.radio("Câu 8: Dan ________ in the living room while we redecorate his bedroom.", [None, "A. sleeps", "B. is sleeping", "C. has slept", "D. does slept"], key="u1_qe8")
                u1_qe9 = st.radio("Câu 9: Unfortunately, Simone ________ a day off very often.", [None, "A. doesn't get", "B. isn't getting", "C. hasn't got", "D. hasn't been getting"], key="u1_qe9")
                u1_qe10 = st.radio("Câu 10: Actually, I ________ a cup of tea first thing every morning but then I switch to coffee.", [None, "A. do drink", "B. am drinking", "C. have drunk", "D. have been drinking"], key="u1_qe10")

            # --- EXERCISE F ---
            with tab_f:
                st.markdown("#### Exercise F: Complete using the correct form of the words in the box (be, disagree, do, include, know, look, see, seem, understand)")
                u1_qf1 = st.text_input("Câu 1: Everyone (1) ________ that humans have been flying for only a few hundred years.", key="u1_qf1")
                u1_qf2 = st.text_input("Câu 2: But (2) ________ it possible that ancient civilizations also had the ability and technology to fly?", key="u1_qf2")
                u1_qf3 = st.text_input("Câu 3: On the ground, they just (3) ________ like straight lines.", key="u1_qf3")
                u1_qf4 = st.text_input("Câu 4: But when you (4) ________ them from the air...", key="u1_qf4")
                u1_qf5 = st.text_input("Câu 5: ...you (5) ________ exactly what they are.", key="u1_qf5")
                u1_qf6 = st.text_input("Câu 6: The pictures (6) ________ animals, birds and symbols.", key="u1_qf6")
                u1_qf7 = st.text_input("Câu 7: One bizarre theory, which most mainstream scientists (7) ________ with...", key="u1_qf7")
                u1_qf8 = st.text_input("Câu 8: It (8) ________ incredible...", key="u1_qf8")
                u1_qf9 = st.text_input("Câu 9: ...but a few people (9) ________ believe it's possible.", key="u1_qf9")

            # --- EXERCISE G ---
            with tab_g:
                st.markdown("#### Exercise G: Match to make sentences")
                match_opts = [None, "A. darker hair than her sister.", "B. I'm going to buy the new Racetrack CD.", "C. a haircut at the moment.", "D. for his glasses. Have you seen them?", "E. not old enough to drive a car.", "F. of getting Dad a CD for his birthday.", "G. very annoying at the moment!", "H. like he needs a holiday!"]
                u1_qg1 = st.radio("1. I think ________", match_opts, key="u1_qg1")
                u1_qg2 = st.radio("2. I'm thinking ________", match_opts, key="u1_qg2")
                u1_qg3 = st.radio("3. Phil's looking ________", match_opts, key="u1_qg3")
                u1_qg4 = st.radio("4. Phil looks ________", match_opts, key="u1_qg4")
                u1_qg5 = st.radio("5. Claire has ________", match_opts, key="u1_qg5")
                u1_qg6 = st.radio("6. Claire is having ________", match_opts, key="u1_qg6")
                u1_qg7 = st.radio("7. Andy is ________", match_opts, key="u1_qg7")
                u1_qg8 = st.radio("8. Andy is being ________", match_opts, key="u1_qg8")

            # --- EXERCISE H ---
            with tab_h:
                st.markdown("#### Exercise H: Find the extra word in each line")
                u1_qh1 = st.text_input("Dòng 1: I've been to travelling round Europe all summer.", key="u1_qh1")
                u1_qh2 = st.text_input("Dòng 2: It's the first time I've ever been going abroad...", key="u1_qh2")
                u1_qh3 = st.text_input("Dòng 3: ...and I have to also made loads of new friends.", key="u1_qh3")
                u1_qh4 = st.text_input("Dòng 4: I've been decided to stay in touch with them now I'm back.", key="u1_qh4")
                u1_qh5 = st.text_input("Dòng 5: One of them, Giselle, is French. She was making on holiday too.", key="u1_qh5")
                u1_qh6 = st.text_input("Dòng 6: We now send text messages and to each other all time.", key="u1_qh6")
                u1_qh7 = st.text_input("Dòng 7: ...because my French isn't very good! I'm planning to have visit her in France...", key="u1_qh7")
                u1_qh8 = st.text_input("Dòng 8: I hope I can. I am love meeting people from other countries...", key="u1_qh8")
                u1_qh9 = st.text_input("Dòng 9: I want to have had lots of friends from all over the world!", key="u1_qh9")
                u1_qh10 = st.text_input("Dòng 10: Travelling certainly broadens the mind but it also is broadens your circle of friends!", key="u1_qh10")

            # --- EXERCISE I ---
            with tab_i:
                st.markdown("#### Exercise I: Write one word in each gap (Holiday Blues)")
                u1_qi1 = st.text_input("Câu 1: You've (1) ________ looking at that timetable for the last ten minutes.", key="u1_qi1")
                u1_qi2 = st.text_input("Câu 2: 'I (2) ________ wish you'd be quiet!'", key="u1_qi2")
                u1_qi3 = st.text_input("Câu 3: 'I've (3) ________ a splitting headache thanks to you!'", key="u1_qi3")
                u1_qi4 = st.text_input("Câu 4: 'You're both (4) ________ very silly.'", key="u1_qi4")
                u1_qi5 = st.text_input("Câu 5: '(5) ________ is no point at all in blaming each other.'", key="u1_qi5")
                u1_qi6 = st.text_input("Câu 6: 'You (6) ________ quite right, darling.'", key="u1_qi6")
                u1_qi7 = st.text_input("Câu 7: 'I (7) ________ sorry,' said Sheila.", key="u1_qi7")
                u1_qi8 = st.text_input("Câu 8: 'Well, it (8) ________ like we've definitely missed the last train today.'", key="u1_qi8")
                u1_qi9 = st.text_input("Câu 9: 'I (9) ________ so,' said Sheila.", key="u1_qi9")
                u1_qi10 = st.text_input("Câu 10: 'Well, one thing is (10) ________ doubt,' said Matt.", key="u1_qi10")
                u1_qi12 = st.text_input("Câu 12: 'This is the worst holiday we've (12) ________ been on,' said Matt.", key="u1_qi12")

            # --- EXERCISE J ---
            with tab_j:
                st.markdown("#### Exercise J: Complete each second sentence using the word given (between 2 and 5 words)")
                u1_qj1 = st.text_input("Câu 1: What is the price of the tickets, Jimmy? (much) -> How ________, Jimmy?", key="u1_qj1")
                u1_qj2 = st.text_input("Câu 2: Are these your trainers? (to) -> Do ________ you?", key="u1_qj2")
                u1_qj3 = st.text_input("Câu 3: Sasha's not keen on team sports at all. (like) -> Sasha ________ team sports at all.", key="u1_qj3")
                u1_qj4 = st.text_input("Câu 4: It's only her second time in a recording studio. (been) -> She ________ in a recording studio once before.", key="u1_qj4")
                u1_qj5 = st.text_input("Câu 5: We got here three hours ago. (have) -> We ________ three hours.", key="u1_qj5")
                u1_qj6 = st.text_input("Câu 6: I started writing this hours ago and it's still not right. (writing) -> I ________ hours and it's still not right.", key="u1_qj6")
                u1_qj7 = st.text_input("Câu 7: This is my first experience of flying alone. (time) -> It is the first ________ alone.", key="u1_qj7")
                u1_qj8 = st.text_input("Câu 8: Sharon's in the bath at the moment. (a) -> Sharon ________ at the moment.", key="u1_qj8")
                u1_qj9 = st.text_input("Câu 9: Paul enjoys surprises apart from on his birthday. (does) -> Paul ________ surprises, just not on his birthday!", key="u1_qj9")

            submit_btn = st.form_submit_button("🚀 Kiểm tra Đáp án (Submit Answers)")

        # ANSWER CHECKING LOGIC FOR UNIT 1
        if submit_btn:
            st.markdown("### 📊 Kết quả Bài làm & Giải thích Chi tiết (Answer Key)")
            
            # EXERCISE A EVALUATION
            st.markdown("#### 📝 Kết quả Exercise A")
            exA_answers = [
                (u1_qa1, "usually goes", "Thói quen hằng ngày (Current habits), dùng Present Simple."),
                (u1_qa2, "is talking", "Hành động đang diễn ra tại thời điểm nói ('right now'), dùng Present Continuous."),
                (u1_qa3, "aren't eating", "Tình huống tạm thời ('at the moment'), dùng Present Continuous."),
                (u1_qa4, "Is air travel getting", "Sự thay đổi, phát triển dần theo thời gian ('increasingly safe'), dùng Present Continuous."),
                (u1_qa5, "calls", "Thói quen lặp đi lặp lại có chu kỳ ('every weekend'), dùng Present Simple."),
                (u1_qa6, "do babysitters generally earn", "Hỏi thực tế/sự thật chung ('generally'), dùng Present Simple."),
                (u1_qa7, "You're always coming", "Thói quen gây phiền phức/bực mình kết hợp với 'always', dùng Present Continuous."),
                (u1_qa8_1, "don't go", "Thói quen cố định ngày trong tuần, dùng Present Simple."),
                (u1_qa8_2, "always try", "Thói quen cố định ngày cuối tuần, dùng Present Simple."),
                (u1_qa9, "does stop", "Emphatic Present Simple: dùng 'does' + V-bare để nhấn mạnh sự thật phản bác ý kiến trước đó."),
                (u1_qa10, "takes", "Thói quen/hoạt động lặp lại thường xuyên ('almost every weekend'), dùng Present Simple.")
            ]
            for idx, (ans, correct, exp) in enumerate(exA_answers, 1):
                label = f"Câu {idx}"
                if ans == correct:
                    st.success(f"✅ **{label}: Chính xác!** (`{correct}`)")
                elif ans is None or ans == "":
                    st.warning(f"⚠️ **{label}: Chưa trả lời / Bỏ trống.** Đáp án đúng là: **{correct}**")
                    st.markdown(f"<div class='explain-box'>💡 <i>Giải thích:</i> {exp}</div>", unsafe_allow_html=True)
                else:
                    st.error(f"❌ **{label}: Chưa chính xác.** (Bạn chọn: `{ans}`) ➔ Đáp án đúng: **{correct}**")
                    st.markdown(f"<div class='explain-box'>💡 <i>Giải thích:</i> {exp}</div>", unsafe_allow_html=True)

            # EXERCISE E EVALUATION
            st.markdown("#### 📝 Kết quả Exercise E (Multiple Choice Questions)")
            exE_answers = [
                (u1_qe1, "B. is taking", "Hành động đang diễn ra lúc nói ('at the moment'), chọn Present Continuous."),
                (u1_qe2, "C. Have you ever been", "Hỏi về trải nghiệm tính đến thời điểm hiện tại ('before'), chọn Present Perfect Simple."),
                (u1_qe3, "C. have already written", "Hành động đã hoàn thành tính đến nay có kết quả cụ thể, chọn Present Perfect Simple."),
                (u1_qe4, "D. Have you been watching", "Nhấn mạnh tính liên tục của hành động xem TV kéo dài suốt 4 tiếng ('for the last four hours')."),
                (u1_qe5, "A. do you usually play", "Hỏi về thói quen/tần suất thường xuyên ('usually'), chọn Present Simple."),
                (u1_qe6, "C. I have got", "Cấu trúc 'That's the first time + Present Perfect Simple'."),
                (u1_qe7, "A. already", "Trạng từ 'already' đứng giữa have/has và V3/ed trong câu khẳng định."),
                (u1_qe8, "B. is sleeping", "Tình huống tạm thời đang diễn ra ('while we redecorate...')."),
                (u1_qe9, "A. doesn't get", "Thói quen/tần suất ('very often'), chọn Present Simple."),
                (u1_qe10, "A. do drink", "Emphatic Present Simple: dùng 'do drink' để nhấn mạnh sự tương phản với việc chuyển sang uống cà phê.")
            ]
            for idx, (ans, correct, exp) in enumerate(exE_answers, 1):
                label = f"Câu {idx}"
                if ans == correct:
                    st.success(f"✅ **{label}: Chính xác!** (`{correct}`)")
                elif ans is None or ans == "":
                    st.warning(f"⚠️ **{label}: Chưa trả lời / Bỏ trống.** Đáp án đúng là: **{correct}**")
                    st.markdown(f"<div class='explain-box'>💡 <i>Giải thích:</i> {exp}</div>", unsafe_allow_html=True)
                else:
                    st.error(f"❌ **{label}: Chưa chính xác.** (Bạn chọn: `{ans}`) ➔ Đáp án đúng: **{correct}**")
                    st.markdown(f"<div class='explain-box'>💡 <i>Giải thích:</i> {exp}</div>", unsafe_allow_html=True)

            # EXERCISE J EVALUATION
            st.markdown("#### 📝 Kết quả Exercise J (Key Word Transformation)")
            exJ_answers = [
                (u1_qj1, ["much do the tickets cost", "much are the tickets"], "How much do the tickets cost / How much are the tickets, Jimmy?"),
                (u1_qj2, ["these trainers belong to"], "Do these trainers belong to you?"),
                (u1_qj3, ["does not like", "doesn't like"], "Sasha does not like / doesn't like team sports at all."),
                (u1_qj4, ["has only been"], "She has only been in a recording studio once before."),
                (u1_qj5, ["have been here for", "have been here (for)"], "We have been here for three hours."),
                (u1_qj6, ["have been writing this for"], "I have been writing this for hours and it's still not right."),
                (u1_qj7, ["time I have flown"], "It is the first time I have flown alone."),
                (u1_qj8, ["is having a bath"], "Sharon is having a bath at the moment."),
                (u1_qj9, ["does enjoy"], "Paul does enjoy surprises, just not on his birthday!")
            ]
            for idx, (ans, corrects, full_sent) in enumerate(exJ_answers, 1):
                label = f"Câu {idx}"
                user_str = ans.strip().lower() if ans else ""
                is_correct = any(c.lower() in user_str for c in corrects)
                if is_correct:
                    st.success(f"✅ **{label}: Chính xác!** (Câu hoàn chỉnh: *{full_sent}*)")
                elif ans is None or user_str == "":
                    st.warning(f"⚠️ **{label}: Chưa trả lời / Bỏ trống.** Đáp án gợi ý: **{corrects[0]}**")
                    st.markdown(f"<div class='explain-box'>💡 <i>Câu hoàn chỉnh chuẩn sách:</i> {full_sent}</div>", unsafe_allow_html=True)
                else:
                    st.error(f"❌ **{label}: Chưa chính xác.** (Bạn nhập: `{ans}`) ➔ Đáp án đúng: **{corrects[0]}**")
                    st.markdown(f"<div class='explain-box'>💡 <i>Câu hoàn chỉnh chuẩn sách:</i> {full_sent}</div>", unsafe_allow_html=True)

    else:
        st.info(f"Bài tập tương tác cho **{selected_quiz_unit}** đang được xây dựng theo chuẩn dữ liệu Destination B2.")

# --- 4. THẺ GHI NHỚ TỪ VỰNG (FLASHCARDS) ---
elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng (Flashcards)")
    st.info("Flashcards từ vựng các Unit Từ vựng (Unit 2, Unit 4, Unit 6...) sẽ hiển thị ở đây.")

# --- 5. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập (Progress Report)")
    completed = st.multiselect("Đánh dấu các Unit bạn đã hoàn thành:", ALL_UNITS_LIST)
    pct = int((len(completed) / len(ALL_UNITS_LIST)) * 100)
    st.progress(pct / 100)
    st.success(f"🎉 Bạn đã hoàn thành {len(completed)} / {len(ALL_UNITS_LIST)} bài ({pct}%)")

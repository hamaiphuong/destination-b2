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
        st.caption("Tra cứu chi tiết Từ vựng, Phrasal Verbs, Phrases & Collocations, Word Patterns và Word Formation.")
        
        tab_v1, tab_v2, tab_v3, tab_v4 = st.tabs([
            "📚 Topic Vocabulary & Phrasal Verbs",
            "💡 Phrases & Collocations (Tách cụm chi tiết)",
            "🧩 Word Patterns (Tách cấu trúc chi tiết)",
            "🔤 Word Formation (Tách từ loại chi tiết)"
        ])
        
        with tab_v1:
            st.markdown("#### 🔹 Topic Vocabulary in Contrast")
            vocab_b2_list = [
                {"Từ vựng": "voyage (n)", "IPA": "/ˈvɔɪ.ɪdʒ/", "Định nghĩa Tiếng Anh": "a long journey, especially on a ship", "Nghĩa Tiếng Việt": "chuyến đi dài bằng đường biển", "Ví dụ": "It was a long voyage from London to New York."},
                {"Từ vựng": "journey (n)", "IPA": "/ˈdʒɜː.ni/", "Định nghĩa Tiếng Anh": "an occasion when you travel from one place to another", "Nghĩa Tiếng Việt": "chuyến đi, hành trình", "Ví dụ": "We had a long journey ahead of us."},
                {"Từ vựng": "trip (n)", "IPA": "/trɪp/", "Định nghĩa Tiếng Anh": "an occasion when you go somewhere and come back again", "Nghĩa Tiếng Việt": "chuyến đi ngắn (đi rồi về)", "Ví dụ": "The whole family went on a trip to Florida."},
                {"Từ vựng": "travel (n/v)", "IPA": "/ˈtræv.əl/", "Định nghĩa Tiếng Anh": "the activity of travelling / to make a journey", "Nghĩa Tiếng Việt": "việc đi lại, du lịch / đi du lịch", "Ví dụ": "Foreign travel never really appealed to him until he retired."},
                {"Từ vựng": "excursion (n)", "IPA": "/ɪkˈskɜː.ʃən/", "Định nghĩa Tiếng Anh": "a short journey that you make for pleasure", "Nghĩa Tiếng Việt": "chuyến tham quan, dã ngoại", "Ví dụ": "My grandmother often talks about excursions to the sea."},
                {"Từ vựng": "view (n)", "IPA": "/vjuː/", "Định nghĩa Tiếng Anh": "the things that you can see from a particular place", "Nghĩa Tiếng Việt": "quang cảnh, tầm nhìn", "Ví dụ": "We had a spectacular view of the mountains from our room."},
                {"Từ vựng": "sight (n)", "IPA": "/saɪt/", "Định nghĩa Tiếng Anh": "a person or a thing that you see that has a particular feature", "Nghĩa Tiếng Việt": "cảnh tượng, danh thắng", "Ví dụ": "Windmills are a common sight in Holland."},
                {"Từ vựng": "world (n)", "IPA": "/wɜːld/", "Định nghĩa Tiếng Anh": "the planet that we live on", "Nghĩa Tiếng Việt": "thế giới, Trái Đất", "Ví dụ": "It's easy these days to communicate with people all over the world."},
                {"Từ vựng": "earth (n)", "IPA": "/ɜːθ/", "Định nghĩa Tiếng Anh": "the land on which we live", "Nghĩa Tiếng Việt": "mặt đất, đất liền", "Ví dụ": "They felt the earth shake."},
                {"Từ vựng": "area (n)", "IPA": "/ˈeə.ri.ə/", "Định nghĩa Tiếng Anh": "a part of a place or building", "Nghĩa Tiếng Việt": "vùng, khu vực", "Ví dụ": "Bus services in rural areas are not very good."},
                {"Từ vựng": "territory (n)", "IPA": "/ˈter.ɪ.tər.i/", "Định nghĩa Tiếng Anh": "an area of land controlled by a country or leader", "Nghĩa Tiếng Việt": "lãnh thổ", "Ví dụ": "Russian troops crossed into Austrian territory."},
                {"Từ vựng": "season (n)", "IPA": "/ˈsiː.zən/", "Định nghĩa Tiếng Anh": "one of the four periods into which the year is divided", "Nghĩa Tiếng Việt": "mùa trong năm / mùa du lịch", "Ví dụ": "It can be quite busy here during the tourist season."},
                {"Từ vựng": "period (n)", "IPA": "/ˈpɪə.ri.əd/", "Định nghĩa Tiếng Anh": "an amount of time", "Nghĩa Tiếng Việt": "giai đoạn, khoảng thời gian", "Ví dụ": "The long dry period ended with heavy rain."},
                {"Từ vựng": "fare (n)", "IPA": "/feər/", "Định nghĩa Tiếng Anh": "the money that you pay for a journey on a vehicle", "Nghĩa Tiếng Việt": "tiền xe, vé tàu xe", "Ví dụ": "The fare from York to Leeds has gone up."},
                {"Từ vựng": "ticket (n)", "IPA": "/ˈtɪk.ɪt/", "Định nghĩa Tiếng Anh": "a piece of paper that shows you have paid for a travel or event", "Nghĩa Tiếng Việt": "vé (máy bay, xem phim...)", "Ví dụ": "We'll send your tickets a week before your flight."},
                {"Từ vựng": "fee (n)", "IPA": "/fiː/", "Định nghĩa Tiếng Anh": "an amount of money that you pay to be allowed to do something", "Nghĩa Tiếng Việt": "lệ phí, phí dịch vụ", "Ví dụ": "The gallery charges a small entrance fee."},
                {"Từ vựng": "miss (v)", "IPA": "/mɪs/", "Định nghĩa Tiếng Anh": "to be too late for something like a train or bus", "Nghĩa Tiếng Việt": "lỡ, nhỡ (tàu, xe)", "Ví dụ": "I missed the last train home again."},
                {"Từ vựng": "lose (v)", "IPA": "/luːz/", "Định nghĩa Tiếng Anh": "to no longer have something", "Nghĩa Tiếng Việt": "làm mất, thất lạc", "Ví dụ": "Mike lost his job last year."},
                {"Từ vựng": "take (v)", "IPA": "/teɪk/", "Định nghĩa Tiếng Anh": "to move or carry someone/something to another place", "Nghĩa Tiếng Việt": "đưa đi, dẫn đi", "Ví dụ": "What time do you take Amy to school?"},
                {"Từ vựng": "bring (v)", "IPA": "/brɪŋ/", "Định nghĩa Tiếng Anh": "to take someone or something with you from one place to another", "Nghĩa Tiếng Việt": "mang theo, đem lại", "Ví dụ": "Bring a coat in case it turns cold."},
                {"Từ vựng": "go (v)", "IPA": "/ɡəʊ/", "Định nghĩa Tiếng Anh": "to move or travel to a place that is away", "Nghĩa Tiếng Việt": "đi", "Ví dụ": "We're planning to go to Spain this winter."},
                {"Từ vựng": "book (v)", "IPA": "/bʊk/", "Định nghĩa Tiếng Anh": "to arrange to have or use something at a particular time", "Nghĩa Tiếng Việt": "đặt chỗ trước", "Ví dụ": "Shall I book a room for you?"},
                {"Từ vựng": "keep (v)", "IPA": "/kiːp/", "Định nghĩa Tiếng Anh": "to continue to have or own something", "Nghĩa Tiếng Việt": "giữ, cất giữ", "Ví dụ": "We should keep this car and sell the other one."},
                {"Từ vựng": "arrive (v)", "IPA": "/əˈraɪv/", "Định nghĩa Tiếng Anh": "to reach a place", "Nghĩa Tiếng Việt": "đến (nơi)", "Ví dụ": "What time does your plane arrive?"},
                {"Từ vựng": "reach (v)", "IPA": "/riːtʃ/", "Định nghĩa Tiếng Anh": "to arrive somewhere", "Nghĩa Tiếng Việt": "đến được, đạt tới", "Ví dụ": "We hoped to reach the camp before dark."},
                {"Từ vựng": "live (v)", "IPA": "/lɪv/", "Định nghĩa Tiếng Anh": "to have your home in a particular place", "Nghĩa Tiếng Việt": "sống, cư trú lâu dài", "Ví dụ": "Paris is a nice place to live."},
                {"Từ vựng": "stay (v)", "IPA": "/steɪ/", "Định nghĩa Tiếng Anh": "to live or remain in a place for a while as a guest", "Nghĩa Tiếng Việt": "ở lại, lưu trú tạm thời", "Ví dụ": "How long is he planning to stay with you?"},
                {"Từ vựng": "border (n)", "IPA": "/ˈbɔː.dər/", "Định nghĩa Tiếng Anh": "the official line that separates two countries or regions", "Nghĩa Tiếng Việt": "biên giới", "Ví dụ": "Thousands of refugees were fleeing across the border."},
                {"Từ vựng": "edge (n)", "IPA": "/edʒ/", "Định nghĩa Tiếng Anh": "the part of something that is furthest from its centre", "Nghĩa Tiếng Việt": "mép, rìa", "Ví dụ": "Victoria was sitting on the edge of the bed."},
                {"Từ vựng": "line (n)", "IPA": "/laɪn/", "Định nghĩa Tiếng Anh": "a long thin mark on the surface of something", "Nghĩa Tiếng Việt": "đường ranh giới, vạch kẻ", "Ví dụ": "Draw a straight line."},
                {"Từ vựng": "length (n)", "IPA": "/leŋkθ/", "Định nghĩa Tiếng Anh": "a measurement of how long something is in size", "Nghĩa Tiếng Việt": "chiều dài, độ dài", "Ví dụ": "The boat was 16 feet in length."},
                {"Từ vựng": "distance (n)", "IPA": "/ˈdɪs.təns/", "Định nghĩa Tiếng Anh": "the amount of space between two people or things", "Nghĩa Tiếng Việt": "khoảng cách", "Ví dụ": "They started to walk the short distance to the camp."},
                {"Từ vựng": "guide (v)", "IPA": "/ɡaɪd/", "Định nghĩa Tiếng Anh": "to show someone where to go by going with them", "Nghĩa Tiếng Việt": "hướng dẫn, dẫn đường", "Ví dụ": "He guided them through the forest."},
                {"Từ vựng": "lead (v)", "IPA": "/liːd/", "Định nghĩa Tiếng Anh": "to take someone to a place by going with them, usually in front", "Nghĩa Tiếng Việt": "dẫn dắt, đi đầu", "Ví dụ": "The estate agent led us into the kitchen."},
                {"Từ vựng": "native (adj)", "IPA": "/ˈneɪ.tɪv/", "Định nghĩa Tiếng Anh": "living in a particular country or area since birth", "Nghĩa Tiếng Việt": "bản xứ, quê hương", "Ví dụ": "My wife is a native New Yorker."},
                {"Từ vựng": "home (town) (n)", "IPA": "/həʊm/", "Định nghĩa Tiếng Anh": "the city or town where you lived as a child", "Nghĩa Tiếng Việt": "quê nhà, nơi sinh sống", "Ví dụ": "My home town is Denver, Colorado."}
            ]
            st.table(pd.DataFrame(vocab_b2_list))
            
            st.markdown("#### 🔹 Phrasal Verbs")
            phrasal_b2_list = [
                {"Phrasal Verb": "catch up with", "IPA": "/kætʃ ʌp wɪð/", "Định nghĩa Tiếng Anh": "reach the same point/level as someone", "Nghĩa Tiếng Việt": "theo kịp, đuổi kịp", "Ví dụ": "Run fast to catch up with the group."},
                {"Phrasal Verb": "check in", "IPA": "/tʃek ɪn/", "Định nghĩa Tiếng Anh": "register at a hotel or an airport", "Nghĩa Tiếng Việt": "làm thủ tục nhận phòng / lên máy bay", "Ví dụ": "Give me your passport and I'll go to the desk to check in."},
                {"Phrasal Verb": "check out", "IPA": "/tʃek aʊt/", "Định nghĩa Tiếng Anh": "leave a hotel; investigate", "Nghĩa Tiếng Việt": "làm thủ tục trả phòng; điều tra", "Ví dụ": "All guests must check out by midday."},
                {"Phrasal Verb": "drop off", "IPA": "/drɒp ɒf/", "Định nghĩa Tiếng Anh": "let someone get out of a vehicle; fall asleep", "Nghĩa Tiếng Việt": "cho ai xuống xe; ngủ gật", "Ví dụ": "I can drop you off at the station."},
                {"Phrasal Verb": "get back", "IPA": "/ɡet bæk/", "Định nghĩa Tiếng Anh": "return from a place", "Nghĩa Tiếng Việt": "trở về từ một nơi", "Ví dụ": "When do you get back from London?"},
                {"Phrasal Verb": "go away", "IPA": "/ɡəʊ əˈweɪ/", "Định nghĩa Tiếng Anh": "go on holiday", "Nghĩa Tiếng Việt": "đi nghỉ mát, đi xa", "Ví dụ": "We're going away for the weekend."},
                {"Phrasal Verb": "keep up with", "IPA": "/kiːp ʌp wɪð/", "Định nghĩa Tiếng Anh": "stay at the same point/level as someone", "Nghĩa Tiếng Việt": "giữ cùng tốc độ / trình độ với ai", "Ví dụ": "He walked so fast that I couldn't keep up with him."},
                {"Phrasal Verb": "make for", "IPA": "/meɪk fɔːr/", "Định nghĩa Tiếng Anh": "go in the direction of a place", "Nghĩa Tiếng Việt": "đi về phía, hướng về", "Ví dụ": "If it starts to rain, make for a nearby shelter."},
                {"Phrasal Verb": "pick up", "IPA": "/pɪk ʌp/", "Định nghĩa Tiếng Anh": "stop in a vehicle to give someone a lift", "Nghĩa Tiếng Việt": "đón ai bằng xe", "Ví dụ": "My dad picks us up outside the cinema."},
                {"Phrasal Verb": "pull in", "IPA": "/pʊl ɪn/", "Định nghĩa Tiếng Anh": "stop by the side of the road in a car", "Nghĩa Tiếng Việt": "tấp xe vào lề đường", "Ví dụ": "Please pull in and stop so I can buy some water."},
                {"Phrasal Verb": "run over", "IPA": "/rʌn ˈəʊ.vər/", "Định nghĩa Tiếng Anh": "hit with a car", "Nghĩa Tiếng Việt": "cán qua, đâm phải (bằng xe)", "Ví dụ": "Stop the car! I think we've run over something."},
                {"Phrasal Verb": "see off", "IPA": "/siː ɒf/", "Định nghĩa Tiếng Anh": "go to a station/airport to see someone leave", "Nghĩa Tiếng Việt": "tiễn ai lên đường", "Ví dụ": "We went to the airport to see Grandpa off."},
                {"Phrasal Verb": "set out/off", "IPA": "/set aʊt / ɒf/", "Định nghĩa Tiếng Anh": "start a journey", "Nghĩa Tiếng Việt": "khởi hành một chuyến đi", "Ví dụ": "We set out early in the morning."},
                {"Phrasal Verb": "take off", "IPA": "/teɪk ɒf/", "Định nghĩa Tiếng Anh": "leave the ground (plane)", "Nghĩa Tiếng Việt": "cất cánh (máy bay)", "Ví dụ": "The plane took off on time."},
                {"Phrasal Verb": "turn round", "IPA": "/tɜːn raʊnd/", "Định nghĩa Tiếng Anh": "go back in the opposite direction", "Nghĩa Tiếng Việt": "quay ngược lại", "Ví dụ": "We got lost and had to turn round."}
            ]
            st.table(pd.DataFrame(phrasal_b2_list))

        with tab_v2:
            st.markdown("#### 🔹 Phrases and Collocations (Tách cụm chi tiết)")
            colloc_b2_data = [
                {"Từ khóa (Keyword)": "accident", "Cụm từ / Collocation": "have an accident", "Nghĩa Tiếng Việt": "gặp tai nạn"},
                {"Từ khóa (Keyword)": "accident", "Cụm từ / Collocation": "be (involved) in an accident", "Nghĩa Tiếng Việt": "dính vào / liên quan tới vụ tai nạn"},
                {"Từ khóa (Keyword)": "accident", "Cụm từ / Collocation": "do sth by accident", "Nghĩa Tiếng Việt": "vô tình / tình cờ làm gì"},
                {"Từ khóa (Keyword)": "advance", "Cụm từ / Collocation": "in advance", "Nghĩa Tiếng Việt": "trước (đặt trước, trả trước)"},
                {"Từ khóa (Keyword)": "advance", "Cụm từ / Collocation": "advance to/towards a place", "Nghĩa Tiếng Việt": "tiến về phía / tiến tới một nơi"},
                {"Từ khóa (Keyword)": "ahead", "Cụm từ / Collocation": "go straight ahead", "Nghĩa Tiếng Việt": "đi thẳng về phía trước"},
                {"Từ khóa (Keyword)": "ahead", "Cụm từ / Collocation": "go ahead", "Nghĩa Tiếng Việt": "tiếp tục / tiến lên"},
                {"Từ khóa (Keyword)": "ahead", "Cụm từ / Collocation": "be ahead of sth/sb", "Nghĩa Tiếng Việt": "dẫn trước / đi trước cái gì hay ai"},
                {"Từ khóa (Keyword)": "direction", "Cụm từ / Collocation": "a change of direction", "Nghĩa Tiếng Việt": "sự đổi hướng"},
                {"Từ khóa (Keyword)": "direction", "Cụm từ / Collocation": "in the direction of sth", "Nghĩa Tiếng Việt": "theo hướng của cái gì"},
                {"Từ khóa (Keyword)": "direction", "Cụm từ / Collocation": "in this/that direction", "Nghĩa Tiếng Việt": "theo hướng này / hướng đó"},
                {"Từ khóa (Keyword)": "head", "Cụm từ / Collocation": "off the top of your head", "Nghĩa Tiếng Việt": "theo trí nhớ (không cần suy nghĩ kỹ)"},
                {"Từ khóa (Keyword)": "head", "Cụm từ / Collocation": "head for/towards a place", "Nghĩa Tiếng Việt": "đi về phía / hướng về một nơi"},
                {"Từ khóa (Keyword)": "head", "Cụm từ / Collocation": "head over heels (in love)", "Nghĩa Tiếng Việt": "yêu say đắm / si mê"},
                {"Từ khóa (Keyword)": "holiday", "Cụm từ / Collocation": "go/be on holiday", "Nghĩa Tiếng Việt": "đi / đang đi nghỉ mát"},
                {"Từ khóa (Keyword)": "holiday", "Cụm từ / Collocation": "have/take a holiday", "Nghĩa Tiếng Việt": "nghỉ phép / thực hiện chuyến nghỉ"},
                {"Từ khóa (Keyword)": "holiday", "Cụm từ / Collocation": "bank holiday", "Nghĩa Tiếng Việt": "ngày nghỉ lễ quốc gia (ngân hàng đóng cửa)"},
                {"Từ khóa (Keyword)": "left", "Cụm từ / Collocation": "go/turn left", "Nghĩa Tiếng Việt": "rẽ trái"},
                {"Từ khóa (Keyword)": "left", "Cụm từ / Collocation": "on the left", "Nghĩa Tiếng Việt": "ở bên trái"},
                {"Từ khóa (Keyword)": "left", "Cụm từ / Collocation": "on the left-hand side", "Nghĩa Tiếng Việt": "ở phía bên tay trái"},
                {"Từ khóa (Keyword)": "left", "Cụm từ / Collocation": "in the left-hand corner", "Nghĩa Tiếng Việt": "ở góc bên trái"},
                {"Từ khóa (Keyword)": "left", "Cụm từ / Collocation": "left-handed", "Nghĩa Tiếng Việt": "thuận tay trái"},
                {"Từ khóa (Keyword)": "route", "Cụm từ / Collocation": "plan your/a route", "Nghĩa Tiếng Việt": "lên kế hoạch tuyến đường đi"},
                {"Từ khóa (Keyword)": "route", "Cụm từ / Collocation": "take a route", "Nghĩa Tiếng Việt": "đi theo một tuyến đường"},
                {"Từ khóa (Keyword)": "sights", "Cụm từ / Collocation": "see the sights", "Nghĩa Tiếng Việt": "ngắm cảnh / đi tham quan các danh thắng"},
                {"Từ khóa (Keyword)": "sightseeing", "Cụm từ / Collocation": "go sightseeing", "Nghĩa Tiếng Việt": "đi tham quan ngắm cảnh"},
                {"Từ khóa (Keyword)": "speed", "Cụm từ / Collocation": "at (high/full/etc) speed", "Nghĩa Tiếng Việt": "ở tốc độ (cao / tối đa...)"},
                {"Từ khóa (Keyword)": "speed", "Cụm từ / Collocation": "a burst of speed", "Nghĩa Tiếng Việt": "sự tăng tốc đột ngột"},
                {"Từ khóa (Keyword)": "speed", "Cụm từ / Collocation": "speed limit", "Nghĩa Tiếng Việt": "tốc độ tối đa cho phép"},
                {"Từ khóa (Keyword)": "tour", "Cụm từ / Collocation": "go on/take a tour of/round somewhere", "Nghĩa Tiếng Việt": "đi tham quan một vòng nơi nào"},
                {"Từ khóa (Keyword)": "tour", "Cụm từ / Collocation": "tour a place", "Nghĩa Tiếng Việt": "đi du lịch / tham quan một nơi"},
                {"Từ khóa (Keyword)": "tour", "Cụm từ / Collocation": "tour guide", "Nghĩa Tiếng Việt": "hướng dẫn viên du lịch"},
                {"Từ khóa (Keyword)": "trip", "Cụm từ / Collocation": "business trip", "Nghĩa Tiếng Việt": "chuyến đi công tác"},
                {"Từ khóa (Keyword)": "trip", "Cụm từ / Collocation": "school trip", "Nghĩa Tiếng Việt": "chuyến dã ngoại của trường"},
                {"Từ khóa (Keyword)": "trip", "Cụm từ / Collocation": "go on a trip", "Nghĩa Tiếng Việt": "đi một chuyến đi"},
                {"Từ khóa (Keyword)": "trip", "Cụm từ / Collocation": "take a trip (to a place)", "Nghĩa Tiếng Việt": "thực hiện chuyến đi (đến đâu)"},
                {"Từ khóa (Keyword)": "way", "Cụm từ / Collocation": "lose/make/find your way", "Nghĩa Tiếng Việt": "lạc đường / tiến tới / tìm đường đi"},
                {"Từ khóa (Keyword)": "way", "Cụm từ / Collocation": "in a way", "Nghĩa Tiếng Việt": "theo một cách nào đó / ở khía cạnh nào đó"},
                {"Từ khóa (Keyword)": "way", "Cụm từ / Collocation": "on the way", "Nghĩa Tiếng Việt": "trên đường đi"},
                {"Từ khóa (Keyword)": "way", "Cụm từ / Collocation": "go all the way (to sth/swh)", "Nghĩa Tiếng Việt": "đi suốt chặng đường (đến đâu)"}
            ]
            st.table(pd.DataFrame(colloc_b2_data))

        with tab_v3:
            st.markdown("#### 🔹 Word Patterns (Tách cấu trúc chi tiết)")
            patterns_b2_data = [
                {"Từ gốc (Word)": "afraid", "Cấu trúc (Pattern)": "afraid of sth/sb/doing", "Nghĩa Tiếng Việt": "sợ / e ngại cái gì / ai / làm gì"},
                {"Từ gốc (Word)": "afraid", "Cấu trúc (Pattern)": "afraid to do", "Nghĩa Tiếng Việt": "sợ không dám làm gì"},
                {"Từ gốc (Word)": "appear", "Cấu trúc (Pattern)": "appear to be", "Nghĩa Tiếng Việt": "dường như / có vẻ như là"},
                {"Từ gốc (Word)": "arrange", "Cấu trúc (Pattern)": "arrange sth (with sb)", "Nghĩa Tiếng Việt": "sắp xếp cái gì (với ai)"},
                {"Từ gốc (Word)": "arrange", "Cấu trúc (Pattern)": "arrange for sb to do", "Nghĩa Tiếng Việt": "sắp xếp cho ai làm gì"},
                {"Từ gốc (Word)": "arrive", "Cấu trúc (Pattern)": "arrive in/at a place", "Nghĩa Tiếng Việt": "đến (một nơi / thành phố / địa điểm)"},
                {"Từ gốc (Word)": "arrive", "Cấu trúc (Pattern)": "arrive here/there", "Nghĩa Tiếng Việt": "đến đây / đến đó"},
                {"Từ gốc (Word)": "continue", "Cấu trúc (Pattern)": "continue sth/doing", "Nghĩa Tiếng Việt": "tiếp tục cái gì / tiếp tục làm gì"},
                {"Từ gốc (Word)": "continue", "Cấu trúc (Pattern)": "continue to do", "Nghĩa Tiếng Việt": "tiếp tục làm gì"},
                {"Từ gốc (Word)": "continue", "Cấu trúc (Pattern)": "continue with sth", "Nghĩa Tiếng Việt": "tiếp tục với cái gì"},
                {"Từ gốc (Word)": "differ", "Cấu trúc (Pattern)": "differ from sth/sb", "Nghĩa Tiếng Việt": "khác biệt so với cái gì / ai"},
                {"Từ gốc (Word)": "dream", "Cấu trúc (Pattern)": "dream about/of sth/sb/doing", "Nghĩa Tiếng Việt": "mơ về cái gì / ai / làm gì"},
                {"Từ gốc (Word)": "invite", "Cấu trúc (Pattern)": "invite sb to do", "Nghĩa Tiếng Việt": "mời ai làm gì"},
                {"Từ gốc (Word)": "keen", "Cấu trúc (Pattern)": "keen to do", "Nghĩa Tiếng Việt": "muốn / thích làm gì"},
                {"Từ gốc (Word)": "keen", "Cấu trúc (Pattern)": "keen on sth/sb/doing", "Nghĩa Tiếng Việt": "ham thích / đam mê cái gì / ai / làm gì"},
                {"Từ gốc (Word)": "live", "Cấu trúc (Pattern)": "live in/at a place", "Nghĩa Tiếng Việt": "sống ở đâu"},
                {"Từ gốc (Word)": "live", "Cấu trúc (Pattern)": "live on/for sth", "Nghĩa Tiếng Việt": "sống dựa vào / sống vì cái gì"},
                {"Từ gốc (Word)": "live", "Cấu trúc (Pattern)": "live here/there", "Nghĩa Tiếng Việt": "sống ở đây / ở đó"},
                {"Từ gốc (Word)": "regret", "Cấu trúc (Pattern)": "regret (not) doing", "Nghĩa Tiếng Việt": "hối hận vì đã (không) làm gì"},
                {"Từ gốc (Word)": "regret", "Cấu trúc (Pattern)": "regret sth", "Nghĩa Tiếng Việt": "hối tiếc điều gì"},
                {"Từ gốc (Word)": "regret", "Cấu trúc (Pattern)": "regret to tell/inform you", "Nghĩa Tiếng Việt": "lấy làm tiếc phải thông báo với bạn"},
                {"Từ gốc (Word)": "think", "Cấu trúc (Pattern)": "think of/about sth/sb/doing", "Nghĩa Tiếng Việt": "nghĩ về / cân nhắc cái gì / ai / làm gì"},
                {"Từ gốc (Word)": "write", "Cấu trúc (Pattern)": "write about sth/sb/doing", "Nghĩa Tiếng Việt": "viết về cái gì / ai / làm gì"},
                {"Từ gốc (Word)": "write", "Cấu trúc (Pattern)": "write (sth) (to sb)", "Nghĩa Tiếng Việt": "viết (cái gì) (cho ai)"},
                {"Từ gốc (Word)": "write", "Cấu trúc (Pattern)": "write sb sth", "Nghĩa Tiếng Việt": "viết cho ai cái gì"},
                {"Từ gốc (Word)": "write", "Cấu trúc (Pattern)": "write sth down", "Nghĩa Tiếng Việt": "ghi chép cái gì lại"}
            ]
            st.table(pd.DataFrame(patterns_b2_data))

        with tab_v4:
            st.markdown("#### 🔹 Word Formation (Tách từ loại chi tiết)")
            formation_b2_data = [
                {"Từ gốc (Base Word)": "arrange (v)", "Từ biến đổi (Derivative)": "rearrange", "Từ loại (POS)": "Verb", "Nghĩa Tiếng Việt": "sắp xếp lại"},
                {"Từ gốc (Base Word)": "arrange (v)", "Từ biến đổi (Derivative)": "arrangement", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "sự sắp xếp, sự thỏa thuận"},
                {"Từ gốc (Base Word)": "arrive (v)", "Từ biến đổi (Derivative)": "arrival", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "sự đến, sự tới nơi"},
                {"Từ gốc (Base Word)": "broad (adj)", "Từ biến đổi (Derivative)": "breadth", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "chiều rộng, bề rộng"},
                {"Từ gốc (Base Word)": "broad (adj)", "Từ biến đổi (Derivative)": "broaden", "Từ loại (POS)": "Verb", "Nghĩa Tiếng Việt": "mở rộng"},
                {"Từ gốc (Base Word)": "culture (n)", "Từ biến đổi (Derivative)": "cultural(ly)", "Từ loại (POS)": "Adj / Adv", "Nghĩa Tiếng Việt": "(thuộc) văn hóa / về mặt văn hóa"},
                {"Từ gốc (Base Word)": "culture (n)", "Từ biến đổi (Derivative)": "(un)cultured", "Từ loại (POS)": "Adjective", "Nghĩa Tiếng Việt": "có / không có văn hóa, học thức"},
                {"Từ gốc (Base Word)": "differ (v)", "Từ biến đổi (Derivative)": "different(ly)", "Từ loại (POS)": "Adj / Adv", "Nghĩa Tiếng Việt": "khác biệt / một cách khác biệt"},
                {"Từ gốc (Base Word)": "differ (v)", "Từ biến đổi (Derivative)": "difference", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "sự khác biệt"},
                {"Từ gốc (Base Word)": "direct (adj/v)", "Từ biến đổi (Derivative)": "indirect", "Từ loại (POS)": "Adjective", "Nghĩa Tiếng Việt": "gián tiếp"},
                {"Từ gốc (Base Word)": "direct (adj/v)", "Từ biến đổi (Derivative)": "direction", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "hướng đi, sự chỉ dẫn"},
                {"Từ gốc (Base Word)": "direct (adj/v)", "Từ biến đổi (Derivative)": "director", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "giám đốc, đạo diễn"},
                {"Từ gốc (Base Word)": "direct (adj/v)", "Từ biến đổi (Derivative)": "(in)directly", "Từ loại (POS)": "Adverb", "Nghĩa Tiếng Việt": "(một cách) trực tiếp / gián tiếp"},
                {"Từ gốc (Base Word)": "distant (adj)", "Từ biến đổi (Derivative)": "distantly", "Từ loại (POS)": "Adverb", "Nghĩa Tiếng Việt": "xa xăm, từ xa"},
                {"Từ gốc (Base Word)": "distant (adj)", "Từ biến đổi (Derivative)": "distance", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "khoảng cách"},
                {"Từ gốc (Base Word)": "enter (v)", "Từ biến đổi (Derivative)": "entrance", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "lối vào, sự đi vào"},
                {"Từ gốc (Base Word)": "inhabit (v)", "Từ biến đổi (Derivative)": "inhabitant", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "cư dân, người ở"},
                {"Từ gốc (Base Word)": "photograph (n/v)", "Từ biến đổi (Derivative)": "photography", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "thuật chụp ảnh, nhiếp ảnh"},
                {"Từ gốc (Base Word)": "photograph (n/v)", "Từ biến đổi (Derivative)": "photographer", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "nhiếp ảnh gia"},
                {"Từ gốc (Base Word)": "photograph (n/v)", "Từ biến đổi (Derivative)": "photographic", "Từ loại (POS)": "Adjective", "Nghĩa Tiếng Việt": "(thuộc) nhiếp ảnh, chụp ảnh"},
                {"Từ gốc (Base Word)": "recognise (v)", "Từ biến đổi (Derivative)": "(un)recognisable", "Từ loại (POS)": "Adjective", "Nghĩa Tiếng Việt": "(không) thể nhận ra"},
                {"Từ gốc (Base Word)": "recognise (v)", "Từ biến đổi (Derivative)": "recognition", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "sự nhận biết, sự công nhận"},
                {"Từ gốc (Base Word)": "time (n)", "Từ biến đổi (Derivative)": "timetable", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "thời khóa biểu, lịch trình"},
                {"Từ gốc (Base Word)": "tour (n/v)", "Từ biến đổi (Derivative)": "tourism", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "ngành du lịch"},
                {"Từ gốc (Base Word)": "tour (n/v)", "Từ biến đổi (Derivative)": "tourist", "Từ loại (POS)": "Noun", "Nghĩa Tiếng Việt": "khách du lịch"},
                {"Từ gốc (Base Word)": "world (n)", "Từ biến đổi (Derivative)": "worldwide", "Từ loại (POS)": "Adj / Adv", "Nghĩa Tiếng Việt": "toàn thế giới / trên toàn cầu"}
            ]
            st.table(pd.DataFrame(formation_b2_data))

    else:
        st.info(f"Nội dung lý thuyết chi tiết cho **{selected_unit}** đang được hoàn thiện dữ liệu từ sách Destination B2.")

# --- 3. BÀI TẬP TƯƠNG TÁC & CHẤM ĐIỂM TỰ ĐỘNG ---
elif menu_option == "✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)":
    st.header("✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)")
    selected_quiz_unit = st.selectbox("🎯 Chọn Unit / Bài Ôn tập làm bài:", ALL_UNITS_LIST)
    
    if "Unit 1" in selected_quiz_unit:
        st.subheader("✍️ Unit 1: Present time - Full Practice Exercises")
        st.info("Hãy hoàn thành các bài tập bên dưới. Tất cả các câu hỏi trắc nghiệm đều được **bỏ trống ban đầu**, hãy tự chọn đáp án đúng trước khi nhấp nút **Kiểm tra Đáp án**.")
        
        tab_a, tab_e, tab_i = st.tabs([
            "Exercise A (Present Simple vs Continuous)",
            "Exercise E (Multiple Choice Questions)",
            "Exercise I (Holiday Blues Gap-Fill)"
        ])
        
        with st.form("unit1_b2_full_form"):
            with tab_a:
                st.markdown("#### Exercise A: Choose the correct word or phrase")
                qa1 = st.radio("Câu 1: Elizabeth ________ to bed at around eleven o'clock.", [None, "A. usually goes", "B. is usually going"], key="qa1")
                qa2 = st.radio("Câu 2: Dan ________ on the other phone right now.", [None, "A. talks", "B. is talking"], key="qa2")
                qa3 = st.radio("Câu 3: We ________ any meat at the moment as we're both on a diet.", [None, "A. don't eat", "B. aren't eating"], key="qa3")
                qa4 = st.radio("Câu 4: ________ increasingly safe?", [None, "A. Does air travel get", "B. Is air travel getting"], key="qa4")
                qa5 = st.radio("Câu 5: My mum ________ me every weekend without fail.", [None, "A. calls", "B. is calling"], key="qa5")

            with tab_e:
                st.markdown("#### Exercise E: Choose the correct answer")
                qe1 = st.radio("Câu 6: Lan ________ a shower at the moment, so could you call back in about half an hour?", [None, "A. takes", "B. is taking", "C. has taken", "D. has been taking"], key="qe1")
                qe2 = st.radio("Câu 7: ________ to Ipswich before?", [None, "A. Do you ever go", "B. Are you ever going", "C. Have you ever been", "D. Have you ever been going"], key="qe2")
                qe3 = st.radio("Câu 8: Jessica has ________ left, I'm afraid.", [None, "A. already", "B. yet", "C. still", "D. so far"], key="qe3")

            with tab_i:
                st.markdown("#### Exercise I: Write one word in each gap (Holiday Blues)")
                qi1 = st.text_input("Câu 9: You've ________ looking at that timetable for the last ten minutes.", key="qi1")
                qi2 = st.text_input("Câu 10: I ________ wish you'd be quiet! I've got a splitting headache.", key="qi2")

            submit_u1 = st.form_submit_button("🚀 Kiểm tra Đáp án Unit 1")

        if submit_u1:
            score = 0
            total = 10
            st.subheader("📊 Kết quả & Giải thích Đáp án Unit 1:")
            
            # Question 1
            if qa1 == "A. usually goes":
                score += 1
                st.success("✅ **Câu 1: Chính xác!** (usually goes - Thói quen hiện tại lặp đi lặp lại).")
            elif qa1 is None:
                st.warning("⚠️ **Câu 1: Chưa trả lời / Bỏ trống.** Đáp án đúng: **A. usually goes**. (Thói quen hiện tại lặp đi lặp lại ở hiện tại đơn).")
            else:
                st.error(f"❌ **Câu 1: Sai.** Đáp án đúng: **A. usually goes**. (Bạn chọn: {qa1}). Giải thích: 'Usually' chỉ thói quen thường xuyên ở Present Simple.")

            # Question 2
            if qa2 == "B. is talking":
                score += 1
                st.success("✅ **Câu 2: Chính xác!** (is talking - Hành động đang diễn ra 'right now').")
            elif qa2 is None:
                st.warning("⚠️ **Câu 2: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. is talking**. (Hành động đang xảy ra tại thời điểm nói 'right now').")
            else:
                st.error(f"❌ **Câu 2: Sai.** Đáp án đúng: **B. is talking**. (Bạn chọn: {qa2}). Giải thích: Cụm 'right now' yêu cầu thì Hiện tại tiếp diễn.")

            # Question 3
            if qa3 == "B. aren't eating":
                score += 1
                st.success("✅ **Câu 3: Chính xác!** (aren't eating - Tình huống tạm thời 'at the moment').")
            elif qa3 is None:
                st.warning("⚠️ **Câu 3: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. aren't eating**. (Tình huống tạm thời kéo dài ở hiện tại 'at the moment').")
            else:
                st.error(f"❌ **Câu 3: Sai.** Đáp án đúng: **B. aren't eating**. (Bạn chọn: {qa3}). Giải thích: 'at the moment' diễn tả hành động/tình huống tạm thời.")

            # Question 4
            if qa4 == "B. Is air travel getting":
                score += 1
                st.success("✅ **Câu 4: Chính xác!** (Is air travel getting - Sự thay đổi/phát triển dần dần).")
            elif qa4 is None:
                st.warning("⚠️ **Câu 4: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. Is air travel getting**. (Sự thay đổi phát triển dần theo thời gian).")
            else:
                st.error(f"❌ **Câu 4: Sai.** Đáp án đúng: **B. Is air travel getting**. (Bạn chọn: {qa4}). Giải thích: Hiện tại tiếp diễn diễn tả xu hướng đang phát triển.")

            # Question 5
            if qa5 == "A. calls":
                score += 1
                st.success("✅ **Câu 5: Chính xác!** (calls - Tần suất định kỳ 'every weekend without fail').")
            elif qa5 is None:
                st.warning("⚠️ **Câu 5: Chưa trả lời / Bỏ trống.** Đáp án đúng: **A. calls**. (Thói quen định kỳ đều đặn dùng Present Simple).")
            else:
                st.error(f"❌ **Câu 5: Sai.** Đáp án đúng: **A. calls**. (Bạn chọn: {qa5}). Giải thích: 'every weekend' là dấu hiệu thói quen ở Hiện tại đơn.")

            # Question 6
            if qe1 == "B. is taking":
                score += 1
                st.success("✅ **Câu 6: Chính xác!** (is taking - Đang tắm tại thời điểm 'at the moment').")
            elif qe1 is None:
                st.warning("⚠️ **Câu 6: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. is taking**. (Đang thực hiện hành động tắm 'at the moment').")
            else:
                st.error(f"❌ **Câu 6: Sai.** Đáp án đúng: **B. is taking**. (Bạn chọn: {qe1}). Giải thích: 'at the moment' chia Hiện tại tiếp diễn.")

            # Question 7
            if qe2 == "C. Have you ever been":
                score += 1
                st.success("✅ **Câu 7: Chính xác!** (Have you ever been - Trải nghiệm từng đến đâu 'ever').")
            elif qe2 is None:
                st.warning("⚠️ **Câu 7: Chưa trả lời / Bỏ trống.** Đáp án đúng: **C. Have you ever been**. (Hỏi trải nghiệm tính đến hiện tại dùng Present Perfect).")
            else:
                st.error(f"❌ **Câu 7: Sai.** Đáp án đúng: **C. Have you ever been**. (Bạn chọn: {qe2}). Giải thích: Hỏi trải nghiệm cuộc đời với 'ever' dùng Present Perfect.")

            # Question 8
            if qe3 == "A. already":
                score += 1
                st.success("✅ **Câu 8: Chính xác!** (already - Đã rời đi rồi).")
            elif qe3 is None:
                st.warning("⚠️ **Câu 8: Chưa trả lời / Bỏ trống.** Đáp án đúng: **A. already**. (Diễn tả việc đã xảy ra rồi trong thì Present Perfect).")
            else:
                st.error(f"❌ **Câu 8: Sai.** Đáp án đúng: **A. already**. (Bạn chọn: {qe3}). Giải thích: 'already' đứng giữa 'has' và P2.")

            # Question 9
            if qi1.strip().lower() in ["been"]:
                score += 1
                st.success("✅ **Câu 9: Chính xác!** (been - You've been looking... Present Perfect Continuous).")
            elif not qi1.strip():
                st.warning("⚠️ **Câu 9: Chưa trả lời / Bỏ trống.** Đáp án đúng: **been**. (Cấu trúc 'have + been + V-ing' chỉ thời lượng 'for the last ten minutes').")
            else:
                st.error(f"❌ **Câu 9: Sai.** Đáp án đúng: **been**. (Bạn điền: {qi1}). Giải thích: Thì Present Perfect Continuous nhấn mạnh thời lượng kéo dài 10 phút.")

            # Question 10
            if qi2.strip().lower() in ["do", "really"]:
                score += 1
                st.success("✅ **Câu 10: Chính xác!** (do / really - Nhấn mạnh mong muốn 'I do wish...').")
            elif not qi2.strip():
                st.warning("⚠️ **Câu 10: Chưa trả lời / Bỏ trống.** Đáp án đúng: **do** (hoặc **really**). (Cấu trúc nhấn mạnh 'do wish' trong câu khẳng định).")
            else:
                st.error(f"❌ **Câu 10: Sai.** Đáp án đúng: **do** / **really**. (Bạn điền: {qi2}). Giải thích: Trợ động từ 'do' đứng trước động từ thường để nhấn mạnh cảm xúc.")

            st.metric("Kết quả bài làm Unit 1", f"{int((score/total)*100)}%", f"{score}/{total} câu đúng")

    elif "Unit 2" in selected_quiz_unit:
        st.subheader("✍️ Unit 2: Travel and transport - Full Practice Exercises")
        st.info("Hãy hoàn thành các bài tập bên dưới. Các câu hỏi trắc nghiệm được **bỏ trống ban đầu**, hãy tự chọn đáp án đúng trước khi nhấp nút **Kiểm tra Đáp án**.")
        
        tab_u2_a, tab_u2_c, tab_u2_e, tab_u2_f = st.tabs([
            "Exercise A (Topic Vocabulary)",
            "Exercise C (Phrasal Verbs)",
            "Exercise E (Phrases & Collocations)",
            "Exercise F (Word Patterns)"
        ])
        
        with st.form("unit2_b2_full_form"):
            with tab_u2_a:
                st.markdown("#### Exercise A: Choose the correct answer (Topic Vocabulary in Contrast)")
                q2a1 = st.radio("Câu 1: You need a passport to cross the ________ between Mexico and the United States.", [None, "A. edge", "B. line", "C. border", "D. rim"], key="q2a1")
                q2a2 = st.radio("Câu 2: The hotel where we are ________ is quite luxurious.", [None, "A. living", "B. remaining", "C. existing", "D. staying"], key="q2a2")
                q2a3 = st.radio("Câu 3: When you ________ your destination, your tour guide will meet you at the airport.", [None, "A. arrive", "B. get", "C. reach", "D. achieve"], key="q2a3")
                q2a4 = st.radio("Câu 4: I always enjoy our school ________ to France.", [None, "A. excursion", "B. journey", "C. trip", "D. travel"], key="q2a4")
                q2a5 = st.radio("Câu 5: Hurry up, or we'll ________ the bus!", [None, "A. avoid", "B. miss", "C. drop", "D. lose"], key="q2a5")

            with tab_u2_c:
                st.markdown("#### Exercise C: Complete using the correct form of phrasal verbs")
                q2c1 = st.radio("Câu 6: Let's go to the airport to ________ Grandpa off when he flies back home.", [None, "A. see", "B. check", "C. pick", "D. set"], key="q2c1")
                q2c2 = st.radio("Câu 7: If it starts to rain, ________ for a nearby cave to wait for it to pass.", [None, "A. get", "B. make", "C. pull", "D. turn"], key="q2c2")
                q2c3 = st.radio("Câu 8: Every Saturday night my dad ________ us up outside the cinema.", [None, "A. catches", "B. pulls", "C. picks", "D. checks"], key="q2c3")

            with tab_u2_e:
                st.markdown("#### Exercise E: Write one word in each gap (Phrases & Collocations)")
                q2e1 = st.text_input("Câu 9: The speed ________ in towns is 50 km/h and you shouldn't go faster than that.", key="q2e1")
                q2e2 = st.text_input("Câu 10: If you buy your plane ticket ________ advance, it's often cheaper.", key="q2e2")

            with tab_u2_f:
                st.markdown("#### Exercise F: Choose the correct answer (Word Patterns)")
                q2f1 = st.radio("Câu 11: I've always dreamt ________ China.", [None, "A. to visit", "B. of visiting", "C. I visit", "D. visit"], key="q2f1")
                q2f2 = st.radio("Câu 12: My dad says he always regrets ________ more.", [None, "A. to not travel", "B. not travelling", "C. he not travel", "D. of not travelling"], key="q2f2")

            submit_u2 = st.form_submit_button("🚀 Kiểm tra Đáp án Unit 2")

        if submit_u2:
            score2 = 0
            total2 = 12
            st.subheader("📊 Kết quả & Giải thích Đáp án Unit 2:")

            # Question 1
            if q2a1 == "C. border":
                score2 += 1
                st.success("✅ **Câu 1: Chính xác!** (border - Ranh giới/biên giới giữa hai quốc gia).")
            elif q2a1 is None:
                st.warning("⚠️ **Câu 1: Chưa trả lời / Bỏ trống.** Đáp án đúng: **C. border**. (border chỉ đường biên giới chính thức phân chia hai nước).")
            else:
                st.error(f"❌ **Câu 1: Sai.** Đáp án đúng: **C. border**. (Bạn chọn: {q2a1}). Giải thích: 'border' là biên giới quốc gia giữa Mexico và Mỹ.")

            # Question 2
            if q2a2 == "D. staying":
                score2 += 1
                st.success("✅ **Câu 2: Chính xác!** (staying - Lưu trú tạm thời tại khách sạn).")
            elif q2a2 is None:
                st.warning("⚠️ **Câu 2: Chưa trả lời / Bỏ trống.** Đáp án đúng: **D. staying**. (staying chỉ việc lưu trú tạm thời ở khách sạn, khác với 'living' là sinh sống lâu dài).")
            else:
                st.error(f"❌ **Câu 2: Sai.** Đáp án đúng: **D. staying**. (Bạn chọn: {q2a2}). Giải thích: 'stay at a hotel' nghĩa là ở tạm thời tại khách sạn.")

            # Question 3
            if q2a3 == "C. reach":
                score2 += 1
                st.success("✅ **Câu 3: Chính xác!** (reach - Reach + destination: đi tới/đạt tới điểm đến).")
            elif q2a3 is None:
                st.warning("⚠️ **Câu 3: Chưa trả lời / Bỏ trống.** Đáp án đúng: **C. reach**. ('reach' đi trực tiếp với tân ngữ điểm đến 'reach your destination' không cần giới từ).")
            else:
                st.error(f"❌ **Câu 3: Sai.** Đáp án đúng: **C. reach**. (Bạn chọn: {q2a3}). Giải thích: 'arrive' cần giới từ 'at/in', trong khi 'reach' đi trực tiếp với tân ngữ.")

            # Question 4
            if q2a4 == "C. trip":
                score2 += 1
                st.success("✅ **Câu 4: Chính xác!** (trip - Chuyến đi ngắn học đường/dã ngoại 'school trip').")
            elif q2a4 is None:
                st.warning("⚠️ **Câu 4: Chưa trả lời / Bỏ trống.** Đáp án đúng: **C. trip**. (Cụm từ cố định 'school trip' chỉ chuyến dã ngoại/đi thực tế của trường).")
            else:
                st.error(f"❌ **Câu 4: Sai.** Đáp án đúng: **C. trip**. (Bạn chọn: {q2a4}). Giải thích: Cụm từ chuẩn B2 là 'school trip'.")

            # Question 5
            if q2a5 == "B. miss":
                score2 += 1
                st.success("✅ **Câu 5: Chính xác!** (miss - Lỡ/nhỡ chuyến xe bus 'miss the bus').")
            elif q2a5 is None:
                st.warning("⚠️ **Câu 5: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. miss**. ('miss the bus' nghĩa là đến muộn và bị lỡ xe bus).")
            else:
                st.error(f"❌ **Câu 5: Sai.** Đáp án đúng: **B. miss**. (Bạn chọn: {q2a5}). Giải thích: Phân biệt 'miss' (lỡ chuyến tàu/xe) và 'lose' (làm mất đồ đạc).")

            # Question 6
            if q2c1 == "A. see":
                score2 += 1
                st.success("✅ **Câu 6: Chính xác!** (see off - Tiễn ai lên đường 'see Grandpa off').")
            elif q2c1 is None:
                st.warning("⚠️ **Câu 6: Chưa trả lời / Bỏ trống.** Đáp án đúng: **A. see**. (Phrasal verb 'see sb off' nghĩa là ra sân bay/nhà ga tiễn ai đi).")
            else:
                st.error(f"❌ **Câu 6: Sai.** Đáp án đúng: **A. see**. (Bạn chọn: {q2c1}). Giải thích: Phrasal verb 'see off' = tiễn biệt ai ở sân bay/bến xe.")

            # Question 7
            if q2c2 == "B. make":
                score2 += 1
                st.success("✅ **Câu 7: Chính xác!** (make for - Đi về phía / hướng về nơi nào đó).")
            elif q2c2 is None:
                st.warning("⚠️ **Câu 7: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. make**. (Phrasal verb 'make for swh' nghĩa là di chuyển hướng về phía nơi nào).")
            else:
                st.error(f"❌ **Câu 7: Sai.** Đáp án đúng: **B. make**. (Bạn chọn: {q2c2}). Giải thích: 'make for a nearby cave' = đi nhanh về phía hang động trú mưa.")

            # Question 8
            if q2c3 == "C. picks":
                score2 += 1
                st.success("✅ **Câu 8: Chính xác!** (picks up - Đón ai bằng xe 'picks us up').")
            elif q2c3 is None:
                st.warning("⚠️ **Câu 8: Chưa trả lời / Bỏ trống.** Đáp án đúng: **C. picks**. ('pick sb up' nghĩa là lái xe đến đón ai).")
            else:
                st.error(f"❌ **Câu 8: Sai.** Đáp án đúng: **C. picks**. (Bạn chọn: {q2c3}). Giải thích: Phrasal verb 'pick up' = ghé xe đón ai.")

            # Question 9
            if q2e1.strip().lower() in ["limit"]:
                score2 += 1
                st.success("✅ **Câu 9: Chính xác!** (limit - Collocation 'speed limit': giới hạn tốc độ).")
            elif not q2e1.strip():
                st.warning("⚠️ **Câu 9: Chưa trả lời / Bỏ trống.** Đáp án đúng: **limit**. (Collocation chuẩn 'speed limit' nghĩa là tốc độ tối đa cho phép).")
            else:
                st.error(f"❌ **Câu 9: Sai.** Đáp án đúng: **limit**. (Bạn điền: {q2e1}). Giải thích: Cụm từ cố định B2 là 'speed limit'.")

            # Question 10
            if q2e2.strip().lower() in ["in"]:
                score2 += 1
                st.success("✅ **Câu 10: Chính xác!** (in - Preposition 'in advance': đặt trước).")
            elif not q2e2.strip():
                st.warning("⚠️ **Câu 10: Chưa trả lời / Bỏ trống.** Đáp án đúng: **in**. (Cụm giới từ cố định 'in advance' = làm cái gì đó trước).")
            else:
                st.error(f"❌ **Câu 10: Sai.** Đáp án đúng: **in**. (Bạn điền: {q2e2}). Giải thích: 'in advance' nghĩa là đặt trước / báo trước.")

            # Question 11
            if q2f1 == "B. of visiting":
                score2 += 1
                st.success("✅ **Câu 11: Chính xác!** (of visiting - Word pattern 'dream of/about doing sth').")
            elif q2f1 is None:
                st.warning("⚠️ **Câu 11: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. of visiting**. (Word pattern 'dream of + V-ing' nghĩa là mơ ước làm gì).")
            else:
                st.error(f"❌ **Câu 11: Sai.** Đáp án đúng: **B. of visiting**. (Bạn chọn: {q2f1}). Giải thích: Sau động từ 'dream' đi với giới từ 'of/about' + V-ing.")

            # Question 12
            if q2f2 == "B. not travelling":
                score2 += 1
                st.success("✅ **Câu 12: Chính xác!** (not travelling - Word pattern 'regret not doing sth').")
            elif q2f2 is None:
                st.warning("⚠️ **Câu 12: Chưa trả lời / Bỏ trống.** Đáp án đúng: **B. not travelling**. (Word pattern 'regret doing/not doing sth' nghĩa là hối tiếc vì đã/không làm gì).")
            else:
                st.error(f"❌ **Câu 12: Sai.** Đáp án đúng: **B. not travelling**. (Bạn chọn: {q2f2}). Giải thích: 'regret not doing sth' = hối hận vì trong quá khứ đã không làm gì.")

            st.metric("Kết quả bài làm Unit 2", f"{int((score2/total2)*100)}%", f"{score2}/{total2} câu đúng")

    else:
        st.info(f"Bài tập tương tác cho **{selected_quiz_unit}** đang được phát triển dữ liệu.")

# --- 4. THẺ GHI NHỚ TỪ VỰNG (FLASHCARDS) ---
elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng B2 (Vocabulary Flashcards)")
    st.caption("Lật thẻ để ôn luyện phản xạ từ vựng, phrasal verbs, collocations và word formation.")
    
    selected_fc_unit = st.selectbox("🎯 Chọn Unit Từ vựng để ôn tập Flashcards:", VOCAB_UNITS)
    
    flashcards_database = {
        "Unit 2: Vocabulary - Travel and transport": [
            {"word": "voyage (n)", "pos": "noun", "def": "a long journey, especially on a ship", "vi": "chuyến đi dài bằng đường biển", "ex": "It was a long voyage from London to New York."},
            {"word": "excursion (n)", "pos": "noun", "def": "a short journey that you make for pleasure", "vi": "chuyến tham quan dã ngoại", "ex": "My grandmother often talks about excursions to the sea."},
            {"word": "catch up with (phr v)", "pos": "phrasal verb", "def": "reach the same point/level as someone", "vi": "theo kịp, đuổi kịp ai", "ex": "Run fast to catch up with the group."},
            {"word": "check in (phr v)", "pos": "phrasal verb", "def": "register at a hotel or an airport", "vi": "làm thủ tục nhận phòng/lên máy bay", "ex": "We checked in at the airport two hours before the flight."},
            {"word": "off the top of your head (colloc)", "pos": "collocation", "def": "from memory, without checking or thinking carefully", "vi": "theo trí nhớ, không cần tra cứu", "ex": "I can't tell you the number off the top of my head."},
            {"word": "in advance (colloc)", "pos": "collocation", "def": "before a particular time or event", "vi": "trước, làm trước", "ex": "You should book your tickets well in advance."},
            {"word": "broaden (v)", "pos": "word formation", "def": "to increase your knowledge or experience", "vi": "mở rộng (tầm mắt, kiến thức)", "ex": "Travel really broadens your horizons."},
            {"word": "unrecognisable (adj)", "pos": "word formation", "def": "so changed that you cannot recognise it", "vi": "không thể nhận ra (do thay đổi)", "ex": "The city has changed so much that it is almost unrecognisable."}
        ]
    }
    
    cards = flashcards_database.get(selected_fc_unit, flashcards_database["Unit 2: Vocabulary - Travel and transport"])
    
    if 'fc_idx' not in st.session_state:
        st.session_state.fc_idx = 0
        
    curr_fc = st.session_state.fc_idx % len(cards)
    card = cards[curr_fc]
    
    col_fc, _ = st.columns([2, 1])
    with col_fc:
        st.markdown(f"""
        <div class="card" style="text-align: center; padding: 2rem;">
            <span class="badge-vocab">{card['pos'].upper()}</span>
            <h2 style="color: #1E3A8A; margin-top: 0.8rem; margin-bottom: 0.5rem;">{card['word']}</h2>
            <hr style="border: 0.5px solid #CBD5E1;">
            <p style="font-size: 1.15rem; color: #1E293B;"><b>📖 Định nghĩa (English):</b> {card['def']}</p>
            <p style="font-size: 1.15rem; color: #047857;"><b>🇻🇳 Nghĩa Tiếng Việt:</b> {card['vi']}</p>
            <p style="font-style: italic; color: #475569;"><b>💬 Ví dụ ngữ cảnh:</b> "{card['ex']}"</p>
        </div>
        """, unsafe_allow_html=True)
        
    c_prev, c_next, _ = st.columns([1, 1, 3])
    with c_prev:
        if st.button("⬅️ Thẻ trước"):
            st.session_state.fc_idx = (curr_fc - 1) % len(cards)
            st.rerun()
    with c_next:
        if st.button("Thẻ tiếp ➡️"):
            st.session_state.fc_idx = (curr_fc + 1) % len(cards)
            st.rerun()
            
    st.caption(f"Thẻ {curr_fc + 1} / {len(cards)}")

# --- 5. GÓC LƯU Ý (WATCH OUT! CORNER) ---
elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý B2 (Watch Out! Corner)")
    st.write("Tổng hợp các bẫy ngữ pháp và từ vựng B2 quan trọng được rút ra từ cuốn Destination B2:")
    
    st.markdown("""
    <div class="watchout-box">
        <h4>⚠️ Watch Out #1: Present Perfect Simple vs Present Perfect Continuous</h4>
        • <b>Present Perfect Simple</b>: Nhấn mạnh <u>kết quả / con số / số lần hoàn thành</u>.<br>
        &nbsp;&nbsp;<i>✔ I've written <b>three letters</b> this morning.</i><br>
        • <b>Present Perfect Continuous</b>: Nhấn mạnh <u>thời lượng / tính liên tục kéo dài</u> của hành động.<br>
        &nbsp;&nbsp;<i>✔ I've been writing letters <b>all morning</b>.</i>
    </div>
    
    <div class="watchout-box">
        <h4>⚠️ Watch Out #2: Stative Verbs in Continuous Tenses</h4>
        Nhiều động từ trạng thái có thể chuyển sang thì tiếp diễn khi mang nét nghĩa HÀNH ĐỘNG:<br>
        • <i>I <b>have</b> a car.</i> (Sở hữu = State)<br>
        • <i>I'm <b>having</b> lunch.</i> (Ăn uống = Action)<br>
        • <i>I <b>think</b> it's a good idea.</i> (Tin tưởng/quan điểm = State)<br>
        • <i>I'm <b>thinking</b> about buying a bike.</i> (Cân nhắc = Action)
    </div>
    
    <div class="watchout-box">
        <h4>⚠️ Watch Out #3: Nhấn mạnh khẳng định với 'Do / Does'</h4>
        Sử dụng <code>do / does + V-bare</code> trong câu khẳng định thì Present Simple để nhấn mạnh cảm xúc hoặc sự đối lập:<br>
        • <i>I don't play much tennis, but I <b>do enjoy</b> watching it!</i>
    </div>
    """, unsafe_allow_html=True)

# --- 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập (Progress Report)")
    st.write("Đánh dấu các Unit bạn đã hoàn thành để theo dõi tỷ lệ phần trăm tiến độ học tập toàn cuốn sách Destination B2.")
    
    completed_units = []
    cols = st.columns(3)
    
    for idx, u in enumerate(ALL_UNITS_LIST):
        col = cols[idx % 3]
        chk = col.checkbox(u, key=f"chk_prog_{idx}", value=(idx in [0, 1]))
        if chk:
            completed_units.append(u)
            
    total_u = len(ALL_UNITS_LIST)
    done_u = len(completed_units)
    pct = int((done_u / total_u) * 100)
    
    st.markdown("---")
    st.subheader("📈 Tiến độ Hoàn thành Khóa học B2:")
    st.progress(pct / 100)
    st.success(f"🎉 Bạn đã hoàn thành **{done_u}/{total_u}** mục học tập ({pct}%)")

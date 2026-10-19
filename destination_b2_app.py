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
    .flashcard-box {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 1rem;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .flashcard-back {
        background: linear-gradient(135deg, #059669 0%, #10B981 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 1rem;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .card-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .card-sub {
        font-size: 1.2rem;
        opacity: 0.9;
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
        st.write("Trích xuất đầy đủ chi tiết từ vựng theo cấu trúc bài học Destination B2:")
        
        tab_v1, tab_v2, tab_v3, tab_v4, tab_v5 = st.tabs([
            "1. Topic Vocabulary in Contrast",
            "2. Phrasal Verbs",
            "3. Phrases and Collocations",
            "4. Word Patterns",
            "5. Word Formation"
        ])
        
        with tab_v1:
            st.markdown("#### 🔹 Topic Vocabulary in Contrast (Từ vựng theo chủ đề dễ nhầm lẫn)")
            topic_vocab_data = [
                {"Từ vựng / Cụm từ": "voyage (n)", "IPA": "/ˈvɔɪ.ɪdʒ/", "Định nghĩa Tiếng Anh": "a long journey, especially on a ship or in space", "Nghĩa Tiếng Việt": "chuyến đi dài bằng đường biển / vũ trụ", "Ví dụ minh họa": "It was a long voyage from London to New York."},
                {"Từ vựng / Cụm từ": "journey (n)", "IPA": "/ˈdʒɜː.ni/", "Định nghĩa Tiếng Anh": "an occasion when you travel from one place to another, especially over a long distance", "Nghĩa Tiếng Việt": "chuyến đi, hành trình", "Ví dụ minh họa": "We had a long journey ahead of us."},
                {"Từ vựng / Cụm từ": "trip (n)", "IPA": "/trɪp/", "Định nghĩa Tiếng Anh": "an occasion when you go somewhere and come back again", "Nghĩa Tiếng Việt": "chuyến đi ngắn (đi rồi về)", "Ví dụ minh họa": "The whole family went on a trip to Florida."},
                {"Từ vựng / Cụm từ": "travel (n/v)", "IPA": "/ˈtræv.əl/", "Định nghĩa Tiếng Anh": "the activity of travelling; to move or travel", "Nghĩa Tiếng Việt": "sự đi lại / du lịch", "Ví dụ minh họa": "Foreign travel never really appealed to him until he retired."},
                {"Từ vựng / Cụm từ": "excursion (n)", "IPA": "/ɪkˈskɜː.ʃən/", "Định nghĩa Tiếng Anh": "a short journey that you make for pleasure", "Nghĩa Tiếng Việt": "chuyến tham quan, dã ngoại", "Ví dụ minh họa": "My grandmother often talks about excursions to the sea."},
                {"Từ vựng / Cụm từ": "view (n)", "IPA": "/vjuː/", "Định nghĩa Tiếng Anh": "the things that you can see from a particular place", "Nghĩa Tiếng Việt": "quang cảnh, tầm nhìn từ một vị trí", "Ví dụ minh họa": "We had a spectacular view of the mountains from our room."},
                {"Từ vựng / Cụm từ": "sight (n)", "IPA": "/saɪt/", "Định nghĩa Tiếng Anh": "a person or a thing that you see that has a particular feature; sights = places of interest", "Nghĩa Tiếng Việt": "cảnh trí / danh lam thắng cảnh", "Ví dụ minh họa": "Windmills are a common sight in this part of the country."},
                {"Từ vựng / Cụm từ": "world (n)", "IPA": "/wɜːld/", "Định nghĩa Tiếng Anh": "the planet that we live on", "Nghĩa Tiếng Việt": "thế giới, hành tinh", "Ví dụ minh họa": "It's easy these days to communicate with people on the other side of the world."},
                {"Từ vựng / Cụm từ": "earth (n)", "IPA": "/ɜːθ/", "Định nghĩa Tiếng Anh": "the land on which we live", "Nghĩa Tiếng Việt": "trái đất, mặt đất", "Ví dụ minh họa": "They felt the earth shake during the earthquake."},
                {"Từ vựng / Cụm từ": "area (n)", "IPA": "/ˈeə.ri.ə/", "Định nghĩa Tiếng Anh": "a part of a place or building", "Nghĩa Tiếng Việt": "vùng, khu vực", "Ví dụ minh họa": "Bus services in rural areas are not very good."},
                {"Từ vựng / Cụm từ": "territory (n)", "IPA": "/ˈter.ɪ.tər.i/", "Định nghĩa Tiếng Anh": "an area of land that is controlled by a particular country, leader or army", "Nghĩa Tiếng Việt": "lãnh thổ", "Ví dụ minh họa": "Russian troops crossed into Austrian territory in February 1849."},
                {"Từ vựng / Cụm từ": "season (n)", "IPA": "/ˈsiː.zən/", "Định nghĩa Tiếng Anh": "one of the four periods into which the year is divided according to the weather", "Nghĩa Tiếng Việt": "mùa (trong năm)", "Ví dụ minh họa": "She likes to paint the changing seasons in the garden."},
                {"Từ vựng / Cụm từ": "period (n)", "IPA": "/ˈpɪə.ri.əd/", "Định nghĩa Tiếng Anh": "an amount of time", "Nghĩa Tiếng Việt": "thời kỳ, khoảng thời gian", "Ví dụ minh họa": "The long dry period ended with heavy rain."},
                {"Từ vựng / Cụm từ": "fare (n)", "IPA": "/feər/", "Định nghĩa Tiếng Anh": "the money that you pay for a journey on a train, bus, plane, etc.", "Nghĩa Tiếng Việt": "tiền xe, vé xe/tàu/máy bay", "Ví dụ minh họa": "The fare from York to Leeds has gone up."},
                {"Từ vựng / Cụm từ": "ticket (n)", "IPA": "/ˈtɪk.ɪt/", "Định nghĩa Tiếng Anh": "a piece of paper that shows that you have paid to do something", "Nghĩa Tiếng Việt": "vé (xem phim, vào cửa, đi lại)", "Ví dụ minh họa": "We'll send your tickets a week before your flight."},
                {"Từ vựng / Cụm từ": "fee (n)", "IPA": "/fiː/", "Định nghĩa Tiếng Anh": "an amount of money that you pay to be allowed to do something", "Nghĩa Tiếng Việt": "lệ phí, phí dịch vụ", "Ví dụ minh họa": "The gallery charges a small entrance fee."},
                {"Từ vựng / Cụm từ": "miss (v)", "IPA": "/mɪs/", "Định nghĩa Tiếng Anh": "to be too late for something such as a train or bus", "Nghĩa Tiếng Việt": "nhỡ, bỏ lỡ (xe, tàu)", "Ví dụ minh họa": "I missed the last train home again."},
                {"Từ vựng / Cụm từ": "lose (v)", "IPA": "/luːz/", "Định nghĩa Tiếng Anh": "to no longer have something", "Nghĩa Tiếng Việt": "đánh mất, thất lạc", "Ví dụ minh họa": "Mike lost his job last year."},
                {"Từ vựng / Cụm từ": "take (v)", "IPA": "/teɪk/", "Định nghĩa Tiếng Anh": "to move or carry someone or something from one place to another", "Nghĩa Tiếng Việt": "đưa đi, mang đi", "Ví dụ minh họa": "What time do you take Amy to school?"},
                {"Từ vựng / Cụm từ": "bring (v)", "IPA": "/brɪŋ/", "Định nghĩa Tiếng Anh": "to take someone or something with you from one place to another", "Nghĩa Tiếng Việt": "mang lại, cầm lại", "Ví dụ minh họa": "Bring a coat in case it turns cold."},
                {"Từ vựng / Cụm từ": "go (v)", "IPA": "/ɡəʊ/", "Định nghĩa Tiếng Anh": "to move or travel to a place that is away from where you are now", "Nghĩa Tiếng Việt": "đi (tới một nơi)", "Ví dụ minh họa": "We're planning to go to Spain this winter."},
                {"Từ vựng / Cụm từ": "book (v)", "IPA": "/bʊk/", "Định nghĩa Tiếng Anh": "to arrange to have or use something at a particular time in the future", "Nghĩa Tiếng Việt": "đặt trước (vé, phòng)", "Ví dụ minh họa": "Shall I book a room for you?"},
                {"Từ vựng / Cụm từ": "keep (v)", "IPA": "/kiːp/", "Định nghĩa Tiếng Anh": "to continue to have or own something", "Nghĩa Tiếng Việt": "giữ, duy trì", "Ví dụ minh họa": "We should keep this car and sell the other one."},
                {"Từ vựng / Cụm từ": "arrive (v)", "IPA": "/əˈraɪv/", "Định nghĩa Tiếng Anh": "to reach a place", "Nghĩa Tiếng Việt": "đến nơi (đi kèm in/at)", "Ví dụ minh họa": "What time does your plane arrive?"},
                {"Từ vựng / Cụm từ": "reach (v)", "IPA": "/riːtʃ/", "Định nghĩa Tiếng Anh": "to arrive somewhere", "Nghĩa Tiếng Việt": "đến, đạt tới (không đi kèm giới từ)", "Ví dụ minh họa": "We hoped to reach the camp before dark."},
                {"Từ vựng / Cụm từ": "live (v)", "IPA": "/lɪv/", "Định nghĩa Tiếng Anh": "to have your home in a particular place", "Nghĩa Tiếng Việt": "sống, cư trú lâu dài", "Ví dụ minh họa": "Paris is a nice place to live."},
                {"Từ vựng / Cụm từ": "stay (v)", "IPA": "/steɪ/", "Định nghĩa Tiếng Anh": "to live or remain in a place for a while as a guest or visitor", "Nghĩa Tiếng Việt": "ở lại, ở tạm", "Ví dụ minh họa": "How long is he planning to stay with you?"},
                {"Từ vựng / Cụm từ": "border (n)", "IPA": "/ˈbɔː.dər/", "Định nghĩa Tiếng Anh": "the official line that separates two countries or regions", "Nghĩa Tiếng Việt": "biên giới", "Ví dụ minh họa": "Thousands of refugees were fleeing across the border."},
                {"Từ vựng / Cụm từ": "edge (n)", "IPA": "/edʒ/", "Định nghĩa Tiếng Anh": "the part of something that is furthest from its centre", "Nghĩa Tiếng Việt": "mép, rìa", "Ví dụ minh họa": "Victoria was sitting on the edge of the bed."},
                {"Từ vựng / Cụm từ": "line (n)", "IPA": "/laɪn/", "Định nghĩa Tiếng Anh": "a long thin mark on the surface of something", "Nghĩa Tiếng Việt": "đường kẻ, ranh giới", "Ví dụ minh họa": "Draw a straight line."},
                {"Từ vựng / Cụm từ": "length (n)", "IPA": "/leŋθ/", "Định nghĩa Tiếng Anh": "a measurement of how long something is in size", "Nghĩa Tiếng Việt": "chiều dài, độ dài", "Ví dụ minh họa": "The boat was 16 feet in length."},
                {"Từ vựng / Cụm từ": "distance (n)", "IPA": "/ˈdɪs.təns/", "Định nghĩa Tiếng Anh": "the amount of space between two people or things", "Nghĩa Tiếng Việt": "khoảng cách", "Ví dụ minh họa": "They started to walk the short distance to the camp."},
                {"Từ vựng / Cụm từ": "guide (v)", "IPA": "/ɡaɪd/", "Định nghĩa Tiếng Anh": "to show someone where to go by going with them", "Nghĩa Tiếng Việt": "dẫn đường, hướng dẫn", "Ví dụ minh họa": "He guided them through the forest."},
                {"Từ vựng / Cụm từ": "lead (v)", "IPA": "/liːd/", "Định nghĩa Tiếng Anh": "to take someone to a place by going in front of them", "Nghĩa Tiếng Việt": "dẫn dắt, đi đầu", "Ví dụ minh họa": "The estate agent led us into the kitchen."},
                {"Từ vựng / Cụm từ": "native (adj)", "IPA": "/ˈneɪ.tɪv/", "Định nghĩa Tiếng Anh": "living in a particular country or area since birth", "Nghĩa Tiếng Việt": "bản địa, tự nhiên từ khi sinh ra", "Ví dụ minh họa": "My wife's a native New Yorker."},
                {"Từ vựng / Cụm từ": "home (town) (n)", "IPA": "/həʊm/", "Định nghĩa Tiếng Anh": "the city or town where you lived as a child", "Nghĩa Tiếng Việt": "quê nhà, nơi sinh sống gắn bó", "Ví dụ minh họa": "I live in Washington, but my home town is Denver."}
            ]
            st.table(pd.DataFrame(topic_vocab_data))

        with tab_v2:
            st.markdown("#### 🔹 Phrasal Verbs (Cụm động từ chủ đề Du lịch & Giao thông)")
            phrasal_verbs_data = [
                {"Cụm động từ": "catch up with", "IPA": "/kætʃ ʌp wɪð/", "Giải thích Tiếng Anh": "reach the same point/level as someone", "Nghĩa Tiếng Việt": "theo kịp, đuổi kịp", "Ví dụ minh họa": "Run fast to catch up with the group."},
                {"Cụm động từ": "check in", "IPA": "/tʃek ɪn/", "Giải thích Tiếng Anh": "register at a hotel or an airport", "Nghĩa Tiếng Việt": "làm thủ tục nhận phòng / lên máy bay", "Ví dụ minh họa": "We checked in at the airport two hours before the flight."},
                {"Cụm động từ": "check out", "IPA": "/tʃek aʊt/", "Giải thích Tiếng Anh": "leave a hotel; investigate", "Nghĩa Tiếng Việt": "làm thủ tục trả phòng / điều tra", "Ví dụ minh họa": "All guests must check out before midday."},
                {"Cụm động từ": "drop off", "IPA": "/drɒp ɒf/", "Giải thích Tiếng Anh": "let someone get out of a vehicle; fall asleep", "Nghĩa Tiếng Việt": "thả ai xuống xe / ngủ gật", "Ví dụ minh họa": "I can drop you off at the station on my way to work."},
                {"Cụm động từ": "get back", "IPA": "/ɡet bæk/", "Giải thích Tiếng Anh": "return from a place", "Nghĩa Tiếng Việt": "trở về (từ một chuyến đi)", "Ví dụ minh họa": "When did you get back from your holiday?"},
                {"Cụm động từ": "go away", "IPA": "/ɡəʊ əˈweɪ/", "Giải thích Tiếng Anh": "go on holiday", "Nghĩa Tiếng Việt": "đi nghỉ mát / đi xa", "Ví dụ minh họa": "We're going away for the weekend."},
                {"Cụm động từ": "keep up with", "IPA": "/kiːp ʌp wɪð/", "Giải thích Tiếng Anh": "stay at the same point/level as", "Nghĩa Tiếng Việt": "theo kịp, giữ cùng tốc độ/trình độ với", "Ví dụ minh họa": "Gordon is finding it hard to keep up with the other students."},
                {"Cụm động từ": "make for", "IPA": "/meɪk fɔː/", "Giải thích Tiếng Anh": "go in the direction of", "Nghĩa Tiếng Việt": "đi về hướng, tiến về phía", "Ví dụ minh họa": "He picked up his umbrella and made for the door."},
                {"Cụm động từ": "pick up", "IPA": "/pɪk ʌp/", "Giải thích Tiếng Anh": "stop in a vehicle to give someone a lift", "Nghĩa Tiếng Việt": "đón ai bằng xe", "Ví dụ minh họa": "I'll pick you up outside the cinema at seven."},
                {"Cụm động từ": "pull in", "IPA": "/pʊl ɪn/", "Giải thích Tiếng Anh": "stop by the side of the road in a car", "Nghĩa Tiếng Việt": "tấp xe vào lề đường", "Ví dụ minh họa": "Please pull in here so I can buy a newspaper."},
                {"Cụm động từ": "run over", "IPA": "/rʌn ˈəʊ.vər/", "Giải thích Tiếng Anh": "hit with a car", "Nghĩa Tiếng Việt": "tông/cán qua (bằng xe)", "Ví dụ minh họa": "The driver couldn't stop in time and ran over a dog."},
                {"Cụm động từ": "see off", "IPA": "/siː ɒf/", "Giải thích Tiếng Anh": "go to a train station, etc, to see someone leave", "Nghĩa Tiếng Việt": "tiễn ai lên đường", "Ví dụ minh họa": "We went to the station to see Colin off."},
                {"Cụm động từ": "set out/off", "IPA": "/set aʊt/ɒf/", "Giải thích Tiếng Anh": "start a journey", "Nghĩa Tiếng Việt": "khởi hành chuyến đi", "Ví dụ minh họa": "They set out early in the morning to avoid traffic."},
                {"Cụm động từ": "take off", "IPA": "/teɪk ɒf/", "Giải thích Tiếng Anh": "leave the ground", "Nghĩa Tiếng Việt": "cất cánh (máy bay)", "Ví dụ minh họa": "The plane took off on time despite the fog."},
                {"Cụm động từ": "turn round", "IPA": "/tɜːn raʊnd/", "Giải thích Tiếng Anh": "go back in the opposite direction", "Nghĩa Tiếng Việt": "quay ngược lại, quay đầu", "Ví dụ minh họa": "We realised we were going the wrong way and turned round."}
            ]
            st.table(pd.DataFrame(phrasal_verbs_data))

        with tab_v3:
            st.markdown("#### 🔹 Phrases and Collocations (Tách lẻ từng cụm từ cố định)")
            phrases_data = [
                {"Từ gốc": "accident", "Cụm từ tiếng Anh": "have an accident", "Nghĩa Tiếng Việt": "gặp tai nạn"},
                {"Từ gốc": "accident", "Cụm từ tiếng Anh": "be (involved) in an accident", "Nghĩa Tiếng Việt": "bị tai nạn / liên quan đến tai nạn"},
                {"Từ gốc": "accident", "Cụm từ tiếng Anh": "do sth by accident", "Nghĩa Tiếng Việt": "vô tình / tình cờ làm gì"},
                {"Từ gốc": "advance", "Cụm từ tiếng Anh": "in advance", "Nghĩa Tiếng Việt": "trước, sớm (về thời gian)"},
                {"Từ gốc": "advance", "Cụm từ tiếng Anh": "advance to/towards a place", "Nghĩa Tiếng Việt": "tiến về phía một nơi"},
                {"Từ gốc": "ahead", "Cụm từ tiếng Anh": "go straight ahead", "Nghĩa Tiếng Việt": "đi thẳng về phía trước"},
                {"Từ gốc": "ahead", "Cụm từ tiếng Anh": "go ahead", "Nghĩa Tiếng Việt": "tiến lên / tiếp tục"},
                {"Từ gốc": "ahead", "Cụm từ tiếng Anh": "be ahead of sth/sb", "Nghĩa Tiếng Việt": "dẫn trước / đi trước ai/cái gì"},
                {"Từ gốc": "direction", "Cụm từ tiếng Anh": "a change of direction", "Nghĩa Tiếng Việt": "sự đổi hướng"},
                {"Từ gốc": "direction", "Cụm từ tiếng Anh": "in the direction of sth", "Nghĩa Tiếng Việt": "theo hướng của cái gì"},
                {"Từ gốc": "direction", "Cụm từ tiếng Anh": "in this/that direction", "Nghĩa Tiếng Việt": "theo hướng này/đó"},
                {"Từ gốc": "head", "Cụm từ tiếng Anh": "off the top of your head", "Nghĩa Tiếng Việt": "theo phản xạ / không cần suy nghĩ kỹ / theo trí nhớ"},
                {"Từ gốc": "head", "Cụm từ tiếng Anh": "head for/towards a place", "Nghĩa Tiếng Việt": "đi về phía / hướng về một nơi"},
                {"Từ gốc": "head", "Cụm từ tiếng Anh": "head over heels (in love)", "Nghĩa Tiếng Việt": "yêu say đắm / điêu đứng vì yêu"},
                {"Từ gốc": "holiday", "Cụm từ tiếng Anh": "go/be on holiday", "Nghĩa Tiếng Việt": "đi/đang nghỉ mát"},
                {"Từ gốc": "holiday", "Cụm từ tiếng Anh": "have/take a holiday", "Nghĩa Tiếng Việt": "có/nghỉ một kỳ nghỉ"},
                {"Từ gốc": "holiday", "Cụm từ tiếng Anh": "bank holiday", "Nghĩa Tiếng Việt": "ngày nghỉ lễ chính thức (ngân hàng/nhà nước)"},
                {"Từ gốc": "left", "Cụm từ tiếng Anh": "go/turn/etc left", "Nghĩa Tiếng Việt": "rẽ/đi sang bên trái"},
                {"Từ gốc": "left", "Cụm từ tiếng Anh": "on the left", "Nghĩa Tiếng Việt": "ở bên trái"},
                {"Từ gốc": "left", "Cụm từ tiếng Anh": "on the left-hand side", "Nghĩa Tiếng Việt": "ở phía bên tay trái"},
                {"Từ gốc": "left", "Cụm từ tiếng Anh": "in the left-hand corner", "Nghĩa Tiếng Việt": "ở góc bên tay trái"},
                {"Từ gốc": "left", "Cụm từ tiếng Anh": "left-handed", "Nghĩa Tiếng Việt": "thuận tay trái"},
                {"Từ gốc": "route", "Cụm từ tiếng Anh": "plan your/a route", "Nghĩa Tiếng Việt": "lên lịch trình / vạch ra tuyến đường"},
                {"Từ gốc": "route", "Cụm từ tiếng Anh": "take a route", "Nghĩa Tiếng Việt": "đi theo một tuyến đường"},
                {"Từ gốc": "sights", "Cụm từ tiếng Anh": "see the sights", "Nghĩa Tiếng Việt": "ngắm cảnh / tham quan danh lam thắng cảnh"},
                {"Từ gốc": "sightseeing", "Cụm từ tiếng Anh": "go sightseeing", "Nghĩa Tiếng Việt": "đi tham quan ngắm cảnh"},
                {"Từ gốc": "speed", "Cụm từ tiếng Anh": "at (high/full/etc) speed", "Nghĩa Tiếng Việt": "ở tốc độ (cao/tối đa...)"},
                {"Từ gốc": "speed", "Cụm từ tiếng Anh": "a burst of speed", "Nghĩa Tiếng Việt": "sự tăng tốc đột ngột"},
                {"Từ gốc": "speed", "Cụm từ tiếng Anh": "speed limit", "Nghĩa Tiếng Việt": "giới hạn tốc độ"},
                {"Từ gốc": "tour", "Cụm từ tiếng Anh": "go on/take a tour of/(a)round somewhere", "Nghĩa Tiếng Việt": "đi tham quan một vòng nơi nào đó"},
                {"Từ gốc": "tour", "Cụm từ tiếng Anh": "tour a place", "Nghĩa Tiếng Việt": "đi du lịch / tham quan một nơi"},
                {"Từ gốc": "tour", "Cụm từ tiếng Anh": "tour guide", "Nghĩa Tiếng Việt": "hướng dẫn viên du lịch"},
                {"Từ gốc": "trip", "Cụm từ tiếng Anh": "business trip", "Nghĩa Tiếng Việt": "chuyến công tác"},
                {"Từ gốc": "trip", "Cụm từ tiếng Anh": "school trip", "Nghĩa Tiếng Việt": "chuyến đi tham quan của trường"},
                {"Từ gốc": "trip", "Cụm từ tiếng Anh": "go on a trip", "Nghĩa Tiếng Việt": "đi tham quan / du lịch"},
                {"Từ gốc": "trip", "Cụm từ tiếng Anh": "take a trip (to a place)", "Nghĩa Tiếng Việt": "thực hiện một chuyến đi (tới đâu)"},
                {"Từ gốc": "way", "Cụm từ tiếng Anh": "lose/make/find your way", "Nghĩa Tiếng Việt": "lạc đường / tiến bước / tìm đường đi"},
                {"Từ gốc": "way", "Cụm từ tiếng Anh": "in a way", "Nghĩa Tiếng Việt": "theo một cách nào đó / ở một khía cạnh nào đó"},
                {"Từ gốc": "way", "Cụm từ tiếng Anh": "on the way", "Nghĩa Tiếng Việt": "trên đường đi"},
                {"Từ gốc": "way", "Cụm từ tiếng Anh": "go all the way (to sth/swh)", "Nghĩa Tiếng Việt": "đi tới tận nơi / đi suốt chặng đường"}
            ]
            st.table(pd.DataFrame(phrases_data))

        with tab_v4:
            st.markdown("#### 🔹 Word Patterns (Tách lẻ từng mẫu cấu trúc đi kèm)")
            patterns_data = [
                {"Từ gốc": "afraid", "Cấu trúc đi kèm": "afraid of sth/sb/doing", "Nghĩa Tiếng Việt": "sợ cái gì/ai/việc gì"},
                {"Từ gốc": "afraid", "Cấu trúc đi kèm": "afraid to do", "Nghĩa Tiếng Việt": "sợ không dám làm gì"},
                {"Từ gốc": "appear", "Cấu trúc đi kèm": "appear to be", "Nghĩa Tiếng Việt": "có vẻ như / dường như là"},
                {"Từ gốc": "arrange", "Cấu trúc đi kèm": "arrange sth (with sb)", "Nghĩa Tiếng Việt": "sắp xếp cái gì với ai"},
                {"Từ gốc": "arrange", "Cấu trúc đi kèm": "arrange for sb to do", "Nghĩa Tiếng Việt": "sắp xếp cho ai làm gì"},
                {"Từ gốc": "arrive", "Cấu trúc đi kèm": "arrive in/at a place", "Nghĩa Tiếng Việt": "đến (vùng, nước / địa điểm)"},
                {"Từ gốc": "arrive", "Cấu trúc đi kèm": "arrive here/there", "Nghĩa Tiếng Việt": "đến đây / đến đó"},
                {"Từ gốc": "continue", "Cấu trúc đi kèm": "continue sth/doing", "Nghĩa Tiếng Việt": "tiếp tục cái gì / làm gì"},
                {"Từ gốc": "continue", "Cấu trúc đi kèm": "continue to do", "Nghĩa Tiếng Việt": "tiếp tục làm gì"},
                {"Từ gốc": "continue", "Cấu trúc đi kèm": "continue with sth", "Nghĩa Tiếng Việt": "tiếp tục công việc/cái gì"},
                {"Từ gốc": "differ", "Cấu trúc đi kèm": "differ from sth/sb", "Nghĩa Tiếng Việt": "khác biệt so với cái gì/ai"},
                {"Từ gốc": "dream", "Cấu trúc đi kèm": "dream about/of sth/sb/doing", "Nghĩa Tiếng Việt": "mơ về cái gì/ai/việc gì"},
                {"Từ gốc": "invite", "Cấu trúc đi kèm": "invite sb to do", "Nghĩa Tiếng Việt": "mời ai làm gì"},
                {"Từ gốc": "keen", "Cấu trúc đi kèm": "keen to do", "Nghĩa Tiếng Việt": "muốn/thích làm gì"},
                {"Từ gốc": "keen", "Cấu trúc đi kèm": "keen on sth/sb/doing", "Nghĩa Tiếng Việt": "ham thích cái gì/ai/việc gì"},
                {"Từ gốc": "live", "Cấu trúc đi kèm": "live in/at a place", "Nghĩa Tiếng Việt": "sống ở nơi nào"},
                {"Từ gốc": "live", "Cấu trúc đi kèm": "live on/for sth", "Nghĩa Tiếng Việt": "sống nhờ vào / sống vì cái gì"},
                {"Từ gốc": "live", "Cấu trúc đi kèm": "live here/there", "Nghĩa Tiếng Việt": "sống ở đây / ở đó"},
                {"Từ gốc": "regret", "Cấu trúc đi kèm": "regret (not) doing", "Nghĩa Tiếng Việt": "hối hận vì đã (không) làm gì"},
                {"Từ gốc": "regret", "Cấu trúc đi kèm": "regret sth", "Nghĩa Tiếng Việt": "hối tiếc về điều gì"},
                {"Từ gốc": "regret", "Cấu trúc đi kèm": "regret to tell/inform you", "Nghĩa Tiếng Việt": "lấy làm tiếc phải thông báo với bạn"},
                {"Từ gốc": "think", "Cấu trúc đi kèm": "think of/about sth/sb/doing", "Nghĩa Tiếng Việt": "suy nghĩ về cái gì/ai/việc gì"},
                {"Từ gốc": "write", "Cấu trúc đi kèm": "write about sth/sb/doing", "Nghĩa Tiếng Việt": "viết về cái gì/ai/việc gì"},
                {"Từ gốc": "write", "Cấu trúc đi kèm": "write (sth) (to sb)", "Nghĩa Tiếng Việt": "viết (cái gì) cho ai"},
                {"Từ gốc": "write", "Cấu trúc đi kèm": "write sb sth", "Nghĩa Tiếng Việt": "viết cho ai cái gì"},
                {"Từ gốc": "write", "Cấu trúc đi kèm": "write sth down", "Nghĩa Tiếng Việt": "ghi chép lại cái gì"}
            ]
            st.table(pd.DataFrame(patterns_data))

        with tab_v5:
            st.markdown("#### 🔹 Word Formation (Tách lẻ từng từ biến đổi)")
            formation_data = [
                {"Từ gốc": "arrange (v)", "Từ biến đổi": "rearrange", "Từ loại": "v", "Nghĩa Tiếng Việt": "sắp xếp lại"},
                {"Từ gốc": "arrange (v)", "Từ biến đổi": "arrangement", "Từ loại": "n", "Nghĩa Tiếng Việt": "sự sắp xếp, thỏa thuận"},
                {"Từ gốc": "arrive (v)", "Từ biến đổi": "arrival", "Từ loại": "n", "Nghĩa Tiếng Việt": "sự đến nơi"},
                {"Từ gốc": "broad (adj)", "Từ biến đổi": "breadth", "Từ loại": "n", "Nghĩa Tiếng Việt": "bề rộng, bề ngang"},
                {"Từ gốc": "broad (adj)", "Từ biến đổi": "broaden", "Từ loại": "v", "Nghĩa Tiếng Việt": "mở rộng, làm rộng ra"},
                {"Từ gốc": "culture (n)", "Từ biến đổi": "cultural(ly)", "Từ loại": "adj/adv", "Nghĩa Tiếng Việt": "thuộc về văn hóa"},
                {"Từ gốc": "culture (n)", "Từ biến đổi": "(un)cultured", "Từ loại": "adj", "Nghĩa Tiếng Việt": "(không) có văn hóa, giáo dục"},
                {"Từ gốc": "differ (v)", "Từ biến đổi": "different(ly)", "Từ loại": "adj/adv", "Nghĩa Tiếng Việt": "khác biệt"},
                {"Từ gốc": "differ (v)", "Từ biến đổi": "difference", "Từ loại": "n", "Nghĩa Tiếng Việt": "sự khác biệt"},
                {"Từ gốc": "direct (adj/v)", "Từ biến đổi": "indirect", "Từ loại": "adj", "Nghĩa Tiếng Việt": "gián tiếp"},
                {"Từ gốc": "direct (adj/v)", "Từ biến đổi": "direction", "Từ loại": "n", "Nghĩa Tiếng Việt": "hướng đi, sự chỉ dẫn"},
                {"Từ gốc": "direct (adj/v)", "Từ biến đổi": "director", "Từ loại": "n", "Nghĩa Tiếng Việt": "giám đốc, đạo diễn"},
                {"Từ gốc": "direct (adj/v)", "Từ biến đổi": "(in)directly", "Từ loại": "adv", "Nghĩa Tiếng Việt": "(không) trực tiếp"},
                {"Từ gốc": "distant (adj)", "Từ biến đổi": "distantly", "Từ loại": "adv", "Nghĩa Tiếng Việt": "xa xăm, xa xôi"},
                {"Từ gốc": "distant (adj)", "Từ biến đổi": "distance", "Từ loại": "n", "Nghĩa Tiếng Việt": "khoảng cách"},
                {"Từ gốc": "enter (v)", "Từ biến đổi": "entrance", "Từ loại": "n", "Nghĩa Tiếng Việt": "lối vào, cổng vào"},
                {"Từ gốc": "inhabit (v)", "Từ biến đổi": "inhabitant", "Từ loại": "n", "Nghĩa Tiếng Việt": "cư dân, người sinh sống"},
                {"Từ gốc": "photograph (v/n)", "Từ biến đổi": "photography", "Từ loại": "n", "Nghĩa Tiếng Việt": "nhiếp ảnh, thuật chụp ảnh"},
                {"Từ gốc": "photograph (v/n)", "Từ biến đổi": "photographer", "Từ loại": "n", "Nghĩa Tiếng Việt": "nhiếp ảnh gia"},
                {"Từ gốc": "photograph (v/n)", "Từ biến đổi": "photographic", "Từ loại": "adj", "Nghĩa Tiếng Việt": "thuộc về nhiếp ảnh"},
                {"Từ gốc": "recognise (v)", "Từ biến đổi": "(un)recognisable", "Từ loại": "adj", "Nghĩa Tiếng Việt": "(không) thể nhận ra"},
                {"Từ gốc": "recognise (v)", "Từ biến đổi": "recognition", "Từ loại": "n", "Nghĩa Tiếng Việt": "sự nhận biết, sự công nhận"},
                {"Từ gốc": "time (n)", "Từ biến đổi": "timetable", "Từ loại": "n", "Nghĩa Tiếng Việt": "thời khóa biểu, lịch trình"},
                {"Từ gốc": "tour (v/n)", "Từ biến đổi": "tourism", "Từ loại": "n", "Nghĩa Tiếng Việt": "ngành du lịch"},
                {"Từ gốc": "tour (v/n)", "Từ biến đổi": "tourist", "Từ loại": "n", "Nghĩa Tiếng Việt": "khách du lịch"},
                {"Từ gốc": "world (n)", "Từ biến đổi": "worldwide", "Từ loại": "adj/adv", "Nghĩa Tiếng Việt": "toàn thế giới"}
            ]
            st.table(pd.DataFrame(formation_data))

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
            total_qs = 10
            st.markdown("### 📊 Kết quả Bài làm & Giải thích Chi tiết (Answer Key)")
            
            # QA1
            if qa1.strip().lower() in ["is taking", "'s taking"]:
                score += 1
                st.success("✅ Câu 1 đúng! (is taking) - Hành động đang diễn ra tại thời điểm nói ('at the moment').")
            elif qa1.strip() == "":
                st.warning("⚠️ Câu 1: Chưa trả lời / Bỏ trống. Đáp án đúng: **is taking** (Present Continuous cho hành động lúc nói).")
            else:
                st.error("❌ Câu 1 chưa chính xác! Đáp án đúng: **is taking** (Thì Hiện tại Tiếp diễn).")
                
            # QA2
            if qa2.strip().lower() in ["have you ever been", "have you ever gone"]:
                score += 1
                st.success("✅ Câu 2 đúng! (Have you ever been) - Hỏi về trải nghiệm ở thời điểm không xác định.")
            elif qa2.strip() == "":
                st.warning("⚠️ Câu 2: Chưa trả lời / Bỏ trống. Đáp án đúng: **Have you ever been**.")
            else:
                st.error("❌ Câu 2 chưa chính xác! Đáp án đúng: **Have you ever been**.")

            # QD1
            if qd1 == "ever":
                score += 1
                st.success("✅ Câu 5 đúng! (ever) - 'Have you ever dreamt...' hỏi trải nghiệm.")
            elif qd1 is None:
                st.warning("⚠️ Câu 5: Chưa trả lời / Bỏ trống. Đáp án đúng: **ever**.")
            else:
                st.error(f"❌ Câu 5 chưa chính xác! (Bạn chọn: {qd1}). Đáp án đúng: **ever**.")

            # QD2
            if qd2 == "yet":
                score += 1
                st.success("✅ Câu 6 đúng! (yet) - Dùng ở cuối câu phủ định 'haven't worked out... yet'.")
            elif qd2 is None:
                st.warning("⚠️ Câu 6: Chưa trả lời / Bỏ trống. Đáp án đúng: **yet**.")
            else:
                st.error(f"❌ Câu 6 chưa chính xác! Đáp án đúng: **yet**.")

            # QD3
            if qd3 == "since":
                score += 1
                st.success("✅ Câu 7 đúng! (since) - Đi kèm mốc thời gian 'he was born'.")
            elif qd3 is None:
                st.warning("⚠️ Câu 7: Chưa trả lời / Bỏ trống. Đáp án đúng: **since**.")
            else:
                st.error(f"❌ Câu 7 chưa chính xác! Đáp án đúng: **since**.")

            # QE1
            if qe1 == "C. I have got":
                score += 1
                st.success("✅ Câu 8 đúng! (C. I have got) - Cấu trúc 'It's/That's the first time + Present Perfect'.")
            elif qe1 is None:
                st.warning("⚠️ Câu 8: Chưa trả lời / Bỏ trống. Đáp án đúng: **C. I have got**.")
            else:
                st.error(f"❌ Câu 8 chưa chính xác! Đáp án đúng: **C. I have got**.")

            # QE2
            if qe2 == "B. has already":
                score += 1
                st.success("✅ Câu 9 đúng! (B. has already) - Vị trí trạng từ 'already' đứng giữa 'has' và V3/ed.")
            elif qe2 is None:
                st.warning("⚠️ Câu 9: Chưa trả lời / Bỏ trống. Đáp án đúng: **B. has already**.")
            else:
                st.error(f"❌ Câu 9 chưa chính xác! Đáp án đúng: **B. has already**.")

            # QG1
            if qg1 == "B. have been waiting":
                score += 1
                st.success("✅ Câu 10 đúng! (B. have been waiting) - Nhấn mạnh thời lượng tính liên tục 'for over an hour'.")
            elif qg1 is None:
                st.warning("⚠️ Câu 10: Chưa trả lời / Bỏ trống. Đáp án đúng: **B. have been waiting**.")
            else:
                st.error(f"❌ Câu 10 chưa chính xác! Đáp án đúng: **B. have been waiting**.")

            # QG2
            if qg2 == "A. have written":
                score += 1
                st.success("✅ Câu 11 đúng! (A. have written) - Nhấn mạnh kết quả con số cụ thể 'three letters'.")
            elif qg2 is None:
                st.warning("⚠️ Câu 11: Chưa trả lời / Bỏ trống. Đáp án đúng: **A. have written**.")
            else:
                st.error(f"❌ Câu 11 chưa chính xác! Đáp án đúng: **A. have written**.")

            # QI1
            if qi1.strip().lower() == "for":
                score += 1
                st.success("✅ Câu 12 đúng! (for) - 'for the last ten minutes' chỉ khoảng thời gian.")
            elif qi1.strip() == "":
                st.warning("⚠️ Câu 12: Chưa trả lời / Bỏ trống. Đáp án đúng: **for**.")
            else:
                st.error("❌ Câu 12 chưa chính xác! Đáp án đúng: **for**.")

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
        st.warning("⚠️ Thẻ ghi nhớ (Flashcards) chỉ dành riêng cho các Unit Từ vựng.")
    elif "Unit 2" in selected_fc_unit:
        st.subheader("🎴 Flashcards Unit 2: Travel and transport")
        
        unit2_cards = [
            # Topic Vocabulary
            {"word": "voyage (n)", "type": "Topic Vocabulary", "vi": "chuyến đi dài bằng đường biển / vũ trụ"},
            {"word": "journey (n)", "type": "Topic Vocabulary", "vi": "chuyến đi, hành trình"},
            {"word": "trip (n)", "type": "Topic Vocabulary", "vi": "chuyến đi ngắn (đi rồi về)"},
            {"word": "travel (n/v)", "type": "Topic Vocabulary", "vi": "sự đi lại / du lịch"},
            {"word": "excursion (n)", "type": "Topic Vocabulary", "vi": "chuyến tham quan, dã ngoại"},
            {"word": "view (n)", "type": "Topic Vocabulary", "vi": "quang cảnh, tầm nhìn"},
            {"word": "sight (n)", "type": "Topic Vocabulary", "vi": "cảnh trí / danh lam thắng cảnh"},
            {"word": "world (n)", "type": "Topic Vocabulary", "vi": "thế giới"},
            {"word": "earth (n)", "type": "Topic Vocabulary", "vi": "trái đất, mặt đất"},
            {"word": "area (n)", "type": "Topic Vocabulary", "vi": "vùng, khu vực"},
            {"word": "territory (n)", "type": "Topic Vocabulary", "vi": "lãnh thổ"},
            {"word": "season (n)", "type": "Topic Vocabulary", "vi": "mùa trong năm"},
            {"word": "period (n)", "type": "Topic Vocabulary", "vi": "thời kỳ, khoảng thời gian"},
            {"word": "fare (n)", "type": "Topic Vocabulary", "vi": "tiền xe, vé xe/tàu/máy bay"},
            {"word": "ticket (n)", "type": "Topic Vocabulary", "vi": "vé (xem phim, vào cửa, đi lại)"},
            {"word": "fee (n)", "type": "Topic Vocabulary", "vi": "lệ phí, phí dịch vụ"},
            {"word": "miss (v)", "type": "Topic Vocabulary", "vi": "nhỡ, bỏ lỡ (xe, tàu)"},
            {"word": "lose (v)", "type": "Topic Vocabulary", "vi": "đánh mất, thất lạc"},
            {"word": "take (v)", "type": "Topic Vocabulary", "vi": "đưa đi, mang đi"},
            {"word": "bring (v)", "type": "Topic Vocabulary", "vi": "mang lại, cầm lại"},
            {"word": "go (v)", "type": "Topic Vocabulary", "vi": "đi (tới một nơi)"},
            {"word": "book (v)", "type": "Topic Vocabulary", "vi": "đặt trước (vé, phòng)"},
            {"word": "keep (v)", "type": "Topic Vocabulary", "vi": "giữ, duy trì"},
            {"word": "arrive (v)", "type": "Topic Vocabulary", "vi": "đến nơi (đi kèm in/at)"},
            {"word": "reach (v)", "type": "Topic Vocabulary", "vi": "đến, đạt tới (không cần giới từ)"},
            {"word": "live (v)", "type": "Topic Vocabulary", "vi": "sống, cư trú lâu dài"},
            {"word": "stay (v)", "type": "Topic Vocabulary", "vi": "ở lại, ở tạm"},
            {"word": "border (n)", "type": "Topic Vocabulary", "vi": "biên giới"},
            {"word": "edge (n)", "type": "Topic Vocabulary", "vi": "mép, rìa"},
            {"word": "line (n)", "type": "Topic Vocabulary", "vi": "đường kẻ, ranh giới"},
            {"word": "length (n)", "type": "Topic Vocabulary", "vi": "chiều dài, độ dài"},
            {"word": "distance (n)", "type": "Topic Vocabulary", "vi": "khoảng cách"},
            {"word": "guide (v)", "type": "Topic Vocabulary", "vi": "dẫn đường, hướng dẫn"},
            {"word": "lead (v)", "type": "Topic Vocabulary", "vi": "dẫn dắt, đi đầu"},
            {"word": "native (adj)", "type": "Topic Vocabulary", "vi": "bản địa, tự nhiên từ khi sinh ra"},
            {"word": "home (town) (n)", "type": "Topic Vocabulary", "vi": "quê nhà, nơi sinh sống gắn bó"},
            
            # Phrasal Verbs
            {"word": "catch up with", "type": "Phrasal Verbs", "vi": "theo kịp, đuổi kịp"},
            {"word": "check in", "type": "Phrasal Verbs", "vi": "làm thủ tục nhận phòng / lên máy bay"},
            {"word": "check out", "type": "Phrasal Verbs", "vi": "làm thủ tục trả phòng / điều tra"},
            {"word": "drop off", "type": "Phrasal Verbs", "vi": "thả ai xuống xe / ngủ gật"},
            {"word": "get back", "type": "Phrasal Verbs", "vi": "trở về (từ một chuyến đi)"},
            {"word": "go away", "type": "Phrasal Verbs", "vi": "đi nghỉ mát / đi xa"},
            {"word": "keep up with", "type": "Phrasal Verbs", "vi": "theo kịp, giữ cùng tốc độ/trình độ với"},
            {"word": "make for", "type": "Phrasal Verbs", "vi": "đi về hướng, tiến về phía"},
            {"word": "pick up", "type": "Phrasal Verbs", "vi": "đón ai bằng xe"},
            {"word": "pull in", "type": "Phrasal Verbs", "vi": "tấp xe vào lề đường"},
            {"word": "run over", "type": "Phrasal Verbs", "vi": "tông/cán qua (bằng xe)"},
            {"word": "see off", "type": "Phrasal Verbs", "vi": "tiễn ai lên đường"},
            {"word": "set out/off", "type": "Phrasal Verbs", "vi": "khởi hành chuyến đi"},
            {"word": "take off", "type": "Phrasal Verbs", "vi": "cất cánh (máy bay)"},
            {"word": "turn round", "type": "Phrasal Verbs", "vi": "quay ngược lại, quay đầu"},

            # Phrases & Collocations
            {"word": "have an accident", "type": "Phrases & Collocations", "vi": "gặp tai nạn"},
            {"word": "be (involved) in an accident", "type": "Phrases & Collocations", "vi": "bị tai nạn / liên quan đến tai nạn"},
            {"word": "do sth by accident", "type": "Phrases & Collocations", "vi": "vô tình / tình cờ làm gì"},
            {"word": "in advance", "type": "Phrases & Collocations", "vi": "trước, sớm (về thời gian)"},
            {"word": "advance to/towards a place", "type": "Phrases & Collocations", "vi": "tiến về phía một nơi"},
            {"word": "go straight ahead", "type": "Phrases & Collocations", "vi": "đi thẳng về phía trước"},
            {"word": "go ahead", "type": "Phrases & Collocations", "vi": "tiến lên / tiếp tục"},
            {"word": "be ahead of sth/sb", "type": "Phrases & Collocations", "vi": "dẫn trước / đi trước ai/cái gì"},
            {"word": "a change of direction", "type": "Phrases & Collocations", "vi": "sự đổi hướng"},
            {"word": "in the direction of sth", "type": "Phrases & Collocations", "vi": "theo hướng của cái gì"},
            {"word": "in this/that direction", "type": "Phrases & Collocations", "vi": "theo hướng này/đó"},
            {"word": "off the top of your head", "type": "Phrases & Collocations", "vi": "theo phản xạ / không cần suy nghĩ kỹ"},
            {"word": "head for/towards a place", "type": "Phrases & Collocations", "vi": "đi về phía / hướng về một nơi"},
            {"word": "head over heels (in love)", "type": "Phrases & Collocations", "vi": "yêu say đắm"},
            {"word": "go/be on holiday", "type": "Phrases & Collocations", "vi": "đi/đang nghỉ mát"},
            {"word": "have/take a holiday", "type": "Phrases & Collocations", "vi": "có/nghỉ một kỳ nghỉ"},
            {"word": "bank holiday", "type": "Phrases & Collocations", "vi": "ngày nghỉ lễ chính thức"},
            {"word": "go/turn/etc left", "type": "Phrases & Collocations", "vi": "rẽ/đi sang bên trái"},
            {"word": "on the left", "type": "Phrases & Collocations", "vi": "ở bên trái"},
            {"word": "on the left-hand side", "type": "Phrases & Collocations", "vi": "ở phía bên tay trái"},
            {"word": "in the left-hand corner", "type": "Phrases & Collocations", "vi": "ở góc bên tay trái"},
            {"word": "left-handed", "type": "Phrases & Collocations", "vi": "thuận tay trái"},
            {"word": "plan your/a route", "type": "Phrases & Collocations", "vi": "lên lịch trình / vạch ra tuyến đường"},
            {"word": "take a route", "type": "Phrases & Collocations", "vi": "đi theo một tuyến đường"},
            {"word": "see the sights", "type": "Phrases & Collocations", "vi": "ngắm cảnh / tham quan danh lam thắng cảnh"},
            {"word": "go sightseeing", "type": "Phrases & Collocations", "vi": "đi tham quan ngắm cảnh"},
            {"word": "at (high/full/etc) speed", "type": "Phrases & Collocations", "vi": "ở tốc độ (cao/tối đa...)"},
            {"word": "a burst of speed", "type": "Phrases & Collocations", "vi": "sự tăng tốc đột ngột"},
            {"word": "speed limit", "type": "Phrases & Collocations", "vi": "giới hạn tốc độ"},
            {"word": "go on/take a tour of/(a)round somewhere", "type": "Phrases & Collocations", "vi": "đi tham quan một vòng nơi nào"},
            {"word": "tour a place", "type": "Phrases & Collocations", "vi": "đi du lịch / tham quan một nơi"},
            {"word": "tour guide", "type": "Phrases & Collocations", "vi": "hướng dẫn viên du lịch"},
            {"word": "business trip", "type": "Phrases & Collocations", "vi": "chuyến công tác"},
            {"word": "school trip", "type": "Phrases & Collocations", "vi": "chuyến đi tham quan của trường"},
            {"word": "go on a trip", "type": "Phrases & Collocations", "vi": "đi tham quan / du lịch"},
            {"word": "take a trip (to a place)", "type": "Phrases & Collocations", "vi": "thực hiện một chuyến đi (tới đâu)"},
            {"word": "lose/make/find your way", "type": "Phrases & Collocations", "vi": "lạc đường / tiến bước / tìm đường đi"},
            {"word": "in a way", "type": "Phrases & Collocations", "vi": "theo một cách nào đó"},
            {"word": "on the way", "type": "Phrases & Collocations", "vi": "trên đường đi"},
            {"word": "go all the way (to sth/swh)", "type": "Phrases & Collocations", "vi": "đi tới tận nơi / đi suốt chặng đường"},

            # Word Patterns
            {"word": "afraid of sth/sb/doing", "type": "Word Patterns", "vi": "sợ cái gì/ai/việc gì"},
            {"word": "afraid to do", "type": "Word Patterns", "vi": "sợ không dám làm gì"},
            {"word": "appear to be", "type": "Word Patterns", "vi": "có vẻ như / dường như là"},
            {"word": "arrange sth (with sb)", "type": "Word Patterns", "vi": "sắp xếp cái gì với ai"},
            {"word": "arrange for sb to do", "type": "Word Patterns", "vi": "sắp xếp cho ai làm gì"},
            {"word": "arrive in/at a place", "type": "Word Patterns", "vi": "đến (vùng, nước / địa điểm)"},
            {"word": "arrive here/there", "type": "Word Patterns", "vi": "đến đây / đến đó"},
            {"word": "continue sth/doing", "type": "Word Patterns", "vi": "tiếp tục cái gì / làm gì"},
            {"word": "continue to do", "type": "Word Patterns", "vi": "tiếp tục làm gì"},
            {"word": "continue with sth", "type": "Word Patterns", "vi": "tiếp tục công việc/cái gì"},
            {"word": "differ from sth/sb", "type": "Word Patterns", "vi": "khác biệt so với cái gì/ai"},
            {"word": "dream about/of sth/sb/doing", "type": "Word Patterns", "vi": "mơ về cái gì/ai/việc gì"},
            {"word": "invite sb to do", "type": "Word Patterns", "vi": "mời ai làm gì"},
            {"word": "keen to do", "type": "Word Patterns", "vi": "muốn/thích làm gì"},
            {"word": "keen on sth/sb/doing", "type": "Word Patterns", "vi": "ham thích cái gì/ai/việc gì"},
            {"word": "live in/at a place", "type": "Word Patterns", "vi": "sống ở nơi nào"},
            {"word": "live on/for sth", "type": "Word Patterns", "vi": "sống nhờ vào / sống vì cái gì"},
            {"word": "live here/there", "type": "Word Patterns", "vi": "sống ở đây / ở đó"},
            {"word": "regret (not) doing", "type": "Word Patterns", "vi": "hối hận vì đã (không) làm gì"},
            {"word": "regret sth", "type": "Word Patterns", "vi": "hối tiếc về điều gì"},
            {"word": "regret to tell/inform you", "type": "Word Patterns", "vi": "lấy làm tiếc phải thông báo với bạn"},
            {"word": "think of/about sth/sb/doing", "type": "Word Patterns", "vi": "suy nghĩ về cái gì/ai/việc gì"},
            {"word": "write about sth/sb/doing", "type": "Word Patterns", "vi": "viết về cái gì/ai/việc gì"},
            {"word": "write (sth) (to sb)", "type": "Word Patterns", "vi": "viết (cái gì) cho ai"},
            {"word": "write sb sth", "type": "Word Patterns", "vi": "viết cho ai cái gì"},
            {"word": "write sth down", "type": "Word Patterns", "vi": "ghi chép lại cái gì"},

            # Word Formation
            {"word": "arrange (v) ➔ rearrange (v)", "type": "Word Formation", "vi": "sắp xếp ➔ sắp xếp lại"},
            {"word": "arrange (v) ➔ arrangement (n)", "type": "Word Formation", "vi": "sắp xếp ➔ sự sắp xếp, thỏa thuận"},
            {"word": "arrive (v) ➔ arrival (n)", "type": "Word Formation", "vi": "đến nơi ➔ sự đến nơi"},
            {"word": "broad (adj) ➔ breadth (n)", "type": "Word Formation", "vi": "rộng ➔ bề rộng, bề ngang"},
            {"word": "broad (adj) ➔ broaden (v)", "type": "Word Formation", "vi": "rộng ➔ mở rộng, làm rộng ra"},
            {"word": "culture (n) ➔ cultural(ly) (adj/adv)", "type": "Word Formation", "vi": "văn hóa ➔ thuộc về văn hóa"},
            {"word": "culture (n) ➔ (un)cultured (adj)", "type": "Word Formation", "vi": "văn hóa ➔ (không) có văn hóa"},
            {"word": "differ (v) ➔ different(ly) (adj/adv)", "type": "Word Formation", "vi": "khác biệt ➔ khác biệt"},
            {"word": "differ (v) ➔ difference (n)", "type": "Word Formation", "vi": "khác biệt ➔ sự khác biệt"},
            {"word": "direct (adj/v) ➔ indirect (adj)", "type": "Word Formation", "vi": "trực tiếp ➔ gián tiếp"},
            {"word": "direct (adj/v) ➔ direction (n)", "type": "Word Formation", "vi": "chỉ đường ➔ hướng đi, sự chỉ dẫn"},
            {"word": "direct (adj/v) ➔ director (n)", "type": "Word Formation", "vi": "chỉ đạo ➔ giám đốc, đạo diễn"},
            {"word": "direct (adj/v) ➔ (in)directly (adv)", "type": "Word Formation", "vi": "trực tiếp ➔ (không) trực tiếp"},
            {"word": "distant (adj) ➔ distantly (adv)", "type": "Word Formation", "vi": "xa xôi ➔ xa xăm"},
            {"word": "distant (adj) ➔ distance (n)", "type": "Word Formation", "vi": "xa xôi ➔ khoảng cách"},
            {"word": "enter (v) ➔ entrance (n)", "type": "Word Formation", "vi": "đi vào ➔ lối vào, cổng vào"},
            {"word": "inhabit (v) ➔ inhabitant (n)", "type": "Word Formation", "vi": "sinh sống ➔ cư dân, người sinh sống"},
            {"word": "photograph (v/n) ➔ photography (n)", "type": "Word Formation", "vi": "chụp ảnh ➔ nhiếp ảnh"},
            {"word": "photograph (v/n) ➔ photographer (n)", "type": "Word Formation", "vi": "chụp ảnh ➔ nhiếp ảnh gia"},
            {"word": "photograph (v/n) ➔ photographic (adj)", "type": "Word Formation", "vi": "chụp ảnh ➔ thuộc về nhiếp ảnh"},
            {"word": "recognise (v) ➔ (un)recognisable (adj)", "type": "Word Formation", "vi": "nhận ra ➔ (không) thể nhận ra"},
            {"word": "recognise (v) ➔ recognition (n)", "type": "Word Formation", "vi": "nhận ra ➔ sự nhận biết, công nhận"},
            {"word": "time (n) ➔ timetable (n)", "type": "Word Formation", "vi": "thời gian ➔ thời khóa biểu, lịch trình"},
            {"word": "tour (v/n) ➔ tourism (n)", "type": "Word Formation", "vi": "du lịch ➔ ngành du lịch"},
            {"word": "tour (v/n) ➔ tourist (n)", "type": "Word Formation", "vi": "du lịch ➔ khách du lịch"},
            {"word": "world (n) ➔ worldwide (adj/adv)", "type": "Word Formation", "vi": "thế giới ➔ toàn thế giới"}
        ]

        categories = ["Tất cả", "Topic Vocabulary", "Phrasal Verbs", "Phrases & Collocations", "Word Patterns", "Word Formation"]
        selected_cat = st.selectbox("📂 Lọc theo phân loại từ vựng:", categories)

        if selected_cat != "Tất cả":
            filtered_cards = [c for c in unit2_cards if c["type"] == selected_cat]
        else:
            filtered_cards = unit2_cards

        if "fc_index" not in st.session_state:
            st.session_state.fc_index = 0
        if "fc_show_back" not in st.session_state:
            st.session_state.fc_show_back = False

        if st.session_state.fc_index >= len(filtered_cards):
            st.session_state.fc_index = 0

        curr_card = filtered_cards[st.session_state.fc_index]

        col_fc1, col_fc2, col_fc3 = st.columns([1, 3, 1])

        with col_fc2:
            st.markdown(f"**📌 Phân loại:** `{curr_card['type']}` | **Thẻ:** `{st.session_state.fc_index + 1} / {len(filtered_cards)}`")
            
            if not st.session_state.fc_show_back:
                st.markdown(f"""
                <div class="flashcard-box">
                    <div class="card-title">{curr_card['word']}</div>
                    <div class="card-sub"><i>(Nhấn 'Lật thẻ' để xem nghĩa tiếng Việt)</i></div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="flashcard-back">
                    <div class="card-title">{curr_card['vi']}</div>
                    <div class="card-sub"><b>{curr_card['word']}</b> ({curr_card['type']})</div>
                </div>
                """, unsafe_allow_html=True)

            btn_prev, btn_flip, btn_next = st.columns([1, 1, 1])
            with btn_prev:
                if st.button("⬅️ Thẻ trước", use_container_width=True):
                    if st.session_state.fc_index > 0:
                        st.session_state.fc_index -= 1
                    else:
                        st.session_state.fc_index = len(filtered_cards) - 1
                    st.session_state.fc_show_back = False
                    st.rerun()

            with btn_flip:
                if st.button("🔄 Lật thẻ", use_container_width=True):
                    st.session_state.fc_show_back = not st.session_state.fc_show_back
                    st.rerun()

            with btn_next:
                if st.button("➡️ Thẻ sau", use_container_width=True):
                    if st.session_state.fc_index < len(filtered_cards) - 1:
                        st.session_state.fc_index += 1
                    else:
                        st.session_state.fc_index = 0
                    st.session_state.fc_show_back = False
                    st.rerun()

    else:
        st.info(f"Thẻ ghi nhớ (Flashcards) cho **{selected_fc_unit}** đang được hoàn thiện.")

# --- 5. GÓC LƯU Ý (WATCH OUT! CORNER) ---
elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý B2 (Watch Out! Corner)")
    
    selected_wo_unit = st.selectbox("🎯 Chọn Unit xem bẫy ngữ pháp & từ vựng:", ALL_UNITS_LIST)
    
    if "Unit 1" in selected_wo_unit:
        st.subheader("⚠️ Watch Out! Unit 1: Present time")
        st.markdown("""
        <div class="watchout-box">
        <b>1. Phân biệt Present Perfect Simple & Continuous:</b><br>
        • <i>Present Perfect Simple</i> nhấn mạnh vào **KẾT QUẢ / SỐ LƯỢNG**: <i>I've written three essays today.</i><br>
        • <i>Present Perfect Continuous</i> nhấn mạnh vào **THỜI LƯỢNG / TÍNH LIÊN TỤC**: <i>I've been writing essays all morning.</i>
        </div>
        
        <div class="watchout-box">
        <b>2. Động từ Trạng thái (Stative Verbs) đa nghĩa:</b><br>
        • <i>I <b>think</b> this is a great idea.</i> (Trạng thái: suy nghĩ/quan điểm ➔ không dùng Continuous)<br>
        • <i>I'm <b>thinking</b> about going to Paris.</i> (Hành động: đang cân nhắc ➔ dùng Continuous)
        </div>
        """, unsafe_allow_html=True)
    elif "Unit 2" in selected_wo_unit:
        st.subheader("⚠️ Watch Out! Unit 2: Travel and transport")
        st.markdown("""
        <div class="watchout-box">
        <b>1. Phân biệt các từ chỉ chuyến đi:</b><br>
        • <b>voyage:</b> chuyến đi dài trên biển / vũ trụ.<br>
        • <b>journey:</b> hành trình dài (thường một chiều).<br>
        • <b>trip:</b> chuyến đi ngắn có quay về.<br>
        • <b>excursion:</b> chuyến tham quan, dã ngoại ngắn ngày.
        </div>
        
        <div class="watchout-box">
        <b>2. Giới từ đi kèm động từ di chuyển:</b><br>
        • <b>arrive IN</b> + quốc gia, thành phố lớn (e.g., <i>arrive in London</i>).<br>
        • <b>arrive AT</b> + địa điểm cụ thể (e.g., <i>arrive at the station / airport</i>).<br>
        • <b>reach</b> + địa điểm (KHÔNG dùng giới từ).
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info(f"Các góc lưu ý bẫy đề thi cho **{selected_wo_unit}** đang được tổng hợp.")

# --- 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập (Progress Report)")
    
    st.markdown("""
    Đánh dấu các bài học bạn đã hoàn thành để hệ thống theo dõi tiến độ tổng thể khóa học B2 của bạn:
    """)
    
    col_p1, col_p2 = st.columns(2)
    
    completed_count = 0
    total_items = len(ALL_UNITS_LIST)
    
    with col_p1:
        st.subheader("✅ Danh sách 28 Units & 14 Reviews:")
        for idx, u_name in enumerate(ALL_UNITS_LIST):
            chk_key = f"prog_{idx}"
            checked = st.checkbox(u_name, key=chk_key)
            if checked:
                completed_count += 1

    with col_p2:
        st.subheader("📈 Tiến độ hoàn thành toàn bộ khóa học B2:")
        progress_pct = completed_count / total_items
        st.progress(progress_pct)
        st.metric(label="Tỷ lệ hoàn thành", value=f"{int(progress_pct * 100)}%", delta=f"{completed_count}/{total_items} mục")
        
        if progress_pct == 1.0:
            st.balloons()
            st.success("🎉 Chúc mừng! Bạn đã hoàn thành 100% chương trình tự học Destination B2!")

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Destination B2 Self-Study Hub",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
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

# ALL 28 UNITS & 14 REVIEWS
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
        Sách gồm **28 Units** đan xen giữa Ngữ pháp và Từ vựng nâng cao, cùng hệ thống bài ôn tập đáp ứng chuẩn đầu ra kỳ thi **Cambridge FCE (B2 Vantage Level)**:
        * **14 Unit Ngữ pháp (Grammar Units)**: Hệ thống quy tắc chuyên sâu, cấu trúc câu nâng cao và các ngoại lệ.
        * **14 Unit Từ vựng (Vocabulary Units)**: Phân loại từ vựng theo chủ đề (*Topic Vocabulary in contrast*), Cụm động từ (*Phrasal Verbs*), Cụm từ cố định (*Phrases and Collocations*), Cấu trúc từ (*Word Patterns*) và Cấu tạo từ (*Word Formation*).
        * **14 Bài Ôn tập (Reviews)**: Ôn tập định kỳ sau mỗi 2 Units.
        * **2 Bài Kiểm tra Tiến độ (Progress Tests)**: Progress Test 1 (Units 1–14) & Progress Test 2 (Units 15–28).
        """)
        
        st.markdown("""
        ### 🗺️ Lộ trình tự học:
        * **Bước 1 (Theory Hub)**: Nắm vững bảng lý thuyết ngữ pháp và danh mục từ vựng chuẩn Cambridge B2.
        * **Bước 2 (Watch Out! Corner)**: Điểm lại các bẫy ngữ pháp và lỗi sai phổ biến mà thí sinh B2 thường mắc phải.
        * **Bước 3 (Interactive Quiz)**: Luyện tập bài tập tương tác, kiểm tra đáp án tự động và đọc giải thích chi tiết (cho cả câu đúng, câu sai và câu chưa làm).
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

    elif "Unit 2" in selected_unit:
        st.subheader("Unit 2: Vocabulary - Travel and transport")
        st.caption("Tra cứu chi tiết từng Từ vựng, Phrasal Verbs, Phrases & Collocations, Word Patterns và Word Formation kèm IPA, Định nghĩa Tiếng Anh & Nghĩa Tiếng Việt (Glossary Destination B2):")
        
        tab_v1, tab_v2, tab_v3, tab_v4, tab_v5 = st.tabs([
            "1. Topic Vocabulary in Contrast",
            "2. Phrasal Verbs",
            "3. Phrases & Collocations",
            "4. Word Patterns",
            "5. Word Formation"
        ])
        
        with tab_v1:
            st.markdown("#### 📚 Topic Vocabulary in Contrast (Phân biệt Từ vựng Chủ đề)")
            unit2_topic_vocab = [
                {"Từ vựng": "voyage (n)", "IPA": "/ˈvɔɪ.ɪdʒ/", "Định nghĩa Tiếng Anh (Glossary)": "a long journey, especially on a ship", "Nghĩa Tiếng Việt": "chuyến đi dài bằng đường biển", "Ví dụ": "It was a long voyage from London to New York."},
                {"Từ vựng": "journey (n)", "IPA": "/ˈdʒɜː.ni/", "Định nghĩa Tiếng Anh (Glossary)": "an occasion when you travel from one place to another, especially over a long distance", "Nghĩa Tiếng Việt": "hành trình, chuyến đi", "Ví dụ": "We had a long journey ahead of us."},
                {"Từ vựng": "trip (n)", "IPA": "/trɪp/", "Định nghĩa Tiếng Anh (Glossary)": "an occasion when you go somewhere and come back again", "Nghĩa Tiếng Việt": "chuyến đi ngắn (đi rồi về)", "Ví dụ": "The whole family went on a trip to Florida."},
                {"Từ vựng": "travel (n)", "IPA": "/ˈtræv.əl/", "Định nghĩa Tiếng Anh (Glossary)": "the activity of travelling in general", "Nghĩa Tiếng Việt": "sự đi lại, việc du lịch", "Ví dụ": "Foreign travel never really appealed to him until he retired."},
                {"Từ vựng": "excursion (n)", "IPA": "/ɪkˈskɜː.ʃən/", "Định nghĩa Tiếng Anh (Glossary)": "a short journey that you make for pleasure", "Nghĩa Tiếng Việt": "chuyến tham quan, dã ngoại", "Ví dụ": "My grandmother often talks about excursions to the sea."},
                {"Từ vựng": "view (n)", "IPA": "/vjuː/", "Định nghĩa Tiếng Anh (Glossary)": "the things that you can see from a particular place", "Nghĩa Tiếng Việt": "quang cảnh, tầm nhìn", "Ví dụ": "We had a spectacular view of the mountains from our room."},
                {"Từ vựng": "sight (n)", "IPA": "/saɪt/", "Định nghĩa Tiếng Anh (Glossary)": "a person or a thing that you see that has a particular feature / famous place", "Nghĩa Tiếng Việt": "cảnh tượng, thắng cảnh", "Ví dụ": "Windmills are a common sight in this part of the country."},
                {"Từ vựng": "world (n)", "IPA": "/wɜːld/", "Định nghĩa Tiếng Anh (Glossary)": "the planet that we live on", "Nghĩa Tiếng Việt": "thế giới, hành tinh", "Ví dụ": "It's easy these days to communicate with people who live on the other side of the world."},
                {"Từ vựng": "earth (n)", "IPA": "/ɜːθ/", "Định nghĩa Tiếng Anh (Glossary)": "the land on which we live / soil", "Nghĩa Tiếng Việt": "trái đất, mặt đất", "Ví dụ": "They felt the earth shake during the earthquake."},
                {"Từ vựng": "area (n)", "IPA": "/ˈeə.ri.ə/", "Định nghĩa Tiếng Anh (Glossary)": "a part of a place or building", "Nghĩa Tiếng Việt": "khu vực, vùng", "Ví dụ": "Bus services in rural areas are not very good."},
                {"Từ vựng": "territory (n)", "IPA": "/ˈter.ɪ.tər.i/", "Định nghĩa Tiếng Anh (Glossary)": "an area of land that is controlled by a particular country, leader or army", "Nghĩa Tiếng Việt": "lãnh thổ", "Ví dụ": "Russian troops crossed into Austrian territory in February 1849."},
                {"Từ vựng": "season (n)", "IPA": "/ˈsiː.zən/", "Định nghĩa Tiếng Anh (Glossary)": "one of the four periods into which the year is divided", "Nghĩa Tiếng Việt": "mùa trong năm", "Ví dụ": "She likes to paint the changing seasons in the garden."},
                {"Từ vựng": "period (n)", "IPA": "/ˈpɪə.ri.əd/", "Định nghĩa Tiếng Anh (Glossary)": "an amount of time", "Nghĩa Tiếng Việt": "giai đoạn, khoảng thời gian", "Ví dụ": "The long dry period ended with heavy rain."},
                {"Từ vựng": "fare (n)", "IPA": "/feər/", "Định nghĩa Tiếng Anh (Glossary)": "the money that you pay for a journey", "Nghĩa Tiếng Việt": "tiền vé xe, tàu, máy bay", "Ví dụ": "The fare from York to Leeds has gone up."},
                {"Từ vựng": "ticket (n)", "IPA": "/ˈtɪk.ɪt/", "Định nghĩa Tiếng Anh (Glossary)": "a piece of paper that shows that you have paid for a journey, event...", "Nghĩa Tiếng Việt": "vé", "Ví dụ": "We'll send your tickets a week before your flight."},
                {"Từ vựng": "fee (n)", "IPA": "/fiː/", "Định nghĩa Tiếng Anh (Glossary)": "an amount of money that you pay to do something or for a professional service", "Nghĩa Tiếng Việt": "lệ phí, phí dịch vụ", "Ví dụ": "The gallery charges a small entrance fee."},
                {"Từ vựng": "miss (v)", "IPA": "/mɪs/", "Định nghĩa Tiếng Anh (Glossary)": "to be too late for something such as a train or bus", "Nghĩa Tiếng Việt": "nhỡ, bỏ lỡ (xe/tàu)", "Ví dụ": "I missed the last train home again."},
                {"Từ vựng": "lose (v)", "IPA": "/luːz/", "Định nghĩa Tiếng Anh (Glossary)": "to no longer have something", "Nghĩa Tiếng Việt": "mất, thất lạc", "Ví dụ": "Mike lost his job last year."},
                {"Từ vựng": "take (v)", "IPA": "/teɪk/", "Định nghĩa Tiếng Anh (Glossary)": "to move or carry someone or something from one place to another", "Nghĩa Tiếng Việt": "đưa đi, dẫn đi", "Ví dụ": "What time do you take Amy to school?"},
                {"Từ vựng": "bring (v)", "IPA": "/brɪŋ/", "Định nghĩa Tiếng Anh (Glossary)": "to take someone or something with you from one place to another", "Nghĩa Tiếng Việt": "mang đến, đem lại", "Ví dụ": "Bring a coat in case it turns cold."},
                {"Từ vựng": "go (v)", "IPA": "/ɡəʊ/", "Định nghĩa Tiếng Anh (Glossary)": "to move or travel to a place", "Nghĩa Tiếng Việt": "đi", "Ví dụ": "We're planning to go to Spain this winter."},
                {"Từ vựng": "book (v)", "IPA": "/bʊk/", "Định nghĩa Tiếng Anh (Glossary)": "to arrange to have or use something at a particular time in the future", "Nghĩa Tiếng Việt": "đặt chỗ, đặt vé", "Ví dụ": "Shall I book a room for you?"},
                {"Từ vựng": "keep (v)", "IPA": "/kiːp/", "Định nghĩa Tiếng Anh (Glossary)": "to continue to have or own something", "Nghĩa Tiếng Việt": "giữ, duy trì", "Ví dụ": "We should keep this car and sell the other one."},
                {"Từ vựng": "arrive (v)", "IPA": "/əˈraɪv/", "Định nghĩa Tiếng Anh (Glossary)": "to reach a place", "Nghĩa Tiếng Việt": "đến nơi (arrive in/at)", "Ví dụ": "What time does your plane arrive?"},
                {"Từ vựng": "reach (v)", "IPA": "/riːtʃ/", "Định nghĩa Tiếng Anh (Glossary)": "to arrive somewhere", "Nghĩa Tiếng Việt": "tới, đạt tới (reach + destination)", "Ví dụ": "We hoped to reach the camp before dark."},
                {"Từ vựng": "live (v)", "IPA": "/lɪv/", "Định nghĩa Tiếng Anh (Glossary)": "to have your home in a particular place", "Nghĩa Tiếng Việt": "sống, cư trú lâu dài", "Ví dụ": "How long is he planning to stay with you?"},
                {"Từ vựng": "stay (v)", "IPA": "/steɪ/", "Định nghĩa Tiếng Anh (Glossary)": "to live or remain in a place for a short time as a guest", "Nghĩa Tiếng Việt": "ở lại, trọ lại tạm thời", "Ví dụ": "We stayed in a hotel near the beach."},
                {"Từ vựng": "border (n)", "IPA": "/ˈbɔː.dər/", "Định nghĩa Tiếng Anh (Glossary)": "the official line that separates two countries or regions", "Nghĩa Tiếng Việt": "biên giới", "Ví dụ": "Thousands of refugees were fleeing across the border."},
                {"Từ vựng": "edge (n)", "IPA": "/edʒ/", "Định nghĩa Tiếng Anh (Glossary)": "the part of something that is furthest from its centre", "Nghĩa Tiếng Việt": "mép, rìa", "Ví dụ": "Victoria was sitting on the edge of the bed."},
                {"Từ vựng": "line (n)", "IPA": "/laɪn/", "Định nghĩa Tiếng Anh (Glossary)": "a long thin mark on the surface of something", "Nghĩa Tiếng Việt": "đường ranh giới, vạch kẻ", "Ví dụ": "Draw a straight line."},
                {"Từ vựng": "length (n)", "IPA": "/leŋθ/", "Định nghĩa Tiếng Anh (Glossary)": "a measurement of how long something is", "Nghĩa Tiếng Việt": "chiều dài, độ dài", "Ví dụ": "The boat was 16 feet in length."},
                {"Từ vựng": "distance (n)", "IPA": "/ˈdɪs.təns/", "Định nghĩa Tiếng Anh (Glossary)": "the amount of space between two people or things", "Nghĩa Tiếng Việt": "khoảng cách", "Ví dụ": "They started to walk the short distance to the camp."},
                {"Từ vựng": "guide (v)", "IPA": "/ɡaɪd/", "Định nghĩa Tiếng Anh (Glossary)": "to show someone where to go by going with them", "Nghĩa Tiếng Việt": "hướng dẫn, dẫn đường", "Ví dụ": "He guided them through the forest."},
                {"Từ vựng": "lead (v)", "IPA": "/liːd/", "Định nghĩa Tiếng Anh (Glossary)": "to take someone to a place by going with them, usually in front of them", "Nghĩa Tiếng Việt": "dẫn dắt, dẫn đầu", "Ví dụ": "The estate agent led us into the kitchen."},
                {"Từ vựng": "native (adj)", "IPA": "/ˈneɪ.tɪv/", "Định nghĩa Tiếng Anh (Glossary)": "living in a particular country or area since birth", "Nghĩa Tiếng Việt": "bản ngữ, bản xứ", "Ví dụ": "My wife is a native New Yorker."},
                {"Từ vựng": "home (town) (n)", "IPA": "/həʊm/", "Định nghĩa Tiếng Anh (Glossary)": "the city or town where you lived as a child", "Nghĩa Tiếng Việt": "quê nhà, quê hương", "Ví dụ": "I live in Washington, but my home town is Denver."}
            ]
            st.table(pd.DataFrame(unit2_topic_vocab))
            
        with tab_v2:
            st.markdown("#### 🔄 Phrasal Verbs (Cụm Động Từ Unit 2)")
            unit2_pv = [
                {"Phrasal Verb": "catch up with", "Định nghĩa Tiếng Anh": "reach the same point/level as someone", "Nghĩa Tiếng Việt": "theo kịp, đuổi kịp", "Ví dụ": "I ran fast to catch up with the others."},
                {"Phrasal Verb": "check in", "Định nghĩa Tiếng Anh": "register at a hotel or an airport", "Nghĩa Tiếng Việt": "làm thủ tục nhận phòng / lên máy bay", "Ví dụ": "Give me your passport and I'll go to the desk to check in."},
                {"Phrasal Verb": "check out", "Định nghĩa Tiếng Anh": "leave a hotel; investigate", "Nghĩa Tiếng Việt": "làm thủ tục trả phòng; điều tra", "Ví dụ": "All guests must check out by midday."},
                {"Phrasal Verb": "drop off", "Định nghĩa Tiếng Anh": "let someone get out of a vehicle; fall asleep", "Nghĩa Tiếng Việt": "cho ai xuống xe; ngủ gật", "Ví dụ": "I'll drop you off outside the station."},
                {"Phrasal Verb": "get back", "Định nghĩa Tiếng Anh": "return from a place", "Nghĩa Tiếng Việt": "trở về từ một nơi", "Ví dụ": "When do you get back from your holiday?"},
                {"Phrasal Verb": "go away", "Định nghĩa Tiếng Anh": "go on holiday", "Nghĩa Tiếng Việt": "đi nghỉ mát, đi xa", "Ví dụ": "We're going away for the weekend."},
                {"Phrasal Verb": "keep up with", "Định nghĩa Tiếng Anh": "stay at the same point/level as someone/something", "Nghĩa Tiếng Việt": "duy trì cùng tốc độ / trình độ", "Ví dụ": "She walks so fast I can't keep up with her."},
                {"Phrasal Verb": "make for", "Định nghĩa Tiếng Anh": "go in the direction of", "Nghĩa Tiếng Việt": "đi về hướng", "Ví dụ": "He made for the door as soon as the meeting ended."},
                {"Phrasal Verb": "pick up", "Định nghĩa Tiếng Anh": "stop in a vehicle to give someone a lift", "Nghĩa Tiếng Việt": "đón ai bằng xe", "Ví dụ": "I'll pick you up at seven."},
                {"Phrasal Verb": "pull in", "Định nghĩa Tiếng Anh": "stop by the side of the road in a car", "Nghĩa Tiếng Việt": "tấp xe vào lề đường", "Ví dụ": "The police car pulled in beside us."},
                {"Phrasal Verb": "run over", "Định nghĩa Tiếng Anh": "hit with a car", "Nghĩa Tiếng Việt": "cán qua, đụng phải (bằng xe)", "Ví dụ": "A dog was run over by a bus."},
                {"Phrasal Verb": "see off", "Định nghĩa Tiếng Anh": "go to a train station, etc, to see someone leave", "Nghĩa Tiếng Việt": "tiễn ai lên đường", "Ví dụ": "We went to the airport to see my uncle off."},
                {"Phrasal Verb": "set out/off", "Định nghĩa Tiếng Anh": "start a journey", "Nghĩa Tiếng Việt": "khởi hành chuyến đi", "Ví dụ": "They set off on a journey across Europe."},
                {"Phrasal Verb": "take off", "Định nghĩa Tiếng Anh": "leave the ground", "Nghĩa Tiếng Việt": "cất cánh (máy bay)", "Ví dụ": "The plane took off on time."},
                {"Phrasal Verb": "turn round", "Định nghĩa Tiếng Anh": "go back in the opposite direction", "Nghĩa Tiếng Việt": "quay ngược lại", "Ví dụ": "We realized we were lost and turned round."}
            ]
            st.table(pd.DataFrame(unit2_pv))
            
        with tab_v3:
            st.markdown("#### 💡 Phrases and Collocations")
            colloc_data = [
                {"Từ chìa khóa": "accident", "Cụm từ cố định": "have an accident; be involved in an accident; do sth by accident"},
                {"Từ chìa khóa": "advance", "Cụm từ cố định": "in advance; advance to/towards a place"},
                {"Từ chìa khóa": "ahead", "Cụm từ cố định": "go straight ahead; go ahead; be ahead of sth/sb"},
                {"Từ chìa khóa": "direction", "Cụm từ cố định": "a change of direction; in the direction of sth; in this/that direction"},
                {"Từ chìa khóa": "head", "Cụm từ cố định": "off the top of your head; head for/towards a place; head over heels (in love)"},
                {"Từ chìa khóa": "holiday", "Cụm từ cố định": "go/be on holiday; have/take a holiday; bank holiday"},
                {"Từ chìa khóa": "left", "Cụm từ cố định": "go/turn/etc left; on the left; on the left-hand side; in the left-hand corner; left-handed"},
                {"Từ chìa khóa": "route", "Cụm từ cố định": "plan your/a route; take a route"},
                {"Từ chìa khóa": "sights", "Cụm từ cố định": "see the sights"},
                {"Từ chìa khóa": "sightseeing", "Cụm từ cố định": "go sightseeing"},
                {"Từ chìa khóa": "speed", "Cụm từ cố định": "at (high/full/etc) speed; a burst of speed; speed limit"},
                {"Từ chìa khóa": "tour", "Cụm từ cố định": "go on/take a tour of/around somewhere; tour a place; tour guide"},
                {"Từ chìa khóa": "trip", "Cụm từ cố định": "business trip; school trip; go on a trip; take a trip (to a place)"},
                {"Từ chìa khóa": "way", "Cụm từ cố định": "lose/make/find your way; in a way; on the way; go all the way (to sth/swh)"}
            ]
            st.table(pd.DataFrame(colloc_data))

        with tab_v4:
            st.markdown("#### 🔗 Word Patterns")
            wp_data = [
                {"Động từ / Tính từ": "afraid", "Cấu trúc đi kèm": "afraid of sth/sb/doing; afraid to do"},
                {"Động từ / Tính từ": "appear", "Cấu trúc đi kèm": "appear to be"},
                {"Động từ / Tính từ": "arrange", "Cấu trúc đi kèm": "arrange sth (with sb); arrange for sb to do"},
                {"Động từ / Tính từ": "arrive", "Cấu trúc đi kèm": "arrive in/at a place; arrive here/there"},
                {"Động từ / Tính từ": "continue", "Cấu trúc đi kèm": "continue to do; continue with sth; continue sth/doing"},
                {"Động từ / Tính từ": "differ", "Cấu trúc đi kèm": "differ from sth/sb"},
                {"Động từ / Tính từ": "dream", "Cấu trúc đi kèm": "dream about/of sth/sb/doing"},
                {"Động từ / Tính từ": "invite", "Cấu trúc đi kèm": "invite sb to do"},
                {"Động từ / Tính từ": "keen", "Cấu trúc đi kèm": "keen to do; keen on sth/sb/doing"},
                {"Động từ / Tính từ": "live", "Cấu trúc đi kèm": "live in/at a place; live on/for sth; live here/there"},
                {"Động từ / Tính từ": "regret", "Cấu trúc đi kèm": "regret (not) doing; regret sth; regret to tell/inform you"},
                {"Động từ / Tính từ": "think", "Cấu trúc đi kèm": "think of/about sth/sb/doing"},
                {"Động từ / Tính từ": "write", "Cấu trúc đi kèm": "write about sth/sb/doing; write (sth) (to sb); write sb sth; write sth down"}
            ]
            st.table(pd.DataFrame(wp_data))

        with tab_v5:
            st.markdown("#### 🔤 Word Formation Database")
            wf_data = [
                {"Từ gốc": "arrange", "Họ từ biến đổi": "rearrange, arrangement"},
                {"Từ gốc": "arrive", "Họ từ biến đổi": "arrival"},
                {"Từ gốc": "broad", "Họ từ biến đổi": "breadth, broaden"},
                {"Từ gốc": "culture", "Họ từ biến đổi": "(culturally), (un)cultured"},
                {"Từ gốc": "differ", "Họ từ biến đổi": "different(ly), difference"},
                {"Từ gốc": "direct", "Họ từ biến đổi": "indirect, direction, director, (in)directly"},
                {"Từ gốc": "distant", "Họ từ biến đổi": "distantly, distance"},
                {"Từ gốc": "enter", "Họ từ biến đổi": "entrance"},
                {"Từ gốc": "inhabit", "Họ từ biến đổi": "inhabitant"},
                {"Từ gốc": "photograph", "Họ từ biến đổi": "photography, photographer, photographic"},
                {"Từ gốc": "recognise", "Họ từ biến đổi": "(un)recognisable, recognition"},
                {"Từ gốc": "time", "Họ từ biến đổi": "timetable"},
                {"Từ gốc": "tour", "Họ từ biến đổi": "tourism, tourist"},
                {"Từ gốc": "world", "Họ từ biến đổi": "worldwide"}
            ]
            st.table(pd.DataFrame(wf_data))

    else:
        st.info(f"Nội dung lý thuyết chi tiết cho **{selected_unit}** đang được cập nhật dữ liệu từ sách Destination B2.")

# --- 3. BÀI TẬP TƯƠNG TÁC & CHẤM ĐIỂM TỰ ĐỘNG ---
elif menu_option == "✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)":
    st.header("✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)")
    selected_quiz_unit = st.selectbox("🎯 Chọn Unit / Bài Ôn tập làm bài:", ALL_UNITS_LIST)
    
    if "Unit 1" in selected_quiz_unit:
        st.subheader("✍️ Unit 1: Present time - Full Practice Exercises")
        st.info("Hãy hoàn thành các bài tập bên dưới. Các câu hỏi trắc nghiệm đều được **bỏ trống ban đầu**, hãy tự chọn đáp án đúng trước khi nhấp nút **Kiểm tra Đáp án**.")
        
        tab_a, tab_b, tab_c, tab_d, tab_e, tab_f, tab_g, tab_h, tab_j = st.tabs([
            "Ex A (Choice)", "Ex B (Rewrite)", "Ex C (Verb Form)", "Ex D (Time Adverbs)",
            "Ex E (Multiple Choice)", "Ex F (Gap Fill)", "Ex G (Matching)", "Ex H (Extra Word)", "Ex J (Transform)"
        ])
        
        with st.form("unit1_full_form"):
            with tab_a:
                st.markdown("#### Exercise A: Circle the correct word or phrase")
                qa1 = st.radio("Câu 1: Elizabeth _____ to bed at around eleven o'clock.", ["usually goes", "is usually going"], index=None, key="b2_u1_qa1")
                qa2 = st.radio("Câu 2: Dan _____ on the other phone right now.", ["talks", "is talking"], index=None, key="b2_u1_qa2")
                qa3 = st.radio("Câu 3: We _____ any meat at the moment as we're both on a diet.", ["don't eat", "aren't eating"], index=None, key="b2_u1_qa3")
                qa4 = st.radio("Câu 4: _____ increasingly safe?", ["Does air travel get", "Is air travel getting"], index=None, key="b2_u1_qa4")
                qa5 = st.radio("Câu 5: My mum _____ me every weekend without fail.", ["calls", "is calling"], index=None, key="b2_u1_qa5")
                qa6 = st.radio("Câu 6: How much _____ ?", ["do babysitters generally earn", "are babysitters generally earning"], index=None, key="b2_u1_qa6")
                qa7 = st.radio("Câu 7: _____ up with excuses for not having done your homework. It's so annoying!", ["You always come", "You're always coming"], index=None, key="b2_u1_qa7")
                qa8 = st.radio("Câu 8: I _____ out much during the week.", ["don't go", "am not going"], index=None, key="b2_u1_qa8")
                qa9 = st.radio("Câu 9: No, the train _____ at Cirencester on Saturdays.", ["does stop", "is stopping"], index=None, key="b2_u1_qa9")
                qa10 = st.radio("Câu 10: My mum _____ part in ice-skating competitions almost every weekend.", ["takes", "is taking"], index=None, key="b2_u1_qa10")

            with tab_b:
                st.markdown("#### Exercise B: Rewrite correctly. Change the phrase in bold")
                qb1 = st.text_input("Câu 1: My dad **is often getting up** late on Saturday mornings.", key="b2_u1_qb1")
                qb2 = st.text_input("Câu 2: **Are you speaking** any other languages apart from English?", key="b2_u1_qb2")
                qb3 = st.text_input("Câu 3: **I already buy** all my Christmas presents and it's only October!", key="b2_u1_qb3")
                qb4 = st.text_input("Câu 4: It's the first time **I'm ever having** a party at home.", key="b2_u1_qb4")
                qb5 = st.text_input("Câu 5: Actually, I think Darren **does works** quite hard sometimes.", key="b2_u1_qb5")
                qb6 = st.text_input("Câu 6: Carlo **is never eating** Chinese food before.", key="b2_u1_qb6")
                qb7 = st.text_input("Câu 7: Sean **already books** a table for tonight.", key="b2_u1_qb7")
                qb8 = st.text_input("Câu 8: **Needs Melanie** any help painting her new flat?", key="b2_u1_qb8")

            with tab_e:
                st.markdown("#### Exercise E: Choose the correct answer")
                qe1 = st.radio("Câu 1: Ian _____ a shower at the moment, so could you call back in about half an hour?", ["takes", "is taking", "has taken", "has been taking"], index=None, key="b2_u1_qe1")
                qe2 = st.radio("Câu 2: _____ to Ipswich before?", ["Do you ever go", "Are you ever going", "Have you ever been", "Have you ever been going"], index=None, key="b2_u1_qe2")
                qe3 = st.radio("Câu 3: I _____ to all the local newspapers and TV stations to complain.", ["already write", "already writing", "have already written", "have already been writing"], index=None, key="b2_u1_qe3")

            submit_u1 = st.form_submit_button("🚀 Submit Answers / Kiểm tra Đáp án Unit 1")

        if submit_u1:
            st.markdown("### 📊 Kết quả & Giải thích Đáp án Unit 1:")
            
            u1_answers = [
                ("A - Câu 1", qa1, "usually goes", "Thói quen sinh hoạt lặp đi lặp lại ở hiện tại dùng Present Simple."),
                ("A - Câu 2", qa2, "is talking", "Hành động đang diễn ra ngay lúc này ('right now') dùng Present Continuous."),
                ("A - Câu 3", qa3, "aren't eating", "Tình huống tạm thời ở hiện tại ('at the moment') dùng Present Continuous."),
                ("A - Câu 4", qa4, "Is air travel getting", "Sự thay đổi, phát triển theo thời gian dùng Present Continuous."),
                ("A - Câu 5", qa5, "calls", "Thói quen lặp đi lặp lại không đổi ('every weekend without fail') dùng Present Simple."),
                ("A - Câu 6", qa6, "do babysitters generally earn", "Hỏi sự thật/mức trung bình chung ('generally') dùng Present Simple."),
                ("A - Câu 7", qa7, "You're always coming", "Thói quen lặp đi lặp lại gây bực mình ('It's so annoying!') dùng Present Continuous + always."),
                ("A - Câu 8", qa8, "don't go", "Thói quen tổng quát trong tuần dùng Present Simple."),
                ("A - Câu 9", qa9, "does stop", "Cấu trúc nhấn mạnh Emphatic Present Simple (does + V-bare) để bác bỏ/khẳng định."),
                ("A - Câu 10", qa10, "takes", "Thói quen diễn ra thường xuyên vào cuối tuần dùng Present Simple."),
                ("E - Câu 1", qe1, "is taking", "Hành động đang diễn ra ngay lúc nói ('at the moment')."),
                ("E - Câu 2", qe2, "Have you ever been", "Trải nghiệm tính đến thời điểm hiện tại ('ever') dùng Present Perfect Simple."),
                ("E - Câu 3", qe3, "have already written", "Hành động vừa hoàn thành có kết quả ở hiện tại ('already') dùng Present Perfect Simple.")
            ]
            
            correct_cnt = 0
            for label, user_ans, correct_ans, expl in u1_answers:
                if user_ans == correct_ans:
                    correct_cnt += 1
                    st.success(f"✅ **{label}: Chính xác!** ({correct_ans})")
                    st.caption(f"💡 *Giải thích:* {expl}")
                elif user_ans is None or str(user_ans).strip() == "":
                    st.warning(f"⚠️ **{label}: Chưa làm / Bỏ trống.**")
                    st.markdown(f"👉 **Đáp án đúng:** `{correct_ans}`")
                    st.caption(f"💡 *Giải thích chi tiết:* {expl}")
                else:
                    st.error(f"❌ **{label}: Chưa đúng.** (Bạn chọn: `{user_ans}`)")
                    st.markdown(f"👉 **Đáp án đúng:** `{correct_ans}`")
                    st.caption(f"💡 *Giải thích chi tiết:* {expl}")
                st.markdown("<hr style='margin: 0.3rem 0;'>", unsafe_allow_html=True)
                
            st.metric("Điểm số tổng kết Unit 1", f"{correct_cnt}/{len(u1_answers)}", f"{int(correct_cnt/len(u1_answers)*100)}%")

    elif "Unit 2" in selected_quiz_unit:
        st.subheader("✍️ Unit 2: Vocabulary - Travel and transport (Full Exercises)")
        st.info("Trọn bộ bài tập từ file `Unit 1 2-DESTINATIONB2-HS.docx` và `GV.docx`. Đáp án trắc nghiệm được **để trống ban đầu**, hệ thống sẽ cung cấp **giải thích chi tiết cho cả câu đúng, câu sai và câu chưa làm**!")
        
        tab_u2_a, tab_u2_b, tab_u2_c, tab_u2_d, tab_u2_e, tab_u2_f, tab_u2_h, tab_u2_i = st.tabs([
            "Ex A (Topic Vocab)", "Ex B (Circle Word)", "Ex C (Phrasal Verbs)", "Ex D (Replace PV)",
            "Ex E (Collocations)", "Ex F (Word Patterns)", "Ex H (Word Formation)", "Ex I (Capitals Change)"
        ])
        
        with st.form("unit2_full_quiz_form"):
            with tab_u2_a:
                st.markdown("#### Exercise A: Choose the correct answer (Topic vocabulary in contrast)")
                u2_a1 = st.radio("Câu 1: You need a passport to cross the _____ between Mexico and the United States.", ["edge", "line", "border", "rim"], index=None, key="u2_a1")
                u2_a2 = st.radio("Câu 2: The hotel where we are _____ is quite luxurious.", ["living", "remaining", "existing", "staying"], index=None, key="u2_a2")
                u2_a3 = st.radio("Câu 3: When you _____ your destination, your tour guide will meet you at the airport.", ["arrive", "get", "reach", "achieve"], index=None, key="u2_a3")
                u2_a4 = st.radio("Câu 4: It can be quite busy here during the tourist _____.", ["season", "period", "phase", "stage"], index=None, key="u2_a4")
                u2_a5 = st.radio("Câu 5: David _____ me to the train station every morning.", ["goes", "takes", "has", "makes"], index=None, key="u2_a5")
                u2_a6 = st.radio("Câu 6: I always enjoy our school _____ to France.", ["excursion", "journey", "trip", "travel"], index=None, key="u2_a6")
                u2_a7 = st.radio("Câu 7: Hurry up, or we'll _____ the bus!", ["avoid", "miss", "drop", "lose"], index=None, key="u2_a7")
                u2_a8 = st.radio("Câu 8: The brochure says that the hotel has a great _____ of the sea.", ["appearance", "look", "sight", "view"], index=None, key="u2_a8")
                u2_a9 = st.radio("Câu 9: I must remember to _____ a souvenir back from Spain for my grandmother.", ["go", "take", "bring", "keep"], index=None, key="u2_a9")
                u2_a10 = st.radio("Câu 10: The _____ from London to Berlin is about 919 kilometres.", ["measure", "length", "gap", "distance"], index=None, key="u2_a10")
                u2_a11 = st.radio("Câu 11: Make sure you _____ a hotel before you come to our island, especially in the summer.", ["book", "keep", "put", "take"], index=None, key="u2_a11")
                u2_a12 = st.radio("Câu 12: I live in Barcelona, but my _____ town is Madrid.", ["birth", "home", "native", "origin"], index=None, key="u2_a12")

            with tab_u2_b:
                st.markdown("#### Exercise B: Circle the correct word")
                u2_b1 = st.radio("Câu 1: I hope to go on a trip round the _____ one day.", ["world", "earth"], index=None, key="u2_b1")
                u2_b2 = st.radio("Câu 2: You learn a lot about the local _____ by speaking to local people.", ["territory", "area"], index=None, key="u2_b2")
                u2_b3 = st.radio("Câu 3: It's good to have someone to _____ you when you are on holiday.", ["lead", "guide"], index=None, key="u2_b3")
                u2_b4 = st.radio("Câu 4: I get the train to work every day and the _____ is quite expensive.", ["fare", "fee"], index=None, key="u2_b4")
                u2_b5 = st.radio("Câu 5: Captain Cook discovered Australia on a _____ to the Pacific.", ["voyage", "travel"], index=None, key="u2_b5")
                u2_b6 = st.radio("Câu 6: Most tourist attractions in London charge an admission _____.", ["fee", "ticket"], index=None, key="u2_b6")
                u2_b7 = st.radio("Câu 7: The sunset over Niagara Falls really is a magnificent _____.", ["look", "sight"], index=None, key="u2_b7")

            with tab_u2_c:
                st.markdown("#### Exercise C: Complete using the correct form of phrasal verbs")
                u2_c1 = st.text_input("Câu 1: Let's go to the airport to _____ Grandpa off when he flies back home.", key="u2_c1")
                u2_c2 = st.text_input("Câu 2: If it starts to rain, _____ for a nearby cave to wait for it to pass.", key="u2_c2")
                u2_c3 = st.text_input("Câu 3: We would like to remind all guests that they must _____ out before midday.", key="u2_c3")
                u2_c4 = st.text_input("Câu 4: Please _____ in and stop so that I can buy something to drink.", key="u2_c4")
                u2_c5 = st.text_input("Câu 5: Every Saturday night my dad _____ us up outside the cinema.", key="u2_c5")
                u2_c6 = st.text_input("Câu 6: I think the neighbours have _____ away for the weekend.", key="u2_c6")
                u2_c7 = st.text_input("Câu 7: John's up ahead so Greg is pedalling fast to _____ up with him.", key="u2_c7")
                u2_c8 = st.text_input("Câu 8: We're going on holiday tomorrow, but we'll call you when we _____ back.", key="u2_c8")

            with tab_u2_d:
                st.markdown("#### Exercise D: Replace words in italics with correct phrasal verbs")
                u2_d1 = st.text_input("Câu 1: We can *start our journey* (________) towards the mountains at dawn.", key="u2_d1")
                u2_d2 = st.text_input("Câu 2: Dad fetched the luggage while Mum *registered* (________) at the hotel.", key="u2_d2")
                u2_d3 = st.text_input("Câu 3: I asked the taxi driver to *let me get out* (________) outside the train station.", key="u2_d3")
                u2_d4 = st.text_input("Câu 4: Oh, no! I've forgotten my passport! We'll have to *go back* (________) and get it!", key="u2_d4")
                u2_d5 = st.text_input("Câu 5: The most exciting moment is when the plane *leaves the ground* (________).", key="u2_d5")
                u2_d6 = st.text_input("Câu 6: Stop the car! I think we've *hit* (________) a dog.", key="u2_d6")
                u2_d7 = st.text_input("Câu 7: I don't think a horse can ever *stay at the same speed as* (________) a car.", key="u2_d7")

            with tab_u2_e:
                st.markdown("#### Exercise E: Phrases and Collocations (Fill in one word)")
                u2_e1 = st.text_input("Câu 1: The speed _____ in towns is 50 km/h and you shouldn't go faster than that.", key="u2_e1")
                u2_e2 = st.text_input("Câu 2: Why don't we _____ the scenic route along the coast?", key="u2_e2")
                u2_e3 = st.text_input("Câu 3: If you buy your plane ticket _____ advance, it's often cheaper.", key="u2_e3")
                u2_e4 = st.text_input("Câu 4: I can't remember the name of the hotel off the _____ of my head.", key="u2_e4")
                u2_e5 = st.text_input("Câu 5: I'm sorry I'm late!! I _____ my way and had to ask for directions.", key="u2_e5")
                u2_e6 = st.text_input("Câu 6: My mum's away in Germany on a business _____ at the moment.", key="u2_e6")
                u2_e7 = st.text_input("Câu 7: Turn left here, then go _____ ahead for a kilometre.", key="u2_e7")
                u2_e8 = st.text_input("Câu 8: If you look on your left-hand _____, you'll see Big Ben.", key="u2_e8")

            with tab_u2_f:
                st.markdown("#### Exercise F: Word Patterns (Choose correct answer)")
                u2_f1 = st.radio("Câu 1: I've always dreamt _____ China.", ["to visit", "of visiting", "I visit", "visit"], index=None, key="u2_f1")
                u2_f2 = st.radio("Câu 2: The travel agency is arranging for us _____ at a really nice hotel.", ["stay", "of staying", "to stay", "staying"], index=None, key="u2_f2")
                u2_f3 = st.radio("Câu 3: My dad says he always regrets _____ more.", ["to not travel", "not travelling", "he not travel", "of not travelling"], index=None, key="u2_f3")
                u2_f4 = st.radio("Câu 4: John seems keen _____ how to drive as soon as he can.", ["of learning", "he learn", "for learn", "to learn"], index=None, key="u2_f4")
                u2_f5 = st.radio("Câu 5: Now, class, I'd like you all to write _____ a description of your last holiday.", ["me", "to me", "it me", "about me"], index=None, key="u2_f5")
                u2_f6 = st.radio("Câu 6: When you arrive _____, have your passport ready.", ["to the airport", "in the airport", "on the airport", "at the airport"], index=None, key="u2_f6")
                u2_f7 = st.radio("Câu 7: The Joneses have invited us _____ to Australia with them this summer.", ["going", "for going", "about going", "to go"], index=None, key="u2_f7")
                u2_f8 = st.radio("Câu 8: The in-flight entertainment may differ _____ that advertised.", ["to", "from", "in", "at"], index=None, key="u2_f8")

            with tab_u2_h:
                st.markdown("#### Exercise H: Word Formation (Complete text)")
                u2_h1 = st.text_input("Câu 1: It's not always easy being a (TOUR) _____.", key="u2_h1")
                u2_h2 = st.text_input("Câu 2: You spend half your time making (ARRANGE) _____ for your holiday.", key="u2_h2")
                u2_h3 = st.text_input("Câu 3: and the other half worrying about sticking to the (TIME) _____.", key="u2_h3")
                u2_h4 = st.text_input("Câu 4: There are no (CULTURE) _____ problems.", key="u2_h4")
                u2_h5 = st.text_input("Câu 5: you don't need someone to be the (PHOTOGRAPH) _____.", key="u2_h5")
                u2_h6 = st.text_input("Câu 6: and you know that the local (INHABIT) _____ are always friendly!", key="u2_h6")

            with tab_u2_i:
                st.markdown("#### Exercise I: Change word in capitals")
                u2_i1 = st.text_input("Câu 1: Beijing has changed so much that it's almost (RECOGNISE) _____.", key="u2_i1")
                u2_i2 = st.text_input("Câu 2: The number of cars (WORLD) _____ is about a billion.", key="u2_i2")
                u2_i3 = st.text_input("Câu 3: The new maglev trains run on a completely (DIFFER) _____ system.", key="u2_i3")
                u2_i4 = st.text_input("Câu 4: Living in a foreign country really does (BROAD) _____ your horizons.", key="u2_i4")
                u2_i5 = st.text_input("Câu 5: I can't find a (DIRECT) _____ flight from London to Delhi.", key="u2_i5")
                u2_i6 = st.text_input("Câu 6: All passengers must complete a visa form upon (ARRIVE) _____.", key="u2_i6")
                u2_i7 = st.text_input("Câu 7: showing the (DISTANT) _____ to the nearest town.", key="u2_i7")
                u2_i8 = st.text_input("Câu 8: next to the (ENTER) _____.", key="u2_i8")

            submit_u2 = st.form_submit_button("🚀 Submit Answers / Kiểm tra Đáp án Unit 2")

        if submit_u2:
            st.markdown("### 📊 Kết quả & Giải thích Đáp án Chi tiết Unit 2:")
            
            u2_eval_list = [
                ("Ex A - Câu 1", u2_a1, "border", "Dùng 'border' để chỉ đường biên giới chính thức giữa hai quốc gia (between Mexico and the US)."),
                ("Ex A - Câu 2", u2_a2, "staying", "Dùng 'staying' khi ở lại khách sạn trong thời gian ngắn/đi nghỉ (stay in a hotel)."),
                ("Ex A - Câu 3", u2_a3, "reach", "'reach + destination' đi trực tiếp với tân ngữ không cần giới từ (reach your destination)."),
                ("Ex A - Câu 4", u2_a4, "season", "Dùng 'tourist season' để chỉ mùa du lịch cao điểm trong năm."),
                ("Ex A - Câu 5", u2_a5, "takes", "Dùng 'take somebody to somewhere' mang nghĩa chở/đưa ai đó đi đâu."),
                ("Ex A - Câu 6", u2_a6, "trip", "Dùng 'school trip' (cụm cố định) chỉ chuyến tham quan/dã ngoại của trường học."),
                ("Ex A - Câu 7", u2_a7, "miss", "Dùng 'miss the bus' nghĩa là lỡ xe buýt."),
                ("Ex A - Câu 8", u2_a8, "view", "Dùng 'view of the sea' chỉ quang cảnh hướng ra biển từ phòng/khách sạn."),
                ("Ex A - Câu 9", u2_a9, "bring", "Dùng 'bring something back from somewhere' nghĩa là mang quà lưu niệm về cho ai."),
                ("Ex A - Câu 10", u2_a10, "distance", "Dùng 'distance' để chỉ khoảng cách giữa hai thành phố (London to Berlin)."),
                ("Ex A - Câu 11", u2_a11, "book", "Dùng 'book a hotel' nghĩa là đặt trước phòng khách sạn."),
                ("Ex A - Câu 12", u2_a12, "home", "Dùng 'home town' (cụm từ cố định) chỉ quê nhà / quê hương."),
                ("Ex B - Câu 1", u2_b1, "world", "Cụm từ 'round the world' nghĩa là vòng quanh thế giới."),
                ("Ex B - Câu 2", u2_b2, "area", "Dùng 'local area' để chỉ khu vực địa phương xung quanh."),
                ("Ex B - Câu 3", u2_b3, "guide", "Dùng 'guide' nghĩa là hướng dẫn viên dẫn đường du lịch."),
                ("Ex B - Câu 4", u2_b4, "fare", "Dùng 'bus/train fare' chỉ tiền vé xe/tàu đi lại."),
                ("Ex B - Câu 5", u2_b5, "voyage", "Dùng 'voyage' chỉ chuyến hành trình dài bằng đường biển."),
                ("Ex B - Câu 6", u2_b6, "fee", "Dùng 'admission fee' chỉ lệ phí vào cửa tham quan."),
                ("Ex B - Câu 7", u2_b7, "sight", "Dùng 'magnificent sight' chỉ cảnh tượng thiên nhiên tuyệt đẹp."),
                ("Ex C - Câu 1", u2_c1, ["see", "see off"], "Phrasal verb 'see off' nghĩa là tiễn ai đó lên đường tại sân bay/ga tàu."),
                ("Ex C - Câu 2", u2_c2, ["make", "make for"], "Phrasal verb 'make for' nghĩa là đi về hướng/tiến về phía."),
                ("Ex C - Câu 3", u2_c3, ["check", "check out"], "Phrasal verb 'check out' nghĩa là làm thủ tục trả phòng khách sạn."),
                ("Ex C - Câu 4", u2_c4, ["pull", "pull in"], "Phrasal verb 'pull in' nghĩa là tấp xe vào lề đường."),
                ("Ex C - Câu 5", u2_c5, ["picks", "pick up"], "Phrasal verb 'pick up' chia ngôi thứ 3 số ít 'picks up' nghĩa là đón ai bằng xe."),
                ("Ex C - Câu 6", u2_c6, ["gone", "gone away"], "Phrasal verb 'go away' ở thì Present Perfect 'gone away' nghĩa là đi xa/đi nghỉ mát."),
                ("Ex C - Câu 7", u2_c7, ["catch", "catch up with"], "Phrasal verb 'catch up with' nghĩa là đạp xe/chạy theo kịp ai phía trước."),
                ("Ex C - Câu 8", u2_c8, ["get", "get back"], "Phrasal verb 'get back' nghĩa là trở về từ chuyến đi."),
                ("Ex D - Câu 1", u2_d1, ["set out", "set off"], "'start a journey' = set out / set off (khởi hành chuyến đi)."),
                ("Ex D - Câu 2", u2_d2, ["checked in", "check in"], "'registered at hotel' = checked in (làm thủ tục nhận phòng - quá khứ đơn)."),
                ("Ex D - Câu 3", u2_d3, ["drop me off"], "'let me get out of vehicle' = drop me off (cho tôi xuống xe)."),
                ("Ex D - Câu 4", u2_d4, ["turn round"], "'go back in opposite direction' = turn round (quay đầu xe lại)."),
                ("Ex D - Câu 5", u2_d5, ["takes off"], "'leaves the ground' = takes off (máy bay cất cánh)."),
                ("Ex D - Câu 6", u2_d6, ["run over"], "'hit with a car' = run over (đụng/cán qua)."),
                ("Ex D - Câu 7", u2_d7, ["keep up with"], "'stay at same speed' = keep up with (duy trì cùng tốc độ)."),
                ("Ex E - Câu 1", u2_e1, "limit", "Cụm từ 'speed limit' nghĩa là tốc độ tối đa cho phép."),
                ("Ex E - Câu 2", u2_e2, "take", "Collocation 'take the scenic route' nghĩa là đi theo con đường cảnh đẹp."),
                ("Ex E - Câu 3", u2_e3, "in", "Cụm từ 'in advance' nghĩa là đặt trước/làm trước."),
                ("Ex E - Câu 4", u2_e4, "top", "Idiom 'off the top of my head' nghĩa là nói ngay không cần suy nghĩ kỹ."),
                ("Ex E - Câu 5", u2_e5, "lost", "Collocation 'lost my way' nghĩa là bị lạc đường (quá khứ của lose)."),
                ("Ex E - Câu 6", u2_e6, "trip", "Cụm từ 'business trip' nghĩa là chuyến đi công tác."),
                ("Ex E - Câu 7", u2_e7, "straight", "Collocation 'go straight ahead' nghĩa là đi thẳng về phía trước."),
                ("Ex E - Câu 8", u2_e8, "side", "Cụm từ 'on your left-hand side' nghĩa là ở phía bên tay trái của bạn."),
                ("Ex F - Câu 1", u2_f1, "of visiting", "Word pattern: dream of doing sth (mơ về việc làm gì)."),
                ("Ex F - Câu 2", u2_f2, "to stay", "Word pattern: arrange for sb to do sth (sắp xếp cho ai làm gì)."),
                ("Ex F - Câu 3", u2_f3, "not travelling", "Word pattern: regret not doing sth (hối hận vì đã không làm gì)."),
                ("Ex F - Câu 4", u2_f4, "to learn", "Word pattern: keen to do sth (hào hứng/muốn làm gì)."),
                ("Ex F - Câu 5", u2_f5, "me", "Word pattern: write sb sth (viết cho ai cái gì - write me a description)."),
                ("Ex F - Câu 6", u2_f6, "at the airport", "Word pattern: arrive at a place (khi tới địa điểm nhỏ như sân bay dùng 'at')."),
                ("Ex F - Câu 7", u2_f7, "to go", "Word pattern: invite sb to do sth (mời ai đi đâu)."),
                ("Ex F - Câu 8", u2_f8, "from", "Word pattern: differ from sth (khác biệt so với cái gì)."),
                ("Ex H - Câu 1", u2_h1, "tourist", "Từ chuyển đổi: tour (n) -> tourist (n - khách du lịch)."),
                ("Ex H - Câu 2", u2_h2, "arrangements", "Từ chuyển đổi: arrange (v) -> arrangements (dạng số nhiều - sự chuẩn bị)."),
                ("Ex H - Câu 3", u2_h3, "timetable", "Từ ghép: time + table -> timetable (n - lịch trình/thời gian biểu)."),
                ("Ex H - Câu 4", u2_h4, "cultural", "Từ chuyển đổi: culture (n) -> cultural (adj - thuộc văn hóa)."),
                ("Ex H - Câu 5", u2_h5, "photographer", "Từ chuyển đổi: photograph -> photographer (n - nhiếp ảnh gia)."),
                ("Ex H - Câu 6", u2_h6, "inhabitants", "Từ chuyển đổi: inhabit -> inhabitants (n - cư dân địa phương)."),
                ("Ex I - Câu 1", u2_i1, "unrecognisable", "Biến đổi từ: RECOGNISE -> unrecognisable (adj - không thể nhận ra)."),
                ("Ex I - Câu 2", u2_i2, "worldwide", "Biến đổi từ: WORLD -> worldwide (adv - trên toàn thế giới)."),
                ("Ex I - Câu 3", u2_i3, "different", "Biến đổi từ: DIFFER -> different (adj - hoàn toàn khác biệt)."),
                ("Ex I - Câu 4", u2_i4, "broaden", "Biến đổi từ: BROAD -> broaden (v - mở rộng tầm mắt/horizons)."),
                ("Ex I - Câu 5", u2_i5, "direct", "Biến đổi từ: DIRECT -> direct flight (chuyến bay thẳng)."),
                ("Ex I - Câu 6", u2_i6, "arrival", "Biến đổi từ: ARRIVE -> arrival (n - sự đến nơi/khi đáp xuống sân bay)."),
                ("Ex I - Câu 7", u2_i7, "distance", "Biến đổi từ: DISTANT -> distance (n - khoảng cách)."),
                ("Ex I - Câu 8", u2_i8, "entrance", "Biến đổi từ: ENTER -> entrance (n - lối vào/cổng vào).")
            ]
            
            score_u2 = 0
            for item in u2_eval_list:
                label = item[0]
                user_val = item[1]
                target_ans = item[2]
                expl = item[3]
                
                is_correct = False
                if isinstance(target_ans, list):
                    if user_val and str(user_val).strip().lower() in [x.lower() for x in target_ans]:
                        is_correct = True
                    target_str = " / ".join(target_ans)
                else:
                    if user_val and str(user_val).strip().lower() == str(target_ans).strip().lower():
                        is_correct = True
                    target_str = str(target_ans)
                    
                if is_correct:
                    score_u2 += 1
                    st.success(f"✅ **{label}: Chính xác!** (`{user_val}`)")
                    st.caption(f"💡 *Giải thích chi tiết:* {expl}")
                elif user_val is None or str(user_val).strip() == "":
                    st.warning(f"⚠️ **{label}: Chưa làm / Bỏ trống.**")
                    st.markdown(f"👉 **Đáp án đúng chuẩn:** `{target_str}`")
                    st.caption(f"💡 *Giải thích chi tiết:* {expl}")
                else:
                    st.error(f"❌ **{label}: Chưa đúng.** (Bạn chọn/nhập: `{user_val}`)")
                    st.markdown(f"👉 **Đáp án đúng chuẩn:** `{target_str}`")
                    st.caption(f"💡 *Giải thích chi tiết:* {expl}")
                st.markdown("<hr style='margin: 0.2rem 0;'>", unsafe_allow_html=True)
                
            total_items = len(u2_eval_list)
            st.metric("Điểm số tổng kết Unit 2", f"{score_u2}/{total_items}", f"{int(score_u2/total_items*100)}%")

    else:
        st.info(f"Nội dung bài tập tương tác cho **{selected_quiz_unit}** đang được hoàn thiện trọn bộ dữ liệu từ sách Destination B2.")

# --- 4. THẺ GHI NHỚ TỪ VỰNG (FLASHCARDS) ---
elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng (Vocabulary Flashcards)")
    st.caption("Lật thẻ thông minh để ghi nhớ Từ vựng, Phiên âm IPA, Định nghĩa Tiếng Anh, Nghĩa Tiếng Việt và Ví dụ thực tế:")
    
    selected_fc_unit = st.selectbox("🎯 Chọn Unit Từ vựng để ôn Flashcards:", VOCAB_UNITS)
    
    if "Unit 2" in selected_fc_unit or "Review 1" in selected_fc_unit:
        flashcards_u2_data = [
            {"word": "voyage (n)", "pos": "Noun", "ipa": "/ˈvɔɪ.ɪdʒ/", "def": "a long journey, especially on a ship", "vi": "chuyến đi dài bằng đường biển", "ex": "It was a long voyage from London to New York."},
            {"word": "journey (n)", "pos": "Noun", "ipa": "/ˈdʒɜː.ni/", "def": "an occasion when you travel from one place to another", "vi": "hành trình, chuyến đi", "ex": "We had a long journey ahead of us."},
            {"word": "trip (n)", "pos": "Noun", "ipa": "/trɪp/", "def": "an occasion when you go somewhere and come back again", "vi": "chuyến đi ngắn (đi rồi về)", "ex": "The whole family went on a trip to Florida."},
            {"word": "excursion (n)", "pos": "Noun", "ipa": "/ɪkˈskɜː.ʃən/", "def": "a short journey that you make for pleasure", "vi": "chuyến dã ngoại, tham quan", "ex": "My grandmother often talks about excursions to the sea."},
            {"word": "fare (n)", "pos": "Noun", "ipa": "/feər/", "def": "the money that you pay for a journey", "vi": "tiền vé xe, tàu, máy bay", "ex": "The bus fare from York to Leeds has gone up."},
            {"word": "catch up with", "pos": "Phrasal Verb", "ipa": "/kætʃ ʌp wɪð/", "def": "reach the same point/level as someone", "vi": "theo kịp, đuổi kịp", "ex": "Run fast to catch up with the group."},
            {"word": "check in", "pos": "Phrasal Verb", "ipa": "/tʃek ɪn/", "def": "register at a hotel or an airport", "vi": "làm thủ tục nhận phòng / lên máy bay", "ex": "Give me your passport and I'll go to check in."},
            {"word": "check out", "pos": "Phrasal Verb", "ipa": "/tʃek aʊt/", "def": "leave a hotel; investigate", "vi": "làm thủ tục trả phòng; điều tra", "ex": "All guests must check out by midday."},
            {"word": "drop off", "pos": "Phrasal Verb", "ipa": "/drɒp ɒf/", "def": "let someone get out of a vehicle; fall asleep", "vi": "cho ai xuống xe; ngủ gật", "ex": "I'll drop you off outside the train station."},
            {"word": "see off", "pos": "Phrasal Verb", "ipa": "/siː ɒf/", "def": "go to a train station, etc, to see someone leave", "vi": "tiễn ai lên đường", "ex": "We went to the airport to see Grandpa off."},
            {"word": "set out / set off", "pos": "Phrasal Verb", "ipa": "/set aʊt/", "def": "start a journey", "vi": "khởi hành chuyến đi", "ex": "They set off on a journey across Europe."},
            {"word": "take off", "pos": "Phrasal Verb", "ipa": "/teɪk ɒf/", "def": "leave the ground", "vi": "cất cánh (máy bay)", "ex": "The plane took off right on time."},
            {"word": "off the top of your head", "pos": "Collocation", "ipa": "/ɒf ðə tɒp əv jɔː hed/", "def": "from memory, without checking or thinking carefully", "vi": "nói ngay không cần suy nghĩ kỹ/nghiên cứu", "ex": "Off the top of my head, I'd say about 50 people were there."},
            {"word": "unrecognisable", "pos": "Word Formation", "ipa": "/ˌʌn.rek.əɡˈnaɪ.zə.bəl/", "def": "so changed that you cannot recognise it", "vi": "không thể nhận ra được", "ex": "Delhi has changed so much that it's practically unrecognisable."}
        ]
        
        fc_idx = st.slider("🎯 Chọn thẻ từ vựng:", 1, len(flashcards_u2_data), 1) - 1
        card = flashcards_u2_data[fc_idx]
        
        st.markdown(f"""
        <div class="card" style="text-align: center; padding: 2rem; border-left: 6px solid #9D174D;">
            <span class="badge-vocab">{card['pos'].upper()}</span>
            <h2 style="color: #1E3A8A; margin-top: 0.5rem;">{card['word']}</h2>
            <p style="color: #6B7280; font-size: 1.1rem; font-weight: 500;">🔊 {card['ipa']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🔍 LẬT THẺ ĐỂ XEM ĐỊNH NGHĨA, NGHĨA TIẾNG VIỆT & VÍ DỤ"):
            st.markdown(f"**📖 Định nghĩa Tiếng Anh:** {card['def']}")
            st.markdown(f"**🇻🇳 Nghĩa Tiếng Việt:** {card['vi']}")
            st.markdown(f"**💬 Ví dụ ngữ cảnh:** *\"{card['ex']}\"*")
            
    else:
        st.info("⚠️ **Thẻ ghi nhớ (Flashcards)** chỉ dành riêng cho các **Unit Từ vựng** và **Bài Ôn tập (Reviews)**. Hãy chọn **Unit 2: Vocabulary - Travel and transport** ở menu phía trên để học ngay!")

# --- 5. GÓC LƯU Ý (WATCH OUT! CORNER) ---
elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý C1/C2 & B2 (Watch Out! Corner)")
    st.write("Tổng hợp các bẫy ngữ pháp và từ vựng đặc biệt quan trọng trong các bài thi Cambridge B2 FCE / C1 CAE / C2 CPE:")
    
    st.markdown("""
    <div class="watchout-box">
        <h4>⚠️ Watch Out #1: Present Perfect Simple vs Present Perfect Continuous</h4>
        <b>Quy tắc B2:</b><br>
        • Sử dụng <b>Present Perfect Simple</b> khi nhấn mạnh <u>số lượng / con số cụ thể</u> đã hoàn thành:<br>
        &nbsp;&nbsp;<i>✔ I've written <b>three essays</b> this morning.</i><br>
        • Sử dụng <b>Present Perfect Continuous</b> khi nhấn mạnh <u>thời lượng / tính liên tục kéo dài</u>:<br>
        &nbsp;&nbsp;<i>✔ I've been writing essays for <b>three hours</b>.</i>
    </div>
    
    <div class="watchout-box">
        <h4>⚠️ Watch Out #2: Stative Verbs in Action Meanings</h4>
        <b>Quy tắc B2:</b><br>
        Một số động từ trạng thái có thể dùng ở thì tiếp diễn khi mô tả <b>HÀNH ĐỘNG</b>:<br>
        • <i>Do you <b>have</b> your plane ticket with you?</i> (Trạng thái: sở hữu)<br>
        • <i>Are you <b>having</b> lunch at the moment?</i> (Hành động: ăn uống)<br>
        • <i>I <b>think</b> it's a great idea.</i> (Trạng thái: quan điểm = believe)<br>
        • <i>I'm <b>thinking</b> about moving to Paris.</i> (Hành động: cân nhắc = consider)
    </div>
    
    <div class="watchout-box">
        <h4>⚠️ Watch Out #3: Topic Vocabulary in Contrast (Unit 2)</h4>
        • <b>voyage</b>: Chuyến đi dài bằng đường biển.<br>
        • <b>journey</b>: Chuyến đi từ nơi này sang nơi khác (thường tính bằng khoảng cách).<br>
        • <b>trip</b>: Chuyến đi ngắn có khứ hồi (đi rồi về, e.g., business trip, day trip).<br>
        • <b>excursion</b>: Chuyến dã ngoại, tham quan ngắm cảnh.
    </div>
    """, unsafe_allow_html=True)

# --- 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập (Progress Report)")
    st.write("Đánh dấu các Unit bạn đã hoàn thành để hệ thống tự động tính phần trăm tiến độ khóa học Destination B2:")
    
    completed_units = []
    st.subheader("✅ Danh sách 28 Units & 14 Reviews:")
    
    cols = st.columns(3)
    for idx, u in enumerate(ALL_UNITS_LIST):
        col = cols[idx % 3]
        checked = col.checkbox(u, key=f"b2_progress_chk_{idx}", value=(idx in [0, 1]))
        if checked:
            completed_units.append(u)
            
    progress = len(completed_units) / len(ALL_UNITS_LIST)
    st.markdown("---")
    st.subheader("📈 Tiến độ hoàn thành toàn bộ khóa học:")
    st.progress(progress)
    st.info(f"🎉 Bạn đã hoàn thành **{len(completed_units)}/{len(ALL_UNITS_LIST)} mục bài học & bài kiểm tra** ({int(progress*100)}%)")

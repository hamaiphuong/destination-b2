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
    .explain-box {
        background-color: #F8FAFC;
        border-left: 4px solid #3B82F6;
        padding: 0.8rem;
        margin-top: 0.3rem;
        border-radius: 4px;
        font-size: 0.95rem;
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
        tab_v1, tab_v2, tab_v3, tab_v4, tab_v5 = st.tabs([
            "1. Topic Vocabulary in Contrast",
            "2. Phrasal Verbs",
            "3. Phrases & Collocations",
            "4. Word Patterns",
            "5. Word Formation"
        ])
        
        with tab_v1:
            st.markdown("#### 🔹 Topic Vocabulary in Contrast (36 cặp/từ vựng phân biệt)")
            v1_data = [
                {"Từ vựng": "voyage (n)", "IPA": "/ˈvɔɪ.ɪdʒ/", "Định nghĩa Tiếng Anh": "a long journey, especially on a ship or in space", "Nghĩa Tiếng Việt": "chuyến đi dài bằng đường biển/vũ trụ", "Ví dụ": "The voyage across the Atlantic took three weeks."},
                {"Từ vựng": "journey (n)", "IPA": "/ˈdʒɜː.ni/", "Định nghĩa Tiếng Anh": "an occasion when you travel from one place to another", "Nghĩa Tiếng Việt": "chuyến đi, hành trình", "Ví dụ": "We had a long journey ahead of us."},
                {"Từ vựng": "trip (n)", "IPA": "/trɪp/", "Định nghĩa Tiếng Anh": "an occasion when you go somewhere and come back again", "Nghĩa Tiếng Việt": "chuyến đi ngắn (đi rồi về)", "Ví dụ": "The whole family went on a trip to Florida."},
                {"Từ vựng": "travel (n/v)", "IPA": "/ˈtræv.əl/", "Định nghĩa Tiếng Anh": "the activity of travelling in general", "Nghĩa Tiếng Việt": "sự đi lại, du lịch nói chung", "Ví dụ": "Foreign travel expands the mind."},
                {"Từ vựng": "excursion (n)", "IPA": "/ɪkˈskɜː.ʃən/", "Định nghĩa Tiếng Anh": "a short journey that you make for pleasure", "Nghĩa Tiếng Việt": "chuyến tham quan, dã ngoại", "Ví dụ": "My grandmother often talks about excursions to the sea."},
                {"Từ vựng": "view (n)", "IPA": "/vjuː/", "Định nghĩa Tiếng Anh": "the things that you can see from a particular place", "Nghĩa Tiếng Việt": "quang cảnh (từ một vị trí cố định)", "Ví dụ": "The view from the hotel window was magnificent."},
                {"Từ vựng": "sight (n)", "IPA": "/saɪt/", "Định nghĩa Tiếng Anh": "a person or thing that you see that is notable or impressive", "Nghĩa Tiếng Việt": "cảnh tượng, danh lam thắng cảnh", "Ví dụ": "Windmills are a common sight in Holland."},
                {"Từ vựng": "world (n)", "IPA": "/wɜːld/", "Định nghĩa Tiếng Anh": "the planet Earth and all the people and things on it", "Nghĩa Tiếng Việt": "thế giới, Trái Đất", "Ví dụ": "He travelled all around the world."},
                {"Từ vựng": "earth (n)", "IPA": "/ɜːθ/", "Định nghĩa Tiếng Anh": "the land on which we live", "Nghĩa Tiếng Việt": "trái đất, mặt đất", "Ví dụ": "They were crushed under tons of earth."},
                {"Từ vựng": "area (n)", "IPA": "/ˈeə.ri.ə/", "Định nghĩa Tiếng Anh": "a part of a country, town, or city", "Nghĩa Tiếng Việt": "khu vực, vùng", "Ví dụ": "He knows the area quite well."},
                {"Từ vựng": "territory (n)", "IPA": "/ˈter.ɪ.tər.i/", "Định nghĩa Tiếng Anh": "an area of land that is controlled by a country or leader", "Nghĩa Tiếng Việt": "lãnh thổ, vùng đất kiểm soát", "Ví dụ": "The army occupied enemy territory."},
                {"Từ vựng": "season (n)", "IPA": "/ˈsiː.zən/", "Định nghĩa Tiếng Anh": "one of the four periods of the year (spring, summer, autumn, winter)", "Nghĩa Tiếng Việt": "mùa trong năm", "Ví dụ": "Autumn is my favourite season."},
                {"Từ vựng": "period (n)", "IPA": "/ˈpɪə.ri.əd/", "Định nghĩa Tiếng Anh": "an amount of time", "Nghĩa Tiếng Việt": "giai đoạn, thời kỳ", "Ví dụ": "The museum is closed for a short period."},
                {"Từ vựng": "fare (n)", "IPA": "/feər/", "Định nghĩa Tiếng Anh": "the money that you pay for a journey on a vehicle", "Nghĩa Tiếng Việt": "tiền vé xe/tàu/máy bay", "Ví dụ": "The bus fare has increased recently."},
                {"Từ vựng": "ticket (n)", "IPA": "/ˈtɪk.ɪt/", "Định nghĩa Tiếng Anh": "a piece of paper or card that shows you have paid for a journey", "Nghĩa Tiếng Việt": "vé (xem phim, tàu xe)", "Ví dụ": "I bought a return ticket to London."},
                {"Từ vựng": "fee (n)", "IPA": "/fiː/", "Định nghĩa Tiếng Anh": "an amount of money that you pay for professional advice or services", "Nghĩa Tiếng Việt": "phí dịch vụ, học phí", "Ví dụ": "You have to pay an entry fee."},
                {"Từ vựng": "miss (v)", "IPA": "/mɪs/", "Định nghĩa Tiếng Anh": "to be too late to catch a train, bus, plane, etc.", "Nghĩa Tiếng Việt": "bỏ lỡ (tàu xe)", "Ví dụ": "I missed the last bus home."},
                {"Từ vựng": "lose (v)", "IPA": "/luːz/", "Định nghĩa Tiếng Anh": "to no longer have something because you do not know where it is", "Nghĩa Tiếng Việt": "thất lạc, đánh mất", "Ví dụ": "I lost my passport at the airport."},
                {"Từ vựng": "take (v)", "IPA": "/teɪk/", "Định nghĩa Tiếng Anh": "to move or carry someone or something from one place to another", "Nghĩa Tiếng Việt": "đưa đi, mang đi", "Ví dụ": "I'll take you to the station."},
                {"Từ vựng": "bring (v)", "IPA": "/brɪŋ/", "Định nghĩa Tiếng Anh": "to take someone or something with you to the place where you are going", "Nghĩa Tiếng Việt": "mang đến (phía người nói)", "Ví dụ": "Don't forget to bring your passport."},
                {"Từ vựng": "go (v)", "IPA": "/ɡəʊ/", "Định nghĩa Tiếng Anh": "to move or travel from one place to another", "Nghĩa Tiếng Việt": "đi", "Ví dụ": "We went to Spain last year."},
                {"Từ vựng": "book (v)", "IPA": "/bʊk/", "Định nghĩa Tiếng Anh": "to arrange to have a seat, room, etc. at a particular time in the future", "Nghĩa Tiếng Việt": "đặt chỗ, đặt vé", "Ví dụ": "I booked a table for two."},
                {"Từ vựng": "keep (v)", "IPA": "/kiːp/", "Định nghĩa Tiếng Anh": "to continue to have or use something", "Nghĩa Tiếng Việt": "giữ, duy trì", "Ví dụ": "Keep your ticket safe."},
                {"Từ vựng": "arrive (v)", "IPA": "/əˈraɪv/", "Định nghĩa Tiếng Anh": "to reach a place, especially at the end of a journey", "Nghĩa Tiếng Việt": "đến nơi", "Ví dụ": "What time does the train arrive?"},
                {"Từ vựng": "reach (v)", "IPA": "/riːtʃ/", "Định nghĩa Tiếng Anh": "to arrive at a place that you have been travelling to", "Nghĩa Tiếng Việt": "đạt tới, đến được", "Ví dụ": "We reached London at midnight."},
                {"Từ vựng": "live (v)", "IPA": "/lɪv/", "Định nghĩa Tiếng Anh": "to have your home in a particular place", "Nghĩa Tiếng Việt": "sống, cư trú lâu dài", "Ví dụ": "They live in a small town."},
                {"Từ vựng": "stay (v)", "IPA": "/steɪ/", "Định nghĩa Tiếng Anh": "to live somewhere for a short time as a visitor or guest", "Nghĩa Tiếng Việt": "ở lại, lưu trú tạm thời", "Ví dụ": "We stayed in a lovely hotel."},
                {"Từ vựng": "border (n)", "IPA": "/ˈbɔː.dər/", "Định nghĩa Tiếng Anh": "the official line that separates two countries or regions", "Nghĩa Tiếng Việt": "biên giới", "Ví dụ": "We crossed the border into France."},
                {"Từ vựng": "edge (n)", "IPA": "/edʒ/", "Định nghĩa Tiếng Anh": "the part of something that is furthest from the centre", "Nghĩa Tiếng Việt": "mép, rìa", "Ví dụ": "Don't stand near the edge of the cliff."},
                {"Từ vựng": "line (n)", "IPA": "/laɪn/", "Định nghĩa Tiếng Anh": "a long thin mark on a surface", "Nghĩa Tiếng Việt": "đường ranh giới, vạch kẻ", "Ví dụ": "Draw a line across the page."},
                {"Từ vựng": "length (n)", "IPA": "/leŋθ/", "Định nghĩa Tiếng Anh": "the measurement of something from one end to the other", "Nghĩa Tiếng Việt": "chiều dài, độ dài", "Ví dụ": "The length of the pool is 50 metres."},
                {"Từ vựng": "distance (n)", "IPA": "/ˈdɪs.təns/", "Định nghĩa Tiếng Anh": "the amount of space between two places or things", "Nghĩa Tiếng Việt": "khoảng cách", "Ví dụ": "It's a short distance from here."},
                {"Từ vựng": "guide (v/n)", "IPA": "/ɡaɪd/", "Định nghĩa Tiếng Anh": "to show someone where to go by going with them", "Nghĩa Tiếng Việt": "hướng dẫn / người hướng dẫn", "Ví dụ": "The tour guide was very knowledgeable."},
                {"Từ vựng": "lead (v)", "IPA": "/liːd/", "Định nghĩa Tiếng Anh": "to control a group of people or an organization", "Nghĩa Tiếng Việt": "dẫn đường, dẫn đầu", "Ví dụ": "She led us through the forest."},
                {"Từ vựng": "native (adj)", "IPA": "/ˈneɪ.tɪv/", "Định nghĩa Tiếng Anh": "connected with the place where you were born", "Nghĩa Tiếng Việt": "bản địa, nơi sinh ra", "Ví dụ": "French is her native language."},
                {"Từ vựng": "home (town) (n)", "IPA": "/həʊm taʊn/", "Định nghĩa Tiếng Anh": "the town or city where you grew up", "Nghĩa Tiếng Việt": "quê hương, thành phố quê nhà", "Ví dụ": "I returned to my home town."}
            ]
            st.table(pd.DataFrame(v1_data))

        with tab_v2:
            st.markdown("#### 🔹 Phrasal Verbs (15 cụm động từ)")
            v2_data = [
                {"Phrasal Verb": "catch up with", "Định nghĩa Tiếng Anh": "reach the same point/level as someone ahead", "Nghĩa Tiếng Việt": "theo kịp, đuổi kịp", "Ví dụ": "Run fast to catch up with the group."},
                {"Phrasal Verb": "check in", "Định nghĩa Tiếng Anh": "register at a hotel or an airport", "Nghĩa Tiếng Việt": "làm thủ tục nhận phòng/lên máy bay", "Ví dụ": "We checked in at the airport early."},
                {"Phrasal Verb": "check out", "Định nghĩa Tiếng Anh": "leave a hotel after paying; investigate", "Nghĩa Tiếng Việt": "làm thủ tục trả phòng / kiểm tra", "Ví dụ": "Guests must check out by 11 am."},
                {"Phrasal Verb": "drop off", "Định nghĩa Tiếng Anh": "let someone get out of a vehicle; fall asleep", "Nghĩa Tiếng Việt": "thả ai xuống xe / ngủ thiếp đi", "Ví dụ": "I'll drop you off at the station."},
                {"Phrasal Verb": "get back", "Định nghĩa Tiếng Anh": "return from a place", "Nghĩa Tiếng Việt": "quay trở về", "Ví dụ": "When did you get back from Paris?"},
                {"Phrasal Verb": "go away", "Định nghĩa Tiếng Anh": "go on holiday; leave a place", "Nghĩa Tiếng Việt": "đi nghỉ mát / rời đi", "Ví dụ": "We're going away for the weekend."},
                {"Phrasal Verb": "keep up with", "Định nghĩa Tiếng Anh": "stay at the same point/level as someone", "Nghĩa Tiếng Việt": "theo kịp, giữ cùng tốc độ", "Ví dụ": "It's hard to keep up with the news."},
                {"Phrasal Verb": "make for", "Định nghĩa Tiếng Anh": "head in the direction of a place", "Nghĩa Tiếng Việt": "đi về phía, hướng về", "Ví dụ": "Let me make for the exit."},
                {"Phrasal Verb": "pick up", "Định nghĩa Tiếng Anh": "stop in a vehicle to give someone a lift", "Nghĩa Tiếng Việt": "đón ai bằng xe", "Ví dụ": "Dad will pick us up after school."},
                {"Phrasal Verb": "pull in", "Định nghĩa Tiếng Anh": "stop by the side of the road in a car", "Nghĩa Tiếng Việt": "tấp xe vào lề đường", "Ví dụ": "The car pulled in to let the ambulance pass."},
                {"Phrasal Verb": "run over", "Định nghĩa Tiếng Anh": "hit with a car or other vehicle", "Nghĩa Tiếng Việt": "cán qua, đụng phải", "Ví dụ": "The dog was run over by a van."},
                {"Phrasal Verb": "see off", "Định nghĩa Tiếng Anh": "go to a train station/airport to say goodbye", "Nghĩa Tiếng Việt": "tiễn ai ra sân bay/nhà ga", "Ví dụ": "They came to see me off at the airport."},
                {"Phrasal Verb": "set out / off", "Định nghĩa Tiếng Anh": "start a journey", "Nghĩa Tiếng Việt": "khởi hành, bắt đầu chuyến đi", "Ví dụ": "We set off early in the morning."},
                {"Phrasal Verb": "take off", "Định nghĩa Tiếng Anh": "leave the ground (plane)", "Nghĩa Tiếng Việt": "cất cánh (máy bay)", "Ví dụ": "The plane took off on time."},
                {"Phrasal Verb": "turn round", "Định nghĩa Tiếng Anh": "go back in the opposite direction", "Nghĩa Tiếng Việt": "quay ngược lại", "Ví dụ": "We had to turn round because we took the wrong road."}
            ]
            st.table(pd.DataFrame(v2_data))

        with tab_v3:
            st.markdown("#### 🔹 Phrases and Collocations (Tách lẻ 40 cụm từ cố định)")
            v3_data = [
                {"Từ gốc": "accident", "Cụm từ Tiếng Anh": "have an accident", "Nghĩa Tiếng Việt": "gặp tai nạn"},
                {"Từ gốc": "accident", "Cụm từ Tiếng Anh": "be (involved) in an accident", "Nghĩa Tiếng Việt": "vướng vào/bị tai nạn"},
                {"Từ gốc": "accident", "Cụm từ Tiếng Anh": "do sth by accident", "Nghĩa Tiếng Việt": "vô tình làm gì"},
                {"Từ gốc": "advance", "Cụm từ Tiếng Anh": "in advance", "Nghĩa Tiếng Việt": "trước (thời gian)"},
                {"Từ gốc": "advance", "Cụm từ Tiếng Anh": "advance to/towards a place", "Nghĩa Tiếng Việt": "tiến về phía một nơi"},
                {"Từ gốc": "ahead", "Cụm từ Tiếng Anh": "go straight ahead", "Nghĩa Tiếng Việt": "đi thẳng về phía trước"},
                {"Từ gốc": "ahead", "Cụm từ Tiếng Anh": "go ahead", "Nghĩa Tiếng Việt": "tiến lên / tiếp tục"},
                {"Từ gốc": "ahead", "Cụm từ Tiếng Anh": "be ahead of sth/sb", "Nghĩa Tiếng Việt": "đi trước/dẫn trước ai"},
                {"Từ gốc": "direction", "Cụm từ Tiếng Anh": "a change of direction", "Nghĩa Tiếng Việt": "sự đổi hướng"},
                {"Từ gốc": "direction", "Cụm từ Tiếng Anh": "in the direction of sth", "Nghĩa Tiếng Việt": "theo hướng của cái gì"},
                {"Từ gốc": "direction", "Cụm từ Tiếng Anh": "in this/that direction", "Nghĩa Tiếng Việt": "theo hướng này/đó"},
                {"Từ gốc": "head", "Cụm từ Tiếng Anh": "off the top of your head", "Nghĩa Tiếng Việt": "theo trí nhớ/không cần suy nghĩ kỹ"},
                {"Từ gốc": "head", "Cụm từ Tiếng Anh": "head for/towards a place", "Nghĩa Tiếng Việt": "đi về phía một nơi"},
                {"Từ gốc": "head", "Cụm từ Tiếng Anh": "head over heels (in love)", "Nghĩa Tiếng Việt": "yêu say đắm"},
                {"Từ gốc": "holiday", "Cụm từ Tiếng Anh": "go/be on holiday", "Nghĩa Tiếng Việt": "đi/đang nghỉ mát"},
                {"Từ gốc": "holiday", "Cụm từ Tiếng Anh": "have/take a holiday", "Nghĩa Tiếng Việt": "kỳ nghỉ / xin nghỉ"},
                {"Từ gốc": "holiday", "Cụm từ Tiếng Anh": "bank holiday", "Nghĩa Tiếng Việt": "ngày nghỉ lễ quốc gia"},
                {"Từ gốc": "left", "Cụm từ Tiếng Anh": "go/turn left", "Nghĩa Tiếng Việt": "đi/rẽ trái"},
                {"Từ gốc": "left", "Cụm từ Tiếng Anh": "on the left", "Nghĩa Tiếng Việt": "ở bên trái"},
                {"Từ gốc": "left", "Cụm từ Tiếng Anh": "on the left-hand side", "Nghĩa Tiếng Việt": "ở phía bên tay trái"},
                {"Từ gốc": "left", "Cụm từ Tiếng Anh": "in the left-hand corner", "Nghĩa Tiếng Việt": "ở góc bên trái"},
                {"Từ gốc": "left", "Cụm từ Tiếng Anh": "left-handed", "Nghĩa Tiếng Việt": "thuận tay trái"},
                {"Từ gốc": "route", "Cụm từ Tiếng Anh": "plan your/a route", "Nghĩa Tiếng Việt": "lập kế hoạch tuyến đường"},
                {"Từ gốc": "route", "Cụm từ Tiếng Anh": "take a route", "Nghĩa Tiếng Việt": "đi theo tuyến đường"},
                {"Từ gốc": "sights", "Cụm từ Tiếng Anh": "see the sights", "Nghĩa Tiếng Việt": "ngắm cảnh danh thắng"},
                {"Từ gốc": "sightseeing", "Cụm từ Tiếng Anh": "go sightseeing", "Nghĩa Tiếng Việt": "đi ngắm cảnh du lịch"},
                {"Từ gốc": "speed", "Cụm từ Tiếng Anh": "at high/full speed", "Nghĩa Tiếng Việt": "ở tốc độ cao/tối đa"},
                {"Từ gốc": "speed", "Cụm từ Tiếng Anh": "a burst of speed", "Nghĩa Tiếng Việt": "sự tăng tốc đột ngột"},
                {"Từ gốc": "speed", "Cụm từ Tiếng Anh": "speed limit", "Nghĩa Tiếng Việt": "giới hạn tốc độ"},
                {"Từ gốc": "tour", "Cụm từ Tiếng Anh": "go on / take a tour of/around a place", "Nghĩa Tiếng Việt": "đi tham quan quanh một nơi"},
                {"Từ gốc": "tour", "Cụm từ Tiếng Anh": "tour guide", "Nghĩa Tiếng Việt": "hướng dẫn viên du lịch"},
                {"Từ gốc": "trip", "Cụm từ Tiếng Anh": "business trip", "Nghĩa Tiếng Việt": "chuyến công tác"},
                {"Từ gốc": "trip", "Cụm từ Tiếng Anh": "school trip", "Nghĩa Tiếng Việt": "chuyến dã ngoại trường học"},
                {"Từ gốc": "trip", "Cụm từ Tiếng Anh": "go on a trip", "Nghĩa Tiếng Việt": "đi du lịch ngắn ngày"},
                {"Từ gốc": "trip", "Cụm từ Tiếng Anh": "take a trip (to a place)", "Nghĩa Tiếng Việt": "thực hiện chuyến đi tới..."},
                {"Từ gốc": "way", "Cụm từ Tiếng Anh": "lose your way", "Nghĩa Tiếng Việt": "lạc đường"},
                {"Từ gốc": "way", "Cụm từ Tiếng Anh": "make your way", "Nghĩa Tiếng Việt": "tự đi tới / tiến lên"},
                {"Từ gốc": "way", "Cụm từ Tiếng Anh": "find your way", "Nghĩa Tiếng Việt": "tìm đường đi"},
                {"Từ gốc": "way", "Cụm từ Tiếng Anh": "in a way", "Nghĩa Tiếng Việt": "theo một cách nào đó"},
                {"Từ gốc": "way", "Cụm từ Tiếng Anh": "on the way", "Nghĩa Tiếng Việt": "trên đường đi"}
            ]
            st.table(pd.DataFrame(v3_data))

        with tab_v4:
            st.markdown("#### 🔹 Word Patterns (Tách lẻ 26 mẫu cấu trúc đi kèm)")
            v4_data = [
                {"Từ gốc": "afraid", "Cấu trúc Tiếng Anh": "afraid of sth/sb/doing", "Nghĩa Tiếng Việt": "sợ cái gì/ai/làm gì"},
                {"Từ gốc": "afraid", "Cấu trúc Tiếng Anh": "afraid to do", "Nghĩa Tiếng Việt": "sợ không dám làm gì"},
                {"Từ gốc": "appear", "Cấu trúc Tiếng Anh": "appear to be", "Nghĩa Tiếng Việt": "có vẻ như là"},
                {"Từ gốc": "arrange", "Cấu trúc Tiếng Anh": "arrange sth (with sb)", "Nghĩa Tiếng Việt": "sắp xếp cái gì với ai"},
                {"Từ gốc": "arrange", "Cấu trúc Tiếng Anh": "arrange for sb to do", "Nghĩa Tiếng Việt": "sắp xếp cho ai làm gì"},
                {"Từ gốc": "arrive", "Cấu trúc Tiếng Anh": "arrive in/at a place", "Nghĩa Tiếng Việt": "đến (tỉnh/thành/địa điểm)"},
                {"Từ gốc": "arrive", "Cấu trúc Tiếng Anh": "arrive here/there", "Nghĩa Tiếng Việt": "đến đây/đó"},
                {"Từ gốc": "continue", "Cấu trúc Tiếng Anh": "continue sth/doing", "Nghĩa Tiếng Việt": "tiếp tục cái gì/làm gì"},
                {"Từ gốc": "continue", "Cấu trúc Tiếng Anh": "continue to do", "Nghĩa Tiếng Việt": "tiếp tục làm gì"},
                {"Từ gốc": "continue", "Cấu trúc Tiếng Anh": "continue with sth", "Nghĩa Tiếng Việt": "tiếp tục với cái gì"},
                {"Từ gốc": "differ", "Cấu trúc Tiếng Anh": "differ from sth/sb", "Nghĩa Tiếng Việt": "khác biệt với cái gì/ai"},
                {"Từ gốc": "dream", "Cấu trúc Tiếng Anh": "dream about/of sth/sb/doing", "Nghĩa Tiếng Việt": "mơ về cái gì/ai/việc gì"},
                {"Từ gốc": "invite", "Cấu trúc Tiếng Anh": "invite sb to do", "Nghĩa Tiếng Việt": "mời ai làm gì"},
                {"Từ gốc": "keen", "Cấu trúc Tiếng Anh": "keen on sth/sb/doing", "Nghĩa Tiếng Việt": "hào hứng/thích cái gì/làm gì"},
                {"Từ gốc": "keen", "Cấu trúc Tiếng Anh": "keen to do", "Nghĩa Tiếng Việt": "rất muốn làm gì"},
                {"Từ gốc": "live", "Cấu trúc Tiếng Anh": "live in/at a place", "Nghĩa Tiếng Việt": "sống ở nơi nào"},
                {"Từ gốc": "live", "Cấu trúc Tiếng Anh": "live on/for sth", "Nghĩa Tiếng Việt": "sống dựa vào / sống vì cái gì"},
                {"Từ gốc": "live", "Cấu trúc Tiếng Anh": "live here/there", "Nghĩa Tiếng Việt": "sống ở đây/đó"},
                {"Từ gốc": "regret", "Cấu trúc Tiếng Anh": "regret (not) doing", "Nghĩa Tiếng Việt": "hối hận vì đã (không) làm gì"},
                {"Từ gốc": "regret", "Cấu trúc Tiếng Anh": "regret to tell/inform you", "Nghĩa Tiếng Việt": "rất tiếc phải thông báo"},
                {"Từ gốc": "think", "Cấu trúc Tiếng Anh": "think of/about sth/sb/doing", "Nghĩa Tiếng Việt": "suy nghĩ về cái gì/ai"},
                {"Từ gốc": "write", "Cấu trúc Tiếng Anh": "write sth (to sb)", "Nghĩa Tiếng Việt": "viết cái gì cho ai"},
                {"Từ gốc": "write", "Cấu trúc Tiếng Anh": "write sb sth", "Nghĩa Tiếng Việt": "viết cho ai cái gì"},
                {"Từ gốc": "write", "Cấu trúc Tiếng Anh": "write about sth/sb/doing", "Nghĩa Tiếng Việt": "viết về cái gì/ai"},
                {"Từ gốc": "write", "Cấu trúc Tiếng Anh": "write sth down", "Nghĩa Tiếng Việt": "ghi chép lại cái gì"}
            ]
            st.table(pd.DataFrame(v4_data))

        with tab_v5:
            st.markdown("#### 🔹 Word Formation (Tách lẻ 26 từ biến đổi)")
            v5_data = [
                {"Từ gốc": "arrange (v)", "Từ biến đổi": "rearrange (v)", "Nghĩa Tiếng Việt": "sắp xếp lại"},
                {"Từ gốc": "arrange (v)", "Từ biến đổi": "arrangement (n)", "Nghĩa Tiếng Việt": "sự sắp xếp, thỏa thuận"},
                {"Từ gốc": "arrive (v)", "Từ biến đổi": "arrival (n)", "Nghĩa Tiếng Việt": "sự đến nơi"},
                {"Từ gốc": "broad (adj)", "Từ biến đổi": "breadth (n)", "Nghĩa Tiếng Việt": "bề rộng, chiều rộng"},
                {"Từ gốc": "broad (adj)", "Từ biến đổi": "broaden (v)", "Nghĩa Tiếng Việt": "mở rộng"},
                {"Từ gốc": "culture (n)", "Từ biến đổi": "cultural(ly) (adj/adv)", "Nghĩa Tiếng Việt": "thuộc về văn hóa"},
                {"Từ gốc": "culture (n)", "Từ biến đổi": "uncultured (adj)", "Nghĩa Tiếng Việt": "không có học thức/văn hóa"},
                {"Từ gốc": "differ (v)", "Từ biến đổi": "different(ly) (adj/adv)", "Nghĩa Tiếng Việt": "khác biệt"},
                {"Từ gốc": "differ (v)", "Từ biến đổi": "difference (n)", "Nghĩa Tiếng Việt": "sự khác biệt"},
                {"Từ gốc": "direct (adj/v)", "Từ biến đổi": "indirect (adj)", "Nghĩa Tiếng Việt": "gián tiếp"},
                {"Từ gốc": "direct (adj/v)", "Từ biến đổi": "direction (n)", "Nghĩa Tiếng Việt": "phương hướng"},
                {"Từ gốc": "direct (adj/v)", "Từ biến đổi": "director (n)", "Nghĩa Tiếng Việt": "giám đốc, đạo diễn"},
                {"Từ gốc": "distant (adj)", "Từ biến đổi": "distantly (adv)", "Nghĩa Tiếng Việt": "xa xôi"},
                {"Từ gốc": "distant (adj)", "Từ biến đổi": "distance (n)", "Nghĩa Tiếng Việt": "khoảng cách"},
                {"Từ gốc": "enter (v)", "Từ biến đổi": "entrance (n)", "Nghĩa Tiếng Việt": "lối vào, cổng vào"},
                {"Từ gốc": "inhabit (v)", "Từ biến đổi": "inhabitant (n)", "Nghĩa Tiếng Việt": "cư dân, người ở"},
                {"Từ gốc": "photograph (v/n)", "Từ biến đổi": "photography (n)", "Nghĩa Tiếng Việt": "ngành nhiếp ảnh"},
                {"Từ gốc": "photograph (v/n)", "Từ biến đổi": "photographer (n)", "Nghĩa Tiếng Việt": "thợ chụp ảnh"},
                {"Từ gốc": "photograph (v/n)", "Từ biến đổi": "photographic (adj)", "Nghĩa Tiếng Việt": "thuộc nhiếp ảnh"},
                {"Từ gốc": "recognise (v)", "Từ biến đổi": "(un)recognisable (adj)", "Nghĩa Tiếng Việt": "(không) thể nhận ra"},
                {"Từ gốc": "recognise (v)", "Từ biến đổi": "recognition (n)", "Nghĩa Tiếng Việt": "sự nhận nhận/nhận ra"},
                {"Từ gốc": "time (n)", "Từ biến đổi": "timetable (n)", "Nghĩa Tiếng Việt": "thời gian biểu, lịch trình"},
                {"Từ gốc": "tour (v/n)", "Từ biến đổi": "tourism (n)", "Nghĩa Tiếng Việt": "ngành du lịch"},
                {"Từ gốc": "tour (v/n)", "Từ biến đổi": "tourist (n)", "Nghĩa Tiếng Việt": "khách du lịch"},
                {"Từ gốc": "world (n)", "Từ biến đổi": "worldwide (adj/adv)", "Nghĩa Tiếng Việt": "toàn thế giới"}
            ]
            st.table(pd.DataFrame(v5_data))

    else:
        st.info(f"Nội dung lý thuyết chi tiết cho **{selected_unit}** đang được hoàn thiện dữ liệu từ sách Destination B2.")

# --- 3. BÀI TẬP TƯƠNG TÁC & CHẤM ĐIỂM TỰ ĐỘNG ---
elif menu_option == "✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)":
    st.header("✍️ Bài tập Tương tác & Chấm điểm tự động (Interactive Quiz)")
    selected_quiz_unit = st.selectbox("🎯 Chọn Unit / Bài Ôn tập làm bài:", ALL_UNITS_LIST)
    
    if "Unit 1" in selected_quiz_unit:
        st.subheader("✍️ Unit 1: Present time - Full Practice Exercises")
        st.info("Hãy hoàn thành các bài tập bên dưới.")
        
        tab_a, tab_b, tab_c, tab_d, tab_e, tab_f, tab_g, tab_h, tab_i, tab_j = st.tabs([
            "Exercise A", "Exercise B", "Exercise C", "Exercise D", "Exercise E",
            "Exercise F", "Exercise G", "Exercise H", "Exercise I", "Exercise J"
        ])
        
        with st.form("unit1_full_quiz_form"):
            with tab_a:
                st.markdown("#### Exercise A: Extract exact sentences from textbook")
                u1_qa1 = st.text_input("Câu 1: Ian ________ (take) a shower at the moment, so could you call back in about half an hour?", key="u1_qa1")
                u1_qa2 = st.text_input("Câu 2: ________ (you / ever / go) to Ipswich before?", key="u1_qa2")
                u1_qa3 = st.text_input("Câu 3: I ________ (write) to all the local newspapers to complain about the noise.", key="u1_qa3")
                u1_qa4 = st.text_input("Câu 4: Eric ________ (play) hockey competitively or just for fun?", key="u1_qa4")

            with tab_d:
                st.markdown("#### Exercise D: Complete using words from the box")
                u1_qd1 = st.radio("Câu 5: Have you ________ dreamt of winning the lottery?", ["already", "ever", "never", "yet"], index=None, key="u1_qd1")
                u1_qd2 = st.radio("Câu 6: I haven't worked out how to set the timer on the video ________.", ["already", "still", "yet", "since"], index=None, key="u1_qd2")
                u1_qd3 = st.radio("Câu 7: My dad's lived in the same house ________ he was born.", ["for", "since", "from", "ever"], index=None, key="u1_qd3")

            with tab_e:
                st.markdown("#### Exercise E: Choose the correct answer")
                u1_qe1 = st.radio("Câu 8: That's the first time I ________ an answer right today!", ["A. I get", "B. I am getting", "C. I have got", "D. I have been getting"], index=None, key="u1_qe1")
                u1_qe2 = st.radio("Câu 9: Jessica ________ left, I'm afraid.", ["A. already", "B. has already", "C. is already", "D. still"], index=None, key="u1_qe2")

            with tab_g:
                st.markdown("#### Exercise G: Present Perfect Simple or Continuous")
                u1_qg1 = st.radio("Câu 10: We ________ for over an hour when the train finally arrived.", ["A. have waited", "B. have been waiting", "C. are waiting"], index=None, key="u1_qg1")
                u1_qg2 = st.radio("Câu 11: I ________ three letters so far this morning.", ["A. have written", "B. have been writing", "C. write"], index=None, key="u1_qg2")

            with tab_i:
                st.markdown("#### Exercise I: Write one word in each gap (Holiday Blues)")
                u1_qi1 = st.text_input("Câu 12: You've been looking at that timetable ________ the last ten minutes.", key="u1_qi1")

            submit_u1_btn = st.form_submit_button("🚀 Nộp bài & Kiểm tra Đáp án Unit 1")

        if submit_u1_btn:
            score = 0
            total = 10
            st.markdown("### 📊 Kết quả Bài làm & Giải thích Chi tiết Unit 1")
            
            # Câu 1
            ans1 = u1_qa1.strip().lower() if u1_qa1 else ""
            if ans1 in ["is taking", "'s taking"]:
                score += 1
                st.success("✅ **Câu 1: Chính xác!** (Đáp án: `is taking`)")
            elif ans1 == "":
                st.warning("⚠️ **Câu 1: Chưa trả lời / Bỏ trống.** Đáp án đúng là: **is taking**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Hành động đang diễn ra tại thời điểm nói ('at the moment') dùng Thì Hiện tại Tiếp diễn.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 1: Chưa chính xác.** (Bạn nhập: `{u1_qa1}`) ➔ Đáp án đúng: **is taking**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Dùng Present Continuous cho hành động diễn ra tạm thời lúc nói.</div>", unsafe_allow_html=True)

            # Câu 5
            if u1_qd1 == "ever":
                score += 1
                st.success("✅ **Câu 5: Chính xác!** (Đáp án: `ever`)")
            elif u1_qd1 is None:
                st.warning("⚠️ **Câu 5: Chưa trả lời / Bỏ trống.** Đáp án đúng là: **ever**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'Have you ever...' dùng để hỏi về trải nghiệm.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 5: Chưa chính xác.** (Bạn chọn: `{u1_qd1}`) ➔ Đáp án đúng: **ever**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Trạng từ 'ever' đứng trước V3/ed trong câu hỏi trải nghiệm.</div>", unsafe_allow_html=True)

            # Câu 8
            if u1_qe1 == "C. I have got":
                score += 1
                st.success("✅ **Câu 8: Chính xác!** (Đáp án: `C. I have got`)")
            elif u1_qe1 is None:
                st.warning("⚠️ **Câu 8: Chưa trả lời / Bỏ trống.** Đáp án đúng là: **C. I have got**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> Sau cấu trúc 'That's the first time...' bắt buộc dùng Thì Hiện tại Hoàn thành.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 8: Chưa chính xác.** (Bạn chọn: `{u1_qe1}`) ➔ Đáp án đúng: **C. I have got**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'That's the first time + Present Perfect Simple'.</div>", unsafe_allow_html=True)

            pct = int((score / total) * 100)
            st.info(f"🏆 Điểm số Unit 1: **{score}/{total}** ({pct}%)")

    elif "Unit 2" in selected_quiz_unit:
        st.subheader("✍️ Unit 2: Travel and transport - Practice Exercises")
        st.info("Hãy hoàn thành các bài tập bên dưới.")
        
        tab_u2_a, tab_u2_b, tab_u2_c, tab_u2_d, tab_u2_e = st.tabs([
            "Exercise A (Topic Vocab)", "Exercise B (Vocabulary)", "Exercise C (Phrasal Verbs)",
            "Exercise D (Phrasal Verbs 2)", "Exercise E (Phrases & Collocations)"
        ])

        with st.form("unit2_full_quiz_form"):
            with tab_u2_a:
                st.markdown("#### Exercise A: Choose the correct answer")
                u2_qa1 = st.radio("Câu 1: You choose the hotel and I'll ________ the tickets.", ["A. book", "B. keep", "C. order", "D. pay"], index=None, key="u2_qa1")
                u2_qa2 = st.radio("Câu 2: The train ________ from platform 4 is the 10:15 for London.", ["A. arriving", "B. reaching", "C. entering", "D. departing"], index=None, key="u2_qa2")
                u2_qa3 = st.radio("Câu 3: We had a long ________ ahead of us.", ["A. voyage", "B. travel", "C. journey", "D. excursion"], index=None, key="u2_qa3")

            with tab_u2_c:
                st.markdown("#### Exercise C: Complete using phrasal verbs")
                u2_qc1 = st.radio("Câu 4: The plane ________ on time despite the bad weather.", ["A. took off", "B. set off", "C. checked in", "D. pulled in"], index=None, key="u2_qc1")
                u2_qc2 = st.radio("Câu 5: We had to ________ at 6 am to catch the early flight.", ["A. check out", "B. set out", "C. drop off", "D. see off"], index=None, key="u2_qc2")

            with tab_u2_e:
                st.markdown("#### Exercise E: Phrases and Collocations")
                u2_qe1 = st.text_input("Câu 6: I had an ________ on my bike yesterday. (accident)", key="u2_qe1")
                u2_qe2 = st.text_input("Câu 7: You must book your tickets in ________. (advance)", key="u2_qe2")

            submit_u2_btn = st.form_submit_button("🚀 Nộp bài & Kiểm tra Đáp án Unit 2")

        if submit_u2_btn:
            score2 = 0
            total2 = 7
            st.markdown("### 📊 Kết quả Bài làm & Giải thích Chi tiết Unit 2")

            # Câu 1
            if u2_qa1 == "A. book":
                score2 += 1
                st.success("✅ **Câu 1: Chính xác!** (Đáp án: `A. book`)")
            elif u2_qa1 is None:
                st.warning("⚠️ **Câu 1: Chưa trả lời / Bỏ trống.** Đáp án đúng là: **A. book**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'book tickets' nghĩa là đặt vé trước.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 1: Chưa chính xác.** (Bạn chọn: `{u2_qa1}`) ➔ Đáp án đúng: **A. book**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'book' + vé/bàn/phòng mang nghĩa đặt chỗ trước.</div>", unsafe_allow_html=True)

            # Câu 3
            if u2_qa3 == "C. journey":
                score2 += 1
                st.success("✅ **Câu 3: Chính xác!** (Đáp án: `C. journey`)")
            elif u2_qa3 is None:
                st.warning("⚠️ **Câu 3: Chưa trả lời / Bỏ trống.** Đáp án đúng là: **C. journey**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'have a long journey ahead' nghĩa là có một chuyến đi/hành trình dài phía trước.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 3: Chưa chính xác.** (Bạn chọn: `{u2_qa3}`) ➔ Đáp án đúng: **C. journey**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'journey' chỉ hành trình di chuyển từ nơi này đến nơi khác.</div>", unsafe_allow_html=True)

            # Câu 4
            if u2_qc1 == "A. took off":
                score2 += 1
                st.success("✅ **Câu 4: Chính xác!** (Đáp án: `A. took off`)")
            elif u2_qc1 is None:
                st.warning("⚠️ **Câu 4: Chưa trả lời / Bỏ trống.** Đáp án đúng là: **A. took off**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'take off' nghĩa là máy bay cất cánh.</div>", unsafe_allow_html=True)
            else:
                st.error(f"❌ **Câu 4: Chưa chính xác.** (Bạn chọn: `{u2_qc1}`) ➔ Đáp án đúng: **A. took off**")
                st.markdown("<div class='explain-box'>💡 <i>Giải thích:</i> 'take off' là phrasal verb chỉ hành động cất cánh.</div>", unsafe_allow_html=True)

            pct2 = int((score2 / total2) * 100)
            st.info(f"🏆 Điểm số Unit 2: **{score2}/{total2}** ({pct2}%)")
    else:
        st.info(f"Bài tập trắc nghiệm & điền từ tương tác cho **{selected_quiz_unit}** đang được xây dựng theo đáp án chuẩn sách B2.")

# --- 4. THẺ GHI NHỚ TỪ VỰNG (FLASHCARDS) ---
elif menu_option == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.header("🎴 Thẻ ghi nhớ Từ vựng (Flashcards)")
    selected_fc_unit = st.selectbox("🎯 Chọn Unit Từ vựng để ôn Flashcards:", VOCAB_UNITS)
    
    if "Grammar" in selected_fc_unit:
        st.warning("⚠️ Thẻ ghi nhớ (Flashcards) chỉ dành riêng cho các Unit Từ vựng. Các Unit Ngữ pháp tập trung vào Lý thuyết và Bài tập Tương tác.")
    else:
        st.subheader("🎴 Flashcards Unit 2: Travel and transport")
        
        flashcards_data = [
            # Topic Vocabulary
            {"word": "voyage (n)", "category": "Topic Vocabulary", "definition": "a long journey, especially on a ship or in space", "vi": "chuyến đi dài bằng đường biển / vũ trụ"},
            {"word": "journey (n)", "category": "Topic Vocabulary", "definition": "an occasion when you travel from one place to another", "vi": "chuyến đi, hành trình"},
            {"word": "trip (n)", "category": "Topic Vocabulary", "definition": "an occasion when you go somewhere and come back again", "vi": "chuyến đi ngắn (đi rồi về)"},
            {"word": "travel (n/v)", "category": "Topic Vocabulary", "definition": "the activity of travelling in general", "vi": "sự đi lại, du lịch nói chung"},
            {"word": "excursion (n)", "category": "Topic Vocabulary", "definition": "a short journey that you make for pleasure", "vi": "chuyến tham quan, dã ngoại"},
            {"word": "fare (n)", "category": "Topic Vocabulary", "definition": "the money that you pay for a journey on a vehicle", "vi": "tiền vé xe/tàu/máy bay"},
            {"word": "fee (n)", "category": "Topic Vocabulary", "definition": "an amount of money that you pay for professional advice or services", "vi": "phí dịch vụ, học phí"},

            # Phrasal Verbs
            {"word": "catch up with", "category": "Phrasal Verbs", "definition": "reach the same point/level as someone ahead", "vi": "theo kịp, đuổi kịp"},
            {"word": "check in", "category": "Phrasal Verbs", "definition": "register at a hotel or an airport", "vi": "làm thủ tục nhận phòng/lên máy bay"},
            {"word": "check out", "category": "Phrasal Verbs", "definition": "leave a hotel after paying; investigate", "vi": "làm thủ tục trả phòng / kiểm tra"},
            {"word": "drop off", "category": "Phrasal Verbs", "definition": "let someone get out of a vehicle; fall asleep", "vi": "thả ai xuống xe / ngủ thiếp đi"},
            {"word": "see off", "category": "Phrasal Verbs", "definition": "go to a train station/airport to say goodbye", "vi": "tiễn ai ra sân bay/nhà ga"},
            {"word": "set out / off", "category": "Phrasal Verbs", "definition": "start a journey", "vi": "khởi hành, bắt đầu chuyến đi"},
            {"word": "take off", "category": "Phrasal Verbs", "definition": "leave the ground (plane)", "vi": "cất cánh (máy bay)"},

            # Phrases & Collocations
            {"word": "have an accident (collocation)", "category": "Phrases & Collocations", "definition": "be involved in an unexpected unfortunate event", "vi": "gặp tai nạn"},
            {"word": "in advance (collocation)", "category": "Phrases & Collocations", "definition": "before a particular time in the future", "vi": "trước (thời gian)"},
            {"word": "off the top of your head (phrase)", "category": "Phrases & Collocations", "definition": "from memory, without checking facts", "vi": "theo trí nhớ / không cần suy nghĩ kỹ"},
            {"word": "go on holiday (collocation)", "category": "Phrases & Collocations", "definition": "take a vacation", "vi": "đi nghỉ mát"},
            {"word": "bank holiday (collocation)", "category": "Phrases & Collocations", "definition": "official public holiday", "vi": "ngày nghỉ lễ quốc gia"},
            {"word": "left-handed (collocation)", "category": "Phrases & Collocations", "definition": "using the left hand more naturally", "vi": "thuận tay trái"},
            {"word": "see the sights (collocation)", "category": "Phrases & Collocations", "definition": "visit famous places as a tourist", "vi": "ngắm cảnh danh thắng"},
            {"word": "speed limit (collocation)", "category": "Phrases & Collocations", "definition": "maximum legal speed on a road", "vi": "giới hạn tốc độ"},
            {"word": "business trip (collocation)", "category": "Phrases & Collocations", "definition": "a journey taken for business purposes", "vi": "chuyến công tác"},

            # Word Patterns
            {"word": "afraid of sth/doing", "category": "Word Patterns", "definition": "feeling fear about something", "vi": "sợ cái gì/làm gì"},
            {"word": "arrange for sb to do", "category": "Word Patterns", "definition": "plan for someone to do something", "vi": "sắp xếp cho ai làm gì"},
            {"word": "arrive in/at a place", "category": "Word Patterns", "definition": "reach a destination", "vi": "đến (thành phố / địa điểm)"},
            {"word": "regret (not) doing", "category": "Word Patterns", "definition": "feel sorry about an action in the past", "vi": "hối hận vì đã (không) làm gì"},

            # Word Formation
            {"word": "arrange (v) ➔ arrangement (n)", "category": "Word Formation", "definition": "plan or preparation", "vi": "sự sắp xếp, thỏa thuận"},
            {"word": "broad (adj) ➔ broaden (v)", "category": "Word Formation", "definition": "make or become wider", "vi": "mở rộng"},
            {"word": "direct (adj) ➔ direction (n)", "category": "Word Formation", "definition": "the course along which someone moves", "vi": "phương hướng"},
            {"word": "recognise (v) ➔ (un)recognisable (adj)", "category": "Word Formation", "definition": "able/unable to be identified", "vi": "(không) thể nhận ra"}
        ]

        # Filter by category
        categories = ["Tất cả"] + sorted(list(set([card["category"] for card in flashcards_data])))
        selected_cat = st.selectbox("📂 Lọc theo phân loại từ vựng:", categories)

        if selected_cat != "Tất cả":
            filtered_cards = [c for c in flashcards_data if c["category"] == selected_cat]
        else:
            filtered_cards = flashcards_data

        if "fc_index" not in st.session_state:
            st.session_state.fc_index = 0
        if "show_back" not in st.session_state:
            st.session_state.show_back = False

        if st.session_state.fc_index >= len(filtered_cards):
            st.session_state.fc_index = 0

        curr_card = filtered_cards[st.session_state.fc_index]

        col_fc1, col_fc2, col_fc3 = st.columns([1, 2, 1])
        with col_fc2:
            st.info(f"📌 Thẻ **{st.session_state.fc_index + 1} / {len(filtered_cards)}** — Nhóm: **{curr_card['category']}**")
            
            if not st.session_state.show_back:
                st.markdown(f"""
                <div style="background-color: #FFFFFF; border: 2px solid #2563EB; border-radius: 12px; padding: 2.5rem; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <h2 style="color: #1E3A8A; margin-bottom: 0.5rem;">{curr_card['word']}</h2>
                    <p style="color: #6B7280; font-size: 1rem;"><i>{curr_card['definition']}</i></p>
                    <p style="color: #9CA3AF; font-size: 0.85rem; margin-top: 1rem;">(Nhấp nút '🔄 Lật thẻ' bên dưới để xem nghĩa Tiếng Việt)</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background-color: #F0FDF4; border: 2px solid #22C55E; border-radius: 12px; padding: 2.5rem; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                    <h3 style="color: #166534; margin-bottom: 0.5rem;">{curr_card['vi']}</h3>
                    <p style="color: #15803D; font-size: 1.1rem;"><b>Từ gốc:</b> {curr_card['word']}</p>
                    <p style="color: #4B5563; font-size: 0.9rem;"><i>{curr_card['definition']}</i></p>
                </div>
                """, unsafe_allow_html=True)

            st.write("")
            btn_col1, btn_col2, btn_col3 = st.columns(3)
            with btn_col1:
                if st.button("⬅️ Thẻ trước", use_container_width=True):
                    st.session_state.fc_index = (st.session_state.fc_index - 1) % len(filtered_cards)
                    st.session_state.show_back = False
                    st.rerun()
            with btn_col2:
                if st.button("🔄 Lật thẻ", use_container_width=True):
                    st.session_state.show_back = not st.session_state.show_back
                    st.rerun()
            with btn_col3:
                if st.button("➡️ Thẻ sau", use_container_width=True):
                    st.session_state.fc_index = (st.session_state.fc_index + 1) % len(filtered_cards)
                    st.session_state.show_back = False
                    st.rerun()

# --- 5. GÓC LƯU Ý (WATCH OUT! CORNER) ---
elif menu_option == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.header("⚠️ Góc lưu ý B2 (Watch Out! Corner)")
    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Lỗi phổ biến Unit 1 (Present Time):</h4>
    • Không dùng thì tiếp diễn với các động từ chỉ trạng thái tinh thần/sở hữu (<i>believe, know, own, belong</i>).<br>
    • Phân biệt nét nghĩa: <i>I have a car</i> (sở hữu - đơn) vs <i>I am having lunch</i> (hành động - tiếp diễn).
    </div>
    <div class="watchout-box">
    <h4>⚠️ Lỗi phổ biến Unit 2 (Travel and Transport):</h4>
    • <b>trip</b> (chuyến đi ngắn đi rồi về) vs <b>journey</b> (hành trình di chuyển một chiều).<br>
    • <b>arrive in</b> + thành phố/quốc gia (<i>arrive in London</i>) vs <b>arrive at</b> + địa điểm nhỏ (<i>arrive at the station</i>).
    </div>
    """, unsafe_allow_html=True)

# --- 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập (Progress Report)")
    st.subheader("✅ Danh sách 28 Units & 14 Reviews:")
    
    col_p1, col_p2 = st.columns(2)
    completed_count = 0
    total_units = len(ALL_UNITS_LIST)
    
    for idx, u_name in enumerate(ALL_UNITS_LIST):
        with (col_p1 if idx % 2 == 0 else col_p2):
            checked = st.checkbox(f"{u_name}", key=f"prog_{idx}")
            if checked:
                completed_count += 1
                
    st.progress(completed_count / total_units)
    st.success(f"📈 Bạn đã hoàn thành **{completed_count} / {total_units}** bài học ({int(completed_count/total_units*100)}%).")

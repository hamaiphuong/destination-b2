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
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .explain-box {
        background-color: #F8FAFC;
        border-left: 4px solid #3B82F6;
        padding: 0.75rem 1rem;
        margin-top: 0.4rem;
        margin-bottom: 0.6rem;
        border-radius: 4px;
        font-size: 0.95rem;
    }
    .tip-box {
        background-color: #F0FDF4;
        border: 1px solid #86EFAC;
        border-left: 5px solid #22C55E;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .watchout-box {
        background-color: #FEF2F2;
        border: 1px solid #FCA5A5;
        border-left: 5px solid #EF4444;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .badge-vocab {
        background-color: #FCE7F3;
        color: #9D174D;
        padding: 0.2rem 0.6rem;
        border-radius: 0.3rem;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .card {
        background-color: #F8FAFC;
        padding: 1.2rem;
        border-radius: 0.6rem;
        border-left: 5px solid #2563EB;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
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

# Initialize Session State for Progress Tracking
if "unit_progress" not in st.session_state:
    st.session_state["unit_progress"] = {}

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
            "5. Stative Verbs & Watch out!"
        ])
        
        with tab_g1:
            st.markdown("#### 🔹 Present Simple (Thì Hiện tại Đơn)")
            g1_data = [
                {"Cách dùng B2": "Current habits (Thói quen hiện tại)", "Ví dụ minh họa": "Toby walks to work."},
                {"Cách dùng B2": "To talk about how often things happen (Tần suất)", "Ví dụ minh họa": "Angela doesn't visit us very often."},
                {"Cách dùng B2": "Permanent situations (Tình huống lâu dài)", "Ví dụ minh họa": "Carlo works in a travel agent's."},
                {"Cách dùng B2": "States (Trạng thái)", "Ví dụ minh họa chuẩn sách": "Do you have an up-to-date passport?"},
                {"Cách dùng B2": "General truths and facts (Sự thật hiển nhiên)", "Ví dụ minh họa": "Poland is in the European Union."}
            ]
            st.table(pd.DataFrame(g1_data))
            st.markdown("""
            <div class="tip-box">
            <b>💡 Watch out! Emphatic Present Simple (Hiện tại đơn nhấn mạnh):</b><br>
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
                {"Cách dùng B2": "Changing and developing situations (Sự thay đổi phát triển)", "Ví dụ minh họa": "Holidays abroad are becoming increasingly popular."},
                {"Cách dùng B2": "Annoying habits (usually with always) (Thói quen phiền phức)", "Ví dụ minh họa": "Dad is always cleaning the car when I want to use it!"}
            ]
            st.table(pd.DataFrame(g2_data))

        with tab_g3:
            st.markdown("#### 🔹 Present Perfect Simple (Thì Hiện tại Hoàn thành Đơn)")
            g3_data = [
                {"Cách dùng B2": "Situations and states that started in the past and are still true", "Ví dụ minh họa": "She's had her motorbike for over six years."},
                {"Cách dùng B2": "A series of actions continuing up to now", "Ví dụ minh họa": "We've travelled by taxi, bus, plane and train - all in the last twenty-four hours!"},
                {"Cách dùng B2": "Completed actions at a time in the past which is not mentioned", "Ví dụ minh họa": "Have you ever flown in a helicopter?"},
                {"Cách dùng B2": "Completed actions where the important thing is the present result", "Ví dụ minh họa": "I've booked the coach tickets."}
            ]
            st.table(pd.DataFrame(g3_data))

        with tab_g4:
            st.markdown("#### 🔹 Present Perfect Continuous (Thì Hiện tại Hoàn thành Tiếp diễn)")
            g4_data = [
                {"Cách dùng B2": "Actions continuing up to the present moment (Nhấn mạnh tính liên tục)", "Ví dụ minh họa": "We have been driving for hours. Can't we have a break soon?"},
                {"Cách dùng B2": "Actions stopping just before the present moment (Có dấu vết/kết quả ở hiện tại)", "Ví dụ minh họa": "I'm out of breath because I've been running to get here in time."}
            ]
            st.table(pd.DataFrame(g4_data))

        with tab_stative:
            st.markdown("#### 🔹 Stative Verbs (Động từ Chỉ Trạng thái B2)")
            st.markdown("""
            * **Thinking**: *believe, imagine, know, mean, think, understand*
            * **Existence**: *be, exist*
            * **Emotions**: *hate, like, love, need, prefer, satisfy, want*
            * **Human Senses**: *hear, see, smell, sound, taste*
            * **Appearance**: *appear, look, resemble, seem*
            * **Possession**: *belong to, consist of, have, include, involve, own*
            """)
            st.markdown("""
            <div class="watchout-box">
            <b>⚠️ Watch out! Stative vs Non-stative meanings:</b><br>
            Một số động từ trạng thái có thể dùng ở tiếp diễn khi chuyển sang nét nghĩa hành động:<br>
            • <i>Do you <b>have</b> your plane ticket with you?</i> (State: sở hữu)<br>
            • <i>Are you <b>having</b> lunch at the moment?</i> (Action: đang ăn)
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
            st.markdown("#### 🔹 Topic Vocabulary in Contrast")
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
            "Ex A", "Ex B", "Ex C", "Ex D",
            "Ex E", "Ex F", "Ex G", "Ex H",
            "Ex I", "Ex J"
        ])
        
        with st.form("unit1_full_quiz_form"):
            with tab_a:
                st.markdown("#### Exercise A: Circle the correct word or phrase")
                qa1 = st.radio("Câu 1: Elizabeth ________ to bed at around eleven o'clock.", ["usually goes", "is usually going"], index=None, key="u1_qa1")
                qa2 = st.radio("Câu 2: Dan ________ on the other phone right now.", ["talks", "is talking"], index=None, key="u1_qa2")
                qa3 = st.radio("Câu 3: We ________ any meat at the moment as we're both on a diet.", ["don't eat", "aren't eating"], index=None, key="u1_qa3")
                qa4 = st.radio("Câu 4: ________ increasingly safe?", ["Does air travel get", "Is air travel getting"], index=None, key="u1_qa4")
                qa5 = st.radio("Câu 5: My mum ________ me every weekend without fail.", ["calls", "is calling"], index=None, key="u1_qa5")
                qa6 = st.radio("Câu 6: How much ________?", ["do babysitters generally earn", "are babysitters generally earning"], index=None, key="u1_qa6")
                qa7 = st.radio("Câu 7: ________ up with excuses for not having done your homework. It's so annoying!", ["You always come", "You're always coming"], index=None, key="u1_qa7")
                qa8 = st.radio("Câu 8: I ________ out much during the week but I ________ to go out somewhere on Saturday night.", ["don't go / always try", "am not going / am always trying"], index=None, key="u1_qa8")
                qa9 = st.radio("Câu 9: No, the train ________ at Cirencester on Saturdays.", ["does stop", "is stopping"], index=None, key="u1_qa9")
                qa10 = st.radio("Câu 10: My mum ________ part in ice-skating competitions almost every weekend.", ["takes", "is taking"], index=None, key="u1_qa10")

            with tab_b:
                st.markdown("#### Exercise B: Rewrite correctly. Change the words or phrases in bold")
                qb1 = st.text_input("Câu 11: My dad **is often getting up** late on Saturday mornings.", key="u1_qb1")
                qb2 = st.text_input("Câu 12: **Are you speaking** any other languages apart from English?", key="u1_qb2")
                qb3 = st.text_input("Câu 13: **I already buy** all my Christmas presents and it's only October!", key="u1_qb3")
                qb4 = st.text_input("Câu 14: It's the first time **I'm ever having** a party at home.", key="u1_qb4")
                qb5 = st.text_input("Câu 15: Actually, I think Darren **does works** quite hard sometimes.", key="u1_qb5")
                qb6 = st.text_input("Câu 16: Carlo **is never eating** Chinese food before.", key="u1_qb6")
                qb7 = st.text_input("Câu 17: Sean **already books** a table for tonight.", key="u1_qb7")
                qb8 = st.text_input("Câu 18: **Needs Melanie** any help painting her new flat?", key="u1_qb8")

            with tab_c:
                st.markdown("#### Exercise C: Complete using the correct form of the verb in brackets")
                qc1 = st.text_input("Câu 19: It's the first time ________ (I / ever / eat) octopus!", key="u1_qc1")
                qc2 = st.text_input("Câu 20: Sandy ________ (not / see) his sister since she went to university.", key="u1_qc2")
                qc3 = st.text_input("Câu 21: They ________ (go) on holiday to Spain and won't be back until the end of the month.", key="u1_qc3")
                qc4 = st.text_input("Câu 22: Poor Tracy! She ________ (write) that essay for hours now and she still hasn't finished!", key="u1_qc4")
                qc5 = st.text_input("Câu 23: ________ (you / ever / meet) anyone famous?", key="u1_qc5")
                qc6 = st.text_input("Câu 24: ________ (I / try) to get in touch with Jenny all morning but I can't find her anywhere.", key="u1_qc6")
                qc7 = st.text_input("Câu 25: ________ (I / not finish) the book yet so I can't tell you what happens.", key="u1_qc7")
                qc8 = st.text_input("Câu 26: ________ (you / already / decide) where you're going this summer?", key="u1_qc8")
                qc9 = st.text_input("Câu 27: ________ (We / live) here for the last six years.", key="u1_qc9")
                qc10 = st.text_input("Câu 28: ________ (I / never / hear) such nonsense!", key="u1_qc10")

            with tab_d:
                st.markdown("#### Exercise D: Complete using the words in the box")
                st.caption("Box: already | before | ever | for | just | rarely | since | so | still | yet")
                qd1 = st.radio("Câu 29: Have you ________ dreamt of winning the lottery?", ["already", "ever", "never", "yet"], index=None, key="u1_qd1")
                qd2 = st.radio("Câu 30: I haven't worked out how to set the timer on the video ________.", ["already", "still", "yet", "since"], index=None, key="u1_qd2")
                qd3 = st.radio("Câu 31: My dad's lived in the same house ________ he was born.", ["for", "since", "from", "ever"], index=None, key="u1_qd3")
                qd4 = st.radio("Câu 32: The film's only been on ________ a couple of minutes.", ["for", "since", "so", "still"], index=None, key="u1_qd4")
                qd5 = st.radio("Câu 33: Bruce has knocked three men out of the competition ________ far.", ["so", "for", "already", "just"], index=None, key="u1_qd5")
                qd6 = st.radio("Câu 34: I ________ get the chance to get any exercise - I'm just too busy.", ["rarely", "still", "yet", "already"], index=None, key="u1_qd6")
                qd7 = st.radio("Câu 35: He's only ________ got home.", ["just", "yet", "already", "ever"], index=None, key="u1_qd7")
                qd8 = st.radio("Câu 36: It's eleven o'clock and Todd ________ hasn't come home. Where could he be?", ["still", "yet", "already", "so"], index=None, key="u1_qd8")
                qd9 = st.radio("Câu 37: I've never met Ruth ________. What's she like?", ["before", "yet", "already", "ever"], index=None, key="u1_qd9")
                qd10 = st.radio("Câu 38: Have you finished ________? That was quick.", ["already", "yet", "still", "before"], index=None, key="u1_qd10")

            with tab_e:
                st.markdown("#### Exercise E: Choose the correct answer")
                qe1 = st.radio("Câu 39: Ian ________ a shower at the moment, so could you call back in about half an hour?", ["A. takes", "B. is taking", "C. has taken", "D. has been taking"], index=None, key="u1_qe1")
                qe2 = st.radio("Câu 40: ________ to Ipswich before?", ["A. Do you ever go", "B. Are you ever going", "C. Have you ever been", "D. Have you ever been going"], index=None, key="u1_qe2")
                qe3 = st.radio("Câu 41: I ________ to all the local newspapers and TV stations to complain.", ["A. already write", "B. already writing", "C. have already written", "D. have already been writing"], index=None, key="u1_qe3")
                qe4 = st.radio("Câu 42: ________ TV for the last four hours? Turn it off and get some exercise!", ["A. Do you watch", "B. Are you watching", "C. Watched you", "D. Have you been watching"], index=None, key="u1_qe4")
                qe5 = st.radio("Câu 43: Eric, ________ hockey competitively or just for fun?", ["A. do you usually play", "B. are you usually playing", "C. have you usually played", "D. have you usually been playing"], index=None, key="u1_qe5")
                qe6 = st.radio("Câu 44: That's the first time ________ an answer right today!", ["A. I get", "B. I am getting", "C. I have got", "D. I have been getting"], index=None, key="u1_qe6")
                qe7 = st.radio("Câu 45: Jessica has ________ left, I'm afraid.", ["A. already", "B. yet", "C. still", "D. so far"], index=None, key="u1_qe7")
                qe8 = st.radio("Câu 46: Dan ________ in the living room while we redecorate his bedroom.", ["A. sleeps", "B. is sleeping", "C. has slept", "D. does sleep"], index=None, key="u1_qe8")
                qe9 = st.radio("Câu 47: Unfortunately, Simone ________ a day off very often.", ["A. doesn't get", "B. isn't getting", "C. hasn't got", "D. hasn't been getting"], index=None, key="u1_qe9")
                qe10 = st.radio("Câu 48: Actually, I ________ a cup of tea first thing every morning but then I switch to coffee.", ["A. do drink", "B. am drinking", "C. have drunk", "D. have been drinking"], index=None, key="u1_qe10")

            with tab_f:
                st.markdown("#### Exercise F: Complete using the correct form of the words in the box (Ancient Aviators)")
                st.caption("Box: be | disagree | do | include | know | look | see | seem | understand")
                qf1 = st.text_input("Gap (1): Everyone ________ that humans have been flying for only a few hundred years.", key="u1_qf1")
                qf2 = st.text_input("Gap (2): But ________ it possible that ancient civilizations also had the ability and technology to fly?", key="u1_qf2")
                qf3 = st.text_input("Gap (3): On the ground, they just ________ like straight lines.", key="u1_qf3")
                qf4 = st.text_input("Gap (4): But when you ________ them from the air...", key="u1_qf4")
                qf5 = st.text_input("Gap (5): ...you ________ exactly what they are.", key="u1_qf5")
                qf6 = st.text_input("Gap (6): The pictures ________ animals, birds and symbols.", key="u1_qf6")
                qf7 = st.text_input("Gap (7): One bizarre theory, which most mainstream scientists ________ with...", key="u1_qf7")
                qf8 = st.text_input("Gap (8): It ________ incredible...", key="u1_qf8")
                qf9 = st.text_input("Gap (9): ...but a few people ________ believe it's possible.", key="u1_qf9")

            with tab_g:
                st.markdown("#### Exercise G: Match to make sentences")
                qg1 = st.radio("1. I think ________", ["A. darker hair than her sister.", "B. I'm going to buy the new Racetrack CD.", "C. a haircut at the moment.", "D. for his glasses."], index=None, key="u1_qg1")
                qg2 = st.radio("2. I'm thinking ________", ["E. not old enough to drive a car.", "F. of getting Dad a CD for his birthday.", "G. very annoying at the moment!", "H. like he needs a holiday!"], index=None, key="u1_qg2")
                qg3 = st.radio("3. Phil's looking ________", ["A. darker hair", "C. a haircut", "D. for his glasses. Have you seen them?", "G. very annoying"], index=None, key="u1_qg3")
                qg4 = st.radio("4. Phil looks ________", ["B. I'm going", "E. not old enough", "F. of getting", "H. like he needs a holiday!"], index=None, key="u1_qg4")
                qg5 = st.radio("5. Claire has ________", ["A. darker hair than her sister.", "B. I'm going", "C. a haircut", "D. for his glasses"], index=None, key="u1_qg5")
                qg6 = st.radio("6. Claire is having ________", ["B. I'm going", "C. a haircut at the moment.", "E. not old enough", "F. of getting"], index=None, key="u1_qg6")
                qg7 = st.radio("7. Andy is ________", ["A. darker hair", "D. for his glasses", "E. not old enough to drive a car.", "G. very annoying"], index=None, key="u1_qg7")
                qg8 = st.radio("8. Andy is being ________", ["C. a haircut", "E. not old enough", "F. of getting", "G. very annoying at the moment!"], index=None, key="u1_qg8")

            with tab_h:
                st.markdown("#### Exercise H: Find the extra word in each line (International Friends)")
                qh1 = st.text_input("Line 1: I've been to travelling round Europe all summer.", key="u1_qh1")
                qh2 = st.text_input("Line 2: It's the first time I've ever been going abroad...", key="u1_qh2")
                qh3 = st.text_input("Line 3: ...and I have to also made loads of new friends.", key="u1_qh3")
                qh4 = st.text_input("Line 4: I've been decided to stay in touch with them now I'm back.", key="u1_qh4")
                qh5 = st.text_input("Line 5: She was making on holiday too.", key="u1_qh5")
                qh6 = st.text_input("Line 6: We now send text messages and to each other all time.", key="u1_qh6")
                qh7 = st.text_input("Line 7: ...I'm planning to have visit her in France next year...", key="u1_qh7")
                qh8 = st.text_input("Line 8: I hope I can, I am love meeting people from other countries...", key="u1_qh8")
                qh9 = st.text_input("Line 9: ...I want to have had lots of friends from all over the world!", key="u1_qh9")
                qh10 = st.text_input("Line 10: Travelling certainly broadens the mind but it also is broadens your circle...", key="u1_qh10")

            with tab_i:
                st.markdown("#### Exercise I: Write one word in each gap (Holiday Blues)")
                qi1 = st.text_input("Gap (1): You've ________ looking at that timetable for the last ten minutes.", key="u1_qi1")
                qi2 = st.text_input("Gap (2): 'I ________ wish you'd be quiet!'", key="u1_qi2")
                qi3 = st.text_input("Gap (3): 'I've ________ a splitting headache thanks to you!'", key="u1_qi3")
                qi4 = st.text_input("Gap (4): 'You're both ________ very silly.'", key="u1_qi4")
                qi5 = st.text_input("Gap (5): '________ is no point at all in blaming each other.'", key="u1_qi5")
                qi6 = st.text_input("Gap (6): 'You ________ quite right, darling.'", key="u1_qi6")
                qi7 = st.text_input("Gap (7): 'I ________ sorry,' said Sheila.", key="u1_qi7")
                qi8 = st.text_input("Gap (8): 'Well, it ________ like we...'", key="u1_qi8")
                qi9 = st.text_input("Gap (9): '... ________ definitely missed the last train today.'", key="u1_qi9")
                qi10 = st.text_input("Gap (10): 'I ________ so,' said Sheila.", key="u1_qi10")
                qi11 = st.text_input("Gap (11): 'Well, one thing is ________ in doubt,' said Matt.", key="u1_qi11")
                qi12 = st.text_input("Gap (12): 'This is the worst holiday we've ________ been on,' said Matt.", key="u1_qi12")

            with tab_j:
                st.markdown("#### Exercise J: Complete each second sentence using the word given")
                qj1 = st.text_input("Câu 1: What is the price of the tickets, Jimmy? (much) -> How ________________________, Jimmy?", key="u1_qj1")
                qj2 = st.text_input("Câu 2: Are these your trainers? (to) -> Do ________________________ you?", key="u1_qj2")
                qj3 = st.text_input("Câu 3: Sasha's not keen on team sports at all. (like) -> Sasha ________________________ team sports at all.", key="u1_qj3")
                qj4 = st.text_input("Câu 4: It's only her second time in a recording studio. (been) -> She ________________________ in a recording studio once before.", key="u1_qj4")
                qj5 = st.text_input("Câu 5: We got here three hours ago. (have) -> We ________________________ three hours.", key="u1_qj5")
                qj6 = st.text_input("Câu 6: I started writing this hours ago and it's still not right. (writing) -> I ________________________ hours and it's still not right.", key="u1_qj6")
                qj7 = st.text_input("Câu 7: This is my first experience of flying alone. (time) -> It is the first ________________________ alone.", key="u1_qj7")
                qj8 = st.text_input("Câu 8: Sharon's in the bath at the moment. (a) -> Sharon ________________________ at the moment.", key="u1_qj8")
                qj9 = st.text_input("Câu 9: Paul enjoys surprises apart from on his birthday. (does) -> Paul ________________________ surprises, just not on his birthday!", key="u1_qj9")

            submit_u1_quiz = st.form_submit_button("🚀 Kiểm tra Đáp án Unit 1")

        if submit_u1_quiz:
            score = 0
            total_qs = 96  # Thay bằng tổng số câu hỏi thực tế của Unit
            st.markdown("### 📊 Kết quả & Giải thích Chi tiết Unit 1")

            # Function helper for evaluating inputs
            def eval_answer(q_id, user_val, correct_vals, explanation):
                if user_val is None or (isinstance(user_val, str) and user_val.strip() == ""):
                    st.warning(f"⚠️ **{q_id}: Chưa trả lời / Bỏ trống.** Đáp án chuẩn: **{correct_vals[0]}**")
                    st.markdown(f'<div class="explain-box">💡 <i>Giải thích:</i> {explanation}</div>', unsafe_allow_html=True)
                    return 0
                
                if isinstance(user_val, str):
                    u_clean = user_val.strip().lower()
                    is_correct = any(u_clean == c.lower() or c.lower() in u_clean for c in correct_vals)
                else:
                    is_correct = False
                    
                if is_correct:
                    st.success(f"✅ **{q_id}: Chính xác!** ({user_val})")
                    return 1
                else:
                    st.error(f"❌ **{q_id}: Chưa chính xác.** (Bạn nhập/chọn: `{user_val}`) ➔ Đáp án chuẩn: **{correct_vals[0]}**")
                    st.markdown(f'<div class="explain-box">💡 <i>Giải thích:</i> {explanation}</div>', unsafe_allow_html=True)
                    return 0

            # Ex A
            score += eval_answer("Ex A - Câu 1", qa1, ["usually goes"], "Trạng từ chỉ tần suất 'usually' đi với Present Simple diễn tả thói quen.")
            score += eval_answer("Ex A - Câu 2", qa2, ["is talking"], "'right now' là dấu hiệu nhận biết thì Present Continuous.")
            score += eval_answer("Ex A - Câu 3", qa3, ["aren't eating"], "'at the moment' diễn tả hành động đang diễn ra tạm thời ở hiện tại.")
            score += eval_answer("Ex A - Câu 4", qa4, ["Is air travel getting"], "Diễn tả sự thay đổi/phát triển kéo dài (changing & developing situation).")
            score += eval_answer("Ex A - Câu 5", qa5, ["calls"], "'every weekend' chỉ lịch trình/thói quen lặp đi lặp lại.")
            score += eval_answer("Ex A - Câu 6", qa6, ["do babysitters generally earn"], "Hỏi về sự thật/thói quen chung chung.")
            score += eval_answer("Ex A - Câu 7", qa7, ["You're always coming"], "Present Continuous + 'always' phàn nàn về thói quen phiền phức.")
            score += eval_answer("Ex A - Câu 8", qa8, ["don't go / always try"], "Thói quen sinh hoạt lặp đi lặp lại ở hiện tại.")
            score += eval_answer("Ex A - Câu 9", qa9, ["does stop"], "Dùng Emphatic Present Simple ('does stop') để nhấn mạnh sự thật.")
            score += eval_answer("Ex A - Câu 10", qa10, ["takes"], "'almost every weekend' diễn tả thói quen lặp đi lặp lại.")

            # Ex B
            score += eval_answer("Ex B - Câu 11", qb1, ["often gets up"], "'often' chỉ thói quen lặp đi lặp lại nên dùng Present Simple.")
            score += eval_answer("Ex B - Câu 12", qb2, ["Do you speak"], "Hỏi về khả năng/ngôn ngữ biết được dùng Present Simple.")
            score += eval_answer("Ex B - Câu 13", qb3, ["I've already bought", "I have already bought"], "Trạng từ 'already' diễn tả hành động đã hoàn thành dùng Present Perfect.")
            score += eval_answer("Ex B - Câu 14", qb4, ["I've ever had", "I have ever had"], "Cấu trúc 'It's the first time + Present Perfect Simple'.")
            score += eval_answer("Ex B - Câu 15", qb5, ["works", "does work"], "Động từ theo sau 'does' nhấn mạnh phải ở dạng nguyên mẫu 'work'.")
            score += eval_answer("Ex B - Câu 16", qb6, ["has never eaten"], "Diễn tả trải nghiệm từ trước tới nay dùng Present Perfect Simple.")
            score += eval_answer("Ex B - Câu 17", qb7, ["has already booked", "Sean has already booked"], "'already' đi với Present Perfect Simple.")
            score += eval_answer("Ex B - Câu 18", qb8, ["Does Melanie need"], "Trợ động từ câu hỏi thì Present Simple là 'Does + S + V-bare'.")

            # Ex C
            score += eval_answer("Ex C - Câu 19", qc1, ["I've ever eaten", "I have ever eaten"], "Cấu trúc 'It's the first time + Present Perfect'.")
            score += eval_answer("Ex C - Câu 20", qc2, ["hasn't seen", "has not seen"], "Mốc thời gian 'since' đi với Present Perfect.")
            score += eval_answer("Ex C - Câu 21", qc3, ["have gone", "'ve gone"], "Hành động đã đi chưa về (họ đang ở Tây Ban Nha).")
            score += eval_answer("Ex C - Câu 22", qc4, ["has been writing", "'s been writing"], "Nhấn mạnh thời lượng kéo dài 'for hours now'.")
            score += eval_answer("Ex C - Câu 23", qc5, ["Have you ever met"], "Hỏi về trải nghiệm với 'ever'.")
            score += eval_answer("Ex C - Câu 24", qc6, ["I've been trying", "I have been trying"], "Nhấn mạnh quá trình liên tục 'all morning'.")
            score += eval_answer("Ex C - Câu 25", qc7, ["I haven't finished", "I have not finished"], "Chưa hoàn thành đi với 'yet' ở Present Perfect.")
            score += eval_answer("Ex C - Câu 26", qc8, ["Have you already decided"], "Hỏi về quyết định đã làm xong đi với 'already'.")
            score += eval_answer("Ex C - Câu 27", qc9, ["We've lived", "We've been living", "We have lived"], "Kéo dài từ quá khứ đến nay với 'for the last six years'.")
            score += eval_answer("Ex C - Câu 28", qc10, ["I've never heard", "I have never heard"], "Trải nghiệm chưa từng làm với 'never'.")

            # Ex D
            score += eval_answer("Ex D - Câu 29", qd1, ["ever"], "'Have you ever dreamt...' hỏi trải nghiệm.")
            score += eval_answer("Ex D - Câu 30", qd2, ["yet"], "'yet' đứng cuối câu phủ định.")
            score += eval_answer("Ex D - Câu 31", qd3, ["since"], "'since he was born' chỉ mốc thời gian.")
            score += eval_answer("Ex D - Câu 32", qd4, ["for"], "'for a couple of minutes' chỉ khoảng thời gian.")
            score += eval_answer("Ex D - Câu 33", qd5, ["so"], "Cụm 'so far' nghĩa là cho đến nay.")
            score += eval_answer("Ex D - Câu 34", qd6, ["rarely"], "Chỉ tần suất hiếm khi.")
            score += eval_answer("Ex D - Câu 35", qd7, ["just"], "'just' diễn tả vừa mới xảy ra.")
            score += eval_answer("Ex D - Câu 36", qd8, ["still"], "'still' nhấn mạnh việc vẫn chưa xảy ra.")
            score += eval_answer("Ex D - Câu 37", qd9, ["before"], "'before' đứng cuối câu mang nghĩa trước đây.")
            score += eval_answer("Ex D - Câu 38", qd10, ["already"], "Diễn tả sự ngạc nhiên vì hoàn thành quá nhanh.")

            # Ex E
            score += eval_answer("Ex E - Câu 39", qe1, ["B. is taking"], "'at the moment' chia Present Continuous.")
            score += eval_answer("Ex E - Câu 40", qe2, ["C. Have you ever been"], "Hỏi trải nghiệm với 'before'.")
            score += eval_answer("Ex E - Câu 41", qe3, ["C. have already written"], "Đã viết xong gửi đi dùng Present Perfect.")
            score += eval_answer("Ex E - Câu 42", qe4, ["D. Have you been watching"], "Nhấn mạnh hành động xem liên tục 'for the last four hours'.")
            score += eval_answer("Ex E - Câu 43", qe5, ["A. do you usually play"], "Hỏi về thói quen chơi thể thao.")
            score += eval_answer("Ex E - Câu 44", qe6, ["C. I have got"], "Cấu trúc 'That's the first time + Present Perfect'.")
            score += eval_answer("Ex E - Câu 45", qe7, ["A. already"], "Trạng từ 'already' đứng giữa 'has' và V3.")
            score += eval_answer("Ex E - Câu 46", qe8, ["B. is sleeping"], "Tình huống tạm thời kéo dài ở hiện tại.")
            score += eval_answer("Ex E - Câu 47", qe9, ["A. doesn't get"], "'very often' chia Present Simple.")
            score += eval_answer("Ex E - Câu 48", qe10, ["A. do drink"], "Emphatic Present Simple nhấn mạnh thói quen hàng ngày.")

            # Ex F
            score += eval_answer("Ex F - Gap 1", qf1, ["knows"], "Sự thật mọi người đều biết.")
            score += eval_answer("Ex F - Gap 2", qf2, ["is"], "Cấu trúc 'Is it possible...'.")
            score += eval_answer("Ex F - Gap 3", qf3, ["look"], "Trông giống như ('look like').")
            score += eval_answer("Ex F - Gap 4", qf4, ["see"], "Nhìn thấy từ trên cao.")
            score += eval_answer("Ex F - Gap 5", qf5, ["understand", "know", "see"], "Hiểu/rõ được ý nghĩa.")
            score += eval_answer("Ex F - Gap 6", qf6, ["include"], "Bao gồm động vật và biểu tượng.")
            score += eval_answer("Ex F - Gap 7", qf7, ["disagree"], "Không đồng tình ('disagree with').")
            score += eval_answer("Ex F - Gap 8", qf8, ["seems"], "Có vẻ như không thể tin được.")
            score += eval_answer("Ex F - Gap 9", qf9, ["do"], "Nhấn mạnh 'do believe' (thực sự tin).")

            # Ex G
            score += eval_answer("Ex G - Q1", qg1, ["B. I'm going to buy the new Racetrack CD."], "'I think' đi với mệnh đề suy nghĩ.")
            score += eval_answer("Ex G - Q2", qg2, ["F. of getting Dad a CD for his birthday."], "'I'm thinking of + V-ing'.")
            score += eval_answer("Ex G - Q3", qg3, ["D. for his glasses. Have you seen them?"], "'look for' tìm kiếm kính.")
            score += eval_answer("Ex G - Q4", qg4, ["H. like he needs a holiday!"], "'look like' trông có vẻ như.")
            score += eval_answer("Ex G - Q5", qg5, ["A. darker hair than her sister."], "'have' chỉ đặc điểm sở hữu.")
            score += eval_answer("Ex G - Q6", qg6, ["C. a haircut at the moment."], "'is having a haircut' chỉ hành động cắt tóc.")
            score += eval_answer("Ex G - Q7", qg7, ["E. not old enough to drive a car."], "'be' chỉ bản chất/độ tuổi.")
            score += eval_answer("Ex G - Q8", qg8, ["G. very annoying at the moment!"], "'is being' chỉ hành vi tạm thời gây phiền.")

            # Ex H
            score += eval_answer("Ex H - Line 1", qh1, ["to"], "Thừa từ 'to' ('been travelling').")
            score += eval_answer("Ex H - Line 2", qh2, ["going"], "Thừa từ 'going' ('been abroad').")
            score += eval_answer("Ex H - Line 3", qh3, ["to"], "Thừa từ 'to' ('have also made').")
            score += eval_answer("Ex H - Line 4", qh4, ["decided", "been"], "Thừa từ 'been' ('I have decided').")
            score += eval_answer("Ex H - Line 5", qh5, ["making"], "Thừa từ 'making' ('was on holiday').")
            score += eval_answer("Ex H - Line 6", qh6, ["to"], "Thừa từ 'to' ('text messages each other').")
            score += eval_answer("Ex H - Line 7", qh7, ["have"], "Thừa từ 'have' ('planning to visit').")
            score += eval_answer("Ex H - Line 8", qh8, ["am"], "Thừa từ 'am' ('I love meeting').")
            score += eval_answer("Ex H - Line 9", qh9, ["had"], "Thừa từ 'had' ('want to have lots').")
            score += eval_answer("Ex H - Line 10", qh10, ["is"], "Thừa từ 'is' ('it also broadens').")

            # Ex I
            score += eval_answer("Ex I - Gap 1", qi1, ["been"], "'You've been looking...'")
            score += eval_answer("Ex I - Gap 2", qi2, ["do"], "'I do wish...' nhấn mạnh.")
            score += eval_answer("Ex I - Gap 3", qi3, ["got", "have"], "'I've got a splitting headache'.")
            score += eval_answer("Ex I - Gap 4", qi4, ["being"], "'You're both being very silly'.")
            score += eval_answer("Ex I - Gap 5", qi5, ["There"], "'There is no point...'.")
            score += eval_answer("Ex I - Gap 6", qi6, ["are"], "'You are quite right'.")
            score += eval_answer("Ex I - Gap 7", qi7, ["am"], "'I am sorry'.")
            score += eval_answer("Ex I - Gap 8", qi8, ["looks"], "'it looks like...'.")
            score += eval_answer("Ex I - Gap 9", qi9, ["have"], "'we have definitely missed...'.")
            score += eval_answer("Ex I - Gap 10", qi10, ["think", "suppose"], "'I think so'.")
            score += eval_answer("Ex I - Gap 11", qi11, ["not"], "'one thing is not in doubt'.")
            score += eval_answer("Ex I - Gap 12", qi12, ["ever"], "'worst holiday we've ever been on'.")

            # Ex J
            score += eval_answer("Ex J - Câu 1", qj1, ["much do the tickets cost", "much are the tickets"], "Cấu trúc hỏi giá tiền với 'much'.")
            score += eval_answer("Ex J - Câu 2", qj2, ["these trainers belong to"], "Thuộc về ai dùng 'belong to'.")
            score += eval_answer("Ex J - Câu 3", qj3, ["does not like", "doesn't like"], "Thích cái gì dùng 'like'.")
            score += eval_answer("Ex J - Câu 4", qj4, ["has only been", "'s only been"], "Đã ở phòng thu lần nào dùng 'has been'.")
            score += eval_answer("Ex J - Câu 5", qj5, ["have been here for", "'ve been here for"], "Đã ở đây bao lâu dùng Present Perfect + 'for'.")
            score += eval_answer("Ex J - Câu 6", qj6, ["have been writing this for", "'ve been writing this for"], "Viết liên tục bao nhiêu giờ dùng Present Perfect Continuous.")
            score += eval_answer("Ex J - Câu 7", qj7, ["time I have flown", "time I've flown", "time that I have flown"], "Lần đầu làm gì dùng 'first time I have V3'.")
            score += eval_answer("Ex J - Câu 8", qj8, ["is having a bath", "'s having a bath"], "Đang tắm dùng 'is having a bath'.")
            score += eval_answer("Ex J - Câu 9", qj9, ["does enjoy"], "Nhấn mạnh việc thực sự thích dùng 'does enjoy'.")
    	    # 3. KẾT THÚC: Tính % và tự động lưu vào Progress Report
            pct = int((score / total_qs) * 100)
            st.info(f"🏆 Điểm số Unit 1 của bạn: **{score}/{total_qs}** ({pct}%)")

            # Lưu kết quả để mục Progress Report tự động nhận điểm %:
            if "completed_units" not in st.session_state:
            st.session_state.completed_units = {}
        
    	    st.session_state.completed_units["Unit 1: Grammar - Present time"] = {
        	"score": score,
        	"total": total_qs,
        	"pct": pct
    	    }

    elif "Unit 2" in selected_quiz_unit:
        st.subheader("✍️ Unit 2: Vocabulary - Travel and Transport - Full Practice Exercises")
        st.info("Hãy hoàn thành các bài tập bên dưới.")
        
        tab_v_a, tab_v_b, tab_v_c, tab_v_d, tab_v_e, tab_v_f, tab_v_g, tab_v_h, tab_v_i = st.tabs([
            "Ex A (MCQs)", "Ex B (Circle)", "Ex C (Phrasal Box)", "Ex D (Phrasal Replace)",
            "Ex E (Collocations)", "Ex F (Patterns)", "Ex G (Extra Word)", "Ex H (Word Form Box)",
            "Ex I (Word Form Change)"
        ])

        with st.form("unit2_full_quiz_form"):
            with tab_v_a:
                st.markdown("#### Exercise A: Choose the correct answer")
                qva1 = st.radio("Câu 1: You need a passport to cross the ________ between Mexico and the United States.", ["A. edge", "B. line", "C. border", "D. rim"], index=None, key="u2_qva1")
                qva2 = st.radio("Câu 2: The hotel where we are ________ is quite luxurious.", ["A. living", "B. remaining", "C. existing", "D. staying"], index=None, key="u2_qva2")
                qva3 = st.radio("Câu 3: When you ________ your destination, your tour guide will meet you at the airport.", ["A. arrive", "B. get", "C. reach", "D. achieve"], index=None, key="u2_qva3")
                qva4 = st.radio("Câu 4: It can be quite busy here during the tourist ________.", ["A. season", "B. period", "C. phase", "D. stage"], index=None, key="u2_qva4")
                qva5 = st.radio("Câu 5: David ________ me to the train station every morning.", ["A. goes", "B. takes", "C. has", "D. makes"], index=None, key="u2_qva5")
                qva6 = st.radio("Câu 6: I always enjoy our school ________ to France.", ["A. excursion", "B. journey", "C. trip", "D. travel"], index=None, key="u2_qva6")
                qva7 = st.radio("Câu 7: Hurry up, or we'll ________ the bus!", ["A. avoid", "B. miss", "C. drop", "D. lose"], index=None, key="u2_qva7")
                qva8 = st.radio("Câu 8: The brochure says that the hotel has a great ________ of the sea.", ["A. appearance", "B. look", "C. sight", "D. view"], index=None, key="u2_qva8")
                qva9 = st.radio("Câu 9: I must remember to ________ a souvenir back from Spain for my grandmother.", ["A. go", "B. take", "C. bring", "D. keep"], index=None, key="u2_qva9")
                qva10 = st.radio("Câu 10: The ________ from London to Berlin is about 919 kilometres.", ["A. measure", "B. length", "C. gap", "D. distance"], index=None, key="u2_qva10")
                qva11 = st.radio("Câu 11: Make sure you ________ a hotel before you come to our island, especially in the summer.", ["A. book", "B. keep", "C. put", "D. take"], index=None, key="u2_qva11")
                qva12 = st.radio("Câu 12: I live in Barcelona, but my ________ town is Madrid.", ["A. birth", "B. home", "C. native", "D. origin"], index=None, key="u2_qva12")

            with tab_v_b:
                st.markdown("#### Exercise B: Circle the correct word")
                qvb1 = st.radio("Câu 13: I hope to go on a trip round the ________ one day.", ["world", "earth"], index=None, key="u2_qvb1")
                qvb2 = st.radio("Câu 14: You learn a lot about the local ________ by speaking to local people.", ["territory", "area"], index=None, key="u2_qvb2")
                qvb3 = st.radio("Câu 15: It's good to have someone to ________ you when you are on holiday.", ["lead", "guide"], index=None, key="u2_qvb3")
                qvb4 = st.radio("Câu 16: I get the train to work every day and the ________ is quite expensive.", ["fare", "fee"], index=None, key="u2_qvb4")
                qvb5 = st.radio("Câu 17: Captain Cook discovered Australia on a ________ to the Pacific.", ["voyage", "travel"], index=None, key="u2_qvb5")
                qvb6 = st.radio("Câu 18: Most tourist attractions in London charge an admission ________.", ["fee", "ticket"], index=None, key="u2_qvb6")
                qvb7 = st.radio("Câu 19: The sunset over Niagara Falls really is a magnificent ________.", ["look", "sight"], index=None, key="u2_qvb7")

            with tab_v_c:
                st.markdown("#### Exercise C: Complete using the correct form of the words in the box (Phrasal Verbs)")
                st.caption("Box: catch | check | get | go | make | pick | pull | see")
                qvc1 = st.text_input("Câu 20: Let's go to the airport to ________ Grandpa off when he flies back home.", key="u2_qvc1")
                qvc2 = st.text_input("Câu 21: If it starts to rain, ________ for a nearby cave to wait for it to pass.", key="u2_qvc2")
                qvc3 = st.text_input("Câu 22: We would like to remind all guests that they must ________ out before midday.", key="u2_qvc3")
                qvc4 = st.text_input("Câu 23: Please ________ in and stop so that I can buy something to drink.", key="u2_qvc4")
                qvc5 = st.text_input("Câu 24: Every Saturday night my dad ________ us up outside the cinema.", key="u2_qvc5")
                qvc6 = st.text_input("Câu 25: I think the neighbours have ________ away for the weekend.", key="u2_qvc6")
                qvc7 = st.text_input("Câu 26: John's up ahead so Greg is pedalling fast to ________ up with him.", key="u2_qvc7")
                qvc8 = st.text_input("Câu 27: We're going on holiday tomorrow, but we'll call you when we ________ back.", key="u2_qvc8")

            with tab_v_d:
                st.markdown("#### Exercise D: Write a phrasal verb in the correct form to replace the words in italics")
                qvd1 = st.text_input("Câu 28: We can *start our journey* ________ towards the mountains at dawn.", key="u2_qvd1")
                qvd2 = st.text_input("Câu 29: Dad fetched the luggage while Mum *registered* ________ at the hotel.", key="u2_qvd2")
                qvd3 = st.text_input("Câu 30: I asked the taxi driver to *let me get out* ________ outside the train station.", key="u2_qvd3")
                qvd4 = st.text_input("Câu 31: Oh, no! I've forgotten my passport! We'll have to *go back* ________ and get it!", key="u2_qvd4")
                qvd5 = st.text_input("Câu 32: The most exciting moment is when the plane *leaves the ground* ________.", key="u2_qvd5")
                qvd6 = st.text_input("Câu 33: Stop the car! I think we've *hit* ________ a dog.", key="u2_qvd6")
                qvd7 = st.text_input("Câu 34: I don't think a horse can ever *stay at the same speed as* ________ a car.", key="u2_qvd7")

            with tab_v_e:
                st.markdown("#### Exercise E: Write one word in each gap (Phrases and Collocations)")
                qve1 = st.text_input("Câu 35: The speed ________ in towns is 50 km/h and you shouldn't go faster than that.", key="u2_qve1")
                qve2 = st.text_input("Câu 36: Why don't we ________ the scenic route along the coast?", key="u2_qve2")
                qve3 = st.text_input("Câu 37: If you buy your plane ticket ________ advance, it's often cheaper than if you wait.", key="u2_qve3")
                qve4 = st.text_input("Câu 38: I can't remember the name of the hotel we stayed at off the ________ of my head.", key="u2_qve4")
                qve5 = st.text_input("Câu 39: I'm sorry I'm late! I ________ my way and had to ask for directions.", key="u2_qve5")
                qve6 = st.text_input("Câu 40: My mum's away in Germany on a business ________ at the moment.", key="u2_qve6")
                qve7 = st.text_input("Câu 41: The bank? Well, turn left here, then go ________ ahead for a kilometre and it's on the left.", key="u2_qve7")
                qve8 = st.text_input("Câu 42: If you look on your left-hand ________ as we turn this corner, you'll see Big Ben.", key="u2_qve8")
                qve9 = st.text_input("Câu 43: I'll look round the shops in the morning and then ________ sightseeing in the afternoon.", key="u2_qve9")
                qve10 = st.text_input("Câu 44: My grandma hasn't driven since she ________ an accident last year.", key="u2_qve10")
                qve11 = st.text_input("Câu 45: I love visiting foreign places, ________ the sights and learning about other cultures.", key="u2_qve11")
                qve12 = st.text_input("Câu 46: During the 70s, many British people started to go ________ holiday to Spain.", key="u2_qve12")
                qve13 = st.text_input("Câu 47: While you're in London, you should take a tour ________ the Houses of Parliament.", key="u2_qve13")

            with tab_v_f:
                st.markdown("#### Exercise F: Choose the correct answer (Word Patterns)")
                qvf1 = st.radio("Câu 48: I've always dreamt ________ China.", ["A. to visit", "B. of visiting", "C. I visit", "D. visit"], index=None, key="u2_qvf1")
                qvf2 = st.radio("Câu 49: The travel agency is arranging for us ________ at a really nice hotel.", ["A. stay", "B. of staying", "C. to stay", "D. staying"], index=None, key="u2_qvf2")
                qvf3 = st.radio("Câu 50: My dad says he always regrets ________ more.", ["A. to not travel", "B. not travelling", "C. he not travel", "D. of not travelling"], index=None, key="u2_qvf3")
                qvf4 = st.radio("Câu 51: John seems keen ________ how to drive as soon as he can.", ["A. of learning", "B. he learn", "C. for learn", "D. to learn"], index=None, key="u2_qvf4")
                qvf5 = st.radio("Câu 52: Now, class, I'd like you all to write ________ a description of your last holiday.", ["A. me", "B. to me", "C. it me", "D. about me"], index=None, key="u2_qvf5")
                qvf6 = st.radio("Câu 53: When you arrive ________, have your passport ready.", ["A. to the airport", "B. in the airport", "C. on the airport", "D. at the airport"], index=None, key="u2_qvf6")
                qvf7 = st.radio("Câu 54: The Joneses have invited us ________ to Australia with them this summer.", ["A. going", "B. for going", "C. about going", "D. to go"], index=None, key="u2_qvf7")
                qvf8 = st.radio("Câu 55: The in-flight entertainment may differ ________ that advertised.", ["A. to", "B. from", "C. in", "D. at"], index=None, key="u2_qvf8")

            with tab_v_g:
                st.markdown("#### Exercise G: Find the extra word in each line (The Cancelled Trip)")
                qvg1 = st.text_input("Line 1: Oh, let tell you about our trip. Did you know that Sara is afraid of be flying?", key="u2_qvg1")
                qvg2 = st.text_input("Line 2: We had arranged it with her family to go to France for a few days.", key="u2_qvg2")
                qvg3 = st.text_input("Line 3: I have always wanted to see Paris and would love to live in there one day.", key="u2_qvg3")
                qvg4 = st.text_input("Line 4: Well, we got to the airport and Sara appeared being nervous.", key="u2_qvg4")
                qvg5 = st.text_input("Line 5: I asked her if she was okay and she said she was fine, so we continued on to our way.", key="u2_qvg5")
                qvg6 = st.text_input("Line 6: We went through passport control and I could see so that Sara wasn't keen...", key="u2_qvg6")
                qvg7 = st.text_input("Line 7: Just then, a voice announced: 'We regret it to inform passengers...'", key="u2_qvg7")
                qvg8 = st.text_input("Line 8: ...that Flight 114 to France is been cancelled.'", key="u2_qvg8")
                qvg9 = st.text_input("Line 9: Sarah said she was glad because of she was too frightened to fly anyway!", key="u2_qvg9")
                qvg10 = st.text_input("Line 10: So, we all went to home. That was the end of that trip!", key="u2_qvg10")

            with tab_v_h:
                st.markdown("#### Exercise H: Use the word given in capitals (Word Formation Box)")
                qvh1 = st.text_input("Gap (1): It's not always easy being a ________. (TOUR)", key="u2_qvh1")
                qvh2 = st.text_input("Gap (2): You spend half your time making ________ for your holiday... (ARRANGE)", key="u2_qvh2")
                qvh3 = st.text_input("Gap (3): ...and the busiest worrying about sticking to the ________. (TIME)", key="u2_qvh3")
                qvh4 = st.text_input("Gap (4): There are no ________ problems... (CULTURE)", key="u2_qvh4")
                qvh5 = st.text_input("Gap (5): ...you don't need someone to be the ________... (PHOTOGRAPH)", key="u2_qvh5")
                qvh6 = st.text_input("Gap (6): ...and you know that the local ________ are always friendly! (INHABIT)", key="u2_qvh6")

            with tab_v_i:
                st.markdown("#### Exercise I: Complete the sentences by changing the form of the word in capitals")
                qvi1 = st.text_input("Câu 56: Beijing has changed so much in the last few years that it's almost ________. (RECOGNISE)", key="u2_qvi1")
                qvi2 = st.text_input("Câu 57: The number of cars ________ (WORLD) is about a billion and is increasing all the time.", key="u2_qvi2")
                qvi3 = st.text_input("Câu 58: The new maglev trains run on a completely ________ (DIFFER) system from ordinary trains.", key="u2_qvi3")
                qvi4 = st.text_input("Câu 59: Living in a foreign country really does ________ (BROAD) your horizons.", key="u2_qvi4")
                qvi5 = st.text_input("Câu 60: I can't find a ________ (DIRECT) flight from London to Delhi so I've booked one that changes in Frankfurt.", key="u2_qvi5")
                qvi6 = st.text_input("Câu 61: All passengers must complete a visa form upon ________ (ARRIVE) at Singapore airport.", key="u2_qvi6")
                qvi7 = st.text_input("Câu 62: You can still see old milestones by the side of the road in England, showing the ________ (DISTANT) to the nearest town.", key="u2_qvi7")
                qvi8 = st.text_input("Câu 63: The Museum of Transport has a full-sized jet plane next to the ________ (ENTER).", key="u2_qvi8")

            submit_u2_quiz = st.form_submit_button("🚀 Kiểm tra Đáp án Unit 2")

        if submit_u2_quiz:
            st.markdown("### 📊 Kết quả & Giải thích Chi tiết Unit 2")
            
            def eval_v_answer(q_id, user_val, correct_vals, explanation):
                if user_val is None or (isinstance(user_val, str) and user_val.strip() == ""):
                    st.warning(f"⚠️ **{q_id}: Chưa trả lời / Bỏ trống.** Đáp án chuẩn: **{correct_vals[0]}**")
                    st.markdown(f'<div class="explain-box">💡 <i>Giải thích:</i> {explanation}</div>', unsafe_allow_html=True)
                    return
                
                if isinstance(user_val, str):
                    u_clean = user_val.strip().lower()
                    is_correct = any(u_clean == c.lower() or c.lower() in u_clean for c in correct_vals)
                else:
                    is_correct = False
                    
                if is_correct:
                    st.success(f"✅ **{q_id}: Chính xác!** ({user_val})")
                else:
                    st.error(f"❌ **{q_id}: Chưa chính xác.** (Bạn nhập/chọn: `{user_val}`) ➔ Đáp án chuẩn: **{correct_vals[0]}**")
                    st.markdown(f'<div class="explain-box">💡 <i>Giải thích:</i> {explanation}</div>', unsafe_allow_html=True)

            # Ex A
            eval_v_answer("Ex A - Câu 1", qva1, ["C. border"], "'border' là đường biên giới giữa hai quốc gia.")
            eval_v_answer("Ex A - Câu 2", qva2, ["D. staying"], "'stay' chỉ việc ở tạm thời tại khách sạn.")
            eval_v_answer("Ex A - Câu 3", qva3, ["C. reach"], "'reach your destination' (không cần giới từ phía sau).")
            eval_v_answer("Ex A - Câu 4", qva4, ["A. season"], "'tourist season' là mùa du lịch.")
            eval_v_answer("Ex A - Câu 5", qva5, ["B. takes"], "'take sb to a place' là chở/đưa ai đến đâu.")
            eval_v_answer("Ex A - Câu 6", qva6, ["C. trip"], "'school trip' là chuyến đi tham quan của trường học.")
            eval_v_answer("Ex A - Câu 7", qva7, ["B. miss"], "'miss the bus' là lỡ chuyến xe buýt.")
            eval_v_answer("Ex A - Câu 8", qva8, ["D. view"], "'view of the sea' là tầm nhìn hướng ra biển.")
            eval_v_answer("Ex A - Câu 9", qva9, ["C. bring"], "'bring sth back' là mang quà/đồ về.")
            eval_v_answer("Ex A - Câu 10", qva10, ["D. distance"], "'distance' là khoảng cách giữa hai địa điểm.")
            eval_v_answer("Ex A - Câu 11", qva11, ["A. book"], "'book a hotel' là đặt phòng khách sạn.")
            eval_v_answer("Ex A - Câu 12", qva12, ["B. home"], "'home town' là quê nhà/thành phố quê hương.")

            # Ex B
            eval_v_answer("Ex B - Câu 13", qvb1, ["world"], "Cụm từ 'round the world' (vòng quanh thế giới).")
            eval_v_answer("Ex B - Câu 14", qvb2, ["area"], "'local area' là khu vực địa phương.")
            eval_v_answer("Ex B - Câu 15", qvb3, ["guide"], "'guide' là hướng dẫn viên dẫn đường.")
            eval_v_answer("Ex B - Câu 16", qvb4, ["fare"], "'fare' là tiền vé tàu xe.")
            eval_v_answer("Ex B - Câu 17", qvb5, ["voyage"], "'voyage' là chuyến đi dài bằng đường biển.")
            eval_v_answer("Ex B - Câu 18", qvb6, ["fee"], "'admission fee' là phí vào cửa.")
            eval_v_answer("Ex B - Câu 19", qvb7, ["sight"], "'magnificent sight' là danh thắng tuyệt đẹp.")

            # Ex C
            eval_v_answer("Ex C - Câu 20", qvc1, ["see"], "'see sb off' là tiễn ai lên đường.")
            eval_v_answer("Ex C - Câu 21", qvc2, ["make"], "'make for' là đi về hướng.")
            eval_v_answer("Ex C - Câu 22", qvc3, ["check"], "'check out' là làm thủ tục trả phòng.")
            eval_v_answer("Ex C - Câu 23", qvc4, ["pull"], "'pull in' là tấp xe vô lề.")
            eval_v_answer("Ex C - Câu 24", qvc5, ["picks"], "'pick sb up' là đón ai bằng xe.")
            eval_v_answer("Ex C - Câu 25", qvc6, ["gone"], "'go away' là đi nghỉ mát xa nhà.")
            eval_v_answer("Ex C - Câu 27", qvc7, ["catch"], "'catch up with' là đuổi kịp.")
            eval_v_answer("Ex C - Câu 28", qvc8, ["get"], "'get back' là trở về.")

            # Ex D
            eval_v_answer("Ex D - Câu 28", qvd1, ["set out", "set off"], "'start our journey' = 'set out/off'.")
            eval_v_answer("Ex D - Câu 29", qvd2, ["checked in"], "'registered' = 'checked in'.")
            eval_v_answer("Ex D - Câu 30", qvd3, ["drop me off"], "'let me get out' = 'drop me off'.")
            eval_v_answer("Ex D - Câu 31", qvd4, ["turn round", "turn back"], "'go back' = 'turn round'.")
            eval_v_answer("Ex D - Câu 32", qvd5, ["takes off"], "'leaves the ground' = 'takes off'.")
            eval_v_answer("Ex D - Câu 33", qvd6, ["run over"], "'hit with a car' = 'run over'.")
            eval_v_answer("Ex D - Câu 34", qvd7, ["keep up with"], "'stay at the same speed as' = 'keep up with'.")

            # Ex E
            eval_v_answer("Ex E - Câu 35", qve1, ["limit"], "'speed limit' là giới hạn tốc độ.")
            eval_v_answer("Ex E - Câu 36", qve2, ["take"], "'take the scenic route' là đi theo con đường đẹp.")
            eval_v_answer("Ex E - Câu 37", qve3, ["in"], "'in advance' nghĩa là đặt trước.")
            eval_v_answer("Ex E - Câu 38", qve4, ["top"], "'off the top of my head' là nhớ mang rợ không suy nghĩ kỹ.")
            eval_v_answer("Ex E - Câu 39", qve5, ["lost"], "'lost my way' là bị lạc đường.")
            eval_v_answer("Ex E - Câu 40", qve6, ["trip"], "'business trip' là chuyến công tác.")
            eval_v_answer("Ex E - Câu 41", qve7, ["straight"], "'go straight ahead' là đi thẳng.")
            eval_v_answer("Ex E - Câu 42", qve8, ["side"], "'left-hand side' là phía bên tay trái.")
            eval_v_answer("Ex E - Câu 43", qve9, ["go"], "'go sightseeing' là đi ngắm cảnh.")
            eval_v_answer("Ex E - Câu 44", qve10, ["had"], "'had an accident' là gặp tai nạn.")
            eval_v_answer("Ex E - Câu 45", qve11, ["seeing"], "'seeing the sights' là đi ngắm cảnh.")
            eval_v_answer("Ex E - Câu 46", qve12, ["on"], "'go on holiday' là đi nghỉ mát.")
            eval_v_answer("Ex E - Câu 47", qve13, ["of", "around"], "'take a tour of' là đi tham quan.")

            # Ex F
            eval_v_answer("Ex F - Câu 48", qvf1, ["B. of visiting"], "'dream of doing sth'.")
            eval_v_answer("Ex F - Câu 49", qvf2, ["C. to stay"], "'arrange for sb to do sth'.")
            eval_v_answer("Ex F - Câu 50", qvf3, ["B. not travelling"], "'regret not doing sth'.")
            eval_v_answer("Ex F - Câu 51", qvf4, ["D. to learn"], "'keen to do sth'.")
            eval_v_answer("Ex F - Câu 52", qvf5, ["A. me"], "'write sb sth' (viết cho ai cái gì).")
            eval_v_answer("Ex F - Câu 53", qvf6, ["D. at the airport"], "'arrive at the airport' (địa điểm cụ thể).")
            eval_v_answer("Ex F - Câu 54", qvf7, ["D. to go"], "'invite sb to do sth'.")
            eval_v_answer("Ex F - Câu 55", qvf8, ["B. from"], "'differ from sth' (khác biệt với cái gì).")

            # Ex G
            eval_v_answer("Ex G - Line 1", qvg1, ["be"], "Thừa từ 'be'.")
            eval_v_answer("Ex G - Line 2", qvg2, ["it"], "Thừa từ 'it'.")
            eval_v_answer("Ex G - Line 3", qvg3, ["there", "in"], "Thừa từ 'there'.")
            eval_v_answer("Ex G - Line 4", qvg4, ["being"], "Thừa từ 'being'.")
            eval_v_answer("Ex G - Line 5", qvg5, ["to"], "Thừa từ 'to'.")
            eval_v_answer("Ex G - Line 6", qvg6, ["so"], "Thừa từ 'so'.")
            eval_v_answer("Ex G - Line 7", qvg7, ["it"], "Thừa từ 'it'.")
            eval_v_answer("Ex G - Line 8", qvg8, ["been"], "Thừa từ 'been'.")
            eval_v_answer("Ex G - Line 9", qvg9, ["of"], "Thừa từ 'of'.")
            eval_v_answer("Ex G - Line 10", qvg10, ["to"], "Thừa từ 'to'.")

            # Ex H
            eval_v_answer("Ex H - Gap 1", qvh1, ["tourist"], "TOUR -> tourist.")
            eval_v_answer("Ex H - Gap 2", qvh2, ["arrangements"], "ARRANGE -> arrangements.")
            eval_v_answer("Ex H - Gap 3", qvh3, ["timetable"], "TIME -> timetable.")
            eval_v_answer("Ex H - Gap 4", qvh4, ["cultural"], "CULTURE -> cultural.")
            eval_v_answer("Ex H - Gap 5", qvh5, ["photographer"], "PHOTOGRAPH -> photographer.")
            eval_v_answer("Ex H - Gap 6", qvh6, ["inhabitants"], "INHABIT -> inhabitants.")

            # Ex I
            eval_v_answer("Ex I - Câu 56", qvi1, ["unrecognisable"], "RECOGNISE -> unrecognisable.")
            eval_v_answer("Ex I - Câu 57", qvi2, ["worldwide"], "WORLD -> worldwide.")
            eval_v_answer("Ex I - Câu 58", qvi3, ["different"], "DIFFER -> different.")
            eval_v_answer("Ex I - Câu 59", qvi4, ["broaden"], "BROAD -> broaden.")
            eval_v_answer("Ex I - Câu 60", qvi5, ["direct"], "DIRECT -> direct.")
            eval_v_answer("Ex I - Câu 61", qvi6, ["arrival"], "ARRIVE -> arrival.")
            eval_v_answer("Ex I - Câu 62", qvi7, ["distance"], "DISTANT -> distance.")
            eval_v_answer("Ex I - Câu 63", qvi8, ["entrance"], "ENTER -> entrance.")

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
    st.write("Tổng hợp các bẫy ngữ pháp và từ vựng nâng cao đặc biệt (Watch out!) từ sách Destination B2.")
    
    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #1: Present Perfect Simple vs Present Perfect Continuous</h4>
    <b>Quy tắc quan trọng:</b><br>
    • Sử dụng <b>Present Perfect Simple</b> khi nhấn mạnh <u>số lượng / kết quả hoàn thành</u>:<br>
    &nbsp;&nbsp;<i>✔ I've written <b>three letters</b> this morning.</i><br>
    • Sử dụng <b>Present Perfect Continuous</b> khi nhấn mạnh <u>thời lượng / tính liên tục</u> của hành động:<br>
    &nbsp;&nbsp;<i>✔ We've been driving for <b>hours</b>.</i>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="watchout-box">
    <h4>⚠️ Watch Out #2: Stative Verbs in Continuous Tenses</h4>
    <b>Quy tắc quan trọng:</b><br>
    Nhiều động từ trạng thái có thể dùng ở thì tiếp diễn khi mô tả <b>HÀNH ĐỘNG</b> thay vì TRẠNG THÁI:<br>
    • <i>Do you <b>have</b> your plane ticket with you?</i> (State: sở hữu)<br>
    • <i>Are you <b>having</b> lunch at the moment?</i> (Action: đang ăn)
    </div>
    """, unsafe_allow_html=True)

# --- 6. BÁO CÁO TIẾN ĐỘ HỌC TẬP ---
elif menu_option == "📊 Báo cáo Tiến độ Học tập (Progress Report)":
    st.header("📊 Báo cáo Tiến độ Học tập Tự động")
    st.write("Hệ thống tự động ghi nhận tiến độ và kết quả khi bạn hoàn thành bài tập ở mục Bài tập Tương tác.")
    
    # 1. Lấy dữ liệu bài đã làm từ session_state
    user_progress = st.session_state.get("completed_units", {})
    total_items = len(ALL_UNITS_LIST)
    completed_count = len(user_progress)
    
    # 2. Tính % tiến độ toàn khóa học
    progress_pct = completed_count / total_items if total_items > 0 else 0.0
    
    # 3. Bảng chỉ số tổng quan (Top Metrics)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📈 Tiến độ toàn khóa", f"{int(progress_pct * 100)}%")
    with col2:
        st.metric("✅ Bài tập đã hoàn thành", f"{completed_count} / {total_items} bài")
    with col3:
        if completed_count > 0:
            avg_score = sum(data["pct"] for data in user_progress.values()) / completed_count
            st.metric("🏆 Điểm trung bình", f"{int(avg_score)}%")
        else:
            st.metric("🏆 Điểm trung bình", "0%")
            
    # Thanh tiến độ
    st.progress(progress_pct)
    st.markdown("---")
    
    # 4. Bảng chi tiết từng Unit
    st.subheader("📋 Chi tiết trạng thái từng Unit")
    table_data = []
    
    for idx, unit_name in enumerate(ALL_UNITS_LIST, 1):
        if unit_name in user_progress:
            info = user_progress[unit_name]
            status = "✅ Đã hoàn thành"
            score_str = f"{info['score']}/{info['total']} ({info['pct']}%)"
        else:
            status = "⏳ Chưa làm bài tập"
            score_str = "---"
            
        table_data.append({
            "STT": idx,
            "Tên Unit / Bài Ôn tập": unit_name,
            "Trạng thái": status,
            "Kết quả Bài tập": score_str
        })
        
    df_progress = pd.DataFrame(table_data)
    st.dataframe(df_progress, use_container_width=True, height=450)
    
    # 5. Nút Đặt lại tiến độ
    if st.button("🔄 Đặt lại toàn bộ Tiến độ"):
        st.session_state.completed_units = {}
        st.rerun()
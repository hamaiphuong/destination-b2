import streamlit as st

# Page config
st.set_page_config(
    page_title="Destination C1 & C2 Self-Study Hub",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .badge-grammar {
        background-color: #2563EB;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .badge-vocab {
        background-color: #059669;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .watchout-box {
        background-color: #FFFBEB;
        border-left: 5px solid #F59E0B;
        padding: 1.2rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .tip-title {
        color: #B45309;
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'completed_units' not in st.session_state:
    st.session_state.completed_units = []
if 'flashcard_idx' not in st.session_state:
    st.session_state.flashcard_idx = 0

# --- DATA STRUCTURES GROUNDED IN DESTINATION C1 & C2 ---

UNITS_DATA = {
    "Unit 1: Grammar - Present time": {
        "type": "Grammar",
        "level": "C1/C2",
        "description": "Thì hiện tại: Present simple, Emphatic present simple, Present continuous, Present perfect simple, Present perfect continuous, Stative verbs & US/UK grammar differences.",
        "theory": {
            "Present Simple": [
                ("General truths", "The left-hand side of the brain controls the right-hand side of the body."),
                ("Current habits", "I don't always go to lectures that are early in the morning!"),
                ("Permanent situations and states", "Angie teaches French at a local adult education centre."),
                ("Telling jokes & informal stories", "So, a man goes to see his psychiatrist ..."),
                ("Live sports commentary", "Adams passes to Kareshi. It's a goal!"),
                ("Newspaper headlines", "HAWKING WINS NOBEL PRIZE"),
                ("Reviews and summaries", "The film ends with us not knowing whether they have been successful or not."),
                ("Instructions and directions", "You turn left at the end of the road and the school is up ahead."),
                ("Proverbs and sayings", "Too many cooks spoil the broth."),
                ("Timetables / Fixed events", "Term ends on 21st December.")
            ],
            "Emphatic Present Simple": [
                ("To emphasise contrast", "Adam doesn't know much about psychiatry but he DOES know quite a lot about psychology."),
                ("To emphasise strong feeling", "I DO like playing word games!")
            ],
            "Present Continuous": [
                ("Actions happening now / around now", "The boys are doing their homework right now."),
                ("Temporary situations and series of actions", "We aren't having any exams while the lecturers are still on strike."),
                ("Changing and developing situations", "More and more people are recognising the advantages of learning a foreign language."),
                ("Annoying or amusing habits (with always)", "Dan's always coming up with the craziest ideas!")
            ],
            "Present Perfect Simple & Continuous": [
                ("Present Perfect Simple (Quantity/Result)", "I've written two essays this week. (emphasises number/completed result)"),
                ("Present Perfect Continuous (Duration)", "I've been working here for five years. (emphasises duration of activity)")
            ],
            "Stative vs Dynamic Uses of Verbs": [
                ("Communication (agree, deny, disagree)", "Simple tenses only."),
                ("Thinking (believe, consider, doubt, expect, know, realise)", "I think it's important to know how to use a computer. (think = believe)"),
                ("Dynamic action with 'think'", "I'm thinking about going on a computer course. (think = consider)"),
                ("Perception & Possession (appear, hear, look, possess, taste)", "The soup tastes delicious. (state) vs Chef is tasting the soup. (action)")
            ]
        },
        "watch_out": [
            "Dùng Present Perfect Simple khi nói về số lượng/số lần cụ thể: 'I've written two essays this week' (KHÔNG dùng Present Perfect Continuous).",
            "Dùng Present Perfect Continuous khi nhấn mạnh thời lượng kéo dài: 'I've been working here for five years' (nhấn mạnh duration).",
            "Động từ trạng thái (Stative verbs) như believe, doubt, know, realise, suppose, understand chỉ dùng thì đơn, ngoại trừ khi biểu thị hành động chủ động."
        ],
        "quiz": [
            {
                "exercise": "Exercise A & D: Present Simple vs Present Continuous & Stative Verbs",
                "question": "1. My brother _____ a degree at university so I don't see him very often, unfortunately. (do)",
                "options": ["is doing", "does", "do"],
                "answer": "is doing",
                "explanation": "Hành động tạm thời xảy ra xung quanh thời điểm hiện tại (temporary situation) -> Present Continuous."
            },
            {
                "exercise": "Exercise A & D: Present Simple vs Present Continuous & Stative Verbs",
                "question": "2. Darren usually _____ home until about eight o'clock. (not / get)",
                "options": ["doesn't get", "isn't getting", "don't get"],
                "answer": "doesn't get",
                "explanation": "Diễn tả thói quen hàng ngày (current habit) với 'usually' -> Present Simple."
            },
            {
                "exercise": "Exercise A & D: Present Simple vs Present Continuous & Stative Verbs",
                "question": "3. Why _____ ice _____? (float)",
                "options": ["does / float", "is / floating", "do / float"],
                "answer": "does / float",
                "explanation": "Sự thật khoa học / Chân lý tự nhiên (General truth) -> Present Simple."
            },
            {
                "exercise": "Exercise D: Circle the correct word or phrase (Stative Verbs)",
                "question": "4. Could you explain what 'antidisestablishmentarianism' _____?",
                "options": ["means", "is meaning", "mean"],
                "answer": "means",
                "explanation": "'mean' biểu thị ý nghĩa định nghĩa là stative verb -> Present Simple."
            },
            {
                "exercise": "Exercise D: Circle the correct word or phrase (Stative Verbs)",
                "question": "5. I think I _____ that woman over there. Wasn't she on that quiz show last night?",
                "options": ["recognise", "am recognising", "recognised"],
                "answer": "recognise",
                "explanation": "'recognise' là động từ tri giác/trạng thái (perception) -> Present Simple."
            },
            {
                "exercise": "Exercise D: Circle the correct word or phrase (Stative Verbs)",
                "question": "6. Right now, my job _____ a huge amount of foreign travel.",
                "options": ["involves", "is involving", "involve"],
                "answer": "involves",
                "explanation": "'involve' mô tả thuộc tính bản chất của công việc -> Present Simple."
            },
            {
                "exercise": "Exercise D: Circle the correct word or phrase (Stative Verbs)",
                "question": "7. We _____ the living room repainted so it's probably best if we go into the kitchen.",
                "options": ["are having", "have", "have had"],
                "answer": "are having",
                "explanation": "'have' ở đây mang nghĩa hành động (cho người khác sơn lại phòng) -> Present Continuous."
            },
            {
                "exercise": "Exercise G: Present Perfect Simple vs Continuous",
                "question": "8. They've _____ six bags with rubbish from the beach already.",
                "options": ["filled", "been filling", "fill"],
                "answer": "filled",
                "explanation": "Nhấn mạnh kết quả hoàn thành với số lượng cụ thể ('six bags') -> Present Perfect Simple."
            },
            {
                "exercise": "Exercise G: Present Perfect Simple vs Continuous",
                "question": "9. It's the first time I've _____ The Editors play live.",
                "options": ["heard", "been hearing", "hear"],
                "answer": "heard",
                "explanation": "Đi với cấu trúc 'It's the first time...' + Present Perfect Simple."
            },
            {
                "exercise": "Exercise G: Present Perfect Simple vs Continuous",
                "question": "10. You can't want to go to the toilet already - we've only _____ for about ten minutes so far!",
                "options": ["been driving", "driven", "drive"],
                "answer": "been driving",
                "explanation": "Nhấn mạnh tính liên tục và thời lượng của hành động ('for about ten minutes') -> Present Perfect Continuous."
            },
            {
                "exercise": "Exercise I: Time Adverbials",
                "question": "11. I've _____ realised what's different! You've changed your hair.",
                "options": ["just", "yet", "still", "already"],
                "answer": "just",
                "explanation": "'just realised' có nghĩa vừa mới nhận ra điều gì."
            },
            {
                "exercise": "Exercise I: Time Adverbials",
                "question": "12. Michael, haven't you done your homework _____? I think it's time you started, isn't it?",
                "options": ["yet", "already", "still", "since"],
                "answer": "yet",
                "explanation": "'yet' dùng ở cuối câu hỏi/câu phủ định diễn tả việc chưa hoàn thành."
            }
        ]
    },
    "Unit 2: Vocabulary - Thinking and learning": {
        "type": "Vocabulary",
        "level": "C1/C2",
        "description": "Từ vựng chủ đề Tư duy & Học tập, Phrasal Verbs, Idioms, Collocations và Word Formation.",
        "theory": {
            "Topic Vocabulary: Thinking": [
                ("assess (v) /əˈses/", "evaluate or estimate the nature, ability, or quality of", "Đánh giá bản chất, giá trị hoặc khả năng của cái gì."),
                ("baffle (v) /ˈbæfl/", "totally bewilder, confuse or perplex", "Gây bối rối, hoàn toàn không thể hiểu được."),
                ("cynical (adj) /ˈsɪnɪkl/", "believing that people are motivated by self-interest", "Hoài nghi về lòng tốt hoặc sự chân thành của con người."),
                ("dubious (adj) /ˈdjuːbiəs/", "hesitating or doubting; not to be relied upon", "Mơ hồ, đáng ngờ, nghi ngại."),
                ("ingenious (adj) /ɪnˈdʒiːniəs/", "clever, original, and inventive", "Khéo léo, thông minh, phát minh độc đáo."),
                ("plausible (adj) /ˈplɔːzəbl/", "seeming reasonable or probable", "Hợp lý, có vẻ đúng, đáng tin cậy.")
            ],
            "Phrasal Verbs": [
                ("brush up (on) /brʌʃ ʌp/", "practise and improve your skills or knowledge", "Rèn luyện, ôn lại để cải thiện kỹ năng/kiến thức."),
                ("come round (to) /kʌm raʊnd/", "change your opinion or decision because someone has persuaded you", "Thay đổi ý kiến/quan điểm vì bị thuyết phục."),
                ("come up with /kʌm ʌp wɪð/", "think of something such as an idea or a plan", "Nghĩ ra một ý tưởng, kế hoạch."),
                ("face up to /feɪs ʌp tuː/", "accept and deal with a difficult fact or problem", "Chấp nhận và đối mặt với thực tế khó khăn."),
                ("mull over /mʌl ˈəʊvə(r)/", "think carefully about something over a period of time", "Suy ngẫm, cân nhắc kỹ lưỡng trong một khoảng thời gian."),
                ("piece together /piːs təˈɡeðə(r)/", "learn the truth about something by considering all the separate bits of information", "Xâu chuỗi các manh mối/thông tin để hiểu sự thật.")
            ],
            "Idioms": [
                ("go to your head", "if success goes to your head, it makes you think that you are better or more important than you really are", "Thành công khiến ai đó trở nên kiêu ngạo."),
                ("have your wits about you", "be able to think quickly and make sensible decisions", "Tỉnh táo, suy nghĩ nhanh để đưa ra quyết định đúng."),
                ("not see the wood for the trees", "be unable to understand what is important because you are paying too much attention to details", "Quá chú ý chi tiết nhỏ mà không thấy bức tranh toàn cảnh."),
                ("quick / slow on the uptake", "taking a short / long time to understand or realise something", "Nảy số nhanh / tiếp thu chậm."),
                ("ring a bell", "something that rings a bell sounds familiar, but you cannot remember the exact details", "Nghe quen quen nhưng không nhớ rõ chi tiết.")
            ],
            "Word Formation Database": [
                ("assume", "assumption, assuming, unassuming, assumed"),
                ("conceive", "concept, conception, conceptual, (in)conceivable, (in)conceivably"),
                ("rational", "rationalise, rationalisation, rationalist, rationalism, (ir)rationality, (ir)rational(ly)"),
                ("sane", "(in)sanity, insane(ly)")
            ]
        },
        "watch_out": [
            "Phân biệt 'cynical' (hoài nghi lòng tốt con người) và 'sceptical/skeptical' (hoài nghi tính đúng đắn của kế hoạch/tin tức).",
            "Phrasal verb 'swot up (on)' nghĩa là học dồn, học chăm chỉ trước kỳ thi (tương tự 'cram')."
        ],
        "quiz": [
            {
                "exercise": "Topic Vocabulary & Phrasal Verbs",
                "question": "1. I spent all evening _____ over the decision before finally deciding to accept the job.",
                "options": ["mulling", "brushing", "puzzling", "piecing"],
                "answer": "mulling",
                "explanation": "'mull over' nghĩa là suy ngẫm, cân nhắc kỹ lưỡng một quyết định."
            },
            {
                "exercise": "Idioms & Collocations",
                "question": "2. Don't let success go to your _____; stay humble and keep working hard.",
                "options": ["head", "mind", "brain", "wit"],
                "answer": "head",
                "explanation": "Idiom 'go to your head' nghĩa là bị sự thành công làm cho kiêu ngạo."
            },
            {
                "exercise": "Topic Vocabulary",
                "question": "3. The proposal sounds completely _____ and well-thought-out.",
                "options": ["plausible", "dubious", "baffled", "naive"],
                "answer": "plausible",
                "explanation": "'plausible' có nghĩa là hợp lý, khả thi, đáng tin."
            }
        ]
    }
}

VOCAB_FLASHCARDS = [
    {
        "word": "assess (v)",
        "ipa": "/əˈses/",
        "pos": "verb",
        "def": "evaluate or estimate the nature, ability, or quality of",
        "vi": "đánh giá, định giá",
        "example": "It's difficult to assess the impact of the new policy."
    },
    {
        "word": "baffle (v)",
        "ipa": "/ˈbæfl/",
        "pos": "verb",
        "def": "totally bewilder, confuse or perplex",
        "vi": "gây bối rối, làm kinh ngạc",
        "example": "His sudden decision to quit baffled everyone in the office."
    },
    {
        "word": "cynical (adj)",
        "ipa": "/ˈsɪnɪkl/",
        "pos": "adjective",
        "def": "believing that people are motivated by self-interest; distrustful of human sincerity",
        "vi": "hoài nghi lòng tốt con người",
        "example": "I've become quite cynical about politicians and their promises."
    },
    {
        "word": "brush up (on)",
        "ipa": "/brʌʃ ʌp/",
        "pos": "phrasal verb",
        "def": "practise and improve your skills or knowledge of something",
        "vi": "ôn luyện, trau dồi lại",
        "example": "I need to brush up on my French before visiting Paris."
    },
    {
        "word": "mull over",
        "ipa": "/mʌl ˈəʊvə(r)/",
        "pos": "phrasal verb",
        "def": "think carefully about something over a period of time",
        "vi": "suy ngẫm, cân nhắc kỹ lưỡng",
        "example": "They offered me the job, but I need a few days to mull it over."
    },
    {
        "word": "go to your head",
        "ipa": "/ɡəʊ tuː jɔː(r) hed/",
        "pos": "idiom",
        "def": "cause someone to become arrogant or overconfident",
        "vi": "làm cho ai đó mắc bệnh ngôi sao / kiêu ngạo",
        "example": "Don't let that promotion go to your head!"
    },
    {
        "word": "ring a bell",
        "ipa": "/rɪŋ ə bel/",
        "pos": "idiom",
        "def": "sound familiar, but you cannot remember the exact details",
        "vi": "nghe quen quen nhưng chưa nhớ rõ",
        "example": "His name rings a bell, but I can't remember where I met him."
    }
]

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📚 Destination C1 & C2")
st.sidebar.caption("Hệ thống Tự học Ngữ pháp & Từ vựng Nâng cao")

menu = st.sidebar.radio(
    "Danh mục học tập",
    [
        "📌 Tổng quan & Lộ trình tự học",
        "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)",
        "✍️ Bài tập Tương tác & Chấm điểm tự động",
        "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)",
        "⚠️ Góc lưu ý (Watch Out! Corner)",
        "📊 Báo cáo Tiến độ Học tập"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Thông tin giáo trình:**")
st.sidebar.write("• Tác giả: Malcolm Mann & Steve Taylore-Knowles")
st.sidebar.write("• Trình độ: C1 & C2 (CAE / CPE)")
st.sidebar.write("• Cấu trúc: 26 Units + 13 Reviews + 8 Tests")

# --- MAIN CONTENT PAGES ---

# 1. OVERVIEW PAGE
if menu == "📌 Tổng quan & Lộ trình tự học":
    st.markdown('<div class="main-header">Destination C1 & C2: Learning Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Nền tảng hỗ trợ học sinh tự học Ngữ pháp & Từ vựng Tiếng Anh C1 & C2 tại nhà</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Cấu trúc Bài học", value="26 Units", delta="13 Grammar + 13 Vocab")
    with col2:
        st.metric(label="Bài Ôn tập & Kiểm tra", value="21 Tests", delta="13 Reviews + 8 Tests")
    with col3:
        st.metric(label="Mục tiêu Trình độ", value="C1 & C2", delta="Cambridge CAE & CPE")
        
    st.markdown("---")
    st.subheader("🎯 Lộ trình Tự học Chuẩn hóa 4 Bước")
    st.write("""
    Mỗi bài học trong sách **Destination C1 & C2** được thiết kế đan xen giữa **1 bài Ngữ pháp (Grammar)** và **1 bài Từ vựng (Vocabulary)** theo chủ đề.
    Ứng dụng học tập giúp bạn nắm vững toàn bộ kiến thức qua 4 bước:
    1. **Nắm vững Lý thuyết (Theory Hub)**: Tra cứu hệ thống quy tắc ngữ pháp dạng bảng so sánh và danh mục từ vựng chủ đề, cụm động từ, thành ngữ có IPA & định nghĩa từ điển.
    2. **Phòng tránh Bẫy thi (Watch Out! Corner)**: Ghi nhớ các bẫy ngữ pháp và từ vựng người học dễ mất điểm nhất.
    3. **Luyện bài tập tương tác (Interactive Quiz)**: Làm trọn vẹn câu hỏi thực hành từng unit, kiểm tra đáp án tự động và xem giải thích chi tiết.
    4. **Ghi nhớ lâu với Flashcards**: Thẻ từ vựng lật thông minh hỗ trợ học sinh ghi nhớ nghĩa, phiên âm IPA, dịch Tiếng Việt và câu ví dụ.
    """)
    
    st.markdown("### 📋 Danh sách Units trong chương trình:")
    st.table([
        {"Unit": "Unit 1", "Loại Unit": "Grammar", "Chủ đề": "Present time", "Trình độ": "C1/C2"},
        {"Unit": "Unit 2", "Loại Unit": "Vocabulary", "Chủ đề": "Thinking and learning", "Trình độ": "C1/C2"},
        {"Unit": "Unit 3", "Loại Unit": "Grammar", "Chủ đề": "Past time", "Trình độ": "C1/C2"},
        {"Unit": "Unit 4", "Loại Unit": "Vocabulary", "Chủ đề": "Change and technology", "Trình độ": "C1/C2"},
        {"Unit": "Unit 5", "Loại Unit": "Grammar", "Chủ đề": "Future time", "Trình độ": "C1/C2"},
        {"Unit": "Unit 6", "Loại Unit": "Vocabulary", "Chủ đề": "Time and work", "Trình độ": "C1/C2"},
        {"Unit": "Unit 11", "Loại Unit": "Grammar", "Chủ đề": "Conditionals", "Trình độ": "C1/C2"},
        {"Unit": "Unit 13", "Loại Unit": "Grammar", "Chủ đề": "Unreal time", "Trình độ": "C1/C2"}
    ])

# 2. THEORY PAGE
elif menu == "📖 Tra cứu Lý thuyết Trọng tâm (Theory Hub)":
    st.markdown('<div class="main-header">📖 Tra cứu Lý thuyết Trọng tâm</div>', unsafe_allow_html=True)
    selected_unit_key = st.selectbox("Chọn Unit muốn học:", list(UNITS_DATA.keys()))
    
    unit_info = UNITS_DATA[selected_unit_key]
    
    badge_class = "badge-grammar" if unit_info["type"] == "Grammar" else "badge-vocab"
    st.markdown(f"### {selected_unit_key}")
    st.markdown(f"**Loại bài:** <span class='{badge_class}'>{unit_info['type']}</span> | **Trình độ:** {unit_info['level']} | **Mô tả:** {unit_info['description']}", unsafe_allow_html=True)
    st.markdown("---")
    
    if unit_info["type"] == "Grammar":
        tab1, tab2 = st.tabs(["📌 Cấu trúc & Quy tắc Ngữ pháp", "⚠️ Hộp Lưu ý (Watch Out!)"])
        with tab1:
            for rule_title, examples in unit_info["theory"].items():
                st.markdown(f"#### 🔹 {rule_title}")
                for item in examples:
                    if len(item) == 2:
                        usage, sentence = item
                        st.markdown(f"- **{usage}**: *{sentence}*")
                    elif len(item) == 3:
                        title, usage, sentence = item
                        st.markdown(f"- **{title}** (`{usage}`): *{sentence}*")
                st.markdown("<br>", unsafe_allow_html=True)
        with tab2:
            st.warning("Các điểm lưu ý quan trọng trong bài thi:")
            for wo in unit_info["watch_out"]:
                st.markdown(f"- {wo}")
                
    elif unit_info["type"] == "Vocabulary":
        tab1, tab2, tab3 = st.tabs(["📚 Từ vựng Chủ đề & Phrasal Verbs", "💡 Idioms & Collocations", "🔤 Word Formation"])
        with tab1:
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                st.markdown("#### Topic Vocabulary")
                for w, def_en, vi_m in unit_info["theory"].get("Topic Vocabulary: Thinking", []):
                    st.markdown(f"• **{w}**")
                    st.caption(f"🇬🇧 *Definition:* {def_en} | 🇻🇳 *Nghĩa:* {vi_m}")
            with col_v2:
                st.markdown("#### Phrasal Verbs")
                for pv, def_en, vi_m in unit_info["theory"].get("Phrasal Verbs", []):
                    st.markdown(f"• **{pv}**")
                    st.caption(f"🇬🇧 *Definition:* {def_en} | 🇻🇳 *Nghĩa:* {vi_m}")
        with tab2:
            st.markdown("#### Idioms")
            for idm, def_en, vi_m in unit_info["theory"].get("Idioms", []):
                st.markdown(f"• **{idm}**")
                st.caption(f"🇬🇧 *Definition:* {def_en} | 🇻🇳 *Nghĩa:* {vi_m}")
        with tab3:
            st.markdown("#### Word Formation Database")
            for base, derivs in unit_info["theory"].get("Word Formation Database", []):
                st.markdown(f"• **{base}** ➔ `{derivs}`")

# 3. INTERACTIVE QUIZ PAGE
elif menu == "✍️ Bài tập Tương tác & Chấm điểm tự động":
    st.markdown('<div class="main-header">✍️ Bài tập Tương tác & Chấm điểm tự động</div>', unsafe_allow_html=True)
    
    selected_quiz_unit = st.selectbox("Chọn Unit bài tập:", list(UNITS_DATA.keys()), key="quiz_unit_select")
    quiz_list = UNITS_DATA[selected_quiz_unit]["quiz"]
    
    st.info("💡 **Hướng dẫn:** Hãy chọn đáp án phù hợp cho từng câu hỏi bên dưới. Hệ thống không chọn sẵn đáp án. Sau khi hoàn thành, nhấp nút **Kiểm tra Đáp án** để xem điểm và giải thích chi tiết.")
    
    user_answers = {}
    with st.form("quiz_form"):
        for i, q in enumerate(quiz_list):
            st.markdown(f"##### 📌 {q.get('exercise', 'Exercise')}")
            st.markdown(f"**Câu {i+1}:** {q['question']}")
            
            # REQUIREMENT: No pre-selected option (index=None)
            user_answers[i] = st.radio(
                f"Chọn đáp án cho câu {i+1}:",
                options=q['options'],
                index=None,
                key=f"q_{selected_quiz_unit}_{i}"
            )
            st.markdown("---")
            
        submitted = st.form_submit_button("🚀 Submit Answers / Kiểm tra Đáp án")
        
    if submitted:
        score = 0
        unanswered = 0
        st.markdown("### 📊 Kết quả Bài làm:")
        
        for i, q in enumerate(quiz_list):
            ans = user_answers[i]
            if ans is None:
                unanswered += 1
                st.warning(f"⚠️ **Câu {i+1}: Chưa chọn đáp án.** (Đáp án đúng: **{q['answer']}**)")
            elif ans == q['answer']:
                score += 1
                st.success(f"✅ **Câu {i+1}: Chính xác!** ({q['answer']})")
            else:
                st.error(f"❌ **Câu {i+1}: Chưa đúng.** Bạn chọn: `{ans}` ➔ Đáp án đúng: **{q['answer']}**")
                
            st.caption(f"💡 *Giải thích chi tiết:* {q['explanation']}")
            st.markdown("<br>", unsafe_allow_html=True)
            
        final_score = int((score / len(quiz_list)) * 100)
        st.metric("Điểm số của bạn", f"{final_score}%", f"{score}/{len(quiz_list)} câu đúng ({unanswered} câu chưa làm)")
        
        if selected_quiz_unit not in st.session_state.completed_units and unanswered == 0:
            st.session_state.completed_units.append(selected_quiz_unit)

# 4. FLASHCARDS PAGE
elif menu == "🎴 Thẻ ghi nhớ Từ vựng (Flashcards)":
    st.markdown('<div class="main-header">🎴 Thẻ ghi nhớ Từ vựng (Flashcards)</div>', unsafe_allow_html=True)
    
    selected_fc_unit = st.selectbox("Chọn Unit muốn học Flashcards:", list(UNITS_DATA.keys()), key="fc_unit_select")
    unit_type = UNITS_DATA[selected_fc_unit]["type"]
    
    # REQUIREMENT: Only vocabulary units have flashcards
    if unit_type != "Vocabulary":
        st.info("ℹ️ **Thẻ ghi nhớ (Flashcards) chỉ dành riêng cho các Unit Từ vựng (Vocabulary Units).**")
        st.write("Các bài Ngữ pháp (Grammar Units) tập trung vào lý thuyết và bài tập thực hành. Vui lòng chọn một **Unit Từ vựng** (như *Unit 2: Vocabulary - Thinking and learning*) ở ô trên để ôn luyện Flashcards.")
    else:
        st.caption("Sử dụng thẻ lật 2 mặt thông minh để ghi nhớ từ vựng, phiên âm IPA, định nghĩa Anh - Việt và ví dụ ngữ cảnh.")
        
        total_fc = len(VOCAB_FLASHCARDS)
        curr_idx = st.session_state.flashcard_idx % total_fc
        card = VOCAB_FLASHCARDS[curr_idx]
        
        col_fc, _ = st.columns([2, 1])
        with col_fc:
            st.markdown(f"""
            <div style="background-color: #EFF6FF; border: 2px solid #2563EB; border-radius: 12px; padding: 2rem; text-align: center; min-height: 240px;">
                <span style="background-color: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 10px; font-weight: 600; font-size: 0.85rem;">{card['pos'].upper()}</span>
                <h2 style="color: #1E3A8A; margin-top: 10px; margin-bottom: 2px;">{card['word']}</h2>
                <p style="color: #4B5563; font-size: 1rem; font-weight: 500;">🔊 IPA: {card['ipa']}</p>
                <hr style="border: 0.5px solid #BFDBFE;">
                <p style="font-size: 1.05rem; color: #1F2937;"><b>Định nghĩa (English):</b> {card['def']}</p>
                <p style="font-size: 1.05rem; color: #059669;"><b>Nghĩa Tiếng Việt:</b> {card['vi']}</p>
                <p style="font-style: italic; color: #4B5563;"><b>💬 Ví dụ ngữ cảnh:</b> "{card['example']}"</p>
            </div>
            """, unsafe_allow_html=True)
            
        c_prev, c_next, _ = st.columns([1, 1, 3])
        with c_prev:
            if st.button("⬅️ Thẻ trước"):
                st.session_state.flashcard_idx = (curr_idx - 1) % total_fc
                st.rerun()
        with c_next:
            if st.button("Thẻ tiếp ➡️"):
                st.session_state.flashcard_idx = (curr_idx + 1) % total_fc
                st.rerun()
                
        st.caption(f"Thẻ {curr_idx + 1} / {total_fc}")

# 5. WATCH OUT PAGE
elif menu == "⚠️ Góc lưu ý (Watch Out! Corner)":
    st.markdown('<div class="main-header">⚠️ Góc Lưu ý Ngữ Pháp & Từ Vựng (Watch Out!)</div>', unsafe_allow_html=True)
    st.write("Tổng hợp các điểm bẫy thi quan trọng giúp học sinh không bị mất điểm trong các kỳ thi Cambridge CAE & CPE:")
    
    st.markdown("""
    <div class="watchout-box">
        <div class="tip-title">1. Present Perfect Simple vs Present Perfect Continuous</div>
        • <b>Present Perfect Simple</b>: Nhấn mạnh vào <i>kết quả hoàn thành</i> hoặc <i>số lượng/số lần cụ thể</i>.<br>
        Ví dụ: <i>I've written two essays this week.</i> (KHÔNG dùng present perfect continuous).<br>
        • <b>Present Perfect Continuous</b>: Nhấn mạnh vào <i>tính liên tục</i> và <i>thời lượng kéo dài</i> của hành động.<br>
        Ví dụ: <i>I've been working here for five years.</i>
    </div>
    
    <div class="watchout-box">
        <div class="tip-title">2. Stative Verbs in Continuous Tenses</div>
        Các động từ như <i>think, feel, have, look, smell, taste</i> chỉ dùng thì đơn khi diễn tả <b>trạng thái / sở hữu / quan điểm</b>, nhưng chuyển sang thì tiếp diễn khi diễn tả <b>hành động chủ động</b>.<br>
        • <i>I think you're right.</i> (trạng thái: think = believe)<br>
        • <i>I'm thinking about going on a course.</i> (hành động: think = consider)
    </div>
    
    <div class="watchout-box">
        <div class="tip-title">3. Always with Present Continuous</div>
        Khi dùng trạng từ <i>always</i> kết hợp với thì Present Continuous, câu mang thái độ phàn nàn/bực mình về một thói quen phiền phức của người khác.<br>
        Ví dụ: <i>Dan's always coming up with the craziest ideas!</i>
    </div>
    
    <div class="watchout-box">
        <div class="tip-title">4. Cynical vs Sceptical</div>
        • <b>Cynical</b>: Hoài nghi về động cơ/lòng tốt của con người (nghĩ ai cũng vị kỷ).<br>
        • <b>Sceptical</b>: Hoài nghi về độ tin cậy của thông tin, tin tức hoặc một tuyên bố.
    </div>
    """, unsafe_allow_html=True)

# 6. PROGRESS TRACKER
elif menu == "📊 Báo cáo Tiến độ Học tập":
    st.markdown('<div class="main-header">📊 Báo cáo Tiến độ Học tập</div>', unsafe_allow_html=True)
    
    completed = len(st.session_state.completed_units)
    total = len(UNITS_DATA)
    pct = int((completed / total) * 100)
    
    st.progress(pct / 100)
    st.subheader(f"Mức độ hoàn thành: {pct}% ({completed}/{total} Units)")
    
    if completed > 0:
        st.success("Các Unit bạn đã hoàn thành bài tập thực hành:")
        for u in st.session_state.completed_units:
            st.write(f"- ✅ {u}")
    else:
        st.info("Bạn chưa hoàn thành bài tập trắc nghiệm nào. Hãy sang mục **✍️ Bài tập Tương tác & Chấm điểm tự động** để thử sức ngay!")

import streamlit as st

# Page config
st.set_page_config(
    page_title="Destination C1 & C2 Learning Hub",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished styling
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
    .badge-c1 {
        background-color: #3B82F6;
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
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'completed_units' not in st.session_state:
    st.session_state.completed_units = []
if 'flashcard_idx' not in st.session_state:
    st.session_state.flashcard_idx = 0

# --- DATA STRUCTURES GROUNDED IN DESTINATION C1 & C2 ---

UNITS_DATA = {
    "Unit 1: Grammar - Present time": {
        "type": "Grammar",
        "level": "C1/C2",
        "description": "Các thì hiện tại: Present simple, Emphatic present simple, Present continuous, Present perfect simple, Present perfect continuous, Stative verbs.",
        "theory": {
            "Present simple": [
                ("General truths", "The left-hand side of the brain controls the right-hand side of the body."),
                ("Current habits", "I don't always go to lectures that are early in the morning!"),
                ("Permanent situations & states", "Angie teaches French at a local adult education centre."),
                ("Proverbs & sayings", "Too many cooks spoil the broth."),
                ("Timetables / Fixed events", "Term ends on 21st December.")
            ],
            "Emphatic present simple": [
                ("To emphasise contrast", "Adam doesn't know much about psychiatry but he DOES know quite a lot about psychology."),
                ("To emphasise strong feeling", "I DO like playing word games!")
            ],
            "Present continuous": [
                ("Actions happening now / around now", "The boys are doing their homework right now."),
                ("Annoying / amusing habits (with always)", "Dan's always coming up with the craziest ideas!"),
                ("Changing and developing situations", "More and more people are recognising the advantages of learning a foreign language.")
            ],
            "Stative vs Non-stative Verbs": [
                ("Stative (Simple tenses)", "I think it's important to know how to use a computer. (think = believe)"),
                ("Dynamic/Action (Continuous tenses)", "I'm thinking about going on a computer course. (think = consider)")
            ]
        },
        "watch_out": [
            "Dùng Present Perfect Simple khi đề cập đến số lượng cụ thể: 'I've written two essays this week' (KHÔNG dùng present perfect continuous).",
            "Dùng Present Perfect Continuous để nhấn mạnh khoảng thời gian kéo dài: 'I've been working here for five years' (nhấn mạnh duration).",
            "Động từ trạng thái (Stative verbs) như believe, doubt, know, realise, suppose, understand chỉ dùng ở thể đơn, ngoại trừ khi chuyển sang nghĩa hành động."
        ],
        "quiz": [
            {
                "question": "1. Could you explain what 'antidisestablishmentarianism' _____?",
                "options": ["means", "is meaning"],
                "answer": "means",
                "explanation": "'mean' là stative verb biểu thị ý nghĩa/định nghĩa, không dùng thì tiếp diễn."
            },
            {
                "question": "2. I _____ that woman over there. Wasn't she on that quiz show last night?",
                "options": ["recognise", "am recognising"],
                "answer": "recognise",
                "explanation": "'recognise' là động từ tri giác/trạng thái (perception), dùng Present Simple."
            },
            {
                "question": "3. Right now, my job _____ a huge amount of foreign travel.",
                "options": ["involves", "is involving"],
                "answer": "involves",
                "explanation": "'involve' mô tả thuộc tính/bản chất công việc, dùng Present Simple."
            },
            {
                "question": "4. We _____ the living room repainted so it's probably best if we go into the kitchen.",
                "options": ["have", "are having"],
                "answer": "are having",
                "explanation": "'have' ở đây mang nghĩa hành động (thuê sơn lại nhà), dùng Present Continuous."
            }
        ]
    },
    "Unit 2: Vocabulary - Thinking and learning": {
        "type": "Vocabulary",
        "level": "C1/C2",
        "description": "Từ vựng chủ đề Tư duy & Học tập, Phrasal Verbs, Idioms, Collocations và Word Formation.",
        "theory": {
            "Topic Vocabulary": [
                ("assess (v)", "Đánh giá bản chất, giá trị hoặc khả năng của cái gì."),
                ("baffle (v)", "Gây bối rối, hoàn toàn không thể hiểu được."),
                ("cynical (adj)", "Hoài nghi về lòng tốt hoặc sự chân thành của con người."),
                ("dubious (adj)", "Mơ hồ, đáng ngờ, nghi ngại."),
                ("ingenious (adj)", "Khéo léo, thông minh, phát minh độc đáo."),
                ("plausible (adj)", "Hợp lý, có vẻ đúng, đáng tin cậy.")
            ],
            "Phrasal Verbs": [
                ("brush up (on)", "Rèn luyện, ôn lại để cải thiện kỹ năng/kiến thức."),
                ("come around (to)", "Thay đổi ý kiến/quan điểm vì bị thuyết phục."),
                ("come up with", "Nghĩ ra một ý tưởng, kế hoạch."),
                ("face up to", "Chấp nhận và đối mặt với thực tế khó khăn."),
                ("mull over", "Suy ngẫm, cân nhắc kỹ lưỡng trong một khoảng thời gian."),
                ("piece together", "Xâu chuỗi các manh mối/thông tin để hiểu sự thật.")
            ],
            "Idioms": [
                ("go to your head", "Thành công khiến ai đó trở nên kiêu ngạo."),
                ("have your wits about you", "Tỉnh táo, suy nghĩ nhanh để đưa ra quyết định đúng."),
                ("not see the wood for the trees", "Quá chú ý chi tiết nhỏ mà không thấy bức tranh toàn cảnh."),
                ("quick / slow on the uptake", "Nảy số nhanh / tiếp thu chậm."),
                ("ring a bell", "Nghe quen quen nhưng không nhớ rõ chi tiết.")
            ],
            "Word Formation": [
                ("assume", "assumption, assuming, unassuming, assumed"),
                ("conceive", "concept, conception, conceptual, (in)conceivable, (in)conceivably"),
                ("rational", "rationalise, rationalisation, rationalist, rationalism, (ir)rationality, (ir)rational(ly)"),
                ("sane", "(in)sanity, insane(ly)")
            ]
        },
        "watch_out": [
            "Phân biệt 'cynical' (hoài nghi nhân cách con người) và 'sceptical/skeptical' (hoài nghi tính đúng đắn của thông tin/kế hoạch).",
            "Phrasal verb 'swot up (on)' nghĩa là học dồn, học chăm chỉ trước kỳ thi (tương tự 'cram')."
        ],
        "quiz": [
            {
                "question": "1. I spent all evening _____ over the decision before finally deciding to accept the job.",
                "options": ["mulling", "brushing", "puzzling", "piecing"],
                "answer": "mulling",
                "explanation": "'mull over' nghĩa là suy ngẫm, cân nhắc kỹ lưỡng một quyết định."
            },
            {
                "question": "2. Don't let success go to your _____; stay humble and keep working hard.",
                "options": ["head", "mind", "brain", "wit"],
                "answer": "head",
                "explanation": "Idiom 'go to your head' nghĩa là bị sự thành công làm cho kiêu ngạo."
            },
            {
                "question": "3. The proposal sounds completely _____ and well-thought-out.",
                "options": ["plausible", "dubious", "baffled", "naive"],
                "answer": "plausible",
                "explanation": "'plausible' có nghĩa là hợp lý, khả thi, đáng tin."
            }
        ]
    },
    "Unit 11: Grammar - Conditionals": {
        "type": "Grammar",
        "level": "C1/C2",
        "description": "Câu điều kiện nâng cao (Zero, 1st, 2nd, 3rd, Mixed Conditionals, Inversion/Đảo ngữ câu điều kiện).",
        "theory": {
            "Conditionals Structure": [
                ("Zero Conditional", "If/when/whenever + present, present (Sự thật khoa học / Chân lý)"),
                ("First Conditional", "If + present, will + bare inf / imperative (Điều kiện có thật ở hiện tại/tương lai)"),
                ("Second Conditional", "If + past simple/continuous, would + bare inf (Giả định trái thực tế hiện tại)"),
                ("Third Conditional", "If + past perfect, would have + past participle (Giả định trái thực tế quá khứ)"),
                ("Mixed Conditionals", "If + past perfect (quá khứ), would + bare inf (kết quả ở hiện tại)")
            ],
            "Inversion (Đảo ngữ)": [
                ("Type 1", "Should you need any assistance, please do not hesitate to ask."),
                ("Type 2", "Were I in your position, I would accept the offer."),
                ("Type 3", "Had we known about the delay, we would have taken an earlier train.")
            ]
        },
        "watch_out": [
            "Trong văn phong trang trọng (Formal/British English), 'were' được dùng cho tất cả các ngôi trong câu điều kiện loại 2 (If I were / If he were).",
            "Có thể dùng các từ nối thay thế 'If' như: provided (that), providing (that), as long as, condition that, suppose, supposing, unless."
        ],
        "quiz": [
            {
                "question": "1. _____ known about the traffic jam, I would have left home half an hour earlier.",
                "options": ["Had I", "Should I", "Were I", "If I"],
                "answer": "Had I",
                "explanation": "Cấu trúc đảo ngữ câu điều kiện loại 3: Had + S + V3/ed..."
            },
            {
                "question": "2. If I _____ you, I would consult a legal expert before signing.",
                "options": ["were", "am", "would be", "had been"],
                "answer": "were",
                "explanation": "Câu điều kiện loại 2 giả định trái với thực tế hiện tại."
            }
        ]
    }
}

FLASHCARDS = [
    {"word": "assess (v)", "pos": "verb", "def": "evaluate or estimate the nature, ability, or quality of", "vi": "đánh giá, định giá", "ex": "It's difficult to assess the impact of the new policy."},
    {"word": "baffle (v)", "pos": "verb", "def": "totally bewilder, confuse or perplex", "vi": "gây bối rối, làm kinh ngạc", "ex": "His sudden decision to quit baffled everyone in the office."},
    {"word": "brush up (on)", "pos": "phrasal verb", "def": "practise and improve your skills or knowledge of something", "vi": "ôn luyện, trau dồi lại", "ex": "I need to brush up on my French before visiting Paris."},
    {"word": "go to your head", "pos": "idiom", "def": "cause someone to become arrogant or overconfident", "vi": "làm cho ai đó mắc bệnh ngôi sao / kiêu ngạo", "ex": "Don't let that promotion go to your head!"},
    {"word": "not see the wood for the trees", "pos": "idiom", "def": "be unable to understand what is important because you are paying too much attention to details", "vi": "không thấy bức tranh toàn cảnh do quá chú ý tiểu tiết", "ex": "He was so focused on formatting that he couldn't see the wood for the trees."}
]

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📚 Destination C1 & C2")
st.sidebar.caption("Hệ thống Tự học Ngữ pháp & Từ vựng Nâng cao")

menu = st.sidebar.radio(
    "Danh mục học tập",
    [
        "📌 Tổng quan & Lộ trình",
        "📖 Góc Lý thuyết (Theory)",
        "✍️ Luyện tập Tương tác (Quiz)",
        "🎴 Thẻ từ vựng (Flashcards)",
        "⚠️ Góc Bẫy thi (Watch Out!)",
        "📊 Tiến độ Học tập"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Thông tin sách:**")
st.sidebar.write("• Tác giả: Malcolm Mann & Steve Taylore-Knowles")
st.sidebar.write("• Trình độ: C1 & C2 (CAE / CPE)")
st.sidebar.write("• Cấu trúc: 26 Units + 13 Reviews")

# --- MAIN CONTENT PAGES ---

# 1. OVERVIEW PAGE
if menu == "📌 Tổng quan & Lộ trình":
    st.markdown('<div class="main-header">Destination C1 & C2: Learning Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Nền tảng hỗ trợ học sinh tự học Ngữ pháp & Từ vựng Tiếng Anh C1 & C2 tại nhà</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Tổng số Bài học", value="26 Units", delta="13 Grammar + 13 Vocab")
    with col2:
        st.metric(label="Bài Ôn tập & Kiểm tra", value="21 Tests", delta="13 Reviews + 8 Tests")
    with col3:
        st.metric(label="Mục tiêu Trình độ", value="C1 & C2", delta="Cambridge CAE & CPE")
        
    st.markdown("---")
    st.subheader("🎯 Lộ trình Tự học Chuẩn hóa")
    st.write("""
    Mỗi bài học trong sách **Destination C1 & C2** được thiết kế đan xen giữa **1 bài Ngữ pháp (Grammar)** và **1 bài Từ vựng (Vocabulary)** theo chủ đề. 
    Hệ thống Web này giúp bạn thẩm thấu kiến thức qua 4 bước:
    1. **Nắm vững Lý thuyết**: Tra cứu quy tắc ngữ pháp dạng bảng so sánh và hệ thống từ vựng chủ đề, cụm động từ, thành ngữ.
    2. **Phòng tránh Bẫy thi (Watch Out!)**: Ghi nhớ các lỗi sai kinh điển người học thường mắc phải trong bài thi CAE/CPE.
    3. **Luyện bài tập tương tác**: Làm bài trực tiếp có chấm điểm tự động và giải thích chi tiết.
    4. **Ghi nhớ lâu với Flashcards**: Thẻ từ vựng thông minh hỗ trợ tra cứu nghĩa, từ loại và ví dụ thực tế.
    """)
    
    st.markdown("### 📋 Danh sách Units chính trong sách:")
    st.table([
        {"Unit": "Unit 1", "Chủ đề": "Grammar: Present time", "Trình độ": "C1/C2"},
        {"Unit": "Unit 2", "Chủ đề": "Vocabulary: Thinking and learning", "Trình độ": "C1/C2"},
        {"Unit": "Unit 3", "Chủ đề": "Grammar: Past time", "Trình độ": "C1/C2"},
        {"Unit": "Unit 4", "Chủ đề": "Vocabulary: Change and technology", "Trình độ": "C1/C2"},
        {"Unit": "Unit 5", "Chủ đề": "Grammar: Future time", "Trình độ": "C1/C2"},
        {"Unit": "Unit 6", "Chủ đề": "Vocabulary: Time and work", "Trình độ": "C1/C2"},
        {"Unit": "Unit 11", "Chủ đề": "Grammar: Conditionals", "Trình độ": "C1/C2"},
        {"Unit": "Unit 13", "Chủ đề": "Grammar: Unreal time", "Trình độ": "C1/C2"}
    ])

# 2. THEORY PAGE
elif menu == "📖 Góc Lý thuyết (Theory)":
    st.markdown('<div class="main-header">📖 Tra cứu Lý thuyết Trọng tâm</div>', unsafe_allow_html=True)
    selected_unit_key = st.selectbox("Chọn Unit muốn học:", list(UNITS_DATA.keys()))
    
    unit_info = UNITS_DATA[selected_unit_key]
    
    st.markdown(f"### {selected_unit_key}")
    st.markdown(f"**Trình độ:** <span class='badge-c1'>{unit_info['level']}</span> | **Mô tả:** {unit_info['description']}", unsafe_allow_html=True)
    st.markdown("---")
    
    if unit_info["type"] == "Grammar":
        tab1, tab2 = st.tabs(["📌 Cấu trúc & Quy tắc Ngữ pháp", "⚠️ Hộp Lưu ý (Watch Out!)"])
        with tab1:
            for rule_title, examples in unit_info["theory"].items():
                st.markdown(f"#### 🔹 {rule_title}")
                for usage, sentence in examples:
                    st.markdown(f"- **{usage}**: *{sentence}*")
                st.markdown("<br>", unsafe_allow_html=True)
        with tab2:
            st.warning("Các điểm ngữ pháp hay bẫy học sinh trong bài thi:")
            for wo in unit_info["watch_out"]:
                st.markdown(f"- {wo}")
                
    elif unit_info["type"] == "Vocabulary":
        tab1, tab2, tab3 = st.tabs(["📚 Từ vựng Chủ đề & Phrasal Verbs", "💡 Idioms & Collocations", "🔤 Word Formation"])
        with tab1:
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                st.markdown("#### Topic Vocabulary")
                for w, d in unit_info["theory"].get("Topic Vocabulary", []):
                    st.markdown(f"• **{w}**: {d}")
            with col_v2:
                st.markdown("#### Phrasal Verbs")
                for pv, m in unit_info["theory"].get("Phrasal Verbs", []):
                    st.markdown(f"• **{pv}**: {m}")
        with tab2:
            st.markdown("#### Idioms")
            for idm, m in unit_info["theory"].get("Idioms", []):
                st.markdown(f"• **{idm}**: {m}")
        with tab3:
            st.markdown("#### Word Formation Database")
            for base, derivs in unit_info["theory"].get("Word Formation", []):
                st.markdown(f"• **{base}** ➔ `{derivs}`")

# 3. QUIZ PRACTICE PAGE
elif menu == "✍️ Luyện tập Tương tác (Quiz)":
    st.markdown('<div class="main-header">✍️ Bài tập Tương tác & Luyện đề</div>', unsafe_allow_html=True)
    selected_quiz_unit = st.selectbox("Chọn bài tập theo Unit:", list(UNITS_DATA.keys()), key="quiz_unit_select")
    
    quiz_list = UNITS_DATA[selected_quiz_unit]["quiz"]
    
    st.info("Hãy chọn đáp án đúng cho mỗi câu hỏi dưới đây và ấn nút **Kiểm tra Đáp án**.")
    
    user_answers = {}
    with st.form("quiz_form"):
        for i, q in enumerate(quiz_list):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            user_answers[i] = st.radio(
                f"Lựa chọn cho câu {i+1}:", 
                q['options'], 
                key=f"q_{selected_quiz_unit}_{i}",
                index=0
            )
            st.markdown("---")
            
        submitted = st.form_submit_button("🚀 Submit Answers / Kiểm tra Đáp án")
        
    if submitted:
        score = 0
        st.markdown("### 📊 Kết quả Bài làm:")
        for i, q in enumerate(quiz_list):
            if user_answers[i] == q['answer']:
                score += 1
                st.success(f"✅ **Câu {i+1}: Chính xác!** ({q['answer']})")
            else:
                st.error(f"❌ **Câu {i+1}: Chưa đúng.** Đáp án đúng là **{q['answer']}** (Bạn chọn: {user_answers[i]})")
            st.caption(f"💡 *Giải thích:* {q['explanation']}")
            st.markdown("<br>", unsafe_allow_html=True)
            
        final_score = int((score / len(quiz_list)) * 100)
        st.metric("Điểm số của bạn", f"{final_score}%", f"{score}/{len(quiz_list)} câu đúng")
        
        if selected_quiz_unit not in st.session_state.completed_units:
            st.session_state.completed_units.append(selected_quiz_unit)

# 4. FLASHCARDS PAGE
elif menu == "🎴 Thẻ từ vựng (Flashcards)":
    st.markdown('<div class="main-header">🎴 Flashcards Từ vựng & Cụm từ C1/C2</div>', unsafe_allow_html=True)
    st.caption("Lật thẻ để học từ vựng, phrasal verbs và idioms trọng tâm.")
    
    total_fc = len(FLASHCARDS)
    curr_idx = st.session_state.flashcard_idx
    card = FLASHCARDS[curr_idx]
    
    col_fc, _ = st.columns([2, 1])
    with col_fc:
        st.markdown(f"""
        <div style="background-color: #EFF6FF; border: 2px solid #3B82F6; border-radius: 12px; padding: 2rem; text-align: center; min-height: 220px;">
            <span style="background-color: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 10px; font-weight: 600; font-size: 0.85rem;">{card['pos'].upper()}</span>
            <h2 style="color: #1E3A8A; margin-top: 10px;">{card['word']}</h2>
            <hr style="border: 0.5px solid #BFDBFE;">
            <p style="font-size: 1.1rem; color: #1F2937;"><b>Định nghĩa (English):</b> {card['def']}</p>
            <p style="font-size: 1.1rem; color: #059669;"><b>Nghĩa tiếng Việt:</b> {card['vi']}</p>
            <p style="font-style: italic; color: #4B5563;"><b>Ví dụ:</b> "{card['ex']}"</p>
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
elif menu == "⚠️ Góc Bẫy thi (Watch Out!)":
    st.markdown('<div class="main-header">⚠️ Góc Bẫy Ngữ Pháp & Từ Vựng (Watch Out!)</div>', unsafe_allow_html=True)
    st.write("Những điểm lưu ý quan trọng giúp bạn không mất điểm đáng tiếc trong kỳ thi Cambridge CAE & CPE:")
    
    st.markdown("""
    <div class="watchout-box">
        <div class="tip-title">1. Stative Verbs in Continuous Tenses</div>
        Các động từ như <i>think, feel, have, look, smell, taste</i> có thể dùng ở thì tiếp diễn khi diễn tả <b>hành động/quá trình</b>, nhưng chỉ dùng thì đơn khi diễn tả <b>trạng thái/sở hữu/quan điểm</b>.
        <br>• <i>I think you're right.</i> (Bản chất: quan điểm = believe)
        <br>• <i>I'm thinking about buying a car.</i> (Hành động: cân nhắc = considering)
    </div>
    
    <div class="watchout-box">
        <div class="tip-title">2. Would Rather vs Would Prefer</div>
        • <b>would rather + bare infinitive</b>: <i>I'd rather stay at home tonight.</i><br>
        • <b>would rather + somebody + Past Simple</b> (diễn tả mong muốn người khác làm gì ở hiện tại): <i>I'd rather you stayed at home.</i><br>
        • <b>would prefer + to infinitive</b>: <i>I'd prefer to eat out tonight.</i>
    </div>
    
    <div class="watchout-box">
        <div class="tip-title">3. Inversion with Negative Adverbials</div>
        Khi đưa các trạng từ phủ định lên đầu câu (Hardly, Barely, Scarcely, No sooner, Not only), bắt buộc phải đảo ngữ động từ:
        <br>• <i>Hardly had I sat down <b>when</b> the phone rang.</i>
        <br>• <i>No sooner had the alarm gone off <b>than</b> the police arrived.</i>
    </div>
    """, unsafe_allow_html=True)

# 6. PROGRESS TRACKER
elif menu == "📊 Tiến độ Học tập":
    st.markdown('<div class="main-header">📊 Báo cáo Tiến độ Tự học</div>', unsafe_allow_html=True)
    
    completed = len(st.session_state.completed_units)
    total = len(UNITS_DATA)
    pct = int((completed / total) * 100)
    
    st.progress(pct / 100)
    st.subheader(f"Hoàn thành: {pct}% ({completed}/{total} Units)")
    
    if completed > 0:
        st.success("Các Unit bạn đã làm bài luyện tập:")
        for u in st.session_state.completed_units:
            st.write(f"- ✅ {u}")
    else:
        st.info("Bạn chưa hoàn thành bài luyện tập nào. Hãy sang mục **✍️ Luyện tập Tương tác (Quiz)** để làm bài ngay!")

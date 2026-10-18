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
        "quiz_sections": {
            "Exercise A: Present Simple or Present Continuous": [
                {
                    "question": "My brother _____ (do) a degree at university so I _____ (see) him very often, unfortunately.",
                    "options": ["is doing / don't see", "does / am not seeing", "is doing / am not seeing"],
                    "answer": "is doing / don't see",
                    "explanation": "'is doing' (sự việc tạm thời ở hiện tại), 'don't see' (thói quen/trạng thái)."
                },
                {
                    "question": "Darren _____ (usually / get) home until about eight o'clock.",
                    "options": ["doesn't usually get", "isn't usually getting", "don't usually get"],
                    "answer": "doesn't usually get",
                    "explanation": "Thói quen hàng ngày dùng Present Simple phủ định."
                },
                {
                    "question": "I'm sorry to hear that your parents _____ (get) divorced.",
                    "options": ["are getting", "get", "are get"],
                    "answer": "are getting",
                    "explanation": "Quá trình đang diễn ra ở hiện tại dùng Present Continuous."
                },
                {
                    "question": "You _____ (go) to the end of the street and _____ (turn) right.",
                    "options": ["go / turn", "are going / are turning", "goes / turns"],
                    "answer": "go / turn",
                    "explanation": "Hướng dẫn đường đi dùng Present Simple."
                },
                {
                    "question": "Why _____ ice _____ (float)?",
                    "options": ["does ... float", "is ... floating", "do ... float"],
                    "answer": "does ... float",
                    "explanation": "Sự thật khoa học / chân lý tự nhiên dùng Present Simple."
                },
                {
                    "question": "It's lovely now the evenings _____ (get) longer, isn't it?",
                    "options": ["are getting", "get", "gets"],
                    "answer": "are getting",
                    "explanation": "Sự thay đổi, phát triển theo thời gian dùng Present Continuous."
                },
                {
                    "question": "My dad _____ (not / eat) meat at all - he's a vegetarian.",
                    "options": ["doesn't eat", "isn't eating", "don't eat"],
                    "answer": "doesn't eat",
                    "explanation": "Thói quen, bản chất kéo dài dùng Present Simple."
                },
                {
                    "question": "Actually, we _____ (listen) to The Libertines - this is Pete Doherty's second band, Babyshambles.",
                    "options": ["aren't listening", "don't listen", "not listening"],
                    "answer": "aren't listening",
                    "explanation": "Hành động ngay lúc nói dùng Present Continuous phủ định."
                },
                {
                    "question": "A man _____ (walk) into a bar. Ouch! Not a good idea to walk into an iron bar!",
                    "options": ["walks", "is walking", "walk"],
                    "answer": "walks",
                    "explanation": "Kể chuyện cười / truyện ngắn dùng Present Simple."
                },
                {
                    "question": "_____ you _____ (phone) me from your mobile? The line's not very good.",
                    "options": ["Are ... phoning", "Do ... phone", "Is ... phoning"],
                    "answer": "Are ... phoning",
                    "explanation": "Hành động đang diễn ra ngay lúc nói dùng Present Continuous."
                },
                {
                    "question": "_____ you often _____ (order) things online?",
                    "options": ["Do ... order", "Are ... ordering", "Does ... order"],
                    "answer": "Do ... order",
                    "explanation": "Hỏi về thói quen có từ nhận biết 'often' dùng Present Simple."
                },
                {
                    "question": "There's an Englishman, an Irishman and a Scotsman. They _____ (walk) across the desert when one of them _____ (spot) a camel in the distance...",
                    "options": ["are walking / spots", "walk / is spotting", "walks / spot"],
                    "answer": "are walking / spots",
                    "explanation": "Bối cảnh hành động đang diễn ra (are walking) và hành động cắt ngang (spots) trong lời kể."
                },
                {
                    "question": "Beckham _____ (have) control of the ball... It's Beckham... And he _____ (score)!",
                    "options": ["has / scores", "is having / is scoring", "has / is scoring"],
                    "answer": "has / scores",
                    "explanation": "Tường thuật thể thao trực tiếp dùng Present Simple."
                },
                {
                    "question": "WOMAN _____ (give) €500 MILLION LOTTERY WIN TO CHARITY",
                    "options": ["GIVES", "IS GIVING", "GIVE"],
                    "answer": "GIVES",
                    "explanation": "Tiêu đề báo chí (Newspaper headlines) dùng Present Simple."
                },
                {
                    "question": "My dad _____ (always / tell) jokes! They're usually rubbish, though.",
                    "options": ["is always telling", "always tells", "always tell"],
                    "answer": "is always telling",
                    "explanation": "Thói quen gây buồn cười/phiền phức đi với 'always' dùng Present Continuous."
                },
                {
                    "question": "'Phil _____ (wear) ties, does he?' 'Actually, he _____ (wear) a tie to work most days.'",
                    "options": ["doesn't usually wear / wears", "isn't usually wearing / is wearing", "don't wear / wear"],
                    "answer": "doesn't usually wear / wears",
                    "explanation": "Sự thật/thói quen lặp đi lặp lại dùng Present Simple."
                }
            ],
            "Exercise B: One Word in Each Gap": [
                {
                    "question": "Why do you _____ leave the light on when you go out of the room? You wait till you start paying the electricity bill!",
                    "options": ["always", "currently", "now"],
                    "answer": "always",
                    "explanation": "'always' dùng diễn tả thói quen phiền phức."
                },
                {
                    "question": "Fifteen teachers are teaching here full-time at _____ .",
                    "options": ["present", "now", "moment"],
                    "answer": "present",
                    "explanation": "Cụm từ 'at present' nghĩa là hiện tại."
                },
                {
                    "question": "My sister's revising for her GCSEs at the _____ .",
                    "options": ["moment", "present", "now"],
                    "answer": "moment",
                    "explanation": "Cụm từ 'at the moment' nghĩa là ngay lúc này."
                },
                {
                    "question": "I'm quite happy living at home for the time _____ , but I guess I'll have to get my own place eventually.",
                    "options": ["being", "now", "running"],
                    "answer": "being",
                    "explanation": "Cụm cố định 'for the time being' nghĩa là tạm thời trong lúc này."
                },
                {
                    "question": "It's true that Ralph calls us quite _____ , but most students only call their parents when they need something, don't they?",
                    "options": ["often", "always", "sometimes"],
                    "answer": "often",
                    "explanation": "Cụm 'quite often' chỉ tần suất thường xuyên."
                },
                {
                    "question": "We go to the cinema _____ now and then, but only if there's something good on.",
                    "options": ["every", "each", "all"],
                    "answer": "every",
                    "explanation": "Cụm thành ngữ 'every now and then' nghĩa là thỉnh thoảng."
                },
                {
                    "question": "I'm alone in my study bedroom reading _____ of the time.",
                    "options": ["most", "much", "many"],
                    "answer": "most",
                    "explanation": "Cụm 'most of the time' nghĩa là hầu hết thời gian."
                },
                {
                    "question": "Tim _____ goes out to play until he's done all his homework. I just don't allow it!",
                    "options": ["never", "rarely", "seldom"],
                    "answer": "never",
                    "explanation": "'never... until' nghĩa là không bao giờ làm gì cho tới khi."
                },
                {
                    "question": "I see Lucinda from _____ to time, but not on a regular basis.",
                    "options": ["time", "now", "moment"],
                    "answer": "time",
                    "explanation": "Cụm 'from time to time' nghĩa là thỉnh thoảng."
                },
                {
                    "question": "I'm sitting in the garden _____ now talking to you on my mobile.",
                    "options": ["right", "just", "even"],
                    "answer": "right",
                    "explanation": "Cụm 'right now' nghĩa là ngay chính lúc này."
                },
                {
                    "question": "That's the last _____ we're inviting Dave to one of our parties!",
                    "options": ["time", "moment", "day"],
                    "answer": "time",
                    "explanation": "Cụm cấu trúc 'That's the last time...' nghĩa là đó là lần cuối cùng."
                },
                {
                    "question": "Do young people these _____ have more free time than they did in the past?",
                    "options": ["days", "times", "years"],
                    "answer": "days",
                    "explanation": "Cụm 'these days' nghĩa là dạo này/ngày nay."
                },
                {
                    "question": "My mum fills up with petrol _____ she goes to the supermarket.",
                    "options": ["whenever", "wherever", "whatever"],
                    "answer": "whenever",
                    "explanation": "'whenever' nghĩa là bất cứ khi nào."
                },
                {
                    "question": "I'm staying in _____ now, but I might go out a bit later on.",
                    "options": ["for", "at", "by"],
                    "answer": "for",
                    "explanation": "Cụm 'for now' nghĩa là trước mắt / trong lúc này."
                },
                {
                    "question": "_____ is the last time I ever order from that pizzeria. It was disgusting!",
                    "options": ["That", "This", "It"],
                    "answer": "That",
                    "explanation": "Cấu trúc nhấn mạnh 'That is the last time...'."
                }
            ],
            "Exercise D: Circle the Correct Word or Phrase": [
                {
                    "question": "Could you explain what 'antidisestablishmentarianism' _____ , please?",
                    "options": ["means", "is meaning"],
                    "answer": "means",
                    "explanation": "'mean' là động từ chỉ ý nghĩa (stative verb), không chia thì tiếp diễn."
                },
                {
                    "question": "Each song only _____ 50 cents at the moment because they're on special offer.",
                    "options": ["costs", "is costing"],
                    "answer": "costs",
                    "explanation": "'cost' chỉ giá trị/chi phí (stative verb), dùng Present Simple."
                },
                {
                    "question": "It _____ which of the books we've studied this term you do your essay on.",
                    "options": ["doesn't matter", "isn't mattering"],
                    "answer": "doesn't matter",
                    "explanation": "'matter' (có ý nghĩa/quan trọng) là stative verb."
                },
                {
                    "question": "It's only a quick call as I _____ from my mobile.",
                    "options": ["am ringing", "ring"],
                    "answer": "am ringing",
                    "explanation": "Hành động đang thực hiện lúc nói dùng Present Continuous."
                },
                {
                    "question": "I think I _____ that woman over there. Wasn't she on that quiz show last night?",
                    "options": ["recognise", "am recognising"],
                    "answer": "recognise",
                    "explanation": "'recognise' (nhận ra) là động từ tri giác/nhận thức, dùng Present Simple."
                },
                {
                    "question": "Excuse me, _____ walnuts? I'm allergic to them.",
                    "options": ["does the nut cake contain", "is the nut cake containing"],
                    "answer": "does the nut cake contain",
                    "explanation": "'contain' (chứa đựng) là động từ trạng thái thuộc tính."
                },
                {
                    "question": "I _____ that capital punishment deters people from committing murder.",
                    "options": ["really don't agree", "am really not agreeing"],
                    "answer": "really don't agree",
                    "explanation": "'agree' (đồng ý) diễn tả quan điểm, dùng Present Simple."
                },
                {
                    "question": "Why _____ football, Mark? I thought you had a match this afternoon.",
                    "options": ["aren't you playing", "don't you play"],
                    "answer": "aren't you playing",
                    "explanation": "Hỏi về sự việc đang xảy ra/không xảy ra ở hiện tại."
                },
                {
                    "question": "Stay out of this, Simon, it _____ you at all.",
                    "options": ["doesn't concern", "isn't concerning"],
                    "answer": "doesn't concern",
                    "explanation": "'concern' (liên quan đến) là động từ trạng thái."
                },
                {
                    "question": "You really _____ your father when you frown like that.",
                    "options": ["resemble", "are resembling"],
                    "answer": "resemble",
                    "explanation": "'resemble' (giống ai) là động từ trạng thái chỉ vẻ ngoài."
                },
                {
                    "question": "If you _____ TV, turn it off!",
                    "options": ["aren't watching", "don't watch"],
                    "answer": "aren't watching",
                    "explanation": "Diễn tả hành động có đang xem hay không ngay thời điểm này."
                },
                {
                    "question": "The number you have dialled _____ . Please try again.",
                    "options": ["does not exist", "is not existing"],
                    "answer": "does not exist",
                    "explanation": "'exist' (tồn tại) là động từ trạng thái."
                },
                {
                    "question": "I want everyone to do exercise H, and that _____ you too, Anne!",
                    "options": ["includes", "is including"],
                    "answer": "includes",
                    "explanation": "'include' (bao gồm) chỉ thuộc tính thành phần, dùng Present Simple."
                },
                {
                    "question": "We _____ the living room repainted so it's probably best if we go into the kitchen.",
                    "options": ["are having", "have"],
                    "answer": "are having",
                    "explanation": "'have' ở đây mang nghĩa hành động (thuê thợ sơn lại nhà)."
                },
                {
                    "question": "Right now, my job _____ a huge amount of foreign travel.",
                    "options": ["involves", "is involving"],
                    "answer": "involves",
                    "explanation": "'involve' (đòi hỏi/bao gồm) chỉ bản chất công việc."
                }
            ],
            "Exercise E: Stative vs Dynamic Verb Pairs": [
                {
                    "question": "A: I _____ for a book on fly fishing. Do you have any in stock?\nB: Stan _____ like he's in a bad mood this morning.",
                    "options": ["am looking / looks", "look / is looking", "am looking / is looking"],
                    "answer": "am looking / looks",
                    "explanation": "'look for' = tìm kiếm (hành động tiếp diễn); 'look like' = trông có vẻ (trạng thái)."
                },
                {
                    "question": "A: How _____ you _____ about inviting Jackie to come with us on Saturday?\nB: Britney _____ very well, so I've told her she can go home.",
                    "options": ["are ... thinking / isn't feeling", "do ... think / doesn't feel", "do ... think / isn't feeling"],
                    "answer": "are ... thinking / isn't feeling",
                    "explanation": "'think about' = cân nhắc (hành động); 'feel well' = cảm giác sức khỏe (trạng thái/tiếp diễn)."
                },
                {
                    "question": "A: Jan and I _____ buying a new flat.\nB: Why _____ you _____ Ray Davis to be a better songwriter than Paul McCartney?",
                    "options": ["are considering / do ... consider", "consider / are ... considering", "are considering / are ... considering"],
                    "answer": "are considering / do ... consider",
                    "explanation": "'consider buying' = cân nhắc mua (hành động); 'consider sb to be' = đánh giá/xem ai như thế nào (quan điểm)."
                },
                {
                    "question": "A: We _____ a barbecue right now, so can I call you back this evening?\nB: _____ the Deacons _____ a swimming pool?",
                    "options": ["are having / Do ... have", "have / Are ... having", "are having / Are ... having"],
                    "answer": "are having / Do ... have",
                    "explanation": "'have a barbecue' = tổ chức tiệc (hành động); 'have a pool' = sở hữu (trạng thái)."
                },
                {
                    "question": "A: The idea of going to a Greek island really _____ to me.\nB: Police _____ for witnesses to the attack.",
                    "options": ["appeals / are appealing", "is appealing / appeal", "appeals / appeal"],
                    "answer": "appeals / are appealing",
                    "explanation": "'appeal to sb' = thu hút ai (trạng thái); 'appeal for' = kêu gọi tìm nhân chứng (hành động)."
                },
                {
                    "question": "A: This chicken _____ very fresh. I think I'll throw it away just to be on the safe side.\nB: Why _____ you _____ that chicken, Mum?",
                    "options": ["doesn't smell / are ... smelling", "isn't smelling / do ... smell", "doesn't smell / do ... smell"],
                    "answer": "doesn't smell / are ... smelling",
                    "explanation": "'smell fresh' = có mùi tươi (trạng thái); 'smell sth' = ngửi cái gì (hành động)."
                },
                {
                    "question": "A: I _____ on you, James. Don't let me down!\nB: Whether we get there by six _____ on the traffic.",
                    "options": ["am depending / depends", "depend / is depending", "am depending / is depending"],
                    "answer": "am depending / depends",
                    "explanation": "'depend on sb' = trông cậy vào ai (hành động tạm thời); 'depend on sth' = phụ thuộc vào điều gì (sự thật)."
                },
                {
                    "question": "A: Julian _____ a bit busy at the moment, actually.\nB: Guys, you _____ too noisy! Can't you keep it down, please?",
                    "options": ["is / are being", "is being / are", "is / are"],
                    "answer": "is / are being",
                    "explanation": "'is busy' = tình trạng bản chất; 'are being noisy' = đang tỏ ra ồn ào bất thường."
                },
                {
                    "question": "A: _____ you _____ Bob would like a CD for his birthday?\nB: Oliver said he _____ about moving out of the city.",
                    "options": ["Do ... think / is thinking", "Are ... thinking / thinks", "Do ... think / thinks"],
                    "answer": "Do ... think / is thinking",
                    "explanation": "'think' = tin/nghĩ rằng (quan điểm); 'think about' = đang trăn trở/cân nhắc (hành động)."
                },
                {
                    "question": "A: I hear that Doug _____ quite a lot of Katy these days. Is that true?\nB: I _____ Manchester United lost again.",
                    "options": ["is seeing / see", "sees / am seeing", "sees / see"],
                    "answer": "is seeing / see",
                    "explanation": "'see sb' = hò hẹn/gặp gỡ ai (hành động); 'see that' = thấy/hiểu rằng (nhận thức)."
                }
            ],
            "Exercise G: Present Perfect Simple vs Continuous": [
                {
                    "question": "They've _____ six bags with rubbish from the beach already.",
                    "options": ["filled", "been filling"],
                    "answer": "filled",
                    "explanation": "Nhấn mạnh số lượng/kết quả đã hoàn thành ('six bags... already') dùng Present Perfect Simple."
                },
                {
                    "question": "Have you _____ that story in the papers about the elephant that escaped from the zoo?",
                    "options": ["been following", "followed"],
                    "answer": "been following",
                    "explanation": "Hỏi về quá trình theo dõi thông tin kéo dài liên tục dùng Present Perfect Continuous."
                },
                {
                    "question": "We've _____ the Tower of London, Buckingham Palace and Oxford Street, and we've only been in London for three hours!",
                    "options": ["seen", "been seeing"],
                    "answer": "seen",
                    "explanation": "Nhấn mạnh các địa điểm đã đi qua (kết quả/số lượng) dùng Present Perfect Simple."
                },
                {
                    "question": "It's the first time I've _____ The Editors play live.",
                    "options": ["heard", "been hearing"],
                    "answer": "heard",
                    "explanation": "Cấu trúc 'It's the first time I have + V3' dùng Present Perfect Simple."
                },
                {
                    "question": "Jake and I have _____ about where to go on holiday for weeks but we just can't decide.",
                    "options": ["been thinking", "thought"],
                    "answer": "been thinking",
                    "explanation": "Nhấn mạnh sự liên tục kéo dài nhiều tuần ('for weeks') dùng Present Perfect Continuous."
                },
                {
                    "question": "You can't want to go to the toilet already - we've only _____ for about ten minutes so far!",
                    "options": ["been driving", "driven"],
                    "answer": "been driving",
                    "explanation": "Nhấn mạnh khoảng thời gian lái xe liên tục ('for about ten minutes') dùng Present Perfect Continuous."
                },
                {
                    "question": "I've _____ up all day and my feet are killing me!",
                    "options": ["been standing", "stood"],
                    "answer": "been standing",
                    "explanation": "Nhấn mạnh khoảng thời gian kéo dài cả ngày ('all day') và hậu quả trực tiếp ở hiện tại."
                },
                {
                    "question": "Has Jan _____ for the company since it started?",
                    "options": ["been working", "worked"],
                    "answer": "been working",
                    "explanation": "Hỏi về tính liên tục của công việc từ quá khứ đến hiện tại với 'since'."
                }
            ],
            "Exercise H: Present Perfect Simple or Continuous Forms": [
                {
                    "question": "I _____ (send off) over 18 press releases this morning so far.",
                    "options": ["have sent off", "have been sending off"],
                    "answer": "have sent off",
                    "explanation": "Có số lượng cụ thể ('over 18 press releases') dùng Present Perfect Simple."
                },
                {
                    "question": "Is it the first time you _____ (ever / eat) squid?",
                    "options": ["have ever eaten", "have ever been eating"],
                    "answer": "have ever eaten",
                    "explanation": "Cấu trúc 'Is it the first time S + have ever + V3'."
                },
                {
                    "question": "We _____ (wait) for you for the past two hours. Where _____ (you / be)?",
                    "options": ["have been waiting / have you been", "have waited / are you"],
                    "answer": "have been waiting / have you been",
                    "explanation": "Nhấn mạnh thời gian chờ đợi liên tục 2 tiếng ('for the past two hours')."
                },
                {
                    "question": "_____ (you / just / receive) an e-mail from Ruth?",
                    "options": ["Have you just received", "Have you just been receiving"],
                    "answer": "Have you just received", "explanation": "Hành động vừa mới xảy ra với 'just' dùng Present Perfect Simple."
                },
                {
                    "question": "I'm afraid we _____ (not / get) any milk. We _____ (expect) a delivery for the past four hours but they _____ (not / show up) yet.",
                    "options": ["haven't got / have been expecting / haven't shown up", "haven't been getting / expect / don't show up"],
                    "answer": "haven't got / have been expecting / haven't shown up",
                    "explanation": "Kết hợp Present Perfect Simple (kết quả không có sữa) và Continuous (chờ đợi liên tục 4 tiếng)."
                },
                {
                    "question": "I _____ (draw up) a list of people to invite to the wedding but I _____ (only / get) so far so far. _____ (you / have) any thoughts about it?",
                    "options": ["have been drawing up / have only got / Have you had", "draw up / get / Do you have"],
                    "answer": "have been drawing up / have only got / Have you had",
                    "explanation": "Quá trình lập danh sách liên tục (have been drawing up) và kết quả hiện tại (have only got)."
                },
                {
                    "question": "Oh, Clair, my mum _____ (mean) to ask you for a while. Would you like to come with us to Wimbledon?",
                    "options": ["has been meaning", "has meant"],
                    "answer": "has been meaning",
                    "explanation": "Ý định ấp ủ liên tục trong thời gian qua ('for a while') dùng Present Perfect Continuous."
                }
            ],
            "Exercise I: Time Adverbs Gap Fill": [
                {
                    "question": "I've _____ realised what's different! You've changed your hair.",
                    "options": ["just", "already", "yet"],
                    "answer": "just",
                    "explanation": "'just' nghĩa là vừa mới nhận ra."
                },
                {
                    "question": "My grandmother's been quite ill _____ , so she's coming to stay with us for a week or two.",
                    "options": ["recently", "since", "for"],
                    "answer": "recently",
                    "explanation": "'recently' nghĩa là gần đây."
                },
                {
                    "question": "We've had broadband at home _____ about 2005.",
                    "options": ["since", "for", "already"],
                    "answer": "since",
                    "explanation": "'since' đi với mốc thời gian (2005)."
                },
                {
                    "question": "Have you really finished your homework _____ ? Okay, you can watch TV, then.",
                    "options": ["already", "yet", "still"],
                    "answer": "already",
                    "explanation": "'already' dùng trong câu hỏi diễn tả sự ngạc nhiên vì làm xong sớm."
                },
                {
                    "question": "We've won every match we've played _____ far this season.",
                    "options": ["so", "until", "yet"],
                    "answer": "so",
                    "explanation": "Cụm 'so far' nghĩa là cho đến nay."
                },
                {
                    "question": "I've always lived in a big house _____ now, so it's taking some time to get used to being in a small flat.",
                    "options": ["until", "since", "for"],
                    "answer": "until",
                    "explanation": "'until now' nghĩa là cho tới tận bây giờ."
                },
                {
                    "question": "We can't cancel the party now - I've _____ invited everyone!",
                    "options": ["already", "yet", "still"],
                    "answer": "already",
                    "explanation": "'already' nghĩa là đã mời rồi."
                },
                {
                    "question": "How long has Sue gone abroad _____ ?",
                    "options": ["for", "since", "until"],
                    "answer": "for",
                    "explanation": "'for' đi với khoảng thời gian đi nước ngoài."
                },
                {
                    "question": "Don't get Matthew that game; I'm pretty sure he's got it _____ .",
                    "options": ["already", "yet", "still"],
                    "answer": "already",
                    "explanation": "'already' đứng cuối câu khẳng định."
                },
                {
                    "question": "Have you _____ thought of going into business on your own?",
                    "options": ["ever", "never", "before"],
                    "answer": "ever",
                    "explanation": "'ever' nghĩa là đã bao giờ (trong câu hỏi)."
                },
                {
                    "question": "We haven't started _____ so you can join in if you like.",
                    "options": ["yet", "already", "still"],
                    "answer": "yet",
                    "explanation": "'yet' ở cuối câu phủ định."
                },
                {
                    "question": "We've never been to New York _____ , so we're both really looking forward to it.",
                    "options": ["before", "ever", "already"],
                    "answer": "before",
                    "explanation": "'before' ở cuối câu mang nghĩa trước đây."
                },
                {
                    "question": "Have they been living in the neighbourhood _____ you moved in?",
                    "options": ["since", "for", "until"],
                    "answer": "since",
                    "explanation": "'since' đi với mệnh đề quá khứ đơn (you moved in)."
                },
                {
                    "question": "I _____ haven't found my sunglasses.",
                    "options": ["still", "yet", "already"],
                    "answer": "still",
                    "explanation": "'still' đứng trước trợ động từ phủ định (haven't)."
                },
                {
                    "question": "I've been looking for a website like this _____ ages!",
                    "options": ["for", "since", "until"],
                    "answer": "for",
                    "explanation": "'for ages' nghĩa là trong một thời gian rất dài."
                },
                {
                    "question": "It's strange you should ring now. We've _____ been talking about you.",
                    "options": ["just", "already", "yet"],
                    "answer": "just",
                    "explanation": "'just' nghĩa là vừa mới nhắc tới xong."
                },
                {
                    "question": "Michael, haven't you done your homework _____ ? I think it's time you started, isn't it?",
                    "options": ["yet", "already", "still"],
                    "answer": "yet",
                    "explanation": "'yet' cuối câu hỏi phủ định."
                }
            ]
        }
    },
    "Unit 2: Vocabulary - Thinking and learning": {
        "type": "Vocabulary",
        "level": "C1/C2",
        "description": "Từ vựng chủ đề Tư duy & Học tập, Phrasal Verbs, Idioms, Collocations và Word Formation.",
        "theory": {
            "Topic Vocabulary": [
                ("assess /əˈses/ (v) [evaluate or estimate the nature, ability, or quality of]", "Đánh giá bản chất, giá trị hoặc khả năng của cái gì."),
                ("baffle /ˈbæf.əl/ (v) [totally bewilder or perplex]", "Gây bối rối, hoàn toàn không thể hiểu được."),
                ("cynical /ˈsɪn.ɪ.kəl/ (adj) [believing that people are motivated by self-interest]", "Hoài nghi về lòng tốt hoặc sự chân thành của con người."),
                ("dubious /ˈdʒuː.bi.əs/ (adj) [hesitating or doubting]", "Mơ hồ, đáng ngờ, nghi ngại."),
                ("ingenious /ɪnˈdʒiː.ni.əs/ (adj) [clever, original, and inventive]", "Khéo léo, thông minh, phát minh độc đáo."),
                ("plausible /ˈplɔː.zə.bəl/ (adj) [seeming reasonable or probable]", "Hợp lý, có vẻ đúng, đáng tin cậy.")
            ],
            "Phrasal Verbs": [
                ("brush up (on) /brʌʃ ʌp ɒn/", "Rèn luyện, ôn lại để cải thiện kỹ năng/kiến thức."),
                ("come around (to) /kʌm əˈraʊnd tuː/", "Thay đổi ý kiến/quan điểm vì bị thuyết phục."),
                ("come up with /kʌm ʌp wɪð/", "Nghĩ ra một ý tưởng, kế hoạch."),
                ("face up to /feɪs ʌp tuː/", "Chấp nhận và đối mặt với thực tế khó khăn."),
                ("mull over /mʌl ˈəʊ.vər/", "Suy ngẫm, cân nhắc kỹ lưỡng trong một khoảng thời gian."),
                ("piece together /piːs təˈɡeð.ər/", "Xâu chuỗi các manh mối/thông tin để hiểu sự thật.")
            ],
            "Idioms": [
                ("go to your head /ɡəʊ tuː jɔː hed/", "Thành công khiến ai đó trở nên kiêu ngạo."),
                ("have your wits about you /hæv jɔː wɪts əˈbaʊt juː/", "Tỉnh táo, suy nghĩ nhanh để đưa ra quyết định đúng."),
                ("not see the wood for the trees /nɒt siː ðə wʊd fɔː ðə triːz/", "Quá chú ý chi tiết nhỏ mà không thấy bức tranh toàn cảnh."),
                ("quick / slow on the uptake /kwɪk / sləʊ ɒn ðə ˈʌp.teɪk/", "Nảy số nhanh / tiếp thu chậm."),
                ("ring a bell /rɪŋ ə bel/", "Nghe quen quen nhưng không nhớ rõ chi tiết.")
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
        "quiz_sections": {
            "Exercise A: Topic Vocabulary & Phrasal Verbs": [
                {
                    "question": "I spent all evening _____ over the decision before finally deciding to accept the job.",
                    "options": ["mulling", "brushing", "puzzling", "piecing"],
                    "answer": "mulling",
                    "explanation": "'mull over' nghĩa là suy ngẫm, cân nhắc kỹ lưỡng một quyết định."
                },
                {
                    "question": "The proposal sounds completely _____ and well-thought-out.",
                    "options": ["plausible", "dubious", "baffled", "naive"],
                    "answer": "plausible",
                    "explanation": "'plausible' có nghĩa là hợp lý, khả thi, đáng tin."
                }
            ],
            "Exercise B: Idioms & Collocations": [
                {
                    "question": "Don't let success go to your _____; stay humble and keep working hard.",
                    "options": ["head", "mind", "brain", "wit"],
                    "answer": "head",
                    "explanation": "Idiom 'go to your head' nghĩa là bị sự thành công làm cho kiêu ngạo."
                }
            ]
        }
    }
}

FLASHCARDS = [
    {"word": "assess", "pos": "verb", "ipa": "/əˈses/", "def": "evaluate or estimate the nature, ability, or quality of", "vi": "đánh giá, định giá", "ex": "It's difficult to assess the impact of the new policy."},
    {"word": "baffle", "pos": "verb", "ipa": "/ˈbæf.əl/", "def": "totally bewilder, confuse or perplex", "vi": "gây bối rối, làm kinh ngạc", "ex": "His sudden decision to quit baffled everyone in the office."},
    {"word": "brush up (on)", "pos": "phrasal verb", "ipa": "/brʌʃ ʌp ɒn/", "def": "practise and improve your skills or knowledge of something", "vi": "ôn luyện, trau dồi lại", "ex": "I need to brush up on my French before visiting Paris."},
    {"word": "mull over", "pos": "phrasal verb", "ipa": "/mʌl ˈəʊ.vər/", "def": "think about something carefully for a period of time", "vi": "suy ngẫm, cân nhắc kỹ lưỡng", "ex": "I need a few days to mull over the job offer."},
    {"word": "go to your head", "pos": "idiom", "ipa": "/ɡəʊ tuː jɔː hed/", "def": "cause someone to become arrogant or overconfident", "vi": "làm cho ai đó mắc bệnh ngôi sao / kiêu ngạo", "ex": "Don't let that promotion go to your head!"},
    {"word": "not see the wood for the trees", "pos": "idiom", "ipa": "/nɒt siː ðə wʊd fɔː ðə triːz/", "def": "be unable to understand what is important because you are paying too much attention to details", "vi": "không thấy bức tranh toàn cảnh do quá chú ý tiểu tiết", "ex": "He was so focused on formatting that he couldn't see the wood for the trees."}
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
    4. **Ghi nhớ lâu với Flashcards**: Thẻ từ vựng thông minh hỗ trợ tra cứu nghĩa, từ loại, IPA và ví dụ thực tế.
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
    st.markdown('<div class="main-header">✍️ Bài tập Tương tác & Chấm điểm tự động</div>', unsafe_allow_html=True)
    selected_quiz_unit = st.selectbox("Chọn Unit bài tập:", list(UNITS_DATA.keys()), key="quiz_unit_select")
    
    unit_obj = UNITS_DATA[selected_quiz_unit]
    quiz_sections = unit_obj["quiz_sections"]
    
    st.info("💡 **Hướng dẫn:** Chọn phần bài tập dưới đây, chọn đáp án phù hợp cho mỗi câu hỏi. Hệ thống **không chọn sẵn** đáp án nào. Sau khi hoàn thành, nhấn nút **Kiểm tra Đáp án** để xem điểm số và giải thích chi tiết.")
    
    section_names = list(quiz_sections.keys())
    tabs = st.tabs(section_names)
    
    for tab_idx, sec_name in enumerate(section_names):
        with tabs[tab_idx]:
            questions = quiz_sections[sec_name]
            st.subheader(f"📝 {sec_name}")
            
            user_answers = {}
            with st.form(f"form_{selected_quiz_unit}_{tab_idx}"):
                for q_idx, q in enumerate(questions):
                    st.markdown(f"**Câu {q_idx + 1}:** {q['question']}")
                    user_answers[q_idx] = st.radio(
                        f"Chọn đáp án cho câu {q_idx + 1}:",
                        q['options'],
                        key=f"q_{selected_quiz_unit}_{tab_idx}_{q_idx}",
                        index=None
                    )
                    st.markdown("---")
                    
                submitted = st.form_submit_button(f"🚀 Submit Exercise / Kiểm tra {sec_name}")
                
            if submitted:
                score = 0
                unanswered = False
                st.markdown("### 📊 Kết quả Bài làm:")
                for q_idx, q in enumerate(questions):
                    ans = user_answers[q_idx]
                    if ans is None:
                        unanswered = True
                        st.warning(f"⚠️ **Câu {q_idx + 1}: Bạn chưa chọn đáp án!** (Đáp án đúng: **{q['answer']}**)")
                    elif ans == q['answer']:
                        score += 1
                        st.success(f"✅ **Câu {q_idx + 1}: Chính xác!** ({q['answer']})")
                    else:
                        st.error(f"❌ **Câu {q_idx + 1}: Chưa đúng.** Đáp án đúng là **{q['answer']}** (Bạn đã chọn: {ans})")
                    st.caption(f"💡 *Giải thích:* {q['explanation']}")
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                total_q = len(questions)
                final_pct = int((score / total_q) * 100)
                st.metric("Điểm phần bài tập này", f"{final_pct}%", f"{score}/{total_q} câu đúng")
                
                if selected_quiz_unit not in st.session_state.completed_units:
                    st.session_state.completed_units.append(selected_quiz_unit)

# 4. FLASHCARDS PAGE
elif menu == "🎴 Thẻ từ vựng (Flashcards)":
    st.markdown('<div class="main-header">🎴 Flashcards Từ vựng & Cụm từ C1/C2</div>', unsafe_allow_html=True)
    selected_fc_unit = st.selectbox("Chọn Unit từ vựng:", list(UNITS_DATA.keys()), key="fc_unit_select")
    
    if UNITS_DATA[selected_fc_unit]["type"] == "Grammar":
        st.warning("ℹ️ Thẻ ghi nhớ (Flashcards) chỉ dành riêng cho các **Unit Từ vựng (Vocabulary)**. Các Unit Ngữ pháp tập trung vào phần Tra cứu Lý thuyết và Bài tập Tương tác.")
    else:
        st.caption("Lật thẻ để học từ vựng, phrasal verbs và idioms trọng tâm.")
        
        total_fc = len(FLASHCARDS)
        curr_idx = st.session_state.flashcard_idx % total_fc
        card = FLASHCARDS[curr_idx]
        
        col_fc, _ = st.columns([2, 1])
        with col_fc:
            st.markdown(f"""
            <div style="background-color: #EFF6FF; border: 2px solid #3B82F6; border-radius: 12px; padding: 2rem; text-align: center; min-height: 240px;">
                <span style="background-color: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 10px; font-weight: 600; font-size: 0.85rem;">{card['pos'].upper()}</span>
                <h2 style="color: #1E3A8A; margin-top: 10px; margin-bottom: 2px;">{card['word']}</h2>
                <p style="color: #6B7280; font-family: monospace; font-size: 1.1rem; margin-top: 0;">{card.get('ipa', '')}</p>
                <hr style="border: 0.5px solid #BFDBFE;">
                <p style="font-size: 1.05rem; color: #1F2937;"><b>Định nghĩa (English):</b> {card['def']}</p>
                <p style="font-size: 1.05rem; color: #059669;"><b>Nghĩa tiếng Việt:</b> {card['vi']}</p>
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

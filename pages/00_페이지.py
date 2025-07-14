import streamlit as st

st.set_page_config(page_title="MBTI 여자 아이돌 추천기", page_icon="🎀")

st.title("🎀 MBTI 기반 여자 아이돌 추천기")
st.write("MBTI 유형을 선택하면, 성격에 어울리는 K-POP 여자 아이돌 3명을 추천해드릴게요!")

# MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI 설명과 아이돌 추천
mbti_idols = {
    "INTJ": {
        "desc": "전략적이고 독립적인 분석가형",
        "idols": ["서리", "문별 (마마무)", "태연 (소녀시대)"]
    },
    "INTP": {
        "desc": "창의적이고 논리적인 아이디어 뱅크",
        "idols": ["아이유", "혜인 (뉴진스)", "미연 ((여자)아이들)"]
    },
    "ENTJ": {
        "desc": "카리스마 있고 리더십 강한 지휘관형",
        "idols": ["이채연", "솔라 (마마무)", "슬기 (레드벨벳)"]
    },
    "ENTP": {
        "desc": "열정 넘치고 창의적인 발명가형",
        "idols": ["제니 (블랙핑크)", "하니 (EXID)", "유나 (ITZY)"]
    },
    "INFJ": {
        "desc": "신념 있고 조용한 이상주의자형",
        "idols": ["지수 (블랙핑크)", "수지", "미연 ((여자)아이들)"]
    },
    "INFP": {
        "desc": "감성적이고 자기 세계가 뚜렷한 중재자형",
        "idols": ["아이유", "청하", "아린 (오마이걸)"]
    },
    "ENFJ": {
        "desc": "이끄는 힘이 있는 따뜻한 리더형",
        "idols": ["문별 (마마무)", "웬디 (레드벨벳)", "이채연"]
    },
    "ENFP": {
        "desc": "열정적이고 자유로운 활동가형",
        "idols": ["유나 (ITZY)", "하니 (EXID)", "윤 (STAYC)"]
    },
    "ISTJ": {
        "desc": "성실하고 책임감 강한 현실주의자형",
        "idols": ["다현 (트와이스)", "은하 (여자친구)", "시은 (STAYC)"]
    },
    "ISFJ": {
        "desc": "따뜻하고 헌신적인 조력자형",
        "idols": ["조이 (레드벨벳)", "지수 (블랙핑크)", "소원 (여자친구)"]
    },
    "ESTJ": {
        "desc": "체계적이고 주도적인 관리자형",
        "idols": ["은비", "솔라 (마마무)", "슬기 (레드벨벳)"]
    },
    "ESFJ": {
        "desc": "사교적이고 배려심 많은 외교관형",
        "idols": ["나연 (트와이스)", "제이 (STAYC)", "지호 (오마이걸)"]
    },
    "ISTP": {
        "desc": "조용하고 실용적인 장인형",
        "idols": ["이채영 (아이즈원)", "비비", "윤진 (르세라핌)"]
    },
    "ISFP": {
        "desc": "예술적이고 감성적인 예술가형",
        "idols": ["청하", "아린 (오마이걸)", "태연 (소녀시대)"]
    },
    "ESTP": {
        "desc": "에너지 넘치고 도전적인 사업가형",
        "idols": ["리사 (블랙핑크)", "쯔위 (트와이스)", "신비 (비비지)"]
    },
    "ESFP": {
        "desc": "활발하고 인기 많은 연예인형",
        "idols": ["유아 (오마이걸)", "츄 (이달소)", "산다라박"]
    }
}

# 사용자 입력
selected = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_list)

# 결과 출력
if selected:
    st.subheader(f"💬 {selected} 성격 요약")
    st.write(mbti_idols[selected]["desc"])

    st.subheader("🌟 어울리는 여자 아이돌 3명")
    for idol in mbti_idols[selected]["idols"]:
        st.markdown(f"- {idol}")

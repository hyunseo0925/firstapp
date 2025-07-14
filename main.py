import streamlit as st

st.title("💼 MBTI 기반 직업 추천기")
st.write("당신의 MBTI 유형을 선택하면, 어울리는 직업을 추천해드려요!")

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI별 직업 추천 데이터 (예시)
mbti_jobs = {
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "연구 개발자"],
    "INTP": ["이론 물리학자", "소프트웨어 엔지니어", "UX 디자이너"],
    "ENTJ": ["CEO", "경영 컨설턴트", "벤처 창업가"],
    "ENTP": ["스타트업 기획자", "마케팅 전문가", "크리에이티브 디렉터"],
    "INFJ": ["심리상담가", "작가", "비영리단체 활동가"],
    "INFP": ["예술가", "시나리오 작가", "인권 변호사"],
    "ENFJ": ["교사", "리더십 코치", "홍보 담당자"],
    "ENFP": ["브랜드 기획자", "유튜버", "사회 운동가"],
    "ISTJ": ["회계사", "법률 전문가", "공무원"],
    "ISFJ": ["간호사", "초등 교사", "도서관 사서"],
    "ESTJ": ["경영 관리자", "군 장교", "현장 감독관"],
    "ESFJ": ["이벤트 플래너", "HR 담당자", "상담 교사"],
    "ISTP": ["기계공", "보안 전문가", "파일럿"],
    "ISFP": ["플로리스트", "사진작가", "제품 디자이너"],
    "ESTP": ["세일즈 전문가", "스포츠 코치", "기업 컨설턴트"],
    "ESFP": ["MC/사회자", "무대 배우", "패션 스타일리스트"]
}

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# 추천 출력
if selected_mbti:
    st.subheader(f"✅ {selected_mbti}에게 어울리는 직업 3가지:")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

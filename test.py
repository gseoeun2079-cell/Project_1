import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="시트1", ttl="10m" )
print(df)

def user_menu_selected(a):
    pass
    
if 'page' not in st.session_state:
    st.session_state.page = '첫화면'

if st.session_state.page == '첫화면':
    st.title("배달 메뉴 추천")
    st.subheader("사용자의 기분에 맞게 배달 메뉴를 추천해드립니다.")
    if st.button("시작하기"):
        st.session_state.page = '선택화면'
        st.rerun()


elif st.session_state.page == '선택화면':
    st.header("질문에 답해주세요")
    selected_option1 = st.selectbox("한식과 중식, 양식 중 골라주세요",("한식","중식","양식","상관없음"))
    selected_option2 = st.selectbox("국물이 있는 음식을 원하시나요?",("국물O","국물X","상관없음"))
    selected_option3 = st.selectbox("매운 음식을 원하시나요?",("매운맛O","매운맛X","상관없음"))
    selected_option4 = st.selectbox("시원한 음식을 원하시나요, 따뜻한 음식을 원하시나요?",("시원한 음식","따뜻한 음식","상관없음"))
    selected_option5 = st.selectbox("밥 종류의 음식을 원하시나요, 면 종류의 음식을 원하시나요?",("밥 종류의 음식","면 종류의 음식","상관없음"))
    selected_option6 = st.selectbox("기름진 음식을 원하시나요, 깔끔한 음식을 원하시나요?",("기름진 음식","깔끔한 음식","상관없음"))
    a = {'selected_option1':selected_option1,'selected_option2':selected_option2,'selected_option3':selected_option3,'selected_option4':selected_option4,'selected_option5':selected_option5,'selected_option6':selected_option6}
    if st.button("선택완료"):
        st.session_state.page = '결과화면'
        user_menu_selected(a)
        st.rerun()
        
elif st.session_state.page == '결과화면':
    st.header("오늘의 추천메뉴는?")
    if st.button("처음으로 돌아가기"):
        st.session_state.page = '첫화면'
        st.rerun()

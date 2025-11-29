import streamlit as st
import pandas as pd
from io import BytesIO
import datetime

st.title("봉사활동 출석부 생성기")

# --- 사용자 입력 ---
st.subheader("파일명 정보 입력")
org_name = st.text_input("기관명 (예: 행복복지관)", "")
period = st.text_input("기간 (예: 2025_1학기)", "")
today = datetime.date.today().strftime("%Y%m%d")

# 파일명 자동 생성
filename = f"{period}_{org_name}_봉사활동출석부_{today}.xlsx".replace(" ", "_")

st.write("📄 **자동 생성된 파일명:**")
st.code(filename)

# --- 기본 출석부 구성 ---
df = pd.DataFrame({
    "번호": range(1, 21),
    "이름": ["" for _ in range(20)],
    "날짜": ["" for _ in range(20)],
    "활동 내용": ["" for _ in range(20)],
    "출석(○/✕)": ["" for _ in range(20)],
    "시작시간": ["" for _ in range(20)],
    "종료시간": ["" for _ in range(20)],
    "봉사시간(시간)": ["" for _ in range(20)],
    "비고": ["" for _ in range(20)],
})

# 엑셀 파일 생성 함수
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='출석부')
    return output.getvalue()

excel_data = to_excel(df)

# 다운로드 버튼
st.download_button(
    label="📥 출석부 다운로드",
    data=excel_data,
    file_name=filename,
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

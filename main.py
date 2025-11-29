import streamlit as st
import math

st.title("🔢 멀티 기능 계산기")

# 입력값
num1 = st.number_input("첫 번째 숫자 입력", value=0.0)
num2 = st.number_input("두 번째 숫자 입력", value=0.0)

# 연산 선택
operation = st.selectbox(
    "연산 선택",
    ["덧셈 (+)", "뺄셈 (-)", "곱셈 (*)", "나눗셈 (/)", 
     "모듈러 (%)", "지수 (x^y)", "로그 (log_x(y))"]
)

# 계산 버튼
if st.button("계산하기"):
    try:
        if operation == "덧셈 (+)":
            result = num1 + num2

        elif operation == "뺄셈 (-)":
            result = num1 - num2

        elif operation == "곱셈 (*)":
            result = num1 * num2

        elif operation == "나눗셈 (/)":
            if num2 == 0:
                result = "0으로 나눌 수 없습니다."
            else:
                result = num1 / num2

        elif operation == "모듈러 (%)":
            if num2 == 0:
                result = "0으로 나눌 수 없습니다."
            else:
                result = num1 % num2

        elif operation == "지수 (x^y)":
            result = num1 ** num2

        elif operation == "로그 (log_x(y))":
            if num1 <= 0 or num1 == 1 or num2 <= 0:
                result = "로그의 밑은 0보다 크고 1이 아니어야 하며, 진수는 0보다 커야 합니다."
            else:
                result = math.log(num2, num1)

        st.success(f"결과: {result}")

    except Exception as e:
        st.error(f"오류 발생: {e}")

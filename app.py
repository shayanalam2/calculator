import streamlit as st

st.title("shayan")
num1=st.number_input("enter first number")
num2=st.number_input("enter your second number")

operation= st.selectboxint("choose operation",["+","-","*","/"])
if st.button("calculate"):
 if operation =="+":
    st.write(num1+num2)
elif operation == "-":
    st.write(num1-num2)
elif operation == "*":
    st.write("*")
elif operation=="/":
    st.write(num1/num2)
else:
    st.write(operation)

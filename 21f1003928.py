pip install streamlit
import streamlit as st
a=st.number_input(int(input("Enter the first number")))
b=st.number_input(int(input("Enter the second number")))
c=st.number_input(int(input("Enter the third number")))

l=a
if(a>b and a>c):
  l=a
elif(b>a and b>c):
  l=b
elif(c>a and c>b):
  l=c
else:
  l=a

print("Largest number is", l)

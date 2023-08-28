import streamlit as st

def find_highest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Highest Number Finder")

    st.write("Enter three numbers:")
    number1 = st.number_input("Number 1")
    number2 = st.number_input("Number 2")
    number3 = st.number_input("Number 3")

    if st.button("Find Highest"):
        highest = find_highest_number(number1, number2, number3)
        st.write(f"The highest number is: {highest}")

if __name__ == "__main__":
    main()

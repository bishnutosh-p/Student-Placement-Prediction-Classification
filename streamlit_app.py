import streamlit as st

def main():
    st.title("Streamlit App with 10 Inputs and 1 Output")

    # Create 10 input fields
    input_values = [st.number_input(f"Input {i+1}", value=0.0) for i in range(10)]

    # Calculate the sum of the input values
    output_value = sum(input_values)

    # Display the output
    st.write(f"Output: {output_value}")

if __name__ == "__main__":
    main()

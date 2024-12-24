import streamlit as st
import statistics

# Function 1: Student Report Generator
def generate_student_report(roll_number):
    roll_number_str = str(roll_number)
    batch_year = roll_number_str[:2]  # First two digits: Batch Year
    dept_code = roll_number_str[2:4]  # Next two digits: Department Code
    student_roll = roll_number_str[4:]  # Last three digits: Student Roll

    batch_year_description = f"Batch Year: 20{batch_year}"  # Assuming batch year starts from 20XX
    dept_code_description = f"Department Code: {dept_code}"
    student_roll_description = f"Student Roll Number: {student_roll}"

    report = f"""
    Student Report
    ---------------
    Roll Number: {roll_number}
    {batch_year_description}
    {dept_code_description}
    {student_roll_description}
    """
    return report

# Function 2: Mean and Median Calculation
def calculate_mean_median(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    return mean, median

# Function 3: Custom Abbreviation Generator
def custom_abbreviation(full_name):
    words = full_name.split()
    abbreviation = []
    skip_words = ["for", "and"]

    for word in words:
        if word.lower() in skip_words:
            continue
        elif word.lower() == "of":
            abbreviation.append("o")
        else:
            abbreviation.append(word[0].upper())

    return ''.join(abbreviation)

# Streamlit app layout
st.title("Student Report, Mean & Median, Abbreviation Generator")

# Student Report Section
st.header("Student Report Generator")
roll_number_input = st.text_input("Enter Student Roll Number (e.g., 1901027):")
if roll_number_input:
    report = generate_student_report(roll_number_input)
    st.subheader("Generated Report:")
    st.write(report)

# Mean and Median Calculation Section
st.header("Mean and Median Calculator")
numbers_input = st.text_input("Enter multiple numbers separated by commas:")
if numbers_input:
    numbers = [float(num.strip()) for num in numbers_input.split(",")]
    mean, median = calculate_mean_median(numbers)
    st.subheader("Results:")
    st.write(f"Mean: {mean}")
    st.write(f"Median: {median}")

# Abbreviation Generator Section
st.header("Abbreviation Generator")
full_name_input = st.text_input("Enter Full Name:")
if full_name_input:
    abbreviation = custom_abbreviation(full_name_input)
    st.subheader("Generated Abbreviation:")
    st.write(f"Abbreviation: {abbreviation}")

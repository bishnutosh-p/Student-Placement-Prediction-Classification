import streamlit as st

def main():
    st.title("Student Placement Predictor")

    fields = ['CGPA','Internships','Projects','Workshops/Certifications','AptitudeTestScore','SoftSkillsRating','ExtracurricularActivities'
             ,'PlacementTraining','SSC_Marks','HSC_Marks','PlacementStatus']
    
    # Create 10 input fields
    input_values = [st.number_input(f"Input {i+1}", value=0.0) for i in range(10)]
    
    # Calculate the sum of the input values
    output_value = sum(input_values)

    # Display the output
    st.write(f"Output: {output_value}")

if __name__ == "__main__":
    main()




# StudentID' has unique values : 10000
# The 'CGPA' has unique values : 27
# The 'Internships' has unique values : 3
# The 'Projects' has unique values : 4
# The 'Workshops/Certifications' has unique values : 4
# The 'AptitudeTestScore' has unique values : 31
# The 'SoftSkillsRating' has unique values : 19
# The 'ExtracurricularActivities' has unique values : 2
# The 'PlacementTraining' has unique values : 2
# The 'SSC_Marks' has unique values : 36
# The 'HSC_Marks' has unique values : 32
# The 'PlacementStatus' has unique values : 2

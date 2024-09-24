import streamlit as st
from datetime import datetime
from PIL import Image
import base64
import io

def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')
def main():
    st.title("S.A. ENGINEERING COLLEGE")
    st.header("COLLEGE ADMISSION FORM")

    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
        st.session_state.selected_course = None

    name = st.text_input("Name")
    father_name = st.text_input("Father's Name")
    mother_name = st.text_input("Mother's Name")
    dob = st.date_input("Date of Birth")
    locality = st.text_input("Locality")
    address = st.text_input("Address")
    mobile_no = st.text_input("Mobile Number", max_chars=15)
    email = st.text_input("Email")
    image_file = st.file_uploader("Profile picture", type=["jpg", "jpeg", "png"])
    school_name = st.text_input("School Name")
    percentage_10 = st.number_input("10th Percentage", min_value=0)
    year_of_10po = st.number_input("Year of 10th Passed Out", min_value=0)
    percentage_12 = st.number_input("12th Percentage", min_value=0)
    year_of_12po = st.number_input("Year of 12th Passed Out", min_value=0)
    physics_mark = st.number_input("12th Physics Mark", min_value=0)
    chemistry_mark = st.number_input("12th Chemistry Mark", min_value=0)
    maths_mark = st.number_input("12th Mathematics Mark", min_value=0)

    if st.button("Submit"):
        dob_str = dob.strftime('%Y-%m-%d')
        phy_chem = (physics_mark + chemistry_mark) / 2
        cutoff = (maths_mark + phy_chem)

        if image_file is not None:
            image = Image.open(image_file)
            image_base64 = encode_image(image)
        st.write(f"Cutoff: {cutoff}")

        if 120 <= cutoff <= 160:
            eligible_courses = [
                "Mechanical Engineering",
                "Civil Engineering",
                "ECE",
                "EEE",
                "Cyber Security",
                "VLSI"
            ]
        elif 161 <= cutoff <= 200:
            eligible_courses = [
                "Mechanical Engineering",
                "Civil Engineering",
                "ECE",
                "EEE",
                "Cyber Security",
                "Computer Science Engineering",
                "Information Technology",
                "AIDS",
                "AIML",
                "VLSI"
            ]
        else:
            st.write("Not eligible")
            return

        st.header("Courses Eligible:")
        for course in eligible_courses:
            st.write(course)

        st.session_state.submitted = True
        st.session_state.eligible_courses = eligible_courses

    if st.session_state.submitted:
        selected_course = st.selectbox("Select the course name", st.session_state.eligible_courses)
        if st.button("Register"):
            if selected_course in st.session_state.eligible_courses:
                st.success("Registered successfully")
            else:
                st.error("Invalid course for your cutoff.")

if __name__ == '__main__':
    main()

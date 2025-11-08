import streamlit as st

#-----------app title---------------
def show_password_test():
    st.title("Password Strength Checker")
    st.write("Check how strong your password is and get an instant feedback!")
    st.markdown("---")

    #-----------input section-----------
    password = st.text_input(
        "Enter your password here: ",
        type="password",
        placeholder="type or paste your password here..."
    )

    #----------function to check password------------
    def check_password_strength(password):
        upperchars, lowerchars, digits, specialchars = 0,0,0,0
        length = len(password)

        if " " in password:
            return "❌ **Password must not contain any spaces.**", "weak"

        if len(password)<12:
            return "❌ **Password must be atleast 12 characters long.**", "weak"
        
        for ch in password:
            if ch.isupper():
                upperchars+=1
            elif ch.islower():
                lowerchars+=1
            elif ch.isdigit():
                digits+=1
            else:
                specialchars+=1
        
        missing_criteria = []
        if upperchars == 0:
            missing_criteria.append("1 uppercase letter")
        if lowerchars == 0:
            missing_criteria.append("1 lowercase letter")
        if digits == 0:
            missing_criteria.append("1 digit")
        if specialchars == 0:
            missing_criteria.append("1 special character")
        
        if missing_criteria:
            return f"⚠ Password missing: {','.join(missing_criteria)}", "weak"
        
        if length>=16:
            return "Password strength is: **Strong** 💪", "Strong"
        else:
            return "Password strength is: **Medium**🙂 ", "Medium"
        
    #-----------button and output------------
    if not password:
        st.warning("Please enter a password to check.")
    else:
        message, status = check_password_strength(password)

        if status == "Strong":
            st.success(message)
        elif status == "Medium":
            st.info(message)
        else:
            st.error(message)

    #-------------footer--------------
    st.markdown("---")
    st.caption("🔒Tip: Use atleast 16 characters with uppercase, lowercase, digits, and special symbols.")

if __name__ == "__main__":
    show_password_test()
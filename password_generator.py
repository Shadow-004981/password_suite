import streamlit as st
import random
import string

#-------------App title---------------
def show_password_generator():
    st.title("🔐 Smart Password Generator")
    st.write("Easily create secure passwords with customizable options!")
    st.markdown("---")

    #--------------password mode selection-----------
    choice = st.radio(
        "Choose password mode: ",
        ["Standard(12 characters)", "Custom"],
        horizontal=True
    )

    #----------------standard mode-----------------
    if choice.startswith("Standard"):
        st.subheader("Standard Password Mode")
        st.write("This will generate a 12-characters secure password with letters, numbers, and special symbols.")

        generate_standard = st.button("Generate Standard Password")
        regenerate_standard = st.button("Regenerate Standard Password")

        if generate_standard or regenerate_standard:
            length = 12
            alphabets = string.ascii_letters
            digits = string.digits
            specials = string.punctuation

            password_chars = [
                random.choice(string.ascii_uppercase),
                random.choice(digits),
                random.choice(specials)
            ]

            remaining = length - len(password_chars)
            password_chars+=random.choices(alphabets + digits + specials, k=remaining)
            random.shuffle(password_chars)
            password = ''.join(password_chars)

            st.success("✔ Your password has been generated!")
            st.code(password, language="")
        

    #---------------custom mode-------------------
    else:
        st.subheader("Custom Password mode")
        st.write("Choose your own password structure!")
        
        total_length = st.number_input("Total password length: ", value=16, step=1)
        uppercase_count = st.number_input("Number uppercase letters: ", value=3, step=1)
        lowercase_count = st.number_input("Number of lower case letters: ", value=3, step=1)
        digits_count = st.number_input("Number of digits: ", value=3, step=1)
        specials_count = st.number_input("Number of special symbols: ", value=3, step=1)

        generate_custom = st.button("Generate Custom Password")
        regenerate_custom = st.button("Regenerate Custom Password")

        if generate_custom or regenerate_custom:
            if(uppercase_count + lowercase_count + digits_count + specials_count) != total_length:
                st.error("❌ sum of all parts must be equal to total length!")
            else:
                password_chars = []
                password_chars += random.choices(string.ascii_uppercase, k=int(uppercase_count))
                password_chars += random.choices(string.ascii_lowercase, k=int(lowercase_count))
                password_chars += random.choices(string.digits, k=int(digits_count))
                password_chars += random.choices(string.punctuation, k=int(specials_count))

                random.shuffle(password_chars)
                password = ''.join(password_chars)
                st.success("✔ Your password has been generated!")
                st.code(password, language="")
                
                
    #--------------footer---------------
    st.markdown("---")
    st.caption("Tip: Use standard mode for a quick strong password, or custom mode for full control!")

if __name__ == "__main__":
    show_password_generator()
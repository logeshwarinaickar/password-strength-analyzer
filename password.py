import streamlit as st 
st.markdown("""
<style>
        .stApp{
            background-color:#DCEBFF;
            }
</style>                        
""",unsafe_allow_html= True)
st.set_page_config(page_title="SecurePass",layout="wide")
st.markdown("<h1 style = 'text-align: Center; color:#1E293B;'>Password Analyzer </h1> ",unsafe_allow_html=True)

password = st.text_input(label= "Enter Password: ", type="password", placeholder="type password")

col1 , col2 = st.columns(2)
with col1:
     with st.container(border=True):
        st.subheader("Password Details")
        length = len(password)
        num = 0 
        for character in password:
            if character.isdigit():
                num += 1

        upp = 0 
        for character in password:
            if character.isupper():
                upp+= 1

        sc = "!@#$%&_"
        scc = 0
        for character in password:
            if character in sc:
                scc+= 1

        st.metric("Length : ", length)
        st.metric("Numbers: ", num)
        st.metric("Uppercase Letters : ", upp)
        st.metric("Special Characters : ", scc)

        st.markdown("---")
        st.subheader("Password Generator")  
        Lenn = st.slider(label="Password Length",min_value= 5 , max_value= 15,value=10)
        import random
        import string
        if st.button("Generate Secure Password"):
            char = []
            U = string.ascii_uppercase
            N = string.digits
            S = sc
            L = string.ascii_lowercase
            upper = random.choice(U)
            numbs = random.choice(N)
            special = random.choice(S)
            char.append(upper)
            char.append(numbs)
            char.append(special)

            new_lenn = Lenn - len(char)

            chars = L+U+N+S 
            for i in range (new_lenn):
                char.append(random.choice(chars)) 
                
            
            random.shuffle(char)
            final_password = "".join(char)
            while final_password[0] in S:
                random.shuffle(char)
                final_password = "".join(char)
                
            st.code(final_password)
            st.success("Password Successfully Generated!!")

with col2:
     with st.container(border=True):
        #results 
        st.subheader("Strength Dashboard")
        if password!= "":
            weak_score = 0 
            medium_score = 0
            strong_score = 0

            if length <= 4:
                weak_score += 25
            elif length <= 7:
                medium_score += 25
            elif length >= 8:
                strong_score += 25 

            if num == 0:
                weak_score += 25
            elif num == 1:
                medium_score += 25
            elif num >= 2:
                strong_score += 25 
            
            if upp == 0:
                weak_score += 25
            elif upp == 1:
                medium_score += 25
            elif upp >= 2:
                strong_score += 25 
            
            if scc == 0:
                weak_score += 25
            elif scc >= 1:
                strong_score += 25 
            
            rc1 , rc2 = st.columns([1,4])
            with rc1:
                st.markdown("##### Weak")
            with rc2:
                st.progress(weak_score)

            rc12 , rc22 = st.columns([1,4])
            with rc12:
                st.markdown("##### Moderate")
            with rc22:
                st.progress(medium_score)
            
            rc13 , rc23 = st.columns([1,4])
            with rc13:
                st.markdown("##### Strong")
            with rc23:
                st.progress(strong_score)
                    
        else:
            st.info("Enter password to begin analysis")
        st.markdown("---")
        st.subheader("Suggestions")
        if password!= "":
            if length < 8:
                st.info("Increase password length to at least 8 characters")

            if num == 0:
                st.info("Add numbers for better security")

            if upp== 0:
                st.info("Include uppercase letters")

            if scc == 0:
                st.info("Use special characters like @ # $ %")
            
            if strong_score == 100:
                st.success("Excellent! Your password is strong and secure.")







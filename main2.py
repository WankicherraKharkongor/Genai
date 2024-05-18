import streamlit as st
import langchain_helper

st.title("Football Club Players")
team_name = st.sidebar.selectbox("Pick a football club team", ("Manchester City", "Real Madrid", "FC Barcelona", "Liverpool", "Manchester United"))

if team_name:
    response = langchain_helper.generate_player_names(team_name)
    st.header(f"Players for {team_name}")
    player_names = response['player_names'].strip().split(",")
    st.write("**Players**")
    for player in player_names:
        st.write(player)




# [hsdfhihdhfiusdhfuihdsuifhsduifhsdiufhisudfh]
# [d,df,d,f,d,f,d,f,d,fd,f,df,r]

# real
#
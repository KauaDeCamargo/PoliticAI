import streamlit as st
from uuid import uuid4
from src.agent import agent

st.set_page_config(page_title='PoliticAI')
st.title('PoliticAI')

st.write('Inicie seu chat abaixo')

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'thread_id' not in st.session_state:
    st.session_state.thread_id = str(uuid4())

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


if prompt := st.chat_input('O que você deseja saber?'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.spinner('Agente pensando...'):
        config = {
            'configurable': {
                'thread_id': st.session_state.thread_id
            }
        }
        result = agent.invoke(
            {
                'messages': [
                    {'role': 'user', 'content': prompt}
                ]
            },
            config=config
        )
        response = result['messages'][-1].content
    st.session_state.messages.append({'role': 'assistant', 'content': response})
    with st.chat_message('assistant'):
        st.markdown(response)
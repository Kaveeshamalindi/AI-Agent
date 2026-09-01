import streamlit as st

from agent import ask_agent


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Agent",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🤖 AI Research Agent")

st.write(
    "Ask questions, search the web, check weather, "
    "or count words."
)


# -----------------------------
# Chat History
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display Previous Messages
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -----------------------------
# Chat Input
# -----------------------------

if prompt := st.chat_input("Ask me anything..."):

    # Display user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = ask_agent(prompt)

                st.markdown(response)

            except Exception as e:

                response = f"❌ Error: {str(e)}"

                st.error(response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
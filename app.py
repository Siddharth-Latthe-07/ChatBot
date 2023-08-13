import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "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"


class PhysicsChatbot:
    def get_response(self, user_input):
        prompt = f"You are a smart Physics chatbot that can answer Class 11 Physics questions.\nUser: {user_input}\nPhysics Buddy:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()


chatbot = PhysicsChatbot()


def main():
    st.title("Physics Chatbot")

    user_input = st.text_input("Ask a question:")

    if st.button("Ask"):
        if user_input:
            response = chatbot.get_response(user_input)
            st.text("Physics Buddy:")
            st.write(response)


if __name__ == "__main__":
    main()

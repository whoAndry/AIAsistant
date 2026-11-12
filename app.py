import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="PyAssistant",
    page_icon="🤖"
)

# Judul aplikasi
st.title("🤖 PyAssistant")

st.write("Halo! Saya asisten AI sederhana.")

# Menyimpan percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan riwayat percakapan
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input pertanyaan
prompt = st.chat_input("Tanyakan sesuatu...")

if prompt:
    # Menampilkan pesan pengguna
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Respons sementara AI
    response = "Halo! Saya PyAssistant. Saya sedang belajar menjawab pertanyaan."

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)
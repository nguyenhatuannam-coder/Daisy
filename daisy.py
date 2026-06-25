import streamlit as st

st.set_page_config(
    page_title="DAISY Team",
    page_icon="🌼",
    layout="wide"
)

members = {
    "Huỳnh Chí Thanh": {
        "birth": "2010",
        "hobby": "Xem Hiha trên YouTube",
        "personality": "Năng động",
        "image": "C:/Users/Tuan Nam/OneDrive/Máy tính/Daisy/Chi Thanh.jpg"
    },

    "Đỗ Thu Thủy": {
        "birth": "2012",
        "hobby": "Bơi lội",
        "personality": "Hoạt bát, năng động",
        "image": "C:/Users/Tuan Nam/OneDrive/Máy tính/Daisy/Thu Thuy.jpg"
    },

    "Đỗ Minh Châu": {
        "birth": "2012",
        "hobby": "Chơi Rubik",
        "personality": "Hòa đồng, thân thiện",
        "image": "C:/Users/Tuan Nam/OneDrive/Máy tính/Daisy/Minh Chau.jpg"
    },

    "Nguyễn Ngọc Minh Khanh": {
        "birth": "2012",
        "hobby": "Vẽ tranh",
        "personality": "Hoạt bát, thân thiện",
        "image": "C:/Users/Tuan Nam/OneDrive/Máy tính/Daisy/Minh Khanh.jpg"
    },

    "Nguyễn Vũ Xuân Thành": {
        "birth": "2012",
        "hobby": "Chơi Rubik",
        "personality": "Hòa đồng, thân thiện",
        "image": "C:/Users/Tuan Nam/OneDrive/Máy tính/Daisy/Xuan Thanh.jpg"
    },

    "Trần Dương Minh Đăng": {
        "birth": "2012",
        "hobby": "Xem bóng đá",
        "personality": "Cá tính, nghịch ngợm",
        "image": "C:/Users/Tuan Nam/OneDrive/Máy tính/Daisy/Minh Dang.jpg"
    },

    "Nguyễn Hà Tuấn Nam": {
        "birth": "2013",
        "hobby": "Xem bóng đá",
        "personality": "Hòa đồng",
        "image": "C:/Users/Tuan Nam/OneDrive/Máy tính/Daisy/Tuan Nam.jpg"
    }
}

# ===== INIT PAGE =====
if "page" not in st.session_state:
    st.session_state.page = "home"

# ================= HOME =================
if st.session_state.page == "home":

    st.markdown(
        "<h1 style='text-align:center; font-size:60px;'>🌼 DAISY TEAM 🌼</h1>",
        unsafe_allow_html=True
    )

    st.write("")
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        if st.button("ENTER DAISY", use_container_width=True):
            st.session_state.page = "menu"
            st.rerun()

# ================= MENU =================
elif st.session_state.page == "menu":

    st.title("🌼 DAISY MEMBERS")

    names = list(members.keys())
    cols = st.columns(3)

    for i, name in enumerate(names):
        with cols[i % 3]:
            if st.button(name, use_container_width=True):
                st.session_state.page = name
                st.rerun()

    st.write("")

    if st.button("🏠 Back Home"):
        st.session_state.page = "home"
        st.rerun()

# ================= PROFILE =================
else:

    member = members[st.session_state.page]

    st.title(st.session_state.page)

    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            st.image(member["image"], use_container_width=True)
        except:
            st.warning("Chưa thêm ảnh")

    with col2:
        st.subheader("Thông tin cá nhân")

        st.write(f"🎂 Năm sinh: {member['birth']}")
        st.write(f"🎯 Sở thích: {member['hobby']}")
        st.write(f"🧠 Tính cách: {member['personality']}")

    st.write("")

    # ===== NAV BUTTONS =====
    colA, colB = st.columns(2)

    with colA:
        if st.button("⬅ Quay lại danh sách"):
            st.session_state.page = "menu"
            st.rerun()

    with colB:
        if st.button("🏠 Về trang chủ"):
            st.session_state.page = "home"
            st.rerun()
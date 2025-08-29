import streamlit as st

st.sidebar.title("Navigation")
if "page" not in st.session_state:
    st.session_state.page = "Homepage" 

if st.sidebar.button("Homepage"):
    st.session_state.page = "Homepage"
if st.sidebar.button("Contact Us"):
    st.session_state.page = "Contact"
if st.sidebar.button("About Us"):
    st.session_state.page = "About"
if st.sidebar.button("FAQs"):
    st.session_state.page = "FAQs"

Israeli_products = [
    "a.p. moller-maersk", "airbnb", "alphabet", "amazon", "apple", "altice international",
    "alstom", "amdocs", "americana group", "bank hapoalim", "bank leumi", "bank of jerusalem",
    "beit haarchiv ltd.", "bezeq", "blackrock", "blackstone", "boeing", "booking.com",
    "booking holdings", "burger king", "caterpillar", "caterpillar inc.", "chevron", "cisco",
    "coca-cola" , "central bottling company (israel)", "crazy labs", "cyberark", "dell technologies",
    "delta galil", "domino's pizza", "egis", "elbit systems", "electra", "export investment company",
    "fiverr", "ford", "general electric", "google cloud / google", "hadar group", "hp", "ibm",
    "imperva", "intel", "kfc", "krispy kreme", "lockheed martin", "maersk", "max brenner",
    "mcdonald's", "microsoft", "moon active", "motorola solutions", "nestlé", "osem", "nvidia",
    "oracle", "palantir technologies", "papa john's", "pepsico", "sodastream", "pizza hut",
    "plarium", "puma", "qualcomm", "radware", "raytheon technologies", "sabra", "sabre", "samsung",
    "sodastream", "starbucks", "strauss group", "tabnine", "teva pharmaceutical industries",
    "varonis", "warner music group", "zara", "minecraft", "acer", "americana", "google", "m&ms"
]

if st.session_state.page == "Homepage":
    st.title("Homepage - Product Checker")

    with st.form("product_check"):
        product = st.text_input("Enter Product")
        submitted = st.form_submit_button("Check")

    if submitted and product.strip():
        if product.lower() in Israeli_products:
            st.write("❌ Sorry to inform you but that supports Israel")
        else:
            st.write("✅ Hmm... seems to not support Israel, but it's always worth checking")
    st.caption("Note : This might not be 100% Accurete so always make sure to check")

elif st.session_state.page == "Contact":
    st.title("Contact Us")
    st.write("We appreciate your comments / questions . Please write them here:")
    comment = st.text_area("")

elif st.session_state.page == "About":
    st.title("About Us")
    st.write("\n We Are a Company wich strives for a world were Palastine lives peacfully \n and the first step to do that is to Stop helping Israel so they leave Palastine alone\n and Thats where We come in to help you be aware of the companies wich do the opposite")

elif st.session_state.page == "FAQs":
    st.title("FAQs")
    st.write("Question : Is the information 100% Accuret?")
    st.write("Answer : we try to give the most accurete answers but they still could be wrong _so always check_!")



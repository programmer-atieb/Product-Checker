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
   [
    "adama",
    "ahava",
    "axa",
    "achva",
    "actavis generics",
    "activision blizzard",
    "adidas",
    "airbnb",
    "amazon",
    "apple",
    "bnp paribas",
    "bp",
    "bankinvest",
    "barak",
    "barclays",
    "booking.com",
    "burger king",
    "carrefour",
    "caterpillar",
    "check point",
    "check point software technologies",
    "chevron",
    "cisco",
    "citibank",
    "coca cola",
    "crazy labs",
    "cyberark",
    "dan hotels",
    "danske bank",
    "dell",
    "deutsche bank",
    "disney",
    "domino's pizza",
    "ea games",
    "eden springs",
    "elite",
    "expedia",
    "exxonmobil",
    "facebook",
    "fiverr",
    "ford",
    "g4s",
    "general electric",
    "general motors",
    "gilat satellite networks",
    "goldman sachs",
    "google",
    "h&m",
    "hp",
    "hsbc",
    "hyundai",
    "ibm",
    "ikea",
    "imperva",
    "indigo",
    "instagram",
    "intel",
    "jpmorgan chase",
    "johnson & johnson",
    "kfc",
    "keter",
    "l'oréal",
    "lg",
    "lumenis",
    "lyft",
    "mazda",
    "mcafee",
    "mcdonalds",
    "micron",
    "microsoft",
    "minecraft",
    "moderna",
    "monday.com",
    "moon active",
    "morgan stanley",
    "nvidia",
    "naandan",
    "nestlé",
    "netafim",
    "netflix",
    "neto malinda trading",
    "nike",
    "nykredit",
    "oracle",
    "ormat",
    "osem",
    "paypal",
    "pepsi",
    "pfizer",
    "plarium",
    "plastro",
    "playtika",
    "prigat",
    "procter & gamble",
    "puma",
    "puregym",
    "qualcomm",
    "rad data communications",
    "radware",
    "ratiopharm",
    "reebok",
    "rivulis",
    "russia",
    "sabra",
    "samsung",
    "shell",
    "siemens",
    "sodastream",
    "sony",
    "starbucks",
    "strauss group",
    "tabnine",
    "tara",
    "telrad networks",
    "tempo",
    "tempur sealy",
    "tesco bank",
    "tesla",
    "teva",
    "teva pharmaceutical industries",
    "texaco",
    "tivall",
    "tnuva",
    "toyota",
    "trip.com",
    "tripadvisor",
    "tui",
    "twitter / x",
    "uber",
    "unilever",
    "varonis",
    "volkswagen",
    "volvo",
    "watergen",
    "wendy's",
    "whatsapp",
    "wix",
    "zara",
    "zim integrated shipping services",
    "ebay"
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



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
    "ADAMA",
    "AHAVA",
    "AXA",
    "Achva",
    "Actavis Generics",
    "Activision Blizzard",
    "Adidas",
    "Airbnb",
    "Amazon",
    "Apple",
    "BNP Paribas",
    "BP",
    "Bankinvest",
    "Barak",
    "Barclays",
    "Booking.com",
    "Burger King",
    "Carrefour",
    "Caterpillar",
    "Check Point",
    "Check Point Software Technologies",
    "Chevron",
    "Cisco",
    "Citibank",
    "Coca Cola",
    "Crazy Labs",
    "CyberArk",
    "Dan Hotels",
    "Danske Bank",
    "Dell",
    "Deutsche Bank",
    "Disney",
    "Domino's Pizza",
    "EA Games",
    "Eden Springs",
    "Elite",
    "Expedia",
    "ExxonMobil",
    "Facebook",
    "Fiverr",
    "Ford",
    "G4S",
    "General Electric",
    "General Motors",
    "Gilat Satellite Networks",
    "Goldman Sachs",
    "Google",
    "H&M",
    "HP",
    "HSBC",
    "Hyundai",
    "IBM",
    "IKEA",
    "Imperva",
    "Indigo",
    "Instagram",
    "Intel",
    "JPMorgan Chase",
    "Johnson & Johnson",
    "KFC",
    "Keter",
    "L'Oréal",
    "LG",
    "Lumenis",
    "Lyft",
    "Mazda",
    "McAfee",
    "McDonalds",
    "Micron",
    "Microsoft",
    "Minecraft",
    "Moderna",
    "Monday.com",
    "Moon Active",
    "Morgan Stanley",
    "NVIDIA",
    "NaanDan",
    "Nestlé",
    "Netafim",
    "Netflix",
    "Neto Malinda Trading",
    "Nike",
    "Nykredit",
    "Oracle",
    "Ormat",
    "Osem",
    "PayPal",
    "Pepsi",
    "Pfizer",
    "Plarium",
    "Plastro",
    "Playtika",
    "Prigat",
    "Procter & Gamble",
    "Puma",
    "PureGym",
    "Qualcomm",
    "RAD Data Communications",
    "Radware",
    "Ratiopharm",
    "Reebok",
    "Rivulis",
    "Russia",
    "Sabra",
    "Sabra Hummus",
    "Samsung",
    "Shell",
    "Siemens",
    "SodaStream",
    "Sony",
    "Starbucks",
    "Strauss Group",
    "Tabnine",
    "Tara",
    "Telrad Networks",
    "Tempo",
    "Tempur Sealy",
    "Tesco Bank",
    "Tesla",
    "Teva",
    "Teva Pharmaceutical Industries",
    "Texaco",
    "Tivall",
    "Tnuva",
    "Toyota",
    "Trip.com",
    "TripAdvisor",
    "Tui",
    "Twitter / X",
    "Uber",
    "Unilever",
    "Varonis",
    "Volkswagen",
    "Volvo",
    "Volvo (AB Volvo trucks)",
    "WaterGen",
    "Wendy's",
    "WhatsApp",
    "Wix",
    "ZARA",
    "ZARA (owned by Inditex)",
    "Zim Integrated Shipping Services",
    "eBay"
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



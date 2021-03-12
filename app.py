##################################################  Importing required packages  #########################################################################################################################
import streamlit as st
import pandas as pd
from io import BytesIO
from PIL import Image

##################################################  Designing the interface  #############################################################################################################
### Changing the name to our desired name and with the QBE logo
img = Image.open('qbE1.jpg')
st.set_page_config(page_title='QBE-Workbench', page_icon=img, initial_sidebar_state='expanded', layout='wide')#  layout="wide"

### Helper function to set a background image of our choice
### For byte encoder
import base64
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

## Helper function to set a background image of our choice
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#87CEFA,white);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

logo = Image.open('QBE.jpg')
st.sidebar.image(logo, use_column_width=True)

################################################  Downloadable link  ###############################################################################################################
## Helper function to create a link for downloading the excel files to the local disk
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download Excel file</a>' # decode b'abc' => abc

########################################################### Main function  #######################################################################################################
def main():
    activities = ['streamlit', 'Alternatives of streamlit', 'XML and ReactJS', 'Demo']
    choices = st.sidebar.radio("Select", activities)
    ###############################################################################################################################################################
    if choices == 'streamlit':
        html_temp = """
                    <div style="background-color:#87CEFA ;padding:10px">
                    <h2 style="color:white;text-align:center;">Streamlit</h2>
                    </div>
                    """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.header("**Why streamlit**")
        st.markdown("✨ **Streamlit's open source app-framework is one of the best ways to create beautiful, custom web apps for machine learning and data science**")
        st.markdown("✨ **We can create wide variety of beautiful widgets and add interactivity with widgets**")
        st.markdown("✨ **We can install components to give the extra functionalities such as embedding video, code snippets, or animations. All from the comfort of python**")
        st.markdown("✨ **Also, we can deploy instantly**")
        st.markdown("✨ **It can handle slightly more than 256 threads where each connected user to a streamlit site produces its own thread**")

        st.header("**Advantages**")
        st.markdown("✨ **No need to worry about routing**")
        st.markdown("✨ **No need to worry about front end development**")
        st.markdown("✨ **Super-fast development to deployment time. Literally minutes**")

        st.header("**Disadvantages**")
        st.markdown("✨ **Will not scale**")
        st.markdown("✨ **Cannot easily customize any of the frontend components**")
        st.markdown("✨ **Relatively new, so there are features that are still beta**")
    ###############################################################################################################################################################
    if choices == 'Alternatives of streamlit':
        html_temp = """
                            <div style="background-color:#87CEFA ;padding:10px">
                            <h2 style="color:white;text-align:center;">Alternatives of Streamlit</h2>
                            </div>
                            """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.markdown("**Considering scalability as the main concern, we have Flask and FastAPI which have a complete edge over streamlit**")

        st.subheader("**Flask**")
        st.markdown("✨ **It is a Python-based framework that allows to hook up websites with less amount of code. We can create a small-scale website with this as it allows customization at every step(highly customizable)**")
        st.markdown("✨ **Being a minimalistic package, only core components are bundled with this and all other extensions require explicit setup**")
        st.markdown("✨ **There are some issues with Flask such as slow nature, no async, and web sockets support that can speed up the processes, and finally no automated docs generation system. We need to manually design the user interface for the usage and examples of the API**")
        st.markdown("✨ **All these issues are resolved in the new framework FastAPI **")

        st.subheader("**FastAPI**")
        st.markdown("✨ **It is a modern framework that allows us to build APIs seamlessly without much effort. It has the ability to separate the server code from the business logic increasing code maintainability**")
        st.markdown("✨ **It is much faster as compared to the flask because it’s built over ASGI instead of WSGI**")
        st.markdown("✨ **It generates the documentation on the go when you are developing the API**")
        st.markdown("✨ **It also generates a nice GUI which solves everything that was missing in the flask**")
        st.markdown("✨**It can handle 9000 requests at a time**")

    ###############################################################################################################################################################
    if choices == 'XML and ReactJS':
        html_temp = """
                                    <div style="background-color:#87CEFA ;padding:10px">
                                    <h2 style="color:white;text-align:center;">XML Parsing and ReactJS</h2>
                                    </div>
                                    """
        st.markdown(html_temp, unsafe_allow_html=True)

        st.subheader("**XML parsing in streamlit**")
        st.markdown("✨ **We can import the XML files and convert them to json to be able to create dataframes and carry out some analysis**")
        st.markdown("**A sample code snippet**")

        code = '''
        import xmltodict
        import json
        import streamlit as st

        file1 = st.file_uploader('File 1')
        file2= st.file_uploader('File 2')

        if st.button('Compare Files'):
            xml = file1.read()
            file1_data = json.loads(json.dumps(xmltodict.parse(xml)))
            st.write(file1_data)
        '''
        st.code(code, language = 'python')

        st.subheader("**ReactJS**")
        st.markdown("✨ **Streamlit has got a component which has two parts**")
        st.markdown("**1. A frontend, which is built out of HTML and any other web tech like (JavaScript, React, Vue, etc.), and gets rendered in Streamlit apps via an iframe tag**")
        st.markdown("**2. A Python API, which Streamlit apps use to instantiate and talk to that frontend**")
    ###############################################################################################################################################################
    if choices == 'Demo':
        html_temp = """
                                            <div style="background-color:#87CEFA ;padding:10px">
                                            <h2 style="color:white;text-align:center;">Demo</h2>
                                            </div>
                                            """
        st.markdown(html_temp, unsafe_allow_html=True)
        ######################################  Portfolio Level  #######################################################
        st.header("**Proposed Pricing Models- Portfolio Level**")
        st.markdown("✨ **Portfolio LOB results**")
        df = pd.DataFrame(
            [["Auto", 1000000, 800000, 0.8, 950000, 0.95],
             ['Property', 500000, 450000, 0.9, 500000, 1],
             ['GL', 1000000, 1200000, 1.2, 1200000, 1.2],
             ['Workers Comp', 2000000, 1750000, 0.88, 1900000, 0.95],
             ['Umbrella', 500000, 300000, 0.6, 450000, 0.9],
             ['Account Total', 5000000, 4500000, 0.9, 5000000, 1]],
            columns=["Line of Business", "Modeled target Premium", "Current Premium", "Factor to modeled premium", "Proposed Premium", "New factor"]
        )
        st.dataframe(df)
        st.markdown(get_table_download_link(df), unsafe_allow_html=True)
        #############################################################################################
        st.markdown("✨ **Portfolio Results by Accounts**")
        df1 = pd.DataFrame(
            [['ABC Inc', 500000, 450000, 0.9, 500000, 1],
             ['Auto Shop', 400000, 450000, 1.13, 550000, 1.38],
             ['123 Main', 1200000, 1300000, 1.08, 1200000, 1],
             ['XYZ Inc', 2500000, 1800000, 0.72, 2100000, 0.84],
             ['RST Co', 400000, 500000, 1.25, 650000, 1.63],
             ['Account Total', 5000000, 4500000, 0.9, 5000000, 1]],
            columns=["Line of Business", "Modeled target Premium", "Current Premium", "Factor to modeled premium",
                     "Proposed Premium", "New factor"]
        )
        st.dataframe(df1)
        st.markdown(get_table_download_link(df1), unsafe_allow_html=True)
        ###################################  Account level  ##########################################################
        st.header("**Proposed Pricing Models- Account Level**")
        account = st.selectbox("Please select any Account", ("Auto Shop", "ABC Inc", "123 Main", "XYZ Inc", "RST Co"))

        if account == "Auto Shop":
            st.text("No data available for this account")

        if account == "ABC Inc":
            st.subheader("Account: ABC Inc")
            df2 = pd.DataFrame(
                [["Auto", 100000, 80000, 0.8, 95000, 0.95],
                 ['Property', 50000, 45000, 0.9, 50000, 1],
                 ['GL', 100000, 120000, 1.2, 120000, 1.2],
                 ['Workers Comp', 200000, 175000, 0.88, 190000, 0.95],
                 ['Umbrella', 50000, 30000, 0.6, 45000, 0.9],
                 ['Account Total', 500000, 450000, 0.9, 500000, 1]],
                columns=["Line of Business", "Modeled target Premium", "Current Premium", "Factor to modeled premium",
                         "Proposed Premium", "New factor"]
            )
            st.dataframe(df2)
            st.markdown(get_table_download_link(df2), unsafe_allow_html=True)

            st.subheader("Rate")
            df3 = pd.DataFrame(
                [["Auto",  80000, 95000, 19],
                 ['Property', 45000, 50000, 11],
                 ['GL',  120000, 120000, 0],
                 ['Workers Comp',  175000,  190000, 9],
                 ['Umbrella', 30000, 45000, 50],
                 ['Account Total',  450000, 500000, 11]],
                columns=["Line of Business", "Current Premium", "Proposed Premium", "Rate(in Percentage)"]
            )
            st.dataframe(df3)
            st.markdown(get_table_download_link(df3), unsafe_allow_html=True)
        #############################################################################################

        if account == "123 Main":
            st.text("No data available for this account")

        if account == "XYZ Inc":
            st.text("No data available for this account")

        if account == "RST Co":
            st.text("No data available for this account")
        #############################################################################################

    #if choices == 'The End':
        #forth = Image.open('thanks.jpg')
        #st.image(forth, use_column_width=True)
        #st.balloons()


if __name__ == '__main__':
    main()
# Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.

# ~~~~~~~~~~~~~~~~~~~~~ Importing required packages -
 
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import webbrowser

# ~~~~~~~~~~~~~~~~~~~~~ Different User pages and respective functions - 

# ~~~~~~~~~~ Home Page -

def home_page():
    # Setting the title - 
    st.title("TAMIDS Data Science Competition")
    
    # Desription -
    st.write("""
             The 2021 TAMIDS Data Science Competition concerns the role of money in US Presidential Elections. The key
             idea of democracy is that every citizen should have input, via a vote, as to who is elected. Enormous amounts of
             money are expended by political campaigns to engage with voters, and so fundraising has become a major
             activity by candidates and other actors. Donations are an additional way for constituents to get involved in political
             races. Unions and corporations are able to donate through Political Action Committees (PACs), while the
             2010 Citizens United ruling by the US Supreme Court has removed caps on corporate donations via PACs and
             allowed campaign ads to be published or broadcast anonymously.  
             """)
    
    # Problem Statement - 
    st.write("""
             ## Problem Statement
             Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    # Data Collection and Pre-processing -
    st.write(" ")
    st.write("""
             ## Data Collection and Pre-processing
             Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    # Overview - 
    st.write("""
             ## Overview of Approach 
             Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    # Navigation - 
    st.write("")
    st.info("Please navigate using the select box in the sidebar on the left.")

# ~~~~~~~~~~ Expenditure Analysis Page -

def get_party_exp_graph(party, category):
    # Getting the Graph - 
    HtmlFile = open(f"Expenditure_Demographics_Analysis/Graphs/{party}_{category}.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=500)

def get_graph_inference(party):
    
    # Understanding Democratics Graph - 
    if party == "Democrats":
        
        st.write("""
                 ### **Plot Overview: Democrats **
                 
                 **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                 Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                 
                 * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                 Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                 Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                 Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                 * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                 Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                 Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                 Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                 * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                 Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                 Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                 Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                 """)
    
    # Understanding Republicans Graph - 
    elif party == "Republicans":
        st.write("""
                     ### **Plot Overview: Republicans**
                     
                     **First General OVerview!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
                     * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                     Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                     Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                     Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     """)

# Get Vote diff graphs - 
def get_vote_diff_graphs(party):
    col1, col2, col3 = st.beta_columns((1,0.1,1))
    # Positive difference plot - 
    with col1:
        # Getting the Graph - 
        HtmlFile = open(f"Expenditure_Demographics_Analysis/Graphs/Positive_Vote_{party}.html", 'r', encoding='utf-8')
        source_code_2 = HtmlFile.read()
        components.html(source_code_2, height=500)
    
    # Negative difference plot - 
    with col3:
        # Getting the Graph - 
        HtmlFile = open(f"Expenditure_Demographics_Analysis/Graphs/Negative_Vote_{party}.html", 'r', encoding='utf-8')
        source_code_2 = HtmlFile.read()
        components.html(source_code_2, height=500)

def get_overall_graphs(party):
    # Getting the Graph - 
    HtmlFile = open("Expenditure_Demographics_Analysis/Graphs/Some_Graph.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=1200)
    
def get_overall_inference(party):
    # Democrats inference - 
    if party == "Democrats":
        # Getting inference -
        st.write("")
        st.write("""
                 ### **Democrats - Plot Overview: **
                
                **Some intersting insight!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                
                Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                """)
    
    # Republicans inference - 
    elif party == "Republicans":
        # Getting inference -
        st.write("")
        st.write("""
                 ### **Republicans - Plot Overview: **
                
                **Some intersting insight!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                
                Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
                Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
                Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
                Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                """)
def expenditure_analysis():
    # Setting the title - 
    st.title("Expenditure and Demographics Analysis!")
    
    # Desription -
    st.write("""
             The key idea of democracy is that every citizen should have input, via a vote, as to who is elected. Enormous amounts of
             money are expended by political campaigns to engage with voters, and so fundraising has become a major
             activity by candidates and other actors. The money is spent for various purposes.
             """)
    
    st.write("")
    
     # Getting the initial image -
    col1, col2, col3 = st.beta_columns((1,2.5,1))
    image = Image.open('Expenditure_Demographics_Analysis/Data_Clean_Preprocess/Initial_Overview.png')
    col2.image(image)
    
    # Showing inital analysis -
    st.write("""
               **EXPLAIN ABOVE GRAPH. INSIGHTS!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
               """)
    
    st.write(" ")
    # State-wise graphs -
    st.write("""
             **TRANSITION INTO NEXT GRAPHS. BRIEF INTRODUCTION.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    st.write(" ")
    col1, col2 = st.beta_columns((1,1))
    # Getting party from the user -
    party_selected = col1.selectbox("Select Party", ['Democrats', 'Republicans'])
    
    # Getting expenditure from the user - 
    expenditure_category_selected = col2.selectbox("Select Expenditure", 
                                                   ["All Expenses", "Communiations Expenses", "Advertisement Expenses",
                                                    "Logistics Expenses", "Others"])
    
    # Getting the graph - 
    get_party_exp_graph(party_selected, expenditure_category_selected)
    
    # Geting the sponding explanation - 
    get_graph_inference(party_selected)
    
    st.write("---")
    # DIFFERENCE PLOT -
    
    st.write("""
             ## Investment to Vote Difference Ratio
             """)
    st.write("""
             **Explanation.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    st.write(" ")
    
    # Choosing party to analyze vote difference.
    col1, col2, col3 = st.beta_columns((1,1.5,1))
    party_selected_2 = col2.selectbox("Choose a party to analyze vote difference over years - ", 
                                     ['Democrats', 'Republicans'])
    st.write(" ")
    
    # Getting vote difference graphs - 
    get_vote_diff_graphs(party_selected_2)
    
    # Getting inference, result, analysis - 
    st.write("""
             **Explanation.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    st.write("---")
    
    # Entering the final plot of Tushar -
    st.write("""
             ## Some Title
             
             **Explain how to read the graph, how it can help.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             """)
    
    # Choosing party to analyze vote difference.
    col1, col2, col3 = st.beta_columns((1,1.5,1))
    party_selected_3 = col2.selectbox("Choose a party to analyze overall graphs - ", 
                                     ['Democrats', 'Republicans'])
    st.write(" ")
    
    # Getting vote difference graphs - 
    get_overall_graphs(party_selected_3)
    
    # Get overall inference - 
    get_overall_inference(party_selected_3)

# ~~~~~~~~~~ Industry Donations Analysis Page -

def get_state_wise_graph(party):
    # Getting the Graph - 
    HtmlFile = open(f"Company_Donations_Analysis/Graphs/{party}_company_donation_statewise.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=450)
    
def get_year_wise_graph():
    # Getting the Graph - 
    HtmlFile = open("Company_Donations_Analysis/Graphs/yearwise_company_donations.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=450)

def get_financial_organization_graph():
    # Getting the Graph - 
    HtmlFile = open("Company_Donations_Analysis/Graphs/financial_organisations_donation.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=450)

def get_educational_graph():
    # Getting the Graph - 
    HtmlFile = open("Company_Donations_Analysis/Graphs/educational_organisations_donation.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=450)
    
def industry_donations_analysis():
    # Setting the title - 
    st.title("Industry Donation Analysis")
    
    # Desription -
    st.write("""
             **Some background thinking. Initial thought process of going into this analysis.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
             """)
    
    st.write("""
             ## Party-wise Donations 
             
             **Some intro into the grpahs. Why we are analyzing it that way.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
             """)
    st.write(" ")
    
    col1, col2, col3 = st.beta_columns((1,1.5,1))
    party_selected_don = col2.selectbox("Select Party - ", ["Democratics", "Republicans"])
    
    # Getting the state wise graph - 
    get_state_wise_graph(party_selected_don)
    
    # Getting inference -
    st.write("")
    st.write("""
             ### **Plot Overview: **
            
            **Some intersting insight!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
            
            Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
            Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
            Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
            """)
    
    # Year-wise Donations - 
    st.write("""
             ## Year-wise Donations 
             
             **Some background thinking. Reason for thinking in this direction!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
              
             """)
    
    # Getting the year wise graph - 
    get_year_wise_graph()
    
    # Inference/Result/Analysis (Insights)
    st.write("""
             ### Inference/Result/Analysis 
             
             **Interesting insights into the grphs** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
             Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
                     
             * **2012:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
             Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
             Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
             Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             * **2016:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
             Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
             Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
             Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
             * **2020:** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
             Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
             Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
             Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
                     
             """)
    
    # Financial Organization -
    st.write("""
             ## Financial Organizations Donations 
             
             **Some background thinking. Reason for thinking in this direction!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
              
             """)
    
    # Get financial graph
    get_financial_organization_graph()
    
    # Getting inference -
    st.write("")
    st.write("""
            **Some intersting insight!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
            
            Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
            Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
            Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
            """)
            
    # Educational Organization -
    st.write("""
             ## Educational Institution Donations 
             
             **Some background thinking. Reason for thinking in this direction!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
             
             """)
    
    # Get financial graph
    get_educational_graph()
    
    # Getting inference -
    st.write("")
    st.write("""
            **Some intersting insight!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. **Year Specific.**  
            
            Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
            Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
            Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
            Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
            """)
            

# ~~~~~~~~~~ Network Analysis Page -

def network_analysis():
    # Setting the title - 
    st.title("Network Analysis")
    
    # Dividing into 2 parts - 
    col1, col2, col3 = st.beta_columns((1,0.1,1))
    
    # Setting the image - 
    image = Image.open('Images/network_photo.png')
    
    # Setting the image width -
    col1.image(image, use_column_width=True)
    
    # Writing description - 
    col3.write("""
               Topological Data Analysis is a clustering algorithm that relies on topology and 
               creates a Cech complex of a point-cloud. Using persistent diagrams, the number of 
               clusters is calculated. From there, using t-distributed stochastic neighbor embedding, 
               the data is projected in a manner such that some properties are preserved. After the 
               projection, a clustering algorithm along with covering balls is applied to the dataset 
               to obtain a 3-dimensional graph. The hyperparameters are autotuned based on the variance 
               and mean valency of the graph. Lastly, the graph is colored according to different 
               attributes associated with the original dataset to provide better visualization.
               """)
    
    st.write("""
             ## Inference/Result/Analysis 
             
             There are some great insights from this model, specifically on the clustering part. 
             There is one cluster with states where DEMOCRATS won and their expense is around the 
             same as republicans. Similarly, there is another one where REPUBLICANS won, which gives 
             us some information on the states where parties spend a similar amount of money and the 
             people tend to vote for the same party. Another cluster has states where democrats did not 
             spend more than the Republicans, but still, they won, which says that the state is blue. 
             These insights were helpful in understanding the relationship between expenditure and 
             voting in different states. 
             """)
    st.write(" ")
    st.write("""
             You can go to the network analysis by clicking the button. Below is a snapshot of the network analysis.
             """)
    
    # To access the network analysis, press the button below - 
    st.write("")
    col1, col2, col3 = st.beta_columns((1,1,1))
    # link = '[Network Analysis](https://ritesh-suhag.github.io./)'
    # col2.markdown(link, unsafe_allow_html=True)
    url = 'https://ritesh-suhag.github.io./'
    if col2.button("Go to the Network Analysis"):
        webbrowser.open_new_tab(url)
    
    st.write(" ")
    # Setting the image - 
    image = Image.open('Images/Network_Analysis.png')
    
    # Setting the image width -
    st.image(image, use_column_width=True)
    
# ~~~~~~~~~~ Others Page -

def authors():
    # Setting the title - 
    st.title("About the Authors")
    st.write(" ")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/ritesh.png')
    
    # Setting the image width -
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Ritesh Singh Suhag")
    
    # About section - 
    col3.write("""
               Aspiring data scientist focused on executing data-driven solutions. Experienced at creating predictive models and analyzing raw data 
               to deliver insights and implement action-oriented solutions to complex business problems.  
               
               * **University:** Texas A&M University (Mays Business School)
               * **Degree:** MS in Management Information Systems (May 2021)
               * **Email:** ritesh_10@tamu.edu
               * **LinkedIn:** [linkedin.com/in/ritesh-singh-suhag/](https://www.linkedin.com/in/ritesh-singh-suhag/)
               * **Github:** [github.com/ritesh-suhag](https://www.github.com/ritesh-suhag)
               """)
    st.write(" ")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/tushar.png')
    
    # Setting the image width -
    col1.write("")
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Tushar Pandey")
    
    # About section - 
    col3.write("""
               Research Area: Quantum Topology and Compressed Sensing     
               
               * **University:** Texas A&M University (Department of Mathematics)
               * **Degree:** PhD Student (2024) 
               * **Email:** tusharp@tamu.edu
               * **LinkedIn:** [linkedin.com/in/tushar-pandey1612/](https://www.linkedin.com/in/tushar-pandey1612/)
               * **Github:** [github.com/pandey-tushar](https://github.com/pandey-tushar)
               """)
    st.write("")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/sambandh.png')
    
    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Sambandh Dhal")
    
    # About section - 
    col3.write("""
               Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque.   
               
               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering) 
               * **Email:** sambandh@tamu.edu
               * **LinkedIn:** [linkedin.com/in/sambandh-dhal9163/](https://www.linkedin.com/in/sambandh-dhal9163/)
               * **Github:** [github.com/ritesh-suhag](https://www.github.com/ritesh-suhag)
               """)
    st.write("")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/swarnabha.png')
    
    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Swarnabha Roy")
    
    # About section - 
    col3.write("""
               Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque.     
               
               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering) 
               * **Email:** swarnabha7@tamu.edu
               * **LinkedIn:** [linkedin.com/in/swarnabha-roy-53a588a4/](https://www.linkedin.com/in/swarnabha-roy-53a588a4/)
               * **Github:** [github.com/ritesh-suhag](https://www.github.com/ritesh-suhag)
               """)
    st.write("")

# ~~~~~~~~~~~~~~~~~~~~~ Main application design -

st.set_page_config(layout='wide', page_title = 'US Elections')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Setting the image - 
image = Image.open('Images/image.png')

# Setting the image width -
st.image(image, use_column_width=True)

# Sidebar navigation for users -
st.sidebar.header('Navigation tab -')
navigation_tab = st.sidebar.selectbox('Choose a tab', ('Home-Page', 'Industry Donations Analysis', 'Expenditure Analysis', 'Network Analysis', 'About the Authors'))

# Displaying pages according to the selection -

# Home page -
if navigation_tab == 'Home-Page':
    home_page()

# First page -
elif navigation_tab == 'Expenditure Analysis':
    expenditure_analysis()

# Second page -
elif navigation_tab == 'Industry Donations Analysis':
    industry_donations_analysis()

# Third Page -
elif navigation_tab == 'Network Analysis':
    network_analysis()

# About Page - 
elif navigation_tab == 'About the Authors':
    authors()

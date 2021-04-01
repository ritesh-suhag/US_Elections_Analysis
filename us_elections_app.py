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
             An analysis of the corporate funding spanning across all the states in the United States of America has been analyzed for the last six presidential elections. A pattern emerging from how the corporate donations from the different sectors of the industry have been studied and inferences have been made accordingly.   
               
             """)
    
    st.write("""
             ## Party-wise Donations 
             
             For each of the states, the donations made to both the political parties: Republicans and Democrats have 
             been analyzed and the impact of these corporate funding have been analyzed on how they determine the final
              outcome. For this purpose, all these companies have been divided into different sectors depending on their
               area of operation and the donation patterns for each of these companies have been analyzed over the past 
               presidential elections and the factors promoting such behavior have been scrutinized for future analysis.
             
             
             For a detailed analysis of these party wise donations, an interactive plot has been shown for both the 
            parties with the help of bubble plots."""
             )
    st.write(" ")
    
    col1, col2, col3 = st.beta_columns((1,1.5,1))
    party_selected_don = col2.selectbox("Select Party - ", ["Democratics", "Republicans"])
    
    # Getting the state wise graph - 
    get_state_wise_graph(party_selected_don)
    
    # Getting inference -
    st.write("")
    st.write("""
             ### **Plot Overview: **
            
            **Some intersting insight!** As we can see, in the bubble plot above, the Transportation companies (FedEx, 
            UPS etc.) have stayed loyal to the Republican party which can be estimated by the massive amount of 
            donations that have been made to the party irrespective of the outcome of the elections. Similarly, 80% of 
            the Tech companies and the Labor Unions have remained loyal to the Democratic Party in the subsequent 
            elections. The Finance and Real Estate companies, baring a few, are the only sector of companies which have 
            shifted their allegiance in each Presidential campaign and have been successful in gauging the winning party
             in most of the cases. Another important observation that can be made in this case is that the major donors 
             of the Republican party in all of these Presidential campaigns have their headquarters located in smaller 
             states, mostly in Michigan and Wisconsin, where as most of the major donors of the Democratic party have 
             their headquarters centered in New York and California.""")
    
    # Year-wise Donations - 
    st.write("""
             ## Year-wise Donations 
             
             **Some background thinking. Reason for thinking in this direction!** We further explore the Donation data 
             over the years to get some insights. We analyzed the Corporate Donation data for the last three 
             Presidential elections. All the money that has been donated by the companies during the non-election years 
             have been taken into account for the next Presidential year. For example, if we have the company wise 
             donation data for 2014 and 2016, we added the donation received by the Political parties in 2014 to the
             donation data received in 2016 so that we have a cumulative donation received by the Political parties 
             during the Political campaign years. 
              
             """)
    
    # Getting the year wise graph - 
    get_year_wise_graph()
    
    # Inference/Result/Analysis (Insights)
    st.write("""
             ### Inference/Result/Analysis 
             
             **Interesting insights into the graphs** The above visualization shows a relation between the money donated 
              to the Republications vs. the money donated to the Democrats over the years by the Corporate Industries.  
              The size of the circle gives a relative understanding of the amount of money donated to the Political 
              parties. The x-axis gives the estimate of the money donated to the Democrats while the y-axis gives the 
              estimate of the money donated to the Republicans. Thus, more the circle is leaning towards the x-axis, more
              the money is invested onto Democrats and vice versa. The color of the circle denotes the category or the sector
               of industry into which the company belongs to. Let's look into the year-wise analysis:
                     
             * **2012:** Most of the donations came from Miscellaneous Business, Financial and Real Estate institutions 
             and Labor based industries. Las Vegas Sands is the biggest contributor from Miscellaneous Business and most
             of the money has been donated to the Republicans. The majority of the companies belonging to the labor 
             industry donated to the Democrats. The money donated by Financial institutions is scattered between both
             Democrats and Republicans.
             * **2016:** The major donors were still the Miscellaneous Business, Financial institutions, Labor and 
             Healthcare institutions. Las Vegas Sands is still the biggest contributor from Miscellaneous Business and 
             most of the money has been donated to the Republicans. Majority of Financial Institutions supported the 
             Democrats this time. Labor industry continued their support for Democrats. 
             * **2020:** The money donations have significantly increased as denoted by the size of the circles. The 
             biggest contributors to the Democrats were the Financial institutions. Miscellaneous Business still 
             supported the Republicans irrespective of the election year. Similarly, the money donated by the labor 
             industries have increased but they stayed loyal to the Democrats and continued their support. 
                     
             """)
    
    # Financial Organization -
    st.write("""
             ## Donations by Financial Organizations 
             
             **Some background thinking. Reason for thinking in this direction!** The Financial institutions, Insurance 
             companies and the Real Estate companies made significant donations to the Political parties and their 
             contributions have swung a lot over the years. These institutions were not loyal in particular to any party
             and they mostly invested in the Political parties that they thought would likely win during that
              Presidential year. 
              
             """)
    
    # Get financial graph
    get_financial_organization_graph()
    
    # Getting inference -
    st.write("")
    st.write("""
            **Some intersting insight!** During the 2012 Presidential elections, the donations received were mostly 
            scattered between the Democrats and the Republicans. Although some of the companies like Perry Homes and 
            Hugo Enterprises donated mostly to the Republicans, majority of the donations were made to the Democrats.
            
            In 2016, the donations were spaced out almost equally between the Democrats and the Republicans. Companies 
            like Bloomberg LP is one of those few companies who have not donated significantly in the past elections 
            campaigns except for 2016 and 2020. 
            
            In 2020, most of the companies shifted their major chunks to the Democratic Party barring Citadel LLC, Ryan 
            Speciality group and Stephens Group which stayed loyal to the Republicans. Companies like Renaissance
             Technologies continued their support to the Democrats irrespective of the election year.
            """)
            
    # Educational Organization -
    
    
    # Get financial graph
    get_educational_graph()
    
    # Getting inference -
    st.write("")
    st.write("""
            Educational institutions also lent their support in the US Presidential Campaigns. In all the campaigns until
            now, the educational institutions, due to the diversity in their student population have donated unanimously
             to the Democratic party.
            """)
            

# ~~~~~~~~~~ Network Analysis Page -

def network_analysis():
    # Setting the title - 
    st.title("Network Analysis")
    
    # Desription -
    st.write("""
             **Explain how to read the graph, how it can help.** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
             """)
    st.write("""
             ### Inference/Result/Analysis 
             
             **Some great inference or anything that helps!** Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. 
               Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. 
               Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. 
               Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.   
               
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
    col1.write("")
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
    col3.write("## Swaranbha Roy")
    
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

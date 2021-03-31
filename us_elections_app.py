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
    st.markdown("""
                <p style='text-align: justify;'>
                
                The 2021 TAMIDS Data Science Competition concerns the role of money in US Presidential Elections. The key
             idea of democracy is that every citizen should have input, via a vote, as to who is elected. Enormous amounts of
             money are expended by political campaigns to engage with voters, and so fundraising has become a major
             activity by candidates and other actors. Donations are an additional way for constituents to get involved in political
             races. Unions and corporations are able to donate through Political Action Committees (PACs), while the
             2010 Citizens United ruling by the US Supreme Court has removed caps on corporate donations via PACs and
             allowed campaign ads to be published or broadcast anonymously.  
                
                </p>
                """, unsafe_allow_html=True)
    
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
                 """)
        st.markdown("""
                    <p style='text-align: justify;'>
                 
                 An outlier corresponding to the state DC was removed because of the unexpectedly high 
                 investment from both parties even though it’s a predominantly Democratic state for ages.
                 For different parties and categories of expenditure, graphs are displayed.  

                 * **2012:**  Interestingly the democrats invested a lesser amount in the states where 
                 Republicans are in a huge majority. At the same time, democrats spent a huge amount 
                 of money to get the clear majority, in states like Illinois, California, Nevada. 

                 * **2016:** All the states where Republicans have a huge margin in their victory 
                 witnessed a huge drop in expenditure from the Democrats. Since Democrats were in 
                 power for the last two sessions, they decided on cutting down the expenses.

                 * **2020:** After some political events, democrats were confident in some states 
                 and knew about the states they couldn’t win, thereby decreasing their investment 
                 in those states. In some states, democrats kept investing money even though they 
                 are far away from winning, planning for long-term success.
                   
                </p>""", unsafe_allow_html=True)
    # Understanding Republicans Graph - 
    elif party == "Republicans":
        st.write("""
                 ### **Plot Overview: Republicans**
                 """)
        st.markdown("""
                    <p style='text-align: justify;'>
                 An outlier corresponding to the state DC was removed because of the unexpectedly high 
                 investment from both parties even though it’s a predominantly Democratic state for ages.
                 For different parties and categories of expenditure, graphs are displayed.  
                 
                 * **2012:**  An interesting correlation was found between states with low 
                     expenditure and election results. All the states where Republicans have spent 
                     around less than $ 3,000,000 are red states crushing the other parties. 

                * **2016:**  The previous states where Republicans didn’t feel the need to spend 
                     money and still get a victory witnessed a decrease in expenditure along with the 
                     other red states. Since Democrats were in power for the last two sessions, 
                     republicans strategically cut down their expenses. 

                * **2020:**  This year’s data is rather interesting because only the aforementioned 
                     states (in 2012) had less expenditure. Perhaps, even in some red states, Republicans
                     have invested a large amount of money because of the increase in Democratic votes. 
                     There are a few states where democrats and republicans were on an investing spree 
                     to secure at least the votes they had in 2016.
                   
                </p>""", unsafe_allow_html=True)

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
    HtmlFile = open(f"Expenditure_Demographics_Analysis/Graphs/{party}_State_Analysis.html", 'r', encoding='utf-8')
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=1200)
    
def get_overall_inference(party):
    # Democrats inference - 
    if party == "Democrats":
        # Getting inference -
        st.write("")
        st.write("""
                 ### **Democrats - Plot Overview: **""")
        st.markdown("""
             <p style='text-align: justify;'>
             States with a higher population of people who are neither African American nor White tend to favor the democrats.
             Another riveting find is that the expenditure is surging for the state's democrats already have a huge advantage in and 
             in the meanwhile where it’s either equal or the republicans are winning, the expenditure has decreased for 2016 which is 
             concurrent with the US politics trend. 
                </p>""", unsafe_allow_html=True)
    
    # Republicans inference - 
    elif party == "Republicans":
        # Getting inference -
        st.write("")
        st.write("""
                 ### **Republicans - Plot Overview: **""")
        st.markdown("""
             <p style='text-align: justify;'>
              States with a higher population of people who are neither African American nor White tend not to favor the Republicans. 
              In contrast to the conclusions drawn from the graph for democrats, the trend in change of expenditure throughout the 
              election years is a little different. Some states saw an increase in the expenditure throughout the three presidential 
              elections, while a general trend is an increase in investment in 2016 because it was a year marked with their victory.
                </p>""", unsafe_allow_html=True)

def expenditure_analysis():
    # Setting the title - 
    st.title("Expenditure and Demographics Analysis!")
    
    # Desription -
    st.markdown("""
                <p style='text-align: justify;'>
                   The key idea of democracy is that every citizen should have input, via a vote, as to who is elected. Enormous amounts of
             money are expended by political campaigns to engage with voters, and so fundraising has become a major
             activity by candidates and other actors. The money is spent for various purposes.
                </p>""", unsafe_allow_html=True)
    
    st.write("")
    
     # Getting the initial image -
    col1, col2, col3 = st.beta_columns((1,2.5,1))
    image = Image.open('Expenditure_Demographics_Analysis/Data_Clean_Preprocess/Initial_Overview.png')
    col2.image(image)
    
    # Showing inital analysis -
    st.markdown("""
                <p style='text-align: justify;'>
                   The above graph demonstrates the trend in amount expenditure of each party for the last 
               10 years. From the graph, the first obvious conclusion is: The campaigning expenditure 
               for each party increased five-fold for the last presidential year. This increased the 
               total voting numbers. Another subtle inference is the change and the difference in the 
               expenditure of Republicans and Democrats from the last presidential election to the 2020 
               presidential election.
                </p>""", unsafe_allow_html=True)
    
    st.write(" ")
    # State-wise graphs -
    st.markdown("""
                <p style='text-align: justify;'>
                   After analyzing the bigger picture, the next thing needed is “micro-analysis”. From looking 
             at a national scope, we switch to states and start looking at different expenses. The 
             dataset which comprised various purposes of expenditure was categorized using NLP with 
             categories: Advertisement, Communications, Logistics, and others.
                </p>""", unsafe_allow_html=True)
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
             ## How much does investment help?
             """)
    st.markdown("""
                <p style='text-align: justify;'>
                From the previous graph, we can see that each party wanted to go all in this time and win the elections. 
             But does investment always lead to an increase in the voting percentage? To answer this question we defined a 
             Return of Investment index for different states based on how much does campaigning influences the results for both parties. 
             </p>""", unsafe_allow_html=True)
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
             ### **Inference**
             """)
    st.markdown("""
                <p style='text-align: justify;'>
             The graphs are divided into two subgraphs where one corresponds to the states where the percentage of votes received by 
             Republicans/Democrats increased and the other subgraph where we see the states when the percentage of votes received by 
             Republicans/Democrats decreased between two presidential elections.  
             
             The first important question, whether investing always helps is answered through all the graphs. In various states, 
             the Republicans lost votes despite an increase in expenditure of millions of dollars. The ROI for republicans is positive 
             (significantly larger than 0) for the states (except Utah) where they lost, which means they reduced their expenditures there. 
             In 2016 in Utah, they reduced their investment and therefore lost a lot of votes (more than 25%), however, the state remained 
             red. But the next presidential election, they invested more and were able to get the votes in their favor. If we look at the 
             Democrats data, only five states witnessed a surge in blue votes whereas in 2020 all the states had an increase in the number 
             of votes for Democratic party. Most of the states with high ROI went Blue, except Utah in 2020. Because of a decrease 
             in Republican votes in 2016, Democrats invested just a little in 2020 and were able to secure 10% more votes than in 2016, 
             thereby giving a huge ROI for the same. This way, the graph helps us understand the trends and the power of campaigning on the 
             minds of different people beautifully.
             </p>""", unsafe_allow_html=True)
    
    st.write("---")
    
    # Entering the final plot of Tushar -
    st.write("""
             ## People, Money, and Voting!""")
    
    st.markdown("""
             <p style='text-align: justify;'>
             A scatter plot with population data, expenditure data, the voting percentage for three presidential election years 
             tells us about some correlation between the certain population in some states and how they affect the electoral votes 
             in their respective states.
             </p>""", unsafe_allow_html=True)
    
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
             
             **Interesting insights into the grphs** The above visualization shows a relation between the money donated 
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
    col3.markdown("""
                <p style='text-align: justify;'>
                Topological Data Analysis is a clustering algorithm that relies on topology and 
               creates a Cech complex of a point-cloud. Using persistent diagrams, the number of 
               clusters is calculated. From there, using t-distributed stochastic neighbor embedding, 
               the data is projected in a manner such that some properties are preserved. After the 
               projection, a clustering algorithm along with covering balls is applied to the dataset 
               to obtain a 3-dimensional graph. The hyperparameters are autotuned based on the variance 
               and mean valency of the graph. Lastly, the graph is colored according to different 
               attributes associated with the original dataset to provide better visualization.
                
                <p> 
                """, unsafe_allow_html=True)
    
    
    st.write("""
             ## Inference 
             
             """)
    st.markdown("""
               <p style='text-align: justify;'> 
               There are some great insights from this model, specifically on the clustering part. 
             There is one cluster with states where DEMOCRATS won and their expense is around the 
             same as republicans. Similarly, there is another one where REPUBLICANS won, which gives 
             us some information on the states where parties spend a similar amount of money and the 
             people tend to vote for the same party. Another cluster has states where democrats did not 
             spend more than the Republicans, but still, they won, which says that the state is blue. 
             These insights were helpful in understanding the relationship between expenditure and 
             voting in different states. 
             <p> 
             """, unsafe_allow_html=True)
                
    st.write(" ")
    st.write("""
             You can go to the network analysis by clicking on the link. Below is a snapshot of the network analysis.
             """)
    
    # To access the network analysis, press the button below - 
    st.write("")
    col1, col2, col3 = st.beta_columns((1,1,1))
    link = '[Go to Network Analysis](https://ritesh-suhag.github.io./)'
    col2.markdown(link, unsafe_allow_html=True)
    # url = 'https://ritesh-suhag.github.io./'
    # if col2.button("Go to the Network Analysis"):
    #     webbrowser.open_new_tab(url)
    
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
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Sambandh Dhal")
    
    # About section - 
    col3.write("""
               Research Area: Error Estimation and Machine Learning.
               
               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering) 
               * **Email:** sambandh@tamu.edu
               * **LinkedIn:** [linkedin.com/in/sambandh-dhal9163/](https://www.linkedin.com/in/sambandh-dhal9163/)
               * **Github:** [github.com/Sambandh](https://github.com/Sambandh)
               """)
    st.write("")
    
    # Dividing screen into 2 parts - 
    col1, col2, col3 = st.beta_columns((0.75,0.1,2))
    
    # Setting the image - 
    image = Image.open('Images/swarnabha.png')
    
    # Setting the image width -
    col1.write("")
    col1.write("")
    col1.image(image, use_column_width=True)
    
    # Ritesh Singh Suhag -
    col3.write("## Swarnabha Roy")
    
    # About section - 
    col3.write("""
               Research Area: Modular Robotics and Virtual Reality.
               
               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering) 
               * **Email:** swarnabha7@tamu.edu
               * **LinkedIn:** [linkedin.com/in/swarnabha-roy-53a588a4/](https://www.linkedin.com/in/swarnabha-roy-53a588a4/)
               * **Github:** [github.com/swarnabha13](https://github.com/swarnabha13)
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

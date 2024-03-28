# ### KICKOFF - CODING AN APP IN STREAMLIT

# ### import libraries
# import pandas as pd
# import streamlit as st
# import numpy as np
# import joblib

# st.write('Streamlit is an open-source app framework for Machine Learning and Data Science teams. For the docs, please click [here](https://docs.streamlit.io/en/stable/api.html). \
#     This is is just a very small window into its capabilities.')


# #######################################################################################################################################
# ### LAUNCHING THE APP ON THE LOCAL MACHINE
# ### 1. Save your *.py file (the file and the dataset should be in the same folder)
# ### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
# ### 3. Execute... streamlit run <name_of_file.py>
# ### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file



# #######################################################################################################################################
# ### Create a title

# st.title("Kickoff - Live coding an app")

# # Press R in the app to refresh after changing the code and saving here

# ### You can try each method by uncommenting each of the lines of code in this section in turn and rerunning the app

# ### You can also use markdown syntax.
# #st.write('# Our last morning kick off :sob:')

# ### To position text and color, you can use html syntax
# #st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)


# #######################################################################################################################################
# ### DATA LOADING

# ### A. define function to load data
# @st.cache_data # <- add decorators after tried running the load multiple times
# def load_data(path, num_rows):

#     df = pd.read_csv(path, nrows=num_rows)

#     # Streamlit will only recognize 'latitude' or 'lat', 'longitude' or 'lon', as coordinates

#     df = df.rename(columns={'Start Station Latitude': 'lat', 'Start Station Longitude': 'lon'})     
#     df['Start Time'] = pd.to_datetime(df['Start Time'])      # reset dtype for column
     
#     return df

# ### B. Load first 50K rows
# df = load_data("NYC_bikes_small.csv", 50000)

# ### C. Display the dataframe in the app
# st.dataframe(df)


# #######################################################################################################################################
# ### STATION MAP

# st.subheader('Location Map - NYC bike stations')      

# st.map(df)   


# #######################################################################################################################################
# ### DATA ANALYSIS & VISUALIZATION

# ### B. Add filter on side bar after initial bar chart constructed

# st.sidebar.subheader("Usage filters")
# round_trip = st.sidebar.checkbox('Round trips only')

# if round_trip:
#     df = df[df['Start Station ID'] == df['End Station ID']]


# ### A. Add a bar chart of usage per hour

# st.subheader("Daily usage per hour")

# counts = df["Start Time"].dt.hour.value_counts()
# st.bar_chart(counts)





# ### The features we have used here are very basic. Most Python libraries can be imported as in Jupyter Notebook so the possibilities are vast.
# #### Visualizations can be rendered using matplotlib, seaborn, plotly etc.
# #### Models can be imported using *.pkl files (or similar) so predictions, classifications etc can be done within the app using previously optimized models
# #### Automating processes and handling real-time data


# #######################################################################################################################################
# ### MODEL INFERENCE

# st.subheader("Using pretrained models with user input")

# # A. Load the model using joblib
# model = joblib.load('sentiment_pipeline.pkl')

# # B. Set up input field
# text = st.text_input('Enter your review text below', 'Best. Restaurant. Ever.')

# # C. Use the model to predict sentiment & write result
# prediction = model.predict({text})

# if prediction == 1:
#     st.write('We predict that this is a positive review!')
# else:
#     st.write('We predict that this is a negative review!')



# #######################################################################################################################################
# ### Streamlit Advantages and Disadvantages
    
# st.subheader("Streamlit Advantages and Disadvantages")
# st.write('**Advantages**')
# st.write(' - Easy, Intuitive, Pythonic')
# st.write(' - Free!')
# st.write(' - Requires no knowledge of front end languages')
# st.write('**Disadvantages**')
# st.write(' - Apps all look the same')
# st.write(' - Not very customizable')
# st.write(' - A little slow. Not good for MLOps, therefore not scalable')




# st.title("Classifying Iris Flowers")
# st.markdown("Toy model to play to classify iris flowers into \
# setosa, versicolor, virginica")

# st.header("Plant Features")
# col1, col2 = st.columns(2)
# with col1:
#     st.text("Sepal characteristics")
#     sepal_l = st.slider("Sepal lenght (cm)", 1.0, 8.0, 0.5)
#     sepal_w = st.slider("Sepal width (cm)", 2.0, 4.4, 0.5)
# with col2:
#     st.text("Pepal characteristics")
#     petal_l = st.slider("Petal lenght (cm)", 1.0, 7.0, 0.5)
#     petal_w = st.slider("Petal width (cm)", 0.1, 2.5, 0.5)


# # st.button("Predict type of Iris")

# from predicction import predict

# if st.button("Predict type of Iris"):
#     result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
#     st.text(result[0])



# import streamlit as st  #used for streamlit api reference

# # below all libraries were part of SMS Spam classifier model building and hence add them again.

# import pickle     #to load the saved pickle files
# import pandas as pd
# import numpy as np
# import string
# import nltk      #natural language tool kit used for text processing
# from nltk.corpus import stopwords  #text processing
# import string
# from nltk.stem.porter import PorterStemmer  #text processing
# import pandas as pd
# ps=PorterStemmer()   
# from xgboost import XGBClassifier

# nltk.download('punkt')
# nltk.download('stopwords')


# stemmer = nltk.stem.PorterStemmer()

# ENGLISH_STOP_WORDS = stopwords.words('english')

# # Custom stopwords to be added

# custom_stopwords = []
# custom_stopwords = ['game', 'games', 'unknown', 'studio', 'inc', 'ltd', 'studios']

# # Extend stopwords with custom stopwords
# ENGLISH_STOP_WORDS.extend(custom_stopwords)

# # my_tokenizer function, to be used when vectorizing
# def my_tokenizer(sentence):
#     # remove punctuation and set to lower case
#     for punctuation_mark in string.punctuation:
#         sentence = sentence.replace(punctuation_mark,'').lower()

#     # split sentence into words
#     listofwords = sentence.split(' ')
#     listofstemmed_words = []
    
#     # remove stopwords and any tokens that are just empty strings
#     for word in listofwords:
#         if (not word in ENGLISH_STOP_WORDS) and (word!=''):
#             # Stem words
#             stemmed_word = stemmer.stem(word)
#             listofstemmed_words.append(stemmed_word)

#     return listofstemmed_words





# #function to convert SMS text to numerical form ,SMS text  we will receive on our deployed app to predict.

# def transform_text(text):
#         text=text.lower()
#         y=[]

#         #tokenization
#         text=nltk.word_tokenize(text)
#         for i in text:
#             if i.isalnum():
#                 y.append(i)
#         text=y[:]
#         y.clear()

#         #removing stopwords and punctuations
#         for i in text:
#             if i not in stopwords.words('english') and i not in string.punctuation:
#                 y.append(i)
#         text=y[:]
#         y.clear()
    
#         #stemming applied on text
#         for i in text:
#             y.append(ps.stem(i))
#         return y



# #loading  both the models from respective directory

# tfidf_name=pickle.load(open('../Models/name.pkl','rb'))
# tfidf_publisher=pickle.load(open('../Models/publisher.pkl','rb'))
# tfidf_developer=pickle.load(open('../Models/developer.pkl','rb'))
# model=pickle.load(open("../Models/xgb_model.pkl",'rb'))


# #streamlit app title

# st.title("Video Games Rating Prediction")


#  #text input where user will enter the SMS text to predict (As shown above)
# input_sms= st.text_area("Enter the message")

# #predict button , when clicked will execute the process
# if st.button('Predict'):

#     #1.preprocess- converting the input_sms received by user on app  

#     transform_sms=transform_text(input_sms)
#     print(type(transform_sms))
#     transform_sms=np.array(transform_sms) #converting the list of string format to array of string format

#     #2.vectorize - converting the received text SMS into numeric for model understanding

#     vector_input=tfidf_name.transform(transform_sms.astype('str')).toarray()
#     print(type(vector_input))
#     print(vector_input)
#     vector_input =    pd.DataFrame(vector_input,columns=tfidf_name.get_feature_names_out())

#     #3.predict - passing the converted text to model to predict if it is spam or ham

#     prediction= model.predict(vector_input)[0]

#     #4.display- the result on app itself , if prediction result is 1 then ui(button) will display  Spam else Not Spam
    
#     if prediction==1:
#         st.header("Spam")
#     else:
#         st.header("Not Spam") 








# conda install streamlit , scikit-learn , pandas , matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import nltk
nltk.download('stopwords')
import string
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from sklearn.preprocessing import RobustScaler
import math



stemmer = nltk.stem.PorterStemmer()

ENGLISH_STOP_WORDS = stopwords.words('english')

# Custom stopwords to be added

custom_stopwords = []
custom_stopwords = ['game', 'games', 'unknown', 'studio', 'inc', 'ltd', 'studios']

# Extend stopwords with custom stopwords
ENGLISH_STOP_WORDS.extend(custom_stopwords)

# my_tokenizer function, to be used when vectorizing
def my_tokenizer(sentence):
    # remove punctuation and set to lower case
    for punctuation_mark in string.punctuation:
        sentence = sentence.replace(punctuation_mark,'').lower()

    # split sentence into words
    listofwords = sentence.split(' ')
    listofstemmed_words = []
    
    # remove stopwords and any tokens that are just empty strings
    for word in listofwords:
        if (not word in ENGLISH_STOP_WORDS) and (word!=''):
            # Stem words
            stemmed_word = stemmer.stem(word)
            listofstemmed_words.append(stemmed_word)

    return listofstemmed_words


def generate_encoded_df(label, options, prefix):
    # UI input
    selected_option = st.selectbox(label, options=options, key=label)

    # Create DataFrame with dummy variables
    encoded_df = pd.DataFrame(np.zeros((1, len(options))), columns=options)

    # Set value for the selected option to 1
    encoded_df.loc[0, selected_option] = 1

    # Add prefix 'x0' to column names
    encoded_df.columns = [prefix + col for col in encoded_df.columns]

    return encoded_df

# Load the models from the file
with open('../Models/xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('../Models/name.pkl', 'rb') as file:
    tfidf_name = pickle.load(file)

with open('../Models/publisher.pkl', 'rb') as file:
    tfidf_publisher = pickle.load(file)

with open('../Models/developer.pkl', 'rb') as file:
    tfidf_developer = pickle.load(file)
    
# with open('robust_scaler.pkl', 'rb') as file:
#     scaler = pickle.load(file)

# Define options for each input
genre_options = ['Action','Action-Adventure','Adventure','Board Game','Fighting',
                 'MMO','Misc','Music','Party','Platform','Puzzle','Racing','Role-Playing',
                 'Sandbox','Shooter','Simulation','Sports','Strategy','Visual Novel']

platform_brand_options = ['Microsoft', 'Nintendo', 'PC', 'Sony']

platform_type_options = ['Handheld', 'HomeConsole', 'PC']


name = pd.Series([st.text_area("Name of the game")], name='name')
publisher = pd.Series([st.text_area("Publisher")], name='publisher')
developer = pd.Series([st.text_area("Developer")], name='developer')



st.title("Game rating prediction")

# Generate encoded DataFrames for each input
genre_df = generate_encoded_df("Genre", genre_options, 'Genre_')
platform_brand_df = generate_encoded_df("Platform Brand", platform_brand_options, 'Platform_Brand_')
platform_type_df = generate_encoded_df("Platform Type", platform_type_options, 'Platform_Type_')

print(genre_df)

# Create a button to trigger predictions
predict_button = st.button('Predict', key='predict_button')



if predict_button:
    # Combine all encoded features
    all_features = pd.concat([genre_df, platform_brand_df, platform_type_df, name, publisher, developer], axis=1)

    X_test_name = tfidf_name.transform(all_features["name"])
    # Drop the column
    columns_to_drop = ['name']

    # Drop multiple columns in-place
    all_features.drop(columns=columns_to_drop, inplace=True)

    # Add the prefix pd for ProjectDescription for columns
    cols = [f'Name_{word}' for word in tfidf_name.get_feature_names_out()]

    # Join the original test dataset and positive bag of words.
    X_test_name = pd.DataFrame(columns=cols, data=X_test_name.toarray())
    X_test_extended_with_name = pd.concat([all_features, X_test_name], axis=1)

    X_test_pub = tfidf_publisher.transform(X_test_extended_with_name["publisher"])
    # Drop the column
    columns_to_drop = ['publisher']

    # Drop multiple columns in-place
    X_test_extended_with_name.drop(columns=columns_to_drop, inplace=True)

    # Add the prefix ap for Applicant for columns
    cols = [f'Publisher_{word}' for word in tfidf_publisher.get_feature_names_out()]

    # Join the original test dataset and positive bag of words.
    X_test_pub = pd.DataFrame(columns=cols, data=X_test_pub.toarray())
    X_test_extended_with_pub = pd.concat([X_test_extended_with_name, X_test_pub], axis=1)


    X_test_dev = tfidf_developer.transform(X_test_extended_with_pub["developer"])
    # Drop the column
    columns_to_drop = ['developer']

    # Drop multiple columns in-place
    X_test_extended_with_pub.drop(columns=columns_to_drop, inplace=True)

    # Add the prefix ap for Applicant for columns
    cols = [f'Developer_{word}' for word in tfidf_developer.get_feature_names_out()]

    # Join the original test dataset and positive bag of words.
    X_test_dev = pd.DataFrame(columns=cols, data=X_test_dev.toarray())
    X_test_extended_with_dev = pd.concat([X_test_extended_with_pub, X_test_dev], axis=1)

    print(X_test_extended_with_dev)
    # X_test_s = scaler.transform(X_test_extended_with_ap)

    cols_when_model_builds = model.get_booster().feature_names
    X_test_extended_with_dev = X_test_extended_with_dev[cols_when_model_builds]

    # Make predictions
    prediction = model.predict(X_test_extended_with_dev)

    if (prediction == 0):
        st.write('Estimated rating: Okay')

    if (prediction == 1):
        st.write('Estimated rating: Strong')

    if (prediction == 2):
        st.write('Estimated rating: Weak')    
    
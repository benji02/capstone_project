
# conda install streamlit , scikit-learn , pandas , matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import string
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from sklearn.preprocessing import RobustScaler
from xgboost import XGBClassifier



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
with open('./Models/xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('./Models/name.pkl', 'rb') as file:
    tfidf_name = pickle.load(file)

with open('./Models/publisher.pkl', 'rb') as file:
    tfidf_publisher = pickle.load(file)

with open('./Models/developer.pkl', 'rb') as file:
    tfidf_developer = pickle.load(file)
    
# with open('robust_scaler.pkl', 'rb') as file:
#     scaler = pickle.load(file)

# Define options for each input
genre_options = ['Action','Action-Adventure','Adventure','Board Game','Fighting',
                 'MMO','Misc','Music','Party','Platform','Puzzle','Racing','Role-Playing',
                 'Sandbox','Shooter','Simulation','Sports','Strategy','Visual Novel']

platform_brand_options = ['Microsoft', 'Nintendo', 'PC', 'Sony']

platform_type_options = ['Handheld', 'HomeConsole', 'PC']



st.header("Gaming Score Forecasting Model", divider=True)

st.image('./Images/header.jpeg')





st.subheader("Improving video game development")

st.write("This is the perfect tool to predict the Metacritic score of a game. \
        Enter the name, the publisher and the developer, and choose the genre, the platform type and \
        the platform type and you will get the Metascore range between Weak, Okay and Strong!")

name = pd.Series([st.text_input("Name of the game")], name='name')

col1, col2 = st.columns(2)

with col1:
    publisher = pd.Series([st.text_input("Publisher")], name='publisher')

with col2:
    developer = pd.Series([st.text_input("Developer")], name='developer')








# Generate encoded DataFrames for each input
genre_df = generate_encoded_df("Genre", genre_options, 'Genre_')
platform_brand_df = generate_encoded_df("Platform Brand", platform_brand_options, 'Platform_Brand_')
platform_type_df = generate_encoded_df("Platform Type", platform_type_options, 'Platform_Type_')


# Create a button to trigger predictions
predict_button = st.button('Predict', key='predict_button')



if predict_button:
    if ((len(name[0])>1) and (len(publisher[0])>1) and (len(developer[0])>1)):
                          
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
        prob = model.predict_proba(X_test_extended_with_dev)

        if (prediction == 0):
            st.write('Predicted Metascore rating range:   Weak')

        if (prediction == 1):
            st.write('Predicted Metascore rating range:   Okay')

        if (prediction == 2):
            st.write('Predicted Metascore rating range:   Strong')
        
        prob_pred = round(prob[0][prediction][0]*100,2)
        st.write(f'This prediction has a probability of ', str(prob_pred), '%.')
        

    else:
        st.write("Fill out all the required boxes to predict the rating!")


st.write("Weak = Metascore rating between 0 and 68.  \n \
        Okay = Metascore rating between 69 and 78.  \n \
        Strong = Metascore rating between 79 and 100.")
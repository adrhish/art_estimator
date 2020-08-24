from datetime import datetime

import joblib
import pandas as pd
import pytz
import streamlit as st

COLS = ['artist',
        'auction_house',
        'dating',
        'inscribed',
        'kind',
       'signed',
       'size',
       'stamped',
       'with_premium']


st.markdown("# Art estimator")
st.markdown("**Price prediction engine**")

def main():
    analysis = st.sidebar.selectbox("choose function", ["prediction", 
    											"recommendation (#TODO)", 'TODO some neat visualisations'])
    
    if analysis == 'TODO some neat visualisations':
    	st.header('this is coming soon')
    	st.markdown("**#TODO**")

    if analysis == "recommendation (#TODO)":
        st.header("This feature comes second")
        st.markdown("**#TODO**")

    if analysis == "prediction":
        
        #pipeline = joblib.load('data/model.joblib')
        print("loaded model")
        st.header("Art price predictor by 434 :) ")

        # inputs from user
        artist = st.text_input('artist','dummy artist name')
        auction_house = st.text_input('auction_house','')
        dating = st.text_input('dating','')
        inscribed = st.selectbox('inscribed',['yes','no'],1)

        kinds_of_paintings = ['Ink on paper', 'Pencil', 'Etching', 'Oil on paper', 
        								'Watercolor on paper', 'Pencil' ,'Unknown']
        kind = st.selectbox('kind',  kinds_of_paintings,len(kinds_of_paintings)-1)
        
        signed = st.selectbox('signed',['yes','no'],1)
        size = st.text_input('size', '' ) 
        stamped = st.selectbox('stamped',['yes','no'],1)
        with_premium = st.selectbox('with_premium',['yes','no'],1)
        
        
        data = pd.DataFrame(pd.read_csv('./paintings_df.csv'))
        #to_predict = [format_input(pickup=pickup_coords, 
        #dropoff=dropoff_coords, passengers=passenger_counts)]
        X = data
        
        #calling the model to make prediction:
        #res = pipeline.predict(X[COLS])
        
        #hashing the relevant output from the prediction:
        st.write(f"💸 estimated price for painting by \
        	{artist}: TODO")#, res[0])
        #st.map(data=data)


# print(colored(proc.sf_query, "blue"))
# proc.test_execute()
if __name__ == "__main__":
    #df = read_data()
    main()
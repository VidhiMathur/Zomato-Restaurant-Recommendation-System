import pickle as p
import streamlit as st
import pandas as pd

# with open('res_dist.pkl','rb') as f:
#        res_dist = p.load(f)
# Randomly sample 60% of your dataframe

def load():
    global df_percent
    global res_dist
    global indices
    global cosine_similarities

    if 'df_percent' not in globals():
        df_percent=pd.read_csv("df_percent.csv")

    if 'res_dist' not in globals():
        res_dist = df_percent.set_index('name')
    
    if 'indices' not in globals():
        indices = pd.Series(df_percent['name'])

    if 'cosine_similarities' not in globals():
        with open("cosine_similarities.pkl",'rb') as f:
            cosine_similarities = p.load(f)

# res_dist = pd.read_csv('zomato.csv', index_col='name')

load()

def recommend(name, cosine_similarities = None):
    global df_percent
    global res_dist
    global indices

    if cosine_similarities is None:
        cosine_similarities = globals()['cosine_similarities']

    # print(name)
    # print(indices)
    
    # Create a list to put top restaurants
    recommend_restaurant = []
    
    # Find the index of the hotel entered
    idx = indices[indices == name].index[0]
    
    # Find the restaurants with a similar cosine-sim value and order them from bigges number
    score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending=False)
    
    # Extract top 30 restaurant indexes with a similar cosine-sim value
    top30_indexes = list(score_series.iloc[0:31].index)

    # print(top30_indexes)
    
    # Names of the top 30 restaurants
    for each in top30_indexes:
        recommend_restaurant.append(list(res_dist.index)[each])
    
    # Creating the new data set to show similar restaurants
    df_new = pd.DataFrame(columns=['cuisines', 'Mean Rating', 'cost'])
    
    # Create the top 30 similar restaurants with some of their columns
    for each in recommend_restaurant:
        df_new = df_new.append(pd.DataFrame(res_dist[['cuisines','Mean Rating', 'cost']][res_dist.index == each].sample()))
    
    # Drop the same named restaurants and sort only the top 10 by the highest rating
    df_new = df_new.drop_duplicates(subset=['cuisines','Mean Rating', 'cost'], keep=False)
    df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(10)
    df_new['name'] = df_new.index
    df_new = df_new.reset_index(drop=True)[['name', 'cuisines', 'Mean Rating', 'cost']]
    
    print('TOP %s RESTAURANTS LIKE %s WITH SIMILAR REVIEWS: ' % (str(len(df_new)), name))
    print('\n'.join(df_new['name'].to_list()))
    
    return df_new['name']

st.title("Zomato Restaurants Recommendation System")
# option = st.selectbox("Enter Any restaurants", res_dist['name'].values)
option = st.selectbox("Enter Any restaurants", df_percent['name'].values)

if st.button("Recommend"):
      opt = f'{option}'
      recommendation=recommend(opt)
      for i in recommendation:
       st.write(i)

# if __name__ == '__main__':
#     print(', '.join(df_percent['name'].to_list()))
#     x = input('Enter: ')
#     print(recommend(x))
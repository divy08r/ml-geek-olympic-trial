import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px



medal = pd.read_csv('file.csv')
medal.head()

st.set_page_config(page_title="Olympic Fit", page_icon='🎗')

page_bg_img = '''
<style>
body {
background-image: url("https://w0.peakpx.com/wallpaper/666/49/HD-wallpaper-olympic-basketball-player-art-beautiful-olympic-artwork-basketball-1916-painting-summer-wide-screen-sports.jpg");
background-size: cover;
}
</style>
'''
set_bg_image = """
      <style>
        [data-testid="stAppViewContainer"] {
            background-image: url('https://cdn1.vectorstock.com/i/1000x1000/08/40/a-decorative-border-from-abstract-colorful-vector-25950840.jpg');
            background-repeat: no-repeat;
            background-size: cover;
        }
        [data-testid="block-container"]{
            background-color: white;
            padding: 3rem 1rem 5rem;
        }
        [data-testid="stMarkdownContainer"]{
            background-color: whitesmoke;
            padding: 0.2rem 0.5rem 0rem;
            margin-bottom: 0.1rem
        }
        .header-img{
            height: 4rem;
            width: 100%;
        }
      </style>
      """
st.markdown(set_bg_image,unsafe_allow_html=True)
st.title('Olympics Medals Analysis')


#sidebar start
st.sidebar.image("https://thumbs.dreamstime.com/b/sports-logo-23077124.jpg", 
             use_column_width=True,
)
st.sidebar.markdown(
    "[Home](www.google.com)"
)
st.sidebar.markdown(
    "[Health Predictor](www.google.com)"
)
# sidebar end

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

st.markdown(
    '''
    <img class="header-img" src="https://library.olympics.com/default/basicimagedownload.ashx?itemGuid=4C1C8DEE-9DE9-4954-A578-0628935017D0" alt="">
    ''',
unsafe_allow_html=True
)
# medal.info()

# medal.describe()

s1 = medal.country_name.value_counts()

new1 = pd.DataFrame({'country_name' : s1.index , 'count' : s1.values})

fig = px.scatter_geo(new1,locations='country_name',locationmode='country names',
                    size="count",color='country_name',title="Country with Medal counts"
                    )


with st.container():
    st.subheader('Performing Data Analysis and Data Visualization')
    st.plotly_chart(fig)


# fig.show()


st.subheader("Types of medals")
s2 = medal.medal_type.value_counts()
s2

new2 = pd.DataFrame({'medal_type' : s2.index , 'count' : s2.values})
new2

st.subheader("Different medal type won")
fig1 = px.pie(new2, values='count', names='medal_type', title='', color='medal_type',hole=0.7,
              color_discrete_map={'GOLD':'gold',
                                 'BRONZE':'brown',
                                 'SILVER':'silver'})
fig1.add_annotation(dict(x=0.5, y=0.5,  align='center',
                        xref = "paper", yref = "paper",
                        showarrow = False, font_size=22,
                        text="Medals"))

st.plotly_chart(fig1)


st.subheader('Types of Events')
s3= medal.event_title.value_counts()

new3 = pd.DataFrame({'event_title' : s3.index , 'players' : s3.values})
new3

df3 = new3[new3['players'] > 100]
df3

fig2 = px.pie(df3, values='players', names='event_title', title='')
st.plotly_chart(fig2)

st.subheader('Discipline')
s4 = medal.discipline_title.value_counts()
s4

new4 = pd.DataFrame({'Discipline' : s4.index , 'players' : s4.values})
new4

df4 = new4[new4['players'] > 100]
df4

fig4 = px.bar(df4 , x = 'Discipline' , y ='players' , title='Players according to Discipline')
st.plotly_chart(fig4)

men_medal = medal[medal['event_title'].str.contains(" men")]
men_medal

women_medal = medal[medal['event_title'].str.contains("women")]
women_medal

event_mixed = medal[medal['event_title'].str.contains("mixed")]
event_mixed


m = men_medal.count()
w = women_medal.count()
em = event_mixed.count()

list1 = ["Men Medals" , "Women Medals" , "Mixed Medals"];
list2 = [m.discipline_title,w.discipline_title,em.discipline_title]
df5 = pd.DataFrame(list(zip(list1,list2)),columns=["gender" , "Number of Player"])
df5

fig3 = px.pie(df5, values='Number of Player', names='gender', title='Medals respect to Gender' , hole=0.7)
fig3.add_annotation(dict(x=0.5, y=0.3,  align='center',
                        xref = "paper", yref = "paper",
                        showarrow = False, font_size=22,
                        text="Gender"))
fig3.add_layout_image(
    dict(
        source="https://i.imgur.com/3Cab96Z.jpg",
        xref="paper", yref="paper",
        x=0.48, y=0.48,
        sizex=0.3, sizey=0.25,
        xanchor="right", yanchor="bottom", sizing= "contain",
    )
)
fig3.add_layout_image(
    dict(
        source="https://i.imgur.com/c6QKoDy.jpg",
        xref="paper", yref="paper",
        x=0.55, y=0.48,
        sizex=0.3, sizey=0.25,
        xanchor="right", yanchor="bottom", sizing= "contain",
    ))

st.plotly_chart(fig3)
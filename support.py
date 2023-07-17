
medal = pd.read_csv('file.csv')
medal.head()
s1 = medal.country_name.value_counts()
#################################################################################################
new1 = pd.DataFrame({'country_name' : s1.index , 'count' : s1.values})
new1 = new1[:20]
df_styled = new1.style.background_gradient()
df_styled.export_png('static/plotly_images/new1.png')
fig = px.scatter_geo(new1,locations='country_name',locationmode='country names',
                    size="count",color='country_name',title="Country with Medal counts"
                    )
fig.write_image("static/plotly_images/fig.jpeg")
#################################################################################################
s2 = medal.medal_type.value_counts()
new2 = pd.DataFrame({'medal_type' : s2.index , 'count' : s2.values})
df_styled2 = new2.style.background_gradient()
df_styled2.export_png('static/plotly_images/new2.png')
fig1 = px.pie(new2, values='count', names='medal_type', title='', color='medal_type',hole=0.7,
              color_discrete_map={'GOLD':'gold',
                                 'BRONZE':'brown',
                                 'SILVER':'silver'})
fig1.add_annotation(dict(x=0.5, y=0.5,  align='center',
                        xref = "paper", yref = "paper",
                        showarrow = False, font_size=22,
                        text="Medals"))
fig1.write_image("static/plotly_images/fig1.jpeg")
#################################################################################################
s3= medal.event_title.value_counts()
new3 = pd.DataFrame({'event_title' : s3.index , 'players' : s3.values})
df3 = new3[new3['players'] > 100]
df_styled2 = df3.style.background_gradient()
df_styled2.export_png('static/plotly_images/new3.png')
fig2 = px.pie(df3, values='players', names='event_title', title='')
fig2.write_image("static/plotly_images/fig2.jpeg")
#################################################################################################
s4 = medal.discipline_title.value_counts()

new4 = pd.DataFrame({'Discipline' : s4.index , 'players' : s4.values})
df4 = new4[new4['players'] > 100]
df41 = df4[: 20]
df42 = df4[20 :]
df_styled4 = df41.style.background_gradient()
df_styled4.export_png('static/plotly_images/new4.png')
df_styled42 = df42.style.background_gradient()
df_styled42.export_png('static/plotly_images/new42.png')
fig4 = px.bar(df4 , x = 'Discipline' , y ='players' , title='Players according to Discipline')
fig4.write_image("static/plotly_images/fig4.jpeg")
#################################################################################################
men_medal = medal[medal['event_title'].str.contains(" men")]
women_medal = medal[medal['event_title'].str.contains("women")]
event_mixed = medal[medal['event_title'].str.contains("mixed")]
m = men_medal.count()
w = women_medal.count()
em = event_mixed.count()
list1 = ["Men Medals" , "Women Medals" , "Mixed Medals"]
list2 = [m.discipline_title,w.discipline_title,em.discipline_title]
df5 = pd.DataFrame(list(zip(list1,list2)),columns=["gender" , "Number of Player"])
df_styled42 = df5.style.background_gradient()
df_styled42.export_png('static/plotly_images/new5.png')
fig5 = px.pie(df5, values='Number of Player', names='gender', title='Medals respect to Gender' , hole=0.7)
fig5.add_annotation(dict(x=0.5, y=0.3,  align='center',
                        xref = "paper", yref = "paper",
                        showarrow = False, font_size=22,
                        text="Gender"))
fig5.add_layout_image(
    dict(
        source="https://i.imgur.com/3Cab96Z.jpg",
        xref="paper", yref="paper",
        x=0.48, y=0.48,
        sizex=0.3, sizey=0.25,
        xanchor="right", yanchor="bottom", sizing= "contain",
    )
)
fig5.add_layout_image(
    dict(
        source="https://i.imgur.com/c6QKoDy.jpg",
        xref="paper", yref="paper",
        x=0.55, y=0.48,
        sizex=0.3, sizey=0.25,
        xanchor="right", yanchor="bottom", sizing= "contain",
    )
)
fig5.write_image("static/plotly_images/fig5.jpeg")
#################################################################################################


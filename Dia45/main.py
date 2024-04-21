from bs4 import BeautifulSoup
import requests

#with open("./Dia45/website.html", encoding="utf-8") as file:
#    content=file.read()

#soup=BeautifulSoup(content, "html.parser")

#all_anchor_tags=soup.find_all(name="a")

#for tag in all_anchor_tags:
#    #print(tag.get("href"))
#    pass

#heading=soup.find(name="h1", id="name")
#print(heading)

#section_heading=soup.find(name="h3", class_="heading")
#print(section_heading)

#company_name=soup.select_one(selector="p a")
#print(company_name)


#response=requests.get("https://news.ycombinator.com/")
#yc_web=response.text

#soup=BeautifulSoup(yc_web, "html.parser")


#news_titles=soup.find(name="span", class_="titleline")
#anchor_news=news_titles.find(name="a")
#print(anchor_news.text)
#article_text=anchor_news.getText()
#article_link=anchor_news.get("href")
#print(article_link)
#article_upvote=soup.find(name="span", class_="score").getText()
#print(article_upvote)

#articles=soup.find_all(name="span", class_="titleline")
#article_texts=[]
#article_links=[]
#
#for article_tag in articles:
#    text=article_tag.getText()
#    article_texts.append(text)
#    
#    anchor_tag=article_tag.find("a")
#    
#    link=anchor_tag.get("href")
#    article_links.append(link)
#
#
#articles_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#largest_number=max(articles_upvotes)
#largest_index=articles_upvotes.index(largest_number)
#
#print(article_links[largest_index])
#print(article_texts[largest_index])
#print(articles_upvotes[largest_index])






response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_rank=response.text
soup=BeautifulSoup(movies_rank, "html.parser")
titles_html=soup.find_all(name="h3", class_="title")
movies=[]

for title in titles_html:
    text=title.getText()
    movies.append(text)

movies.reverse()

with open("./Dia45/movie_rank.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie} \n")
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

### Je résume dans une fonction le ***scrapping du sommaire*** (pour l'appliquer après à chaque article) :
def scrap_sommaire(url, sub_url):
    sub_page = requests.get(url+sub_url)
    soup = bs(sub_page.content,'html.parser')
    sommaire = soup.select(".toc__menu") # class concernant le Sommaire

    sommaire_dict = {'Sommaire':[]}
    for list in sommaire[0]:
        if list.ul:
            sommaire_dict['Sommaire'].append(list.find("a").get_text())
            for sublist in list.ul:
                sommaire_dict['Sommaire'].append(sublist.find("a").get_text())
        else:
            sommaire_dict['Sommaire'].append(list.find("a").get_text())

    return pd.DataFrame(sommaire_dict)

### Boucle sur **CHAQUE ARTICLE** de la page principale :
### on stocke le titre, l'URL, la description, le temps de lecture, ET le sommaire en format DataFrame Pandas (autre méthode possible)
welcome_url = "https://www.charlesbordet.com"
welcome_page = requests.get(welcome_url+"/fr/blog/")
welcome_soup = bs(welcome_page.content, 'html.parser')

liste_articles = welcome_soup.select(".list__item")             #rassemble TOUS les articles de la page principale
article_titles = welcome_soup.select(".archive__item-title")    #rassemble les titres avec url de chaque article

articles_infos = []
for i in range(len(article_titles)):    #on boucle sur le nombre d'article recensé dans la page d'accueil

    title = article_titles[i].find("a").get_text()
    description = liste_articles[i].select(".archive__item-excerpt")[0].text
    reading_time = liste_articles[i].select(".page__meta")[0].get_text().strip()
    sub_url = article_titles[i].find("a").get("href")
    sommaire = scrap_sommaire(welcome_url, sub_url) # fonction 'scrap_sommaire' qui boucle sur les url
    articles_infos.append({'Title': title,
                           'Description': description,
                           'Temps de lecture': reading_time,
                           'URL': sub_url,
                           'Sommaire': sommaire})

print(articles_infos) #liste de dictionnaires contenant 'Titre/Description/url'

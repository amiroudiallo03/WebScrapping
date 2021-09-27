from bs4 import BeautifulSoup
import requests




def scrap_worldfoot():


    url = "https://www.worldfootball.net"


    def get_detail(detail_url):
        
        """
        Fonction permettant de scrapper la description de l'article 
        """
        detail = ""
        reponse = requests.get(detail_url)
        if reponse.ok:
            soup = BeautifulSoup(reponse.text, 'html.parser')
            detail = soup.find('div',{"class": 'wfb-news-content'})
            
            return detail.text


    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        football = soup.find('div',{'class':'wfb-news-list-home'})
        foots = football.find('div',{'class':'module module-newmon module-newmon-default'})
        for i in range(1, 11):
            item = foots.findAll('div',{'class': f'item item_{i}'})
            #lien =  item.find('div',{'class': 'module-newmon-content'})
            for item_ in item:
                link = item_.find('a')
                link_ = link['href']
                title = item_.find('h4')
                image = item_.find('img')
                date_publication = item_.find('time')
                detail_url = url + link_
                get_detail(detail_url)
                print(url+link['href']+ 'le titre est:', title.text, image['src'], date_publication.text, get_detail(detail_url))

if __name__ == '__main__':
    scrap_worldfoot()















#url = "https://www.vice.com/fr"

#response = requests.get(url)

#soup = BeautifulSoup(response.text, 'html.parser')
#dic = {}
# article = soup.find('div', {'class': 'vice-
# '})
# for i in article:
#     # lien_div = article.find('div', {'class': 'vice-card-rubric vice-card-rubric--dark vice-card__vice-card-rubric'})
#     # lien = lien_div.find('a')
#     paragraphe = i.find('p', {'class': 'vice-card-dek vice-card-dek--dark vice-card__vice-card-dek'})
#     titre = i.find('h3')


#     #dic['lien'] = "https://www.vice.com/fr" + lien['href']
#     dic['paragraphe'] = paragraphe
#     dic['titre'] = titre

# categorie = soup.find('ul', {'class': 'nav-bar__title-bar-links'})
 
# new_item = []
# lien = categorie.findAll('li', {'class': 'nav-bar__title-bar-links__primary-link'})
# lien2 = categorie.findAll('li', {'class': 'nav-bar__title-bar-links__secondary-link'})
# for element in lien:
#     dic = {}
#     link = element.a['href']
#     link_name = element.a.text
#     dic['lien'] = link 
#     dic['category'] = link_name
#     new_item.append(dic)

# for i in lien2:
#     dico = {}
#     link = i.a['href']
#     link_name = i.a.text
#     dico['lien'] = link 
#     dico['category'] = link_name
#     new_item.append(dico)tyuioupyteyuiozpn^nn 





        #print(item)
    #print(foots)
    

# parent = soup.find('section', {'class': 'homepage-latest'})

# article_all = parent.find('div',{'class':'latest-feed'})

# for element in article_all:
#     dic = {}
#     article = element.find('div',{'class':'feed'})
#     dic['article': article]
#     dico.append(dic)


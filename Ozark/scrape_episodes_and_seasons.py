from selenium import webdriver
import pandas as pd

class Ozark:      

    def wikipedia(self, url):

        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files\chromedriver.exe')

        self.driver.get(url)

        overall_id = range(30)
        director_list = []

        # Needs updating
        directors = self.driver.find_elements_by_xpath('//td[@style="text-align:center"]')[3:121:4]
        for director in directors:
            director_list.append(director.text)

        self.driver.close()

        self.df_wiki = pd.DataFrame({'overall_id': overall_id, 'director': director_list})

    def imdb(self, url):

        self.driver = webdriver.Chrome(executable_path=r'C:\Program Files\chromedriver.exe')

        season_numbers = []
        episode_numbers = []
        rating_numbers = []
        episode_titles = []
        release_date = []
        synopsis_list = []

        # Needs updatings
        for season in range(1, 4):
            self.driver.get(url + str(season))

            #Episodes and seasons
            episode_nums = self.driver.find_elements_by_xpath('//td[@class="text-center"]')[::2]
            for episode_num in episode_nums:
                season_numbers.append(season)
                episode_numbers.append(episode_num.text)

            # Rating
            rating_nums = self.driver.find_elements_by_xpath('//td[@class="text-center"]')[1::2]
            for rating in rating_nums:
                rating_numbers.append(rating.text)

            # Synopsis
            synopsis_nums = self.driver.find_elements_by_xpath('//span[@class="text-lightf"]')[1::2]
            for synopsis in synopsis_nums:
                synopsis_list.append(synopsis.text)

            # Episode titles
            titles = self.driver.find_elements_by_xpath('//span[@class="text-large1"]')
            for title in titles:
                episode_titles.append(title.text)

            # Release dates
            dates = self.driver.find_elements_by_xpath('//span[@class="text-lightf"]')[::2]
            for date in dates:
                release_date.append(date.text)

        self.driver.close()

        self.df_imdb = pd.DataFrame({'season': season_numbers, 
                        'episode_num': episode_numbers,
                        'imdb_rating': rating_numbers, 
                        'title': episode_titles, 
                        'release_date': release_date,
                        'synopsis': synopsis_list})

    def clean_data(self):

        df = self.df_imdb.merge(self.df_wiki, how = 'inner', left_index = True, right_on = 'overall_id')
        df['release_date'] = df['release_date'].str.replace('(', '')
        df['release_date'] = df['release_date'].str.replace(')', '')
        df['release_date'] = df['release_date'].str.replace('.', '')
        df['release_date'] = pd.to_datetime(df['release_date'], format='%d %b %Y')
        df['synopsis'] = df['synopsis'].str.replace(',', ';')
        df['episode_id'] = df['season'].astype(str) + '_' + df['episode_num'].astype(str)
        df['season_id'] = df['season'].astype(str)
        df.to_csv(r'C:\Users\bezlui\Documents\Python\Flask\Ozark\IMDB.csv', index = False, sep = '|')

if __name__ == "__main__":
    ozark = Ozark()
    ozark.wikipedia('https://en.wikipedia.org/wiki/Ozark_(TV_series)#Episodes')
    ozark.imdb('https://imdb-api.com/episodes/tt5071412/')
    ozark.clean_data()



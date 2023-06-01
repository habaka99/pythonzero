import requests
standing_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
data = requests.get(standing_url)
rom bs4 import BeautifulSoup
soup = BeautifulSoup(data.text)
standing_table = soup.select("table.stats_table")[0]
links  = standing_table.find_all("a")
links = [l.get("href") for l in links]
links = [l for l in links if '/squads/' in l]
links
['/en/squads/b8fd03ef/Manchester-City-Stats',
 '/en/squads/822bd0ba/Liverpool-Stats',
 '/en/squads/cff3d9bb/Chelsea-Stats',
 '/en/squads/361ca564/Tottenham-Hotspur-Stats',
 '/en/squads/18bb7c10/Arsenal-Stats',
 '/en/squads/19538871/Manchester-United-Stats',
 '/en/squads/7c21e445/West-Ham-United-Stats',
 '/en/squads/a2d435b3/Leicester-City-Stats',
 '/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats',
 '/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats',
 '/en/squads/b2b47a98/Newcastle-United-Stats',
 '/en/squads/47c64c55/Crystal-Palace-Stats',
 '/en/squads/cd051869/Brentford-Stats',
 '/en/squads/8602292d/Aston-Villa-Stats',
 '/en/squads/33c895d4/Southampton-Stats',
 '/en/squads/d3fd31cc/Everton-Stats',
 '/en/squads/5bfb9659/Leeds-United-Stats',
 '/en/squads/943e8050/Burnley-Stats',
 '/en/squads/2abfe087/Watford-Stats',
 '/en/squads/1c781004/Norwich-City-Stats']
 team_urls = [f"https://fbref.com{l}" for l in links]
team_urls 
['https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats',
 'https://fbref.com/en/squads/822bd0ba/Liverpool-Stats',
 'https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats',
 'https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats',
 'https://fbref.com/en/squads/18bb7c10/Arsenal-Stats',
 'https://fbref.com/en/squads/19538871/Manchester-United-Stats',
 'https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats',
 'https://fbref.com/en/squads/a2d435b3/Leicester-City-Stats',
 'https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats',
 'https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats',
 'https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats',
 'https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats',
 'https://fbref.com/en/squads/cd051869/Brentford-Stats',
 'https://fbref.com/en/squads/8602292d/Aston-Villa-Stats',
 'https://fbref.com/en/squads/33c895d4/Southampton-Stats',
 'https://fbref.com/en/squads/d3fd31cc/Everton-Stats',
 'https://fbref.com/en/squads/5bfb9659/Leeds-United-Stats',
 'https://fbref.com/en/squads/943e8050/Burnley-Stats',
 'https://fbref.com/en/squads/2abfe087/Watford-Stats',
 'https://fbref.com/en/squads/1c781004/Norwich-City-Stats']
team_url = team_urls[0]
ata = requests.get(team_url)
import pandas as pd
matches = pd.read_html(data.text, match = "Scores & Fixtures")
matches[0].head()
oup = BeautifulSoup(data.text)
links = soup.find_all("a")
links = [l.get("href") for l in links]
links = [l for l in links if l and "all_comps/shooting/" in l]
links
['/en/squads/b8fd03ef/2021-2022/matchlogs/all_comps/shooting/Manchester-City-Match-Logs-All-Competitions',
 '/en/squads/b8fd03ef/2021-2022/matchlogs/all_comps/shooting/Manchester-City-Match-Logs-All-Competitions',
 '/en/squads/b8fd03ef/2021-2022/matchlogs/all_comps/shooting/Manchester-City-Match-Logs-All-Competitions',
 '/en/squads/b8fd03ef/2021-2022/matchlogs/all_comps/shooting/Manchester-City-Match-Logs-All-Competitions']
data = requests.get(f"https://fbref.com{links[0]}")
shooting = pd.read_html(data.text, match = "Shooting")[0]
shooting.head()
shooting.columns = shooting.columns.droplevel()
shooting.head()
team_data = matches[0].merge(shooting[["Date", "Sh", "SoT", "Dist","FK", "PK", "PKatt"]], on = "Date")
team_data.head()
matches[0].shape
(58, 19)
shooting.shape
(59, 26)
team_data.shape
(58, 25)
years = list(range(2022,2020, -1))
years
[2022, 2021]
all_matches = []
standing_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
import time
for year in years:
    data = requests.get(standing_url)
    soup = BeautifulSoup(data.text)
    standing_table = soup.select("table.stats_table")[0]
    
    links = standing_table.find_all("a")
    links = [l.get("href") for l in links]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in links]
    
    previous_season = soup.select("a.prev")[0].get("href")
    standing_url = f"https://fbref.com/{previous_season}"
    
    for team_url in team_urls:
        team_name = team_url.split("/")[-1].replace("-Stats","").replace("-"," ")
        
        data = requests.get(team_url)
        matches = pd.read_html(data.text, match = "Scores & Fixtures")[0]
        
        soup = BeautifulSoup(data.text)
        links = soup.find_all("a")
        links = [l.get("href") for l in links]
        links = [l for l in links if l and "all_comps/shooting/" in l]
        data = requests.get(f"https://fbref.com{links[0]}")
        shooting = pd.read_html(data.text, match = "Shooting")[0]
        shooting.columns = shooting.columns.droplevel()
        
        try:
            team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist","FK", "PK", "PKatt"]], on = "Date")
        except ValueError:
            continue
            
        team_data = team_data[team_data["Comp"] == "Premier League"]
        team_data["Season"] = year
        team_data["Team"] = team_name
        all_matches.append(team_data)
        time.sleep(1)

     
            
team_url.split("/")[-1].replace("-Stats","").replace("-"," ")
'Manchester City'
match_df = pd.concat(all_matches)
match_df.columns = [c.lower() for c in match_df.columns]
match_df.to_csv("matches.csv")
match_df.head()
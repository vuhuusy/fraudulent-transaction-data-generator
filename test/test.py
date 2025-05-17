import requests

def fetch_zip_demographics(self, zip_code):
    if zip_code in ZIP_DEMOGRAPHIC_CACHE:
        return ZIP_DEMOGRAPHIC_CACHE[zip_code]

    API_KEY = 'af02c5077ec45d51b3613b71192cfd77e380c910'
    url = 'https://api.census.gov/data/2021/acs/acs5'
    params = {
        'get': 'B19013_001E,B01003_001E,B01002_001E,B25010_001E',
        'for': f'zip code tabulation area:{zip_code}',
        'key': API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            values = data[1]
            demographic = {
                'median_income': values[0],
                'total_population': values[1],
                'median_age': values[2],
                'avg_household_size': values[3]
            }
        else:
            demographic = {'median_income': '', 'total_population': '', 'median_age': '', 'avg_household_size': ''}
    except:
        demographic = {'median_income': '', 'total_population': '', 'median_age': '', 'avg_household_size': ''}

    ZIP_DEMOGRAPHIC_CACHE[zip_code] = demographic
    return demographic

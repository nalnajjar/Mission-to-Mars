{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dependencies\n",
    "import pandas as pd\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "executable_path = {\"executable_path\": \"/usr/local/bin/chromedriver\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "# NASA News on Mars\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)\n",
    "\n",
    "# HTML\n",
    "html = browser.html\n",
    "\n",
    "# Parse with BS\n",
    "news_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Mars 2020 Rover Goes Coast-to-Coast to Prep for Launch\n",
      "The agency's first step in returning rocks from Mars just arrived at Kennedy Space Center. The Mars 2020 team now begins readying for a launch to the Red Planet this July.\n"
     ]
    }
   ],
   "source": [
    "# Latest Mars Article Title & Text\n",
    "news_title = news_soup.find(\"div\", class_=\"content_title\").find('a').text\n",
    "news_p = news_soup.find(\"div\", class_=\"article_teaser_body\").text.strip()\n",
    "\n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23707-640x350.jpg\n"
     ]
    }
   ],
   "source": [
    "# JPL Mars Images\n",
    "featured_image_url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(featured_image_url)\n",
    "\n",
    "# HTML\n",
    "html_image = browser.html\n",
    "\n",
    "# Parse with BS\n",
    "image_soup = BeautifulSoup(html_image, 'html.parser')\n",
    "\n",
    "# Pull Image\n",
    "image = soup.find(\"img\", class_=\"thumb\")[\"src\"]\n",
    "featured_image_url = \"https://www.jpl.nasa.gov\" + image\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'text'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-73-6f26b0f99ffc>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mhtml_weather\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhtml\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0msoup\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBeautifulSoup\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhtml_weather\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"html.parser\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0mmars_weather\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msoup\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"p\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m \u001b[0;31m#refuses to acknowledge text\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmars_weather\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'text'"
     ]
    }
   ],
   "source": [
    "# Pull Mars Weather from Latest Tweet\n",
    "url_weather = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(url_weather)\n",
    "\n",
    "html_weather = browser.html\n",
    "soup = BeautifulSoup(html_weather, \"html.parser\")\n",
    "\n",
    "mars_weather = soup.find(\"p\", class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\").text #refuses to acknowledge text\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Scrape Mars Facts\n",
    "url_facts = \"https://space-facts.com/mars/\"\n",
    "table = pd.read_html(url_facts)\n",
    "table[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Answer</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fact</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Answer\n",
       "Fact                                               \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create Dataframe \n",
    "df_mars_facts = table[0]\n",
    "df_mars_facts.columns = [\"Fact\", \"Answer\"]\n",
    "df_mars_facts.set_index([\"Fact\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>Fact</th>      <th>Answer</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Equatorial Diameter:</td>      <td>6,792 km</td>    </tr>    <tr>      <th>1</th>      <td>Polar Diameter:</td>      <td>6,752 km</td>    </tr>    <tr>      <th>2</th>      <td>Mass:</td>      <td>6.39 × 10^23 kg (0.11 Earths)</td>    </tr>    <tr>      <th>3</th>      <td>Moons:</td>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>4</th>      <td>Orbit Distance:</td>      <td>227,943,824 km (1.38 AU)</td>    </tr>    <tr>      <th>5</th>      <td>Orbit Period:</td>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>6</th>      <td>Surface Temperature:</td>      <td>-87 to -5 °C</td>    </tr>    <tr>      <th>7</th>      <td>First Record:</td>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>8</th>      <td>Recorded By:</td>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert to HTML Table String\n",
    "mars_html_table = df_mars_facts.to_html()\n",
    "mars_html_table = mars_html_table.replace(\"\\n\", \"\")\n",
    "mars_html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the USGS Site\n",
    "usgs_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(usgs_url)\n",
    "\n",
    "# To Collect URLs\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# Get a List of All the Hemispheres\n",
    "links = browser.find_by_css(\"a.product-item h3\")\n",
    "for item in range(len(links)):\n",
    "    hemisphere = {}\n",
    "    \n",
    "    # Find Element on Each Loop to Avoid a Stale Element Exception\n",
    "    browser.find_by_css(\"a.product-item h3\")[item].click()\n",
    "    \n",
    "    # Find Sample Image Anchor Tag & Extract <href>\n",
    "    sample_element = browser.find_link_by_text(\"Sample\").first\n",
    "    hemisphere[\"img_url\"] = sample_element[\"href\"]\n",
    "    \n",
    "    # Get Hemisphere Title\n",
    "    hemisphere[\"title\"] = browser.find_by_css(\"h2.title\").text\n",
    "    \n",
    "    # Append Hemisphere Object to List\n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "    \n",
    "    # Navigate Backwards\n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Display List\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "null",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

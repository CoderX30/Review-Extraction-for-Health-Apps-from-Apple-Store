#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install app_store_scraper 


# In[1]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

apple_health = AppStore(country="us", app_name='apple-health', app_id = '1242545199')

apple_health.review(how_many=2000)


# In[2]:


apple_health.reviews


# In[3]:


apple_health_df = pd.DataFrame(np.array(apple_health.reviews),columns=['review'])
apple_health_df2 = apple_health_df.join(pd.DataFrame(apple_health_df.pop('review').tolist()))
apple_health_df2["Country"] = 'US'
apple_health_df2.head()


# In[4]:


apple_health_df2.to_csv('apple_health_US_reviews.csv', index=False)


# ----------------------------------------------------------------------------------

# In[5]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

apple_health = AppStore(country="gb", app_name='apple-health', app_id = '1242545199')

apple_health.review(how_many=2000)


# In[6]:


apple_health.reviews


# In[7]:


apple_health_df = pd.DataFrame(np.array(apple_health.reviews),columns=['review'])
apple_health_df2 = apple_health_df.join(pd.DataFrame(apple_health_df.pop('review').tolist()))
apple_health_df2["Country"] = 'GB'
apple_health_df2.head()


# In[8]:


apple_health_df2.to_csv('apple_health_UK_reviews.csv', index=False)


# ----------------------------------------------------------------------------------

# In[9]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

apple_health = AppStore(country="au", app_name='apple-health', app_id = '1242545199')

apple_health.review(how_many=2000)


# In[10]:


apple_health.reviews


# In[11]:


apple_health_df = pd.DataFrame(np.array(apple_health.reviews),columns=['review'])
apple_health_df2 = apple_health_df.join(pd.DataFrame(apple_health_df.pop('review').tolist()))
apple_health_df2["Country"] = 'AUS'
apple_health_df2.head()


# In[12]:


apple_health_df2.to_csv('apple_health_AUS_reviews.csv', index=False)


# -------------------

# In[13]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

apple_health = AppStore(country="ca", app_name='apple-health', app_id = '1242545199')

apple_health.review(how_many=2000)


# In[14]:


apple_health.reviews


# In[15]:


apple_health_df = pd.DataFrame(np.array(apple_health.reviews),columns=['review'])
apple_health_df2 = apple_health_df.join(pd.DataFrame(apple_health_df.pop('review').tolist()))
apple_health_df2["Country"] = 'CAN'
apple_health_df2.head()


# In[16]:


apple_health_df2.to_csv('apple_health_CAN_reviews.csv', index=False)


# -----------

# In[17]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

apple_health = AppStore(country="IN", app_name='apple-health', app_id = '1242545199')

apple_health.review(how_many=2000)


# In[18]:


apple_health.reviews


# In[19]:


apple_health_df = pd.DataFrame(np.array(apple_health.reviews),columns=['review'])
apple_health_df2 = apple_health_df.join(pd.DataFrame(apple_health_df.pop('review').tolist()))
apple_health_df2["Country"] = 'IND'
apple_health_df2.head()


# In[20]:


apple_health_df2.to_csv('apple_health_IND_reviews.csv', index=False)


# ## ----------------------------------------------------------------------------------------------------------------------------

# # Heartify

# In[21]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heartify = AppStore(country="us", app_name='heartify-heart-health-monitor', app_id = '1546156891')

heartify.review(how_many=2000)


# In[22]:


heartify.reviews


# In[23]:


heartify_df = pd.DataFrame(np.array(heartify.reviews),columns=['review'])
heartify_df2 = heartify_df.join(pd.DataFrame(heartify_df.pop('review').tolist()))
heartify_df2["Country"] = 'US'
heartify_df2.head()


# In[24]:


heartify_df2.to_csv('Heartify_US_reviews.csv', index=False)


# ---------

# In[25]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heartify = AppStore(country="gb", app_name='heartify-heart-health-monitor', app_id = '1546156891')

heartify.review(how_many=2000)


# In[26]:


heartify.reviews


# In[27]:


heartify_df = pd.DataFrame(np.array(heartify.reviews),columns=['review'])
heartify_df2 = heartify_df.join(pd.DataFrame(heartify_df.pop('review').tolist()))
heartify_df2["Country"] = 'UK'
heartify_df2.head()


# In[28]:


heartify_df2.to_csv('Heartify_UK_reviews.csv', index=False)


# -------------

# In[29]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heartify = AppStore(country="au", app_name='heartify-heart-health-monitor', app_id = '1546156891')

heartify.review(how_many=2000)


# In[30]:


heartify.reviews


# In[31]:


heartify_df = pd.DataFrame(np.array(heartify.reviews),columns=['review'])
heartify_df2 = heartify_df.join(pd.DataFrame(heartify_df.pop('review').tolist()))
heartify_df2["Country"] = 'AUS'
heartify_df2.head()


# In[32]:


heartify_df2.to_csv('Heartify_AUS_reviews.csv', index=False)


# ----------------

# In[33]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heartify = AppStore(country="ca", app_name='heartify-heart-health-monitor', app_id = '1546156891')

heartify.review(how_many=2000)


# In[34]:


heartify.reviews


# In[35]:


heartify_df = pd.DataFrame(np.array(heartify.reviews),columns=['review'])
heartify_df2 = heartify_df.join(pd.DataFrame(heartify_df.pop('review').tolist()))
heartify_df2["Country"] = 'CAN'
heartify_df2.head()


# In[36]:


heartify_df2.to_csv('Heartify_CAN_reviews.csv', index=False)


# --------------

# In[38]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heartify = AppStore(country="in", app_name='heartify-heart-health-monitor', app_id = '1546156891')

heartify.review(how_many=2000)


# In[39]:


heartify.reviews


# In[40]:


heartify_df = pd.DataFrame(np.array(heartify.reviews),columns=['review'])
heartify_df2 = heartify_df.join(pd.DataFrame(heartify_df.pop('review').tolist()))
heartify_df2["Country"] = 'IND'
heartify_df2.head()


# In[41]:


heartify_df2.to_csv('Heartify_IND_reviews.csv', index=False)


# # -----------------------------------------------------------------------------------------------

# # Welltory

# In[44]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

welltory = AppStore(country="us", app_name='welltory-heart-rate-monitor', app_id = '1074367771')

welltory.review(how_many=2000)


# In[45]:


welltory.reviews


# In[46]:


welltory_df = pd.DataFrame(np.array(welltory.reviews),columns=['review'])
welltory_df2 = welltory_df.join(pd.DataFrame(welltory_df.pop('review').tolist()))
welltory_df2["Country"] = 'US'
welltory_df2.head()


# In[47]:


welltory_df2.to_csv('Welltory_US_reviews.csv', index=False)


# --------------

# In[48]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

welltory = AppStore(country="gb", app_name='welltory-heart-rate-monitor', app_id = '1074367771')

welltory.review(how_many=2000)


# In[49]:


welltory.reviews


# In[50]:


welltory_df = pd.DataFrame(np.array(welltory.reviews),columns=['review'])
welltory_df2 = welltory_df.join(pd.DataFrame(welltory_df.pop('review').tolist()))
welltory_df2["Country"] = 'UK'
welltory_df2.head()


# In[51]:


welltory_df2.to_csv('Welltory_UK_reviews.csv', index=False)


# -----------------

# In[53]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

welltory = AppStore(country="au", app_name='welltory-heart-rate-monitor', app_id = '1074367771')

welltory.review(how_many=2000)


# In[54]:


welltory.reviews


# In[55]:


welltory_df = pd.DataFrame(np.array(welltory.reviews),columns=['review'])
welltory_df2 = welltory_df.join(pd.DataFrame(welltory_df.pop('review').tolist()))
welltory_df2["Country"] = 'AUS'
welltory_df2.head()


# In[56]:


welltory_df2.to_csv('Welltory_AUS_reviews.csv', index=False)


# ----------------

# In[57]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

welltory = AppStore(country="ca", app_name='welltory-heart-rate-monitor', app_id = '1074367771')

welltory.review(how_many=2000)


# In[58]:


welltory.reviews


# In[59]:


welltory_df = pd.DataFrame(np.array(welltory.reviews),columns=['review'])
welltory_df2 = welltory_df.join(pd.DataFrame(welltory_df.pop('review').tolist()))
welltory_df2["Country"] = 'CAN'
welltory_df2.head()


# In[60]:


welltory_df2.to_csv('Welltory_CAN_reviews.csv', index=False)


# --------------------------

# In[61]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

welltory = AppStore(country="in", app_name='welltory-heart-rate-monitor', app_id = '1074367771')

welltory.review(how_many=2000)


# In[62]:


welltory.reviews


# In[63]:


welltory_df = pd.DataFrame(np.array(welltory.reviews),columns=['review'])
welltory_df2 = welltory_df.join(pd.DataFrame(welltory_df.pop('review').tolist()))
welltory_df2["Country"] = 'IND'
welltory_df2.head()


# In[64]:


welltory_df2.to_csv('Welltory_IND_reviews.csv', index=False)


# # ----------------------------------------------------------------------------------------------

# # Heart Analyzer: Cardio Monitor

# In[65]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heart_analyzer = AppStore(country="us", app_name='heart-analyzer-cardio-monitor', app_id = '1006420410')

heart_analyzer.review(how_many=2000)


# In[66]:


heart_analyzer.reviews


# In[67]:


heart_analyzer_df = pd.DataFrame(np.array(heart_analyzer.reviews),columns=['review'])
heart_analyzer_df2 = heart_analyzer_df.join(pd.DataFrame(heart_analyzer_df.pop('review').tolist()))
heart_analyzer_df2["Country"] = 'US'
heart_analyzer_df2.head()


# In[68]:


heart_analyzer_df2.to_csv('Heart_Analyzer_US_reviews.csv', index=False)


# ------------------------

# In[69]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heart_analyzer = AppStore(country="gb", app_name='heart-analyzer-cardio-monitor', app_id = '1006420410')

heart_analyzer.review(how_many=2000)


# In[70]:


heart_analyzer.reviews


# In[71]:


heart_analyzer_df = pd.DataFrame(np.array(heart_analyzer.reviews),columns=['review'])
heart_analyzer_df2 = heart_analyzer_df.join(pd.DataFrame(heart_analyzer_df.pop('review').tolist()))
heart_analyzer_df2["Country"] = 'UK'
heart_analyzer_df2.head()


# In[72]:


heart_analyzer_df2.to_csv('Heart_Analyzer_UK_reviews.csv', index=False)


# -------------------------------

# In[73]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heart_analyzer = AppStore(country="au", app_name='heart-analyzer-cardio-monitor', app_id = '1006420410')

heart_analyzer.review(how_many=2000)


# In[74]:


heart_analyzer.reviews


# In[75]:


heart_analyzer_df = pd.DataFrame(np.array(heart_analyzer.reviews),columns=['review'])
heart_analyzer_df2 = heart_analyzer_df.join(pd.DataFrame(heart_analyzer_df.pop('review').tolist()))
heart_analyzer_df2["Country"] = 'AUS'
heart_analyzer_df2.head()


# In[76]:


heart_analyzer_df2.to_csv('Heart_Analyzer_AUS_reviews.csv', index=False)


# ---------------------

# In[77]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heart_analyzer = AppStore(country="ca", app_name='heart-analyzer-cardio-monitor', app_id = '1006420410')

heart_analyzer.review(how_many=2000)


# In[78]:


heart_analyzer.reviews


# In[79]:


heart_analyzer_df = pd.DataFrame(np.array(heart_analyzer.reviews),columns=['review'])
heart_analyzer_df2 = heart_analyzer_df.join(pd.DataFrame(heart_analyzer_df.pop('review').tolist()))
heart_analyzer_df2["Country"] = 'CAN'
heart_analyzer_df2.head()


# In[80]:


heart_analyzer_df2.to_csv('Heart_Analyzer_CAN_reviews.csv', index=False)


# ------------------------------

# In[81]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

heart_analyzer = AppStore(country="in", app_name='heart-analyzer-cardio-monitor', app_id = '1006420410')

heart_analyzer.review(how_many=2000)


# In[82]:


heart_analyzer.reviews


# In[83]:


heart_analyzer_df = pd.DataFrame(np.array(heart_analyzer.reviews),columns=['review'])
heart_analyzer_df2 = heart_analyzer_df.join(pd.DataFrame(heart_analyzer_df.pop('review').tolist()))
heart_analyzer_df2["Country"] = 'IND'
heart_analyzer_df2.head()


# In[84]:


heart_analyzer_df2.to_csv('Heart_Analyzer_IND_reviews.csv', index=False)


# # -----------------------------------------------------------------------------------

# #  AI Stress Monitor

# In[1]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

AI_Stress_Monitor = AppStore(country="us", app_name='stress-monitor-for-watch', app_id = '1510429086')

AI_Stress_Monitor.review(how_many=2000)


# In[2]:


AI_Stress_Monitor.reviews


# In[3]:


AI_Stress_Monitor_df = pd.DataFrame(np.array(AI_Stress_Monitor.reviews),columns=['review'])
AI_Stress_Monitor_df2 = AI_Stress_Monitor_df.join(pd.DataFrame(AI_Stress_Monitor_df.pop('review').tolist()))
AI_Stress_Monitor_df2["Country"] = 'US'
AI_Stress_Monitor_df2.head()


# In[4]:


AI_Stress_Monitor_df2.to_csv('AI_Stress_Monitor_US_reviews.csv', index=False)


# ----------------------------

# In[5]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

AI_Stress_Monitor = AppStore(country="gb", app_name='stress-monitor-for-watch', app_id = '1510429086')

AI_Stress_Monitor.review(how_many=2000)


# In[6]:


AI_Stress_Monitor.reviews


# In[7]:


AI_Stress_Monitor_df = pd.DataFrame(np.array(AI_Stress_Monitor.reviews),columns=['review'])
AI_Stress_Monitor_df2 = AI_Stress_Monitor_df.join(pd.DataFrame(AI_Stress_Monitor_df.pop('review').tolist()))
AI_Stress_Monitor_df2["Country"] = 'UK'
AI_Stress_Monitor_df2.head()


# In[8]:


AI_Stress_Monitor_df2.to_csv('AI_Stress_Monitor_UK_reviews.csv', index=False)


# -----------------------------

# In[9]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

AI_Stress_Monitor = AppStore(country="au", app_name='stress-monitor-for-watch', app_id = '1510429086')

AI_Stress_Monitor.review(how_many=2000)


# In[10]:


AI_Stress_Monitor.reviews


# In[11]:


AI_Stress_Monitor_df = pd.DataFrame(np.array(AI_Stress_Monitor.reviews),columns=['review'])
AI_Stress_Monitor_df2 = AI_Stress_Monitor_df.join(pd.DataFrame(AI_Stress_Monitor_df.pop('review').tolist()))
AI_Stress_Monitor_df2["Country"] = 'AUS'
AI_Stress_Monitor_df2.head()


# In[12]:


AI_Stress_Monitor_df2.to_csv('AI_Stress_Monitor_AUS_reviews.csv', index=False)


# ------------------------

# In[13]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

AI_Stress_Monitor = AppStore(country="ca", app_name='stress-monitor-for-watch', app_id = '1510429086')

AI_Stress_Monitor.review(how_many=2000)


# In[14]:


AI_Stress_Monitor.reviews


# In[15]:


AI_Stress_Monitor_df = pd.DataFrame(np.array(AI_Stress_Monitor.reviews),columns=['review'])
AI_Stress_Monitor_df2 = AI_Stress_Monitor_df.join(pd.DataFrame(AI_Stress_Monitor_df.pop('review').tolist()))
AI_Stress_Monitor_df2["Country"] = 'CAN'
AI_Stress_Monitor_df2.head()


# In[16]:


AI_Stress_Monitor_df2.to_csv('AI_Stress_Monitor_CAN_reviews.csv', index=False)


# ---------------------------

# In[38]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

AI_Stress_Monitor = AppStore(country="ind", app_name='stress-monitor-for-watch', app_id = '1510429086')

AI_Stress_Monitor.review(how_many=2000)


# In[18]:


AI_Stress_Monitor.reviews


# In[19]:


AI_Stress_Monitor_df = pd.DataFrame(np.array(AI_Stress_Monitor.reviews),columns=['review'])
AI_Stress_Monitor_df2 = AI_Stress_Monitor_df.join(pd.DataFrame(AI_Stress_Monitor_df.pop('review').tolist()))
AI_Stress_Monitor_df2["Country"] = 'IND'
AI_Stress_Monitor_df2.head()


# In[20]:


AI_Stress_Monitor_df2.to_csv('AI_Stress_Monitor_IND_reviews.csv', index=False)


# # --------------------------------------------------------------------------------------------------------

# In[31]:


import time
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

def fetch_reviews_with_backoff(app):
    retry_count = 0
    while retry_count < 5:  # Maximum number of retries
        try:
            app.review(how_many=5000)
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying after waiting...")
            time.sleep(2 ** retry_count)  # Wait using exponential backoff
            retry_count += 1

# Create an instance of AppStore
CardioBot = AppStore(country="us", app_name='cardiobot-heart-rate-monitor', app_id = '1149412984')

# Fetch reviews with exponential backoff
fetch_reviews_with_backoff(CardioBot)


# In[32]:


CardioBot.reviews


# In[33]:


CardioBot_df = pd.DataFrame(np.array(CardioBot.reviews),columns=['review'])
CardioBot_df2 = CardioBot_df.join(pd.DataFrame(CardioBot_df.pop('review').tolist()))
CardioBot_df2["Country"] = 'US'
CardioBot_df2.head()


# In[34]:


CardioBot_df2.to_csv('CardioBot_US_reviews.csv', index=False)


# ------------------------------

# In[36]:


import time
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

def fetch_reviews_with_backoff(app):
    retry_count = 0
    while retry_count < 5:  # Maximum number of retries
        try:
            app.review(how_many=5000)
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying after waiting...")
            time.sleep(2 ** retry_count)  # Wait using exponential backoff
            retry_count += 1

# Create an instance of AppStore
CardioBot = AppStore(country="gb", app_name='cardiobot-heart-rate-monitor', app_id = '1149412984')

# Fetch reviews with exponential backoff
fetch_reviews_with_backoff(CardioBot)


# In[36]:


CardioBot.reviews


# In[37]:


CardioBot_df = pd.DataFrame(np.array(CardioBot.reviews),columns=['review'])
CardioBot_df2 = CardioBot_df.join(pd.DataFrame(CardioBot_df.pop('review').tolist()))
CardioBot_df2["Country"] = 'UK'
CardioBot_df2.head()


# In[38]:


CardioBot_df2.to_csv('CardioBot_UK_reviews.csv', index=False)


# -----------------------------------------------

# In[37]:


import time
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

def fetch_reviews_with_backoff(app):
    retry_count = 0
    while retry_count < 5:  # Maximum number of retries
        try:
            app.review(how_many=5000)
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying after waiting...")
            time.sleep(2 ** retry_count)  # Wait using exponential backoff
            retry_count += 1

# Create an instance of AppStore
CardioBot = AppStore(country="au", app_name='cardiobot-heart-rate-monitor', app_id = '1149412984')

# Fetch reviews with exponential backoff
fetch_reviews_with_backoff(CardioBot)


# In[40]:


CardioBot.reviews


# In[41]:


CardioBot_df = pd.DataFrame(np.array(CardioBot.reviews),columns=['review'])
CardioBot_df2 = CardioBot_df.join(pd.DataFrame(CardioBot_df.pop('review').tolist()))
CardioBot_df2["Country"] = 'AUS'
CardioBot_df2.head()


# In[42]:


CardioBot_df2.to_csv('CardioBot_AUS_reviews.csv', index=False)


# -----------------------------

# In[43]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

CardioBot = AppStore(country="ca", app_name='cardiobot-heart-rate-monitor', app_id = '1149412984')

CardioBot.review(how_many=2000)


# In[44]:


CardioBot.reviews


# In[45]:


CardioBot_df = pd.DataFrame(np.array(CardioBot.reviews),columns=['review'])
CardioBot_df2 = CardioBot_df.join(pd.DataFrame(CardioBot_df.pop('review').tolist()))
CardioBot_df2["Country"] = 'CAN'
CardioBot_df2.head()


# In[46]:


CardioBot_df2.to_csv('CardioBot_CAN_reviews.csv', index=False)


# -----------------------------------

# In[34]:


import time
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

def fetch_reviews_with_backoff(app):
    retry_count = 0
    while retry_count < 5:  # Maximum number of retries
        try:
            app.review(how_many=5000)
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying after waiting...")
            time.sleep(2 ** retry_count)  # Wait using exponential backoff
            retry_count += 1

# Create an instance of AppStore
CardioBot = AppStore(country="ind", app_name='cardiobot-heart-rate-monitor', app_id = '1149412984')

# Fetch reviews with exponential backoff
fetch_reviews_with_backoff(CardioBot)


# In[35]:


CardioBot.reviews


# In[51]:


CardioBot_df = pd.DataFrame(np.array(CardioBot.reviews),columns=['review'])
CardioBot_df2 = CardioBot_df.join(pd.DataFrame(CardioBot_df.pop('review').tolist()))
CardioBot_df2["Country"] = 'IND'
CardioBot_df2.head()


# In[52]:


CardioBot_df2.to_csv('CardioBot_IND_reviews.csv', index=False)


# ---------------------

# In[54]:


import pandas as pd

df1 = pd.read_csv('CardioBot_US_reviews.csv')
df2 = pd.read_csv('CardioBot_UK_reviews.csv')
df3 = pd.read_csv('CardioBot_AUS_reviews.csv')
df4 = pd.read_csv('CardioBot_CAN_reviews.csv')
df5 = pd.read_csv('CardioBot_IND_reviews.csv')

# Concatenate the two DataFrames vertically
Cardiobot_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# Write the combined DataFrame to a new CSV file
Cardiobot_df.to_csv('Cardiobot.csv', index=False)


# # ----------------------------------------------------------------------------------------------------

# # Pillow: Sleep cycle tracker

# In[1]:


import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

Pillow = AppStore(country="us", app_name='pillow-sleep-cycle-tracker', app_id = '878691772')
Pillow.review(how_many=4000)


# In[2]:


Pillow.reviews


# In[3]:


Pillow_df = pd.DataFrame(np.array(Pillow.reviews),columns=['review'])
Pillow_df2 = Pillow_df.join(pd.DataFrame(Pillow_df.pop('review').tolist()))
Pillow_df2["Country"] = 'US'
Pillow_df2.head()


# In[4]:


Pillow_df2.to_csv('Pillow_US_reviews.csv', index=False)


# -------------------------

# In[16]:


import time
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

def fetch_reviews_with_backoff(app):
    retry_count = 0
    while retry_count < 5:  # Maximum number of retries
        try:
            app.review(how_many=5000)
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying after waiting...")
            time.sleep(2 ** retry_count)  # Wait using exponential backoff
            retry_count += 1

# Create an instance of AppStore
Pillow = AppStore(country="gb", app_name='pillow-sleep-cycle-tracker', app_id='878691772')

# Fetch reviews with exponential backoff
fetch_reviews_with_backoff(Pillow)


# In[17]:


Pillow.reviews


# In[18]:


Pillow_df = pd.DataFrame(np.array(Pillow.reviews),columns=['review'])
Pillow_df2 = Pillow_df.join(pd.DataFrame(Pillow_df.pop('review').tolist()))
Pillow_df2["Country"] = 'UK'
Pillow_df2.head()


# In[19]:


Pillow_df2.to_csv('Pillow_UK_reviews.csv', index=False)


# ------------------------

# In[12]:


import time
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

def fetch_reviews_with_backoff(app):
    retry_count = 0
    while retry_count < 5:  # Maximum number of retries
        try:
            app.review(how_many=5000)
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying after waiting...")
            time.sleep(2 ** retry_count)  # Wait using exponential backoff
            retry_count += 1

# Create an instance of AppStore
Pillow = AppStore(country="au", app_name='pillow-sleep-cycle-tracker', app_id='878691772')

# Fetch reviews with exponential backoff
fetch_reviews_with_backoff(Pillow)


# In[13]:


Pillow.reviews


# In[14]:


Pillow_df = pd.DataFrame(np.array(Pillow.reviews),columns=['review'])
Pillow_df2 = Pillow_df.join(pd.DataFrame(Pillow_df.pop('review').tolist()))
Pillow_df2["Country"] = 'AUS'
Pillow_df2.head()


# In[15]:


Pillow_df2.to_csv('Pillow_AUS_reviews.csv', index=False)


# --------------------------------

# In[20]:


import time
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

def fetch_reviews_with_backoff(app):
    retry_count = 0
    while retry_count < 5:  # Maximum number of retries
        try:
            app.review(how_many=5000)
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying after waiting...")
            time.sleep(2 ** retry_count)  # Wait using exponential backoff
            retry_count += 1

# Create an instance of AppStore
Pillow = AppStore(country="ca", app_name='pillow-sleep-cycle-tracker', app_id='878691772')

# Fetch reviews with exponential backoff
fetch_reviews_with_backoff(Pillow)


# In[21]:


Pillow.reviews


# In[22]:


Pillow_df = pd.DataFrame(np.array(Pillow.reviews),columns=['review'])
Pillow_df2 = Pillow_df.join(pd.DataFrame(Pillow_df.pop('review').tolist()))
Pillow_df2["Country"] = 'CAN'
Pillow_df2.head()


# In[23]:


Pillow_df2.to_csv('Pillow_CAN_reviews.csv', index=False)


# --------------------------

# In[24]:


import time
import pandas as pd
import numpy as np
import json

from app_store_scraper import AppStore

def fetch_reviews_with_backoff(app):
    retry_count = 0
    while retry_count < 5:  # Maximum number of retries
        try:
            app.review(how_many=5000)
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying after waiting...")
            time.sleep(2 ** retry_count)  # Wait using exponential backoff
            retry_count += 1

# Create an instance of AppStore
Pillow = AppStore(country="in", app_name='pillow-sleep-cycle-tracker', app_id='878691772')

# Fetch reviews with exponential backoff
fetch_reviews_with_backoff(Pillow)


# In[25]:


Pillow.reviews


# In[26]:


Pillow_df = pd.DataFrame(np.array(Pillow.reviews),columns=['review'])
Pillow_df2 = Pillow_df.join(pd.DataFrame(Pillow_df.pop('review').tolist()))
Pillow_df2["Country"] = 'IND'
Pillow_df2.head()


# In[27]:


Pillow_df2.to_csv('Pillow_IND_reviews.csv', index=False)


# ------

# In[28]:


import pandas as pd

df1 = pd.read_csv('Pillow_US_reviews.csv')
df2 = pd.read_csv('Pillow_UK_reviews.csv')
df3 = pd.read_csv('Pillow_AUS_reviews.csv')
df4 = pd.read_csv('Pillow_CAN_reviews.csv')
df5 = pd.read_csv('Pillow_IND_reviews.csv')

# Concatenate the two DataFrames vertically
Pillow_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# Write the combined DataFrame to a new CSV file
Pillow_df.to_csv('Pillow.csv', index=False)


![food](https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/7c0c003a-96f5-4252-bdc0-b6b1a20e08c1)

# Eat Safe, Love

In this Challenge, I've been contracted by the editors of a food magazine, Eat Safe, Love, to evaluate ratings data for where to focus future articles; the data comes from the UK Food Standards Agency, which evaluates various establishments across the United Kingdom. 

Due to a request from the magazine's editors, I make some modifications to the data imported into a MongoDB database such as adding information for an exciting new halal restaurant in Greenwich, "Penang Flavours".  The magazine is not interested in any establishments in Dover, so I remove any establishments within the Dover Local Authority from the database and check the number of documents to ensure they are not present.  Some of the values in each MongoDB document such as latitude, longitude, and rating value are text when they should be numbers; to facilitate future inquiry, I appropriately change these data types.

For the analysis, I use my knowledge of Python, PyMongo, and MongoDB to answer specific questions posed by the management and staff of Eat Safe, Love.  Here are the questions and their query results.

1. Which establishments have a hygiene score equal to 20 (the worst possible rating)?
<img width="580" alt="Screenshot 2024-04-27 at 5 45 03 PM" src="https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/cdecf369-9643-4f21-b3dd-31772a8e6620"><img width="603" alt="Screenshot 2024-04-27 at 5 45 14 PM" src="https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/80b4897c-1138-46e0-84f3-74e7b3b9ed81">

<img width="1105" alt="food1" src="https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/8422cc1b-40a4-47a6-bff5-db6c54ee7997">

2. Which establishments in London have a high rating value greater than or equal to 4 (1-5)?
<img width="530" alt="Screenshot 2024-04-27 at 5 46 12 PM" src="https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/092dc46f-c512-413d-8174-71858d1100f4"><img width="611" alt="Screenshot 2024-04-27 at 5 46 22 PM" src="https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/64b919a8-a5b8-4073-8d1b-e5bfaef2499a">

<img width="1107" alt="food2" src="https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/31e7221f-1e0a-4443-a1b4-3cbd240f7a67">

4. What are the top 5 establishments with a rating value of 5, sorted by best hygiene score, nearest to the new restaurant added, "Penang Flavours?
<img width="1106" alt="food3" src="https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/82cbe99a-3be0-4750-baff-7547d5b42f63">

5. How many establishments in each Local Authority area have a hygiene score of 0 (the best possible rating)? Sort the number of establishments from highest to lowest, and print out the top ten local authority areas.
<img width="1107" alt="food4" src="https://github.com/njgeorge000158/UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB/assets/137228821/425a135c-9aea-45c8-8b1b-373ed8a7fd39">

From the analysis, there are a number of insightful conclusions.  The locations with the worst hygiene scores are on or near the coastline outside of London. There is a concentration of highly rated restaurants inside the city of London proper. Greenwich is the location with establishments scoring highest in both value and hygiene; for hygiene alone, Thanet is the best location.

----

### Copyright

Nicholas J. George © 2023. All Rights Reserved.

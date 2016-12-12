
## Name: Waseem Azher and AzharUddin H Mohammad
## Project: Mongo DB
## Course: 5303 - Advance Database management Systems

### Curl Commands to run the Queries.

1) curl -X GET http://104.236.3.96:5000/find_zips/zip=89117,89122:start=0:limit=20   -- no issues

2) curl -X GET http://104.236.3.96:5000/rest_city/city="las%20vegas":start=0:limit=20  -- no issues

3) curl -X GET http://104.236.3.96:5000/closest/lon=-80.839186:lat=35.226504:start=0:limit=20

  output:
  {"data": [{"name": "Budget Blinds"}, {"name": "Sheraton Charlotte Airport Hotel"}, {"name": "Fairpoint Communications"},
  {"name": "Bank of America Corporate Center Parking"}, {"name": "Avis Rent A Car"}, {"name": "Green's Lunch"}, 
  {"name": "Charlotte Center City Partners"}, {"name": "Jackson's Java"}, {"name": "Dunhill Hotel"}, 
  {"name": "McColl Center for Art + Innovation"}, {"name": "McNinch House Restaurant"}, {"name": "Alexander Michael's"}, 
  {"name": "St Peter's Episcopal Church"}, {"name": "Showmars Third Street"}, {"name": "Levine Museum of the New South"}, 
  {"name": "New Creations Inc"}, {"name": "Morton's The Steakhouse"}, {"name": "Matt's Chicago Dog"}, {"name": "Starbucks"}, 
  {"name": "Fox and Hound Smokehouse & Tavern"}]}


4) curl -X GET http://104.236.3.96:5000/reviews/id=hB3kH0NgM5LkEWMnMMDnHw:start=0:limit=20   -- no issues

5) curl -X GET http://104.236.3.96:5000/reviews_5stars/id=hB3kH0NgM5LkEWMnMMDnHw:stars=5:start=0:limit=20  -- Breaking the Server

7) curl -X GET http://104.236.3.96:5000/most_likes/start=0:limit=20

8) curl -X GET http://104.236.3.96:5000/review_count/   --- no issues

9) curl -X GET http://104.236.3.96:5000/elite/start=0:limit=20

10) curl -X GET http://104.236.3.96:5000/long_elite/start=0:limit=1

    curl -X GET http://104.236.3.96:5000/elite/start=0:limit=1:sorted=reverse
   
11) curl -X GET http://104.236.3.96:5000/avg_elite/




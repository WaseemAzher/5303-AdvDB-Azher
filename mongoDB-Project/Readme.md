## Name: Waseem Azher and AzharUddin H Mohammad
## Project: Mongo DB
## Course: 5303 - Advance Database management Systems

### Curl Commands to run the Queries.

1) curl -X GET http://107.170.48.163:5000/find_zips/zip=89117,89122

  output: Data is printing on the output but limits was creating the problem we commented the limit code..
-------------------------------------------------------------------------------------------------------------------------------

2) curl -X GET http://107.170.48.163:5000/rest_city/city="Las%20Vegas":start=0:limit=20

   output:

 {"data": [{"city": "Las Vegas", "name": "Apex Medical Center"}, {"city": "Las Vegas", "name": "Psychic Eye Book Shops"},
 {"city": "Las Vegas", "name": "Timberlake"}, {"city": "Las Vegas", "name": "Gap"}, {"city": "Las Vegas", "name": 
 "Great Clips"}, {"city": "Las Vegas", "name": "SuperPawn"}, {"city": "Las Vegas", "name": "Linda Woodson 
 Dermatology"}, {"city": "Las Vegas", "name": "Chianti Cafe"},{"city": "Las Vegas", "name": "Ken Landow, MD"}, {"city": "Las Vegas", "name": "Terrible Herbst"}, {"city":  "Las Vegas", "name": "Re-Bath"},{"city": "Las Vegas", "name": "Smith Susan DDS"}, {"city": "Las Vegas", "name": "Gps City"}, {"city": "Las Vegas", "name": "Boulder Station Hotel & Casino"}, {"city": "Las Vegas", "name": "Lionel J Handler, MD"}, {"city": "Las Vegas", "name": "All American Van & Storage"},{"city": "Las Vegas", "name": "LVTS - Used & OEM Automotive Parts"}, {"city": "Las Vegas", "name": "USS Fish N Chips"},{"city": "Las Vegas", "name": "Neil Smith's Vegas Guitars Custom Shop"}, {"city": "Las Vegas", "name": "Petco"}]}
--------------------------------------------------------------------------------------------------------------------------------
3) curl -X GET http://107.170.48.163:5000/closest/lon=-80.839186:lat=35.226504:start=0:limit=20

   output:
  {"data": [{"name": "Budget Blinds"}, {"name": "Sheraton Charlotte Airport Hotel"}, {"name": "Fairpoint Communications"},
  {"name": "Bank of America Corporate Center Parking"}, {"name": "Avis Rent A Car"}, {"name": "Green's Lunch"},  {"name": "Charlotte Center City Partners"}, {"name": "Jackson's Java"}, {"name": "Dunhill Hotel"}, 
  {"name": "McColl Center for Art + Innovation"}, {"name": "McNinch House Restaurant"}, {"name": "Alexander Michael's"}, 
  {"name": "St Peter's Episcopal Church"}, {"name": "Showmars Third Street"}, {"name": "Levine Museum of the New South"}, 
  {"name": "New Creations Inc"}, {"name": "Morton's The Steakhouse"}, {"name": "Matt's Chicago Dog"}, {"name": "Starbucks"}, 
  {"name": "Fox and Hound Smokehouse & Tavern"}]}
----------------------------------------------------------------------------------------------------------------------------------
4) curl -X GET http://107.170.48.163:5000/reviews/id=hB3kH0NgM5LkEWMnMMDnHw:start=0:limit=20

   output:
   {"data": [{"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"},
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"},
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, 
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"},
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, 
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"},
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw"}]}
   
-----------------------------------------------------------------------------------------------------------------------------------
5) curl -X GET http://107.170.48.163:5000/reviews_5stars/id=hB3kH0NgM5LkEWMnMMDnHw:num_stars=5:start=0:limit=20

   output :

   {"data": [{"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, 
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, 
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, 
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, 
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5},
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5},
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, 
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, 
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5},
   {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}, {"business_id": "hB3kH0NgM5LkEWMnMMDnHw", "stars": 5}]}
-------------------------------------------------------------------------------------------------------------------------------------
6) curl -X GET http://107.170.48.163:5000/yelping/

   output: Data is printing on the output but limits was creating the problem we commented the limit code.. 


-------------------------------------------------------------------------------------------------------------------------------------


7) curl -X GET http://107.170.48.163:5000/most_likes/start=0:limit=20 

   output:

   {"data": [{"business_id": "iTLwGhF-NyHGrgoYzGK7xw"}, {"business_id": "ILoDsxtqtLU2oTMaf_laGQ"},
   {"business_id": "Es300Ys1XXPYg8aI7BKVYQ"}, {"business_id": "v9_MNjWori0tLWErWP7y2g"}, {"business_id": "-r_4cKz_A8tj_SkiOL50yQ"},
   {"business_id": "1U1GRksKXF7q8FKcW0e5VQ"}, {"business_id": "hVSuSlR4uYNnap2LU-6Tcg"}, {"business_id": "c2VrKERabMII-L5vUGi5iQ"}, 
   {"business_id": "ehvCTJMIVMyc4z3Bq2AnXA"}, {"business_id": "4M1fVHmnSyNg-fNW247-QA"}, {"business_id": "gj_8sI7cjD_1pH6gPBcNRg"}, 
   {"business_id": "bYhpy9u8fKkGhYHtvYXazQ"}, {"business_id": "szw8OGJlsqaA3i2oe7dn9A"}, {"business_id": "ILoDsxtqtLU2oTMaf_laGQ"},
   {"business_id": "j4iIYoFSxfWGppLfL7FlvA"}, {"business_id": "GlJel_6U3zyWenXDnO_fPQ"}, {"business_id": "Qu_19GEp2B7MfRtI5hErrg"}, 
   {"business_id": "yYbgcTsSWIRJNxFXoVuMQw"}, {"business_id": "85qXvq1L8xsY10OPArHipw"}, {"business_id": "x_MCZPQ9G-IsDnwkJBceIQ"}]}
-------------------------------------------------------------------------------------------------------------------------------------
8) curl -X GET http://107.170.48.163:5000/review_count/

   output: This is very big data getting printed on the output screen
    
-------------------------------------------------------------------------------------------------------------------------------------

9) curl -X GET http://107.170.48.163:5000/elite/start=0:limit=20

   ouput :

   {"data": [{"user_id": "fHtTaujcyKvXglE33Z5yIw", "name": "Ken"}, {"user_id": "SIBCL7HBkrP4llolm4SC2A", "name": "Katherine"},
   {"user_id": "ysYmC-ufbdmVEX9yAv-VEQ", "name": "George"}, {"user_id": "WPOKvkacSKHx_bIG1alFiA", "name": "Mary"},
   {"user_id": "UTS9XcT14H2ZscRIf0MYHQ", "name": "Nader"}, {"user_id": "18kPq7GPye-YQ3LyKyAZPw", "name": "Russel"}, 
   {"user_id": "rpOyqD_893cqmDAtJLbdog", "name": "Jeremy"}, {"user_id": "4U9kSBLuBDU391x6bxU-YA", "name": "Michael"}, 
   {"user_id": "1blidZhgxDVSBuJ_dbTU6g", "name": "Kiffen"}, {"user_id": "qL7Astun3i7qwr2IL5iowA", "name": "Joseph"},
   {"user_id": "ZWOj6LmzwGvMDh-A85EOtA", "name": "Helen"}, {"user_id": "HDQixQ-WZEV0LVPJlIGQeQ", "name": "Yishan"}, 
   {"user_id": "9i8tV1cWR3nSiOTtg4OEAg", "name": "David"}, {"user_id": "bWNn5RzthU9-yo5VYQB20g", "name": "Angela"}, 
   {"user_id": "xu_KA5FxXfb5-vx0uz_BNg", "name": "Michelle"}, {"user_id": "5OlCB4cJ3CUksr3ONw6Ezw", "name": "Jeffrey"},
   {"user_id": "e-hBnxMWmzSut-BlyxR2KQ", "name": "Lynda"}, {"user_id": "E_DJ1nTDPt9Qk2abWFTefQ", "name": "Heather"}, 
   {"user_id": "LCbwNuo4r-WdAmw6LeGPog", "name": "Jeff"}, {"user_id": "xOQVHYN1roRZKpLvAT-a2A", "name": "Chad"}]}
--------------------------------------------------------------------------------------------------------------------------------------
10) curl -X GET http://107.170.48.163:5000/long_elite/start=0:limit=1:sorted=reverse

  output: 

   {"data": [{"_id": null, "maxelite": 12}]
 --------------------------------------------------------------------------------------------------------------------------------------  
11) curl -X GET http://107.170.48.163:5000/avg_elite/

   output:

   {"data": [{"avg_elite_yrs": 0.16248929439113488, "_id": 0}]}

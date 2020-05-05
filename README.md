# NLP KEYWORDS MINING API FOR RECIPES DATA

Flask api to get recipes keyword of given title and body

1. Create virtual environment.

# python3 -m venv env

2. Copy paste the code of this repository

3. Activate virtual environment

# source env/bin/activate

4. Install the packages

# pip install

5. Run the api

# python app.py

6. POST request to http://127.0.0.1:5000/nlp/api/textminer/keywords, pass the parameters given as sample

{
	"title":"Cod Fish Tacos",
	"body": "4 pieces 4 oz each skinless firm white fish such as cod, (or snapper fillet, mahi mahi), fresh is best, if frozen thawed. 1/2 teaspoon cumin. 1/2 teaspoons kosher salt. 3/4 teaspoons lime chili seasoning, such as Tajin Classic. 1/4 cup fat free Greek Yogurt. 3 tablespoons light mayonnaise. 1 tablespoon lime juice. 1-2 tablespoons water, to thin. 3/4 teaspoon chili-lime seasoning salt, such as Tajin Classic. 1/8 teaspoon kosher salt. 1/4 cup chopped cilantro. 1 cup white cabbage, sliced. 1 cup red cabbage, sliced. 1/4 cup shredded carrots. 1 tablespoon olive oil. 1 tablespoon lime juice. 1/4 teaspoon kosher salt. 8 corn tortillas, charred on the open flame 30 seconds on each side. lime wedges, for serving",
	"keywords": 10
}

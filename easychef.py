from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		ing = request.form.get("ingredients")

		url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex"

		querystring = {"query":f"{ing}","excludeIngredients":"bacon","ranking":"2","instructionsRequired":"true","addRecipeInformation":"true","limitLicense":"true","number":"1"}

		headers = {
		    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
		    'x-rapidapi-key': "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679"
		    }

		response = requests.request("GET", url, headers=headers, params=querystring)
		data = response.json()

		try:
			# Accessing dictionary
			data = data['results'][0]

			# Title of recipe
			title = data['title']

			# Time to cook
			duration = data['readyInMinutes']

			# URL source
			url_source = data['sourceUrl']

			# image URL
			image = data['image']

			# List of recipes
			analyzedInstructions = data['analyzedInstructions'][0]
			steps = analyzedInstructions['steps']

			recipe = "Your receipe has been found!"
			meal = "Click MY MEAL to find your recipe."
			return render_template('home.html', title=title, duration=duration, image=image, url_source=url_source, steps=steps, recipe=recipe, meal=meal)
		except:
			data = "No results"
			void = "EasyCHEF! could not find you a meal,"
			error = "please try using different ingredients."
			return render_template('home.html', void=void, error=error)


if __name__ == '__main__':
    app.run(debug=True)

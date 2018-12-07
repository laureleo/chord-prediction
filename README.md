<!DOCTYPE html>
<html lang="en">
<head>
  <title>cs_team_beta_hw2: Open Food Facts</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
	
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://unpkg.com/scrollreveal/dist/scrollreveal.min.js"></script>
    <script type="text/javascript" src="js/d3.min.js"></script>
    <script>
    (function() {
        var config = {
            viewFactor: 0.20,
            duration: 2000,
            reset: true,
        }
        window.sr = new ScrollReveal(config)
    })()
    </script>
	 
  <style>
	footer {
      padding-top: 70px;
      padding-bottom: 70px;
      background-color: #2f2f2f; /* Black Gray */
      color: #fff;
	  text-align: center;
	  
	}
  
	.reveal_left {
		width: 90%;
		}

	.reveal_right {
		width: 90%;
		}

	.reveal_left_alternate {
		width: 90%;
		background-color:whitesmoke;
		}

	.reveal_right_alternate {
		width: 90%;
		background-color:whitesmoke;
		}


		
		
		
		/* Style the tab */
.tab {
    float: left;
    border: 1px solid #ccc;
    background-color: #f1f1f1;
    width: 30%;
    height: 300px;
}

/* Style the buttons that are used to open the tab content */
.tab button {
    display: block;
    background-color: inherit;
    color: black;
    padding: 22px 16px;
    width: 100%;
    border: none;
    outline: none;
    text-align: left;
    cursor: pointer;
}

/* Change background color of buttons on hover */
.tab button:hover {
    background-color: #ddd;
}

/* Create an active/current "tab button" class */
.tab button.active {
    background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
    float: left;
    padding: 0px 12px;
    border: 1px solid #ccc;
    width: 70%;
    border-left: none;
    height: 300px;
    display: none;
}

		</style>
  



</head>
<body>

<div class="jumbotron text-center">
  <h1>Eeat less sugar, you're sweet enough already</h1>
  <p>cs_team_beta_hw2</p> 
  <p style="font-size:9px;color:gray">Automn 2018</p>
  <p></p>
  <p>
	<a href="https://world.openfoodfacts.org/data" target="_blank">
	<img width="178" height="150" id="logo" style="margin-bottom:0.5rem" alt="Open Food Facts" src="https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-en-178x150.png" srcset="https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-en-356x300.png 2x">
	</a>
  </p>
</div>
  
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <h3>#Abstract</h3>
      <p>
		Many people consume too much sugar and even more than they realize. Some products contain added or hidden sugar like Low-fat Yogurst, BBQ Sauce, ketchup or Fruit Juice. To put in perspective, some sauces may contains more than 50 per cent of sugar. (<a href="https://www.healthyfoodguide.com.au/articles/2015/july/how-much-sugar-sauce">*Ref1</a>)

		Based on the "AHA Scientific Statement" (<a href="https://www.ahajournals.org/doi/pdf/10.1161/circulationaha.109.192627">*Ref2</a>), the major sources of added sugars are mainly coming form those Food Categories: regular soft drinks, sugars, candy, cakes, cookies, pies and fruit drinks, dairy desserts and milk products:

		<table style="border:1px solid;"><tr style="border:1px solid;background-color:whitesmoke;">
		<td><b>Food categories</b></td><td><b>Contribution to added sugar intake</b><br>
		(% of total added sugar consumed)</td></tr>
		<tr><td>Regular soft drinks</td><td>33.0</td></tr>
		<tr><td>Sugars and candy</td><td>16.1</td></tr>
		<tr><td>Cakes, cookies, pies</td><td>12.9</td></tr>
		<tr><td>Fruit drinks (fruitades and fruit punch)</td><td>9.7</td></tr>
		<tr><td>Dairy desserts and milk products (ice cream sweetened yogurt, and sweetened milk)</td><td>8.6</td></tr>
		<tr><td>Other grains (cinnamon toast and honey-nut waffles)</td><td>5.8</td></tr>
		</table>


	</p>
	
		<p>
		From there, it's easy understandable that eating too much sugar is not healthy and can cause Weight Gain, increase the risk of Hear Disease, Diabetes (<a href="https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/sugar/added-sugars">*Ref3</a>) or even Cancer, ...
		</p><p>
		Therefore, it's crucial to limit the consumption of foods with high amounts of added sugars. According to the American Heart Association (AHA) (<a href="https://www.ahajournals.org/doi/pdf/10.1161/circulationaha.109.192627">*Ref4</a>), the maximum amount of added sugars per day are limited to:
		</p><p>
		<ul><li>
		<b>Men</b>: 150 calories per day (37.5 grams or 9 teaspoons or ~6.30 pieces of sugar)
		</li><li>
		<b>Women</b>: 100 calories per day (25 grams or 6 teaspoons or ~4.20 pieces of sugar)
		</li></ul>
		The US dietary guidelines advise people to limit their intake to less than 10% of their daily calorie intake. For a person eating 2,000 calories per day, this would equal 50 grams of sugar, or about 12.5 teaspoons or 8.4 pieces of sugar. (<a href="https://health.gov/dietaryguidelines/2015/guidelines/executive-summary/">*Ref5</a>)
		</p><p>
		“Keeping intake of free sugars to less than 10% of total energy intake reduces the risk of overweight, obesity and tooth decay,” says Dr Francesco Branca, Director of WHO’s Department of Nutrition for Health and Development.(<a href="http://www.who.int/mediacentre/news/releases/2015/sugar-guideline/en/">*Ref6</a>)
		</p><p>
		Based on the information above, we would like to explore the "Open Food Facts Datbase", apply the knowledge of data analysis technics and best practices acquired during attending Applied Data Analysis course at EPFL in Lausanne in Autumn 2018 and figure out meaninful/insightful relationship between different dimensions used to categorize the data or external metrics.
		</p>


    </div>
    <div class="col-sm-4">
      <h3># Research questions</h3>
      <p>1. There are lots of different dimensions/metrics which could be used to analyse/slice the data: dates when the product was added and last modified, produced country, brand, categories (e.g. snack, dessert), country / store where the product was purchased, size and weight of the product, amount of fat, sugar, vitamins, chemicals, ingredients as text etc
			We will explore the dimensions/metrics above and relate some of those to each other or such generic metrics as country (producer or consumer) GDP, life expectancy (vitamins, salt, sugar, other chemicals), expore which country/store is the biggest produce/consumer of product by brand/ingredients etc. We will also check how some of the metrics evolve over time.</p>
			<p>
			2. Explore the quality of the data, find and estimate inconsistencies (e.g. accuracy of the text description)</p>
			<p>
			3. Finally, there are images available for each product, so we will try to analyse those using Deep Learning techniques (CNN) and relate to some of the deminsions avialable in the dataset.
			</p>
			   <p>
			   We were maybe a little ambition about the analyis we would like to perform and discovered many discrepancies on the Data. Indeed, we learnt during the lecturer that the main activities performed by a Data Scientist is Data Cleaning. Based on the Data Quality of the www.openFoodFacts.org Data, we are fully agree with this assertion and we even decided to spend more time on Data Analyis.
			</p>
			  <p>
			Indeed in order to perform good analysis, it's crucial to consolidate the firt layer and understand the Data Set. We even think that this open Database should be more normalized and structured, which may offer a more solid base for further Analyis and Data Cleaning.
			</p>

			<p>
			What is the goal to perform deeper analyis, when underlying data are not certified, checked, cleaned, cleansed and normalized. Furtheremore as you will discover in this Notebook, most of the dimensions have to be used with precaution.
			</p>


			<p>
			<b>
			Could we trust OpenFoodFacts Data ?
			</b>
			</p>
			<p>
			<b>
			Should we eat too much sugar ?
			</b>
			</p>
			   
			   
   
    </div>
    




		
	<div class="col-sm-4">
      <h3># Dataset</h3>        
		<p>
			Open Food Facts database contains the information on food products from around the world. For each item, the database stores its generic name, quantity, type of packaging, brand, category, manufacturing or processing locations, countries and stores where the product is sold, list of ingredients, any traces. 
			<a href="https://world.openfoodfacts.org">https://world.openfoodfacts.org</a>
		</p>
    </div>


	
	<div class="col-sm-4">
      <h3># Milestone 3</h3>        
		<p>
 A list of internal milestones up until project milestone 3
The data was messier and more difficult to manage than we had initially thought. Many of our original ideas turned out infeasible and we have had to change our approach to things.
</p>
<p>
Our current plan until  the third milestone the 15 December is as follows:
<ul>
<li>25 to 28 November: Select three to five questions relating to sugar and health that we can answer with this data</li>
<li>29 to 30 November: Select a platform for our story</li>
<li>01 to 07 December: Answer the questions</li>
<li>07 to 14 December: Finalize the story</li>
</ul>
</p>
</div>	
	
	
	
	
	<div class="col-sm-4">
      <h3># Questions for TA</h3>        
      <p>NA</p>
    </div>
  

	<div class="col-sm-4">
      <h3># References/Sources</h3>
		<p>
		<ul>
			<li>
			<a href="https://www.healthyfoodguide.com.au/articles/2015/july/how-much-sugar-sauce">
				*Ref1 Heathy Food: How much sugar is in that sauces ?
			</a>
			</li>
			<li>
			<a href="https://www.ahajournals.org/doi/pdf/10.1161/circulationaha.109.192627">
			*Ref2 Major Sources of Added Sugars in the American Diet
			</a>
			</li>
			<li>
			<a href="https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/sugar/added-sugars">
			*Ref3 Maximum amount of added sugars recommendation from the American Heart Association
			</a>
			</li>
			<li>
			<a href="https://journals.plos.org/plosone/article/figure?id=10.1371/journal.pone.0057873.g002">
			*Ref3 Relationship of Sugar to Population-Level Diabetes Prevalence
			</href>
			</li>
			<li>
			<a href="https://www.ahajournals.org/doi/pdf/10.1161/circulationaha.109.192627">
			*Ref4 Major Sources of Added Sugars in the American Diet
			</a>
			</li>
			<li>
			<a href="https://health.gov/dietaryguidelines/2015/guidelines/executive-summary/">
			*Ref5 US Dietary guideleines 
			</a>
			</li>
			<li>
			<a href="http://www.who.int/mediacentre/news/releases/2015/sugar-guideline/en/">
			*Ref6 World Health Organization: Reduce sugars intake 
			</a>
			</li>
		</ul>	
		</p>
      </div>
  </div>

	  
	  

<!-------------------------------------------------------------------------------------------------------------------->	  
<!-- Paragraph1 																									-->
<!-------------------------------------------------------------------------------------------------------------------->
<div class="row">
	<div id="paragraph1_title" class="container reveal_top">
		<h2> Paragraph1 </h2>
	</div>

	<div id="paragraph1_content" >	
		<div class="container reveal_left">
			<p>
				<img class="picture" src="./images/ImageTopCreator.JPG" style="height:600px"/>					
				left, left blablabla. 
			</p>
		</div>
		
		<div class="container reveal_right">
			<p>
				right. right.
			</p>
		</div>	
	</div>
</div>


<!-------------------------------------------------------------------------------------------------------------------->	  
<!-- Paragraph2 																									-->
<!-------------------------------------------------------------------------------------------------------------------->
<div style="background-color:whitesmoke class="row">
	<div id="paragraph2_title" class="container reveal_top">
		<h2> Paragraph2 </h2>
	</div>

	<div style="background-color:whitesmoke;">	
		<div class="container reveal_left">
			<p>
				<img class="picture" src="./images/ImageTopCreator.JPG" style="height:600px"/>					
				left, left blablabla. 
			</p>
		</div>
		
		<div class="container reveal_right">
			<p>
				right. right.
			</p>
		</div>	
	</div>
</div>

<!-------------------------------------------------------------------------------------------------------------------->	  
<!-- Paragraph3 																									-->
<!-------------------------------------------------------------------------------------------------------------------->
<div>
	<div id="paragraph3_title" class="container reveal_top">
		<h2> Paragraph3 </h2>
	</div>

	<div id="paragraph3_content" class="row">	
		<div class="container reveal_left">
			<p>
				<img class="picture" src="./images/ImageTopCreator.JPG" style="height:600px"/>					
				left, left blablabla. 
			</p>
		</div>
		
		<div class="container reveal_right">
			<p>
				right. right.
			</p>
		</div>	
	</div>
</div>


<!-------------------------------------------------------------------------------------------------------------------->	  
<!-- Paragraph4 																									-->
<!-------------------------------------------------------------------------------------------------------------------->
<div style="background-color:whitesmoke;">
	<div id="paragraph4_title" class="container reveal_top">
		<h2> Paragraph4 </h2>		
	</div>

	<div id="paragraph4_content" class="row">	
		<div class="container reveal_left">
			<p>
								<div class='tableauPlaceholder' id='viz1543532631134' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cl&#47;Classeur1_921&#47;Tableaudebord1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Classeur1_921&#47;Tableaudebord1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cl&#47;Classeur1_921&#47;Tableaudebord1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1543532631134');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
			</p>
		</div>
		
		<div class="container reveal_right">
			<p>
				right. right.
			</p>
		</div>	
	</div>
</div>


<!-------------------------------------------------------------------------------------------------------------------->	  
<!-- Paragraph5 																									-->
<!-------------------------------------------------------------------------------------------------------------------->
<div>
	<div id="paragraph5_title" class="container reveal_top">
		<h2> Paragraph5 </h2>
	</div>

	<div id="paragraph5_content" class="row">	
		<div class="container reveal_left">
			<p>
				<img class="picture" src="./images/ImageTopCreator.JPG" style="width:400px"/>					
				
			</p>
			<p>
			<div class='tableauPlaceholder' id='viz1543529547939' style='position: relative'>
			<noscript><a href='#'>
			<img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cl&#47;Classeur1_921&#47;Feuille1&#47;1_rss.png' style='border: none' /></a>
			</noscript>
			<object class='tableauViz'  style='display:none;'>
				<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
				<param name='embed_code_version' value='3' /> 
				<param name='path' value='views&#47;Classeur1_921&#47;Feuille1?:embed=y&amp;:display_count=y&amp;publish=yes' /> 
				<param name='toolbar' value='yes' />
				<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cl&#47;Classeur1_921&#47;Feuille1&#47;1.png' /> 
				<param name='animate_transition' value='yes' />
				<param name='display_static_image' value='yes' />
				<param name='display_spinner' value='yes' />
				<param name='display_overlay' value='yes' />
				<param name='display_count' value='yes' />
			</object>
			</div>                
			<script type='text/javascript'>                    
			var divElement = document.getElementById('viz1543529547939');                    
			var vizElement = divElement.getElementsByTagName('object')[0];                    
			vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    
			var scriptElement = document.createElement('script');                    
			scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
			vizElement.parentNode.insertBefore(scriptElement, vizElement);                
			</script>
			</p>
		</div>
		
		<div class="container reveal_right">
			<p>

			</p>
		</div>	
	</div>
</div>




</div>
<!-------------------------------------------------------------------------------------------------------------------->	  
<!-- FOOTER		 																									-->
<!-------------------------------------------------------------------------------------------------------------------->
<footer>
	<p>steve.rey@epfl.ch</p>
	<p>yauheni.samasionak@epfl.ch</p>
	<p>victor.wiklund@epfl.ch</p> 
</footer>



<!-------------------------------------------------------------------------------------------------------------------->	  
<!-- Script																											-->
<!-------------------------------------------------------------------------------------------------------------------->
<script>
    // JavaScript
    window.sr = ScrollReveal();
    sr.reveal('.reveal_left', { origin: 'left', distance: '200px' });
    sr.reveal('.reveal_right', { origin: 'right', distance: '200px' });
    sr.reveal('.reveal_top', { origin: 'top', distance: '200px' });
</script>


<script>
function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
</script>
	
</body>
</html>

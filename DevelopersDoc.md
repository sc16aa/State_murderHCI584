#Developer's Documentation

##State Murder Data Visualization Project

This project was created to help people understand that the US judicial system makes mistakes when sentencing
citizens to life in prison or death. The project aims to show the patterns in the judicial system's sentencing. The project is mostly
finished but I'd like to clean it up a bit. The UI could use a lot of improvements. 

This project was created mostly with two libraries. The Plotly graphing library and the Dash library to launch the interactive
website. All the information in how to use these libraries can be found online. 
The majority of the project is filtering through the 'filtered.csv.' The choropleth map is filtered using the 'StateAggregates.csv.'

###Flow of the Code
The app code is broken up into about 3 parts
	1. Calling the libraries necessary and incorporating the necessary csv documents for the graphs
  2. Setting up the app layout using html
			- The first set of radio buttons coordinates to the choropleth map and links to 'StateAggregates.csv'
	 		- The second set of radio buttons coordinates to the histogram and links to 'filtered.csv'
	3. Defining the two functions to update the graphs is the final part of the code 

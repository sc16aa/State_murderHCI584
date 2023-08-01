<h1> Developer's Documentation</h1>

<h2>State Murder Data Visualization Project</h2>

This project was created to help people understand that the US judicial system makes mistakes when sentencing
citizens to life in prison or death. The project aims to show the patterns in the judicial system's sentencing. The project is mostly
finished but I'd like to clean it up a bit. The UI could use a lot of improvements. 

This project was created mostly with two libraries. The Plotly graphing library and the Dash library to launch the interactive
website. All the information in how to use these libraries can be found online. 
The majority of the project is filtering through the 'filtered.csv.' The choropleth map is filtered using the 'StateAggregates.csv.'

<h3>Flow of the Code </h3>
The app code is broken up into about 3 parts <p>
<ol>	
<li> Calling the libraries necessary and incorporating the necessary csv documents for the graphs
<li> Setting up the app layout using html
			<ol type='a'> <li>The first set of radio buttons coordinates to the choropleth map and links to 'StateAggregates.csv'
	 		<li> The second set of radio buttons coordinates to the histogram and links to 'filtered.csv'</ol>
<li>Defining the two functions to update the graphs is the final part of the code
</ol>
<h4> Final Thoughts </h4>
<p> I don't expect this application to be used in any official capacity.
However, I would like to keep working on the UI and adding more information for people.
This information could include a system to look up the user's congressperson or state rep or a link to any states considering abolishing the death penalty. </p>

# **fastapi-toy-server**
This is a toy FastAPI server, demonstrating basic functionalities of it.  It's also related to a series of docker challenges in my company (Tosan), in which the project should be dockerized.


[![Python](https://img.shields.io/badge/python-3.7-green)](https://www.python.org/downloads/release/python-370/)
<h2> Installation </h2>
<ul>
	<li> Install requirements: 
		<ol type="a">
			<li> Install <b> "python3.7" </b> </li>
			<li>  Install <b> "virtualenv" </b>
        			<pre><code>pip install virtualenv</code></pre> 
			</li>
			<li>
        			Create the virtual environment using following command:
        			<pre><code>virtualenv .env</code></pre>
    			</li>
			<li> Active virtualenv:
				<ul>
					<li> For windows:
       						<pre><code>.env\Scripts\activate</code></pre>
					</li>					
				</ul>	
    			</li>
			<li> Now you can install libraries and dependencies listed in requirements file:
        			<pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>
                You can exit from virtual environment using following command:
                <pre><code>deactivate</code></pre>
            </li>
		</ol>
	</li>
			
</ul>
<h2> Running the app </h2>
	<ul>
		<li>Set environment variables:
			<ul>
			    <li> Set the path to config file:
                <pre><code>FAST_API_TOY_SERVER_ENV=path\to\config</code></pre>
                </li>
                <li> Specify the port number (if you don't, it will default to 8080): 
                        <pre><code>PORT_NUMBER=5000</code></pre>
                </li>
                <li> For development: 
                        <pre><code>FAST_API_ENV=development</code></pre>
                </li>
                <li> For production:
                       <pre><code>FAST_API_ENV=production</code></pre>
                </li>					
            </ul>
		</li>
		<li>Run the app:
		    <pre><code>python asgi.py</code></pre>
		</li>
	</ul>
<h2> Documentation </h2>
    Navigate to the following links to browse the server documentation:
        <ul>
            <li> Redoc documentation: 
                    <pre>http://localhost:8080/redoc</pre>
            </li>
            <li> Swagger UI documentation:
                   <pre>http://localhost:8080/docs</pre>
            </li>					
        </ul>

<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="djangodashboard_0"></a>django-dashboard</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Installation_2"></a>Installation</h2>
<p class="has-line-data" data-line-start="4" data-line-end="5">The repo requires [Python] to run.</p>
<p class="has-line-data" data-line-start="6" data-line-end="7">Install the dependencies and start the server.</p>
<pre><code class="has-line-data" data-line-start="9" data-line-end="17" class="language-sh"><span class="hljs-built_in">cd</span> django-dashboard
virtualenv env
.\env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver <span class="hljs-comment"># default port 8000</span>
</code></pre>

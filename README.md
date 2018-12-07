<body>

<h2>Simple Python + Pytest + Selenium + Allure automation test project</h2>

<div>
<ul>
	<li>Created some tests</li>
	<li>Created tests configuration</li>
	<li>Enabled allure reporter</li>
</ul>
</div>

<div>
<h3>To integrate PyCharm with PyTest</h3>
<p>Preferences -> Tools -> Default test runner -> PyCharm</p>
<div>

<div>
<h3>To run marked tests </h3>
<p>For example: you have tests @pytest.mark.uitest that execute them you need to:<br>
pytest -m uitest</p>
<div>

<div>
<h3>To rerun tests </h3>
<p>For rerun failed tests:<br>
pytest --reruns 2</p>
<div>

<div>
<h3>To run tests in paralell</h3>
<p>pytest /tests -n 3<p>
</div>

<div>
<h3>To generate HTML report:</h3>
<p>pytest --html=report.html<p>
</div>

<div>
<h3>To generate allure report</h3>
<p>pytest --alluredir ./my-allure<p>
<p>allure generate ./my-allure</p>
</div>
</body>
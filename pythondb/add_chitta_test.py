#!/usr/bin/python

import MySQLdb
import time

credit = 0
debit = 0
date = time.strftime("%d/%m/%Y")
date = "21/12/2016"
db = MySQLdb.connect("localhost", "guest", "guest123", "SREEVANEE")

cursor = db.cursor()
cursor.execute("SELECT NAME FROM COMPANY_TABLE")
if cursor.rowcount > 1:
    result = cursor.fetchall()
    result_set = []
    for row in result:
        result_set.append(row[0])
else:
    result = cursor.fetchone()
    result_set = [result[0]]
chitta = []
cursor.execute("SELECT * FROM CHITTA_TABLE WHERE DATE = '{}'".format(date))
if cursor.rowcount > 1:
    chitta = cursor.fetchall()
else:
    result = cursor.fetchone()
    chitta.append(result)

print "Content-type:text/html\r\n\r\n"
print """
<!DOCTYPE html>
<html>
<head>
	<title>Sree Vanee Silk</title>
	<style type="text/css">
		#form_table{
			border-collapse: collapse;
			text-align: left;
			padding: 5px;
		}
		#view_table{
			border: 1px solid black;
			border-collapse: collapse;
			text-align: center;
			padding: 5px;
		}
	</style>
	<script type="text/javascript">
		var credit = function() {
    	var credit_div = document.getElementById('credit');
    	credit_div.style.display = 'block';
    	var debit_div = document.getElementById('debit');
    	debit_div.style.display = 'none';
		};

		var debit = function() {
    	var credit_div = document.getElementById('credit');
    	credit_div.style.display = 'none';
    	var debit_div = document.getElementById('debit');
    	debit_div.style.display = 'block';
		};

		var own_desc = function() {
		var own_div = document.getElementById('own_description');
		own_div.style.display = 'block';
		var company_div = document.getElementById('company_description');
		company_div.style.display = 'none'
		};

		var company_desc = function() {
		var own_div = document.getElementById('own_description');
		own_div.style.display = 'none';
		var company_div = document.getElementById('company_description');
		company_div.style.display = 'block'
		};

		var result = function() {
		var button_text = document.getElementById('result_button');
		var div = document.getElementById('result');
    	if (div.style.display !== 'none') {
        div.style.display = 'none';
        result_button.value = 'Show Calculations'
    	}
    	else {
        div.style.display = 'block';
        result_button.value = 'Hide Calculations'
    	}
		};

	</script>
</head>
<body>
	<form action="" method="post">
	<table id="form_table" style="width: 100%;">
	<tr>
		<th id="form_table" style="width: 33%">Select the field to enter details &nbsp;:</th>
		<th id="form_table">
		<br>
		<input type="radio" id="credit_radio" name="type" checked="checked" value="credit" onclick="credit()">Credit<br>
		<input type="radio" id="debit_radio" name="type" onclick="debit()" value="debit">Debit
		</th>
	</tr>
	<tr id="form_table">
		<td id="form_table" style="text-align: left; vertical-align: top;"><b>Credit/Debit details&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></td>
		<td id="form_table">
			<div id="credit">
				Enter credit details&nbsp;&nbsp; : <input type="text" name="credit_description"><br><br>
				Enter credit amount : <input type="text" name="credit_amount">
			</div><br>
			<div id="debit" style="display: none;">
				Enter debit details &nbsp;:
				<input type="radio" name="debit_radio" value="own" checked="checked" onclick="own_desc()">Own
				<input type="radio" name="debit_radio" value="company" onclick="company_desc()">Company<br><br>
				<div id="own_description">
					Enter description&nbsp;&nbsp; : <input type="text"><br><br>
				</div>
				<div id="company_description" style="display: none;">
					Select Company name :
					<select> """
for opt in result_set:
    print "                        <option value=\"{}\">{}</option>".format(opt, opt)

print """                    </select>
				</div><br>
				Enter amount : <input type="text" name="debit_amount"><br>
			</div>
		</td>
	</tr>
	<tr>
	</tr>
	</table>
	<br>
	<input type="submit" value="Add to chitta" style="margin-left: 23%">
	</form><br><br>
	<table id="view_table" style="width: 100%">
	<tr>
		<th id="view_table" style="width: 20%">Date</th>
		<th id="view_table" style="width: 40%">Description</th>
		<th id="view_table" style="width: 20%">Credit</th>
		<th id="view_table" style="width: 20%">Debit</th>
	</tr>
	"""
for row in chitta:
    if row[2] != '':
        credit += int(row[2])
    if row[3] != '':
        debit += int(row[3])
    print """
    	<tr>
    	<td id="view_table">{}</td>
		<td id="view_table">{}</td>
		<td id="view_table">{}</td>
		<td id="view_table">{}</td></tr>""".format(row[0], row[1], row[2], row[3])
print """
	</table><br><br><br>
	<input type="button" id="result_button" value="Show Calculations" onclick="result()"><br><br>
	<div id="result" style="display:none">
		Total Credit amount : {}<br>
		Total Debit amount &nbsp;: {}<br>
		Tally amount &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: {}<br>
	</div>
</body>
</html>
""".format(credit, debit, credit-debit)

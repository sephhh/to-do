%#template to generate an HTML table from a list
<p>You still have to do this stuff!</p>
<table border="1">
%for row in rows:
	<tr>
	%for col in row:
		<td>{{col}}</td>
	%end
	</tr>
%end
</table>
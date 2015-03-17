%#template for editing a task
%#the template expects to a receive a value for "no" as well as "old", the text of the todo item
<p>Edit task number {{no}}</p>
<form action="/edit/{{no}}" method="get">
<input type="text" name ="task" value="{{old[0]}}" size="100" maxlength="100">
<select name="status">
<option>open</option>
<option>closed</option>
</select>
<br/>
<input type="submit" name="save" value="save">
</form>
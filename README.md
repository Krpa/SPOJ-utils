SPOJ-utils
==========
Tools for online judge called SPOJ: http://www.spoj.com/.

Goal
==========
Current goal is to make this program serve as a todo list manager.
It should be able to do instructions such as add, delete, list and similar.
When it's done, I would like to add more features, such as backing up all solutions,
making interesting statistics, integrate it with dropbox and others.

init.txt
==========
Contains initialization data. You should change it according to your wishes.

Instructions
==========
<b> 1. add prob1,prob2,prob3...probn </b> <br>
 Adds problems to todo list, problems that already exist in the todo list won't be added again. Arguments should be seperated only by "," and they should be codes for problems.<br>
<b> 2. del prob1,prob2,prob3...probn </b> <br>
 Deletes problems from todo list. <br>
<b> 3. clear </b> <br>
   Clears the todo list. <br>
<b> 4. getHtml file </b> <br>
   Makes html file with links to problems in the todo list. Takes one argument "file" that should be a path with filename to create, e.g. C:\TODO\todo.html . <br>
<b> 5. ls </b> <br>
   Prints todo list to console. <br>

Instructions to add
==========
- <b> update</b>: update the list for certain user(remove problems from the list that are solved by given user)
- <b> addUser</b>: add all problems that are solved by certain user and aren't in todo list

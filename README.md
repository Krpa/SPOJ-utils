SPOJ-utils
==========
Tools for online judge called SPOJ: http://www.spoj.com/.

Goal
==========
Current goal is to make this program serve as a todo list manager.
It should be able to do instructions such as add, delete, list and similar.
When it's done, I would like to add more features, such as backing up all solutions,
making interesting statistics and other.

init.txt
==========
Contains initialization data. You should change it according to your wishes.

Instructions
==========
<b> 1. add prob1,prob2,prob3...probn </b> <br>
   - adds problems to todo list, problems that already exist in the todo list won't be added again.

Instructions to add
==========
- <b> del</b>: delete a task from todo list
- <b> list</b>: show todo list
- <b> getHtml</b>: make a html file with links to problems
- <b> update</b>: update the list for certain user(remove problems from the list that are solved by given user)
- <b> addUser</b>: add all problems that are solved by certain user and aren't in todo list

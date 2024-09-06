# Main Structure

### Motivation:
Build complete API using FastAPI, PostgreSQL, Docker, Git.

### Main functionality:
1. Register:
	* Auth with username/email
2. Boards:
	* C/R/U/D of boards
	* Edit members
	* Control roles/permissions
3. Lists (todo, backlog etc.):
	* C/R/U/D lists
	* Reorder lists
4. Individual tasks:
	* C/R/U/D tasks
	* Status
	* User assigned
	* Due data
	* Description
	* Comment section

| Data Models:	 | Pydantic API Schemas: |
|:-------------:|:---------------------:|
|   UserModel   |      UserSchema       |
|  BoardModel   |      BoardSchema      |
| TaskListModel |    TaskListSchema     |
|   TaskModel   |      TaskSchema       |
| CommentModel  |     CommentSchema     | 
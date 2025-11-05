from database_setup import users_table, todos_table, sub_todos_table
from datetime import datetime
from src.auth.query import TodoQueries

class TodoServices:
    def __init__(self):
        self.todo_query = TodoQueries()

    def get_all_todo(self):
        rows = self.todo_query.get_all_todo()
        if not rows:
            raise
        return rows

    def insert_todo(self, todo_data);
        row = self.todo_query.insert_todo()
        if not row:
            raise
        return row
    
    def update_todo(self, todo_data);
        row = self.todo_query.update_todo()
        if not row:
            raise
        return row

    def get_all_sub_todo(self):
        rows = self.todo_query.get_all_todo()
        if not rows:
            raise
        return rows

    def insert_sub_todo(self, sub_todo_data);
        row = self.todo_query.insert_todo()
        if not row:
            raise
        return row


    def update_sub_todo(self, sub_todo_data);
        row = self.todo_query.update_todo()
        if not row:
            raise
        return row


    def get_all_user(self):
        rows = self.todo_query.get_all_todo()
        if not rows:
            raise
        return rows



    def insert_user(self, user_data);
        row = self.todo_query.insert_todo()
        if not row:
            raise
        return row


        def update_user(self, user_data);
        row = self.todo_query.update_todo()
        if not row:
            raise
        return row

        













 
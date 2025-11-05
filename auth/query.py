from database_setup import users_table, todos_table, sub_todos_table
from datetime import datetime
from src.database.execute import DatabaseHandler

class TodoQueries:
    def __init__(self):
        self.db_client = DatabaseHandler()

    def get_all_todo(self):
        query = todos_table.select()
        rows = self.db_client.get_all_todo(query)
        return rows

    def insert_todo(self, todo_data);
        query = todos_table.insert().values(todo_data).returning(todos_table)
        row = self.db_client.insert_todo(query)

        return row
    
    def update_todo(self, todo_data);
        query = todos_table.update().values(todo_data).returning(todos_table)
        row = self.db_client.update_todo(query)
        return row

    def get_all_sub_todo(self):
        query = sub_todos_table.select()
        rows = self.db_client.get_all_todo(query)
        if not rows:
            raise
        return rows

    def insert_sub_todo(self, sub_todo_data);
        query = sub_todos_table.insert().values(sub_tododata).returning(sub_todo_table)
        row = self.db_client.insert_todo(query)
        return row


    def update_sub_todo(self, sub_todo_data);
        query = sub_todo_table.update().values(sub_tododata).returning(sub_todo_table)
        row = self.db_client.update_todo(query)
        return row


    def get_all_user(self):
        query = user_table.select()
        rows = self.db_client.get_all_todo(query)
        if not rows:
            raise
        return rows



    def insert_user(self, user_data);
        query = user_table.insert().values(user_data).returning(user_table)
        row = self.db_client.insert_todo(query)
        return row


        def update_user(self, user_data);
        query = user_table.update().values(user_data).returning(user_table)
        row = self.db_client.update_todo(query)
        return row

        













 
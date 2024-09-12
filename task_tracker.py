import datetime, json, sys
from config import get_config

class TaskTracker():
    def __init__(self, environment="production"):
        """Class entry point"""
        self.config = get_config(environment)

    def init(self):
        if (len(sys.argv) == 1):
            print("Usage: path/to/main.py [command]\n")
            print("Available commands\n")
            print("add                 Add a task to the list")
            print("update              Update a task")
            print("delete              Delete a task")
            print("mark-in-progress    Mark a task in progress")
            print("mark-done           Mark a task done")
            print("list                List all tasks")
            print("list-done           List all done tasks")
            print("list-not-done       List all not done tasks")
            print("list-in-progress    List all in progress tasks")
        else:
            option = sys.argv[1]

            if option == "add":
                self.add()
            elif option == "update":
                self.update()
            elif option == "delete":
                self.delete()
            elif option == "mark-in-progress":
                self.mark_in_progress()
            elif option == "mark-done":
                self.mark_done()
            elif option == "list":
                self.list()
            elif option == "list-done":
                self.list_done()
            elif option == "list-not-done":
                self.list_not_done()
            elif option == "list-in-progress":
                self.list_in_progress()
            else:
                print("This command is not available")

    def write_file(self, data):
        """
        Open the file in write mode and dump the content into it. If the file doesn't exists, it'll be created
        """
        with open(self.config["file_name"], mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add(self):
        """
        Add a new task. Arguments:
        - 0) File
        - 1) add
        - 2) description
        """
        try:
            if (len(sys.argv) > 3):
                print("You must to use quotation marks to enclose the description")
            else:
                description = sys.argv[2]
                task = {
                    "id": None,
                    "description": description,
                    "status": "todo",
                    "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            
                with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                    data = json.load(file)

                if len(data) > 0:
                    id = data[-1]["id"] + 1
                    task["id"] = id
                    data.append(task)

                    self.write_file(data)
        except IndexError:
            print("You must to input the task description")
        except FileNotFoundError:
            task["id"] = 1
            tasks_list = [task]
            self.write_file(tasks_list)

    def update(self):
        """
        Update a task. Arguments:
        - 0) File
        - 1) update
        - 2) Id
        - 2) description
        """
        try:
            if (len(sys.argv) > 4):
                print("You must to use quotation marks to enclose the description")
            else:
                id = sys.argv[2]
                description = sys.argv[3]

                with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                    data = json.load(file)

                for task_index, task_value in enumerate(data):
                    if data[task_index]["id"] == int(id):
                        data[task_index]["description"] = description
                        data[task_index]["updated_at"]= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        break

                self.write_file(data)
        except IndexError:
            print("You must to input all parameters. Example: update [task_id] [task_description]")
        except FileNotFoundError:
            print("File not found")
        
    def delete(self):
        """
        Delete a task. Arguments:
        - 0) File
        - 1) delete
        - 2) Id
        """
        try:
            if (len(sys.argv) > 3):
                print("You must to input all parameters. Example: delete [task_id]")
            else:
                id = sys.argv[2]

                with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                    data = json.load(file)

                for task_index, task_value in enumerate(data):
                    if data[task_index]["id"] == int(id):
                        del data[task_index]
                        break
                
                self.write_file(data)
        except IndexError:
            print("You must to input all parameters. Example: delete [task_id]")
        except FileNotFoundError:
            print("File not found")

    def mark_in_progress(self):
        """
        Update a task marking it as in progress. Arguments:
        - 0) File
        - 1) mark-in-progress
        - 2) Id
        """
        try:
            if (len(sys.argv) > 3):
                print("You must to input all parameters. Example: delete [task_id]")
            else:
                id = sys.argv[2]

                with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                    data = json.load(file)

                for task_index, task_value in enumerate(data):
                    if data[task_index]["id"] == int(id):
                        data[task_index]["status"] = "in-progress"
                        data[task_index]["updated_at"]= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        break

                self.write_file(data)
        except IndexError:
            print("You must to input all parameters. Example: delete [task_id]")
        except FileNotFoundError:
            print("File not found")

    def mark_done(self):
        """
        Update a task marking it as done. Arguments:
        - 0) File
        - 1) mark-done
        - 2) Id
        """
        try:
            if (len(sys.argv) > 3):
                print("You must to input all parameters. Example: delete [task_id]")
            else:
                id = sys.argv[2]

                with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                    data = json.load(file)

                for task_index, task_value in enumerate(data):
                    if data[task_index]["id"] == int(id):
                        data[task_index]["status"] = "done"
                        data[task_index]["updated_at"]= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        break

                self.write_file(data)
        except IndexError:
            print("You must to input all parameters. Example: delete [task_id]")
        except FileNotFoundError:
            print("File not found")

    def list(self):
        """
        List all tasks. Arguments:
        - 0) File
        - 1) list
        """
        try:
            with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                data = json.load(file)

            print("id / Description / status / created / updated")

            for task in data:
                print(f"{task["id"]} / {task["description"]} / {task["status"]} / {task["created_at"]} / {task["updated_at"]}")

            self.write_file(data)
        except FileNotFoundError:
            print("File not found")

    def list_done(self):
        """
        List all done tasks. Arguments:
        - 0) File
        - 1) list-done
        """
        try:
            with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                data = json.load(file)

            print("id / Description / status / created / updated")

            for task in data:
                if task["status"] == "done":
                    print(f"{task["id"]} / {task["description"]} / {task["status"]} / {task["created_at"]} / {task["updated_at"]}")

            self.write_file(data)
        except FileNotFoundError:
            print("File not found")

    def list_not_done(self):
        """
        List all not done tasks. Arguments:
        - 0) File
        - 1) list-not-done
        """
        try:
            with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                data = json.load(file)

            print("id / Description / status / created / updated")

            for task in data:
                if task["status"] == "todo":
                    print(f"{task["id"]} / {task["description"]} / {task["status"]} / {task["created_at"]} / {task["updated_at"]}")

            self.write_file(data)
        except FileNotFoundError:
            print("File not found")

    def list_in_progress(self):
        """
        List all in progress tasks. Arguments:
        - 0) File
        - 1) list-not-done
        """
        try:
            with open(self.config["file_name"], mode="r", encoding="utf-8") as file:
                data = json.load(file)

            print("id / Description / status / created / updated")

            for task in data:
                if task["status"] == "in-progress":
                    print(f"{task["id"]} / {task["description"]} / {task["status"]} / {task["created_at"]} / {task["updated_at"]}")

            self.write_file(data)
        except FileNotFoundError:
            print("File not found")
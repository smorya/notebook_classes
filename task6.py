""" Notebook realisation"""
import datetime
class Note:
    """
    Combines o=all details of the note.
    """
    def __init__(self, memo, creation_date, tags):
        '''
        Inits attributes.
        '''
        self.memo = memo
        self.creation_date = creation_date
        self.tags = tags

    def match(self,search_filter:str)-> bool:
        """
        Returns bool whether the filter is in the note or no.
        """
        if search_filter in self.memo:
            return True
        else:
            return False

class Notebook:
    """
    Navigates th eprocesses inside the notebook.
    """

    def __init__(self, notes=None):
        """
        Inits attributes needed
        """
        self.notes = notes
        self.notes = []

    def search(self,filterr:str):
        """
        Gives to specific notes a command to search filter prases and gives a result.
        """
        found_notes = []
        for id, note in enumerate(self.notes):
            if Note.match(note, filterr) == True:
                found_notes.append(id)
        if len(found_notes) != 0:
            print("Your phrase was found in these notes")
            print(found_notes)
        else:
            print( "No notes were found")

    def new_note(self, memo, tags=''):
        """
        Creates a new note.
        """
        date = datetime.date
        note = Note(memo, date, tags)
        self.notes.append(note)

    def modify_memo(self, note_id, memo):
        """
        Modifies the information inside the memo
        """
        self = self.notes[int(note_id)]
        self.memo = self.memo + memo
    def modify_tags(note_id, tags):
        """
        Modifies the tags.
        """
        self = Notebook.search(self,note_id)
        self.tags = tags


class CommandOption:
    def func():
        """
        Just quits. She is useless, but I had to leave her.
        """
        quit()

class Menu:
    """
    Main menu of notebook
    """
    def program(self):
        """
        Mecahism of program's work.
        """
        print("""Greetings""")
        while True:
            print("""
    press 1 to search a note through specific phrase
    press 2 to make new note
    press 3 to modify previous notes
    press 4 to modify tags
    press <quit> to quit
    """)
            answer = input(">>> ")
            if answer =='1':
                print("Text a phrase to search")
                filterr = input(">>> ")
                Notebook.search(self, filterr)
                print("The action is done.")


            elif answer =='2':
                print("Enter tags for a note")
                tags = input(">>> ")
                print("Text everything for note here. When done, press enter two times.")
                lines =[]
                while True:
                    line = input()
                    if line:
                        lines.append(line)
                    else:
                        break
                memo = '\n'.join(lines)
                Notebook.new_note(self, memo, tags)
                print("The action is done.")


            elif answer =='3':
                print("Search for note by the id.")
                note_id = input(">>> ")
                print("Add new text")
                lines =[]
                while True:
                    line = input()
                    if line:
                        lines.append(line)
                    else:
                        break
                memo = '\n'.join(lines)
                Notebook.modify_memo(self, note_id, memo)
                print("The action is done.")


            elif answer =='4':
                print("Search for note by the id.")
                note_id = input(">>> ")
                print("Enter new tags for a note")
                new_tags = input(">>> ")
                Notebook.modify_tags(self, note_id, new_tags)
                print("The action is done.")

            elif answer == "quit":
                print("Thanks for choosing us.Bye!")
                CommandOption.func()
            else:
                print("Enter valid answer")

if __name__ == "__main__":
    notebook = Notebook()
    Menu.program(notebook)


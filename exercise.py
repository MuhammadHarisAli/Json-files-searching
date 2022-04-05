import json
class Search():
    def __init__(self):
        # Consttructor to initialize the base object with all the fields needed
        with open('users.json', 'r') as f:
          self.data_user = json.load(f)
        with open('tickets.json', 'r') as f:
          self.data_ticket = json.load(f)
        with open('organizations.json', 'r') as f:
          self.data_organization = json.load(f)
        try:
            self.user_fields = self.data_user[0].keys()
        except Exception as IndexError:
            self.user_fields = []
        try:
            self.tickets_fields = self.data_ticket[0].keys()
        except Exception as IndexError:
            self.tickets_fields = []
        try:
            self.organization_fields = self.data_organization[0].keys()
        except Exception as IndexError:
            self.organization_fields = []

    @staticmethod
    def searchOptions():
        print('1 for users, 2 for tickets, 3 for organizations and 4 for main menu')
        user_input_search_option = raw_input("Input: ")
        return user_input_search_option

    def searchUserJson(self, user_search_item, user_search_value):
        Search.findValue(self.data_user, user_search_item, user_search_value)

    def searchTicketJson(self, user_search_item, user_search_value):
        Search.findValue(self.data_ticket, user_search_item, user_search_value)

    def searchOrganizationJson(self, user_search_item, user_search_value):
        Search.findValue(self.data_organization, user_search_item, user_search_value)

    def getSearchInput(self):
        # get atttribue and value from user in for any fields
        user_search_item = raw_input("Search Item: ")
        user_search_value = raw_input("Search Value: ")
        print("*****************")
        if user_search_value.isdigit():
            user_search_value = int(user_search_value)
        elif user_search_value.lower() == 'true':
            user_search_value = True
        elif user_search_value.lower() == 'false':
            user_search_value = False
        return user_search_item, user_search_value

    @staticmethod
    def printFields(fields):
        # print menu for files fields
        for keys in list(fields):
            print(keys)

    @staticmethod
    def findValue(obj_to_iterate, user_search_item, user_search_value):
        # find values in related json files objects which user has selected
        if not user_search_item:
            return
        if isinstance(user_search_value, str):
            user_search_value = user_search_value.decode('utf-8')
        for data in obj_to_iterate:
            try:
                if isinstance(data[user_search_item], list) and user_search_value in data[user_search_item]:
                    print(data)
                elif data[user_search_item] == user_search_value:
                    print(data)
            except Exception as KeyError:
                continue


def main():
    while True:
        obj = Search()
        print('Welcome To Search System')
        print('Press 1 to Search')
        print('Press 2 to get search fields')
        print('type quit to exit this task')
        print("*****************")
        user_input = raw_input("Input:")
        if user_input == 'quit':
            break
        elif user_input == '1':
            user_input_search_option = obj.searchOptions()
            if user_input_search_option == '1':
                user_search_item, user_search_value = obj.getSearchInput()
                obj.searchUserJson(user_search_item, user_search_value)
            elif user_input_search_option == '2':
                user_search_item, user_search_value = obj.getSearchInput()
                obj.searchTicketJson(user_search_item, user_search_value)
            elif user_input_search_option == '3':
                user_search_item, user_search_value = obj.getSearchInput()
                obj.searchOrganizationJson(user_search_item, user_search_value)
            else:
                continue

        elif user_input == '2':
            print('user_fields')
            obj.printFields(obj.user_fields)
            print("*****************")
            print('tickets_fields')
            obj.printFields(obj.tickets_fields)
            print("*****************")
            print('organization_fields')
            obj.printFields(obj.organization_fields)
            print("*****************")

if __name__ == "__main__":
    main()





from collections import UserString


class SearchingString(UserString):
    def find_all(self, substring):
        found_indexes = []
        ?

        while index < len(self.data):
            index = self.data.find(substring, index)
            if index == -1:
                break
            found_indexes.append(index)
            index += len(substring)

        return found_indexes
        


search_string = SearchingString('Hellolo Hello Hello')
print('Hellolo Hello Hello'.find('lo'))
print(search_string.find_all('lo'))
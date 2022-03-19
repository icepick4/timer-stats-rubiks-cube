from pages.menu import mainMenu
from variables import date
import json

def main():
    mainMenu()

    
    #########WRITING IN JSON DATA##################
    # with open("data.json", "r") as f:
    #     data = json.load(f)
    # data['2x2'].append({"time": 18, "date":date})
    # print(len(data['2x2']))
    # with open("data.json", "w") as f:
    #     json.dump(data, f, indent=4)
if __name__ == "__main__":
    main()

import re #more like import the fukken antichrist

keyword_list = ['kurwa', 'ja', '9gag', 'vo', 'bitch', 'kom dan', 'jonko', 'broer', 'dominion', 'any', 'urwa', 'drunu', 'fietsen', 'lopen', 'PAAL', 'kanker']

def History_to_data(name, path_to_history, group_name = "private"):
    """This will create a txt file with only the times and dates that dennis 
    fucking send you a 9gag link.
    name: str, name of dennis in your whatsapp history
    path_to_history: str, path to whatsapp.txt history file
    save_path: str, will save the clean history at this path. Default is clean.txt
    group_name: str, specify the group name. If the data is not from a group simply leave open."""                     
    history = open(path_to_history, 'r', encoding='utf-8')
    text = history.read()
    f = open("saved_history.txt", 'w')
    
    date_regex = "(\d{1,2}[\W\D]\d{1,2}[\W\D](?:\d{4}|\d{2}))[\W\D]+(\d{1,2}[\W\D]\d{1,2})[\W\s]+"
    for keyword in keyword_list: #various keyword check
        reg_ex = (date_regex+ name +":[^\n]+(" + keyword +
                  ")[^\n]+\n"+date_regex +"([^:]+):")
        filtered_history = re.findall(reg_ex, text)

        for line in filtered_history:
            f.write(','.join(line) + ','+ group_name + '\n')
            
    #check if 9gag got posted from android
    reg_ex =  (date_regex + name +
               ":[^\n]+9gag.com[^\n](android)[^\n]+\n" + date_regex +"([^:]+):")
    
    filtered_history = re.findall(reg_ex, text)
    
    for line in filtered_history:
        f.write(','.join(line) + ',' + group_name + '\n')
    f.close()
    
    history.close()
    
    return

name = input("Exact naam van dennis in je whatsapp: ")
path_data = input("Name of the data file (protip: rename it to 1.txt by hand :P): ")
group_data = input("Name of the group the data is from. If its a 1on1 conversation type private: ")
History_to_data(name, path_data, group_data)
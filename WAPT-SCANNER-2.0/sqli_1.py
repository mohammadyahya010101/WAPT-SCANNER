from bs4 import BeautifulSoup
import urllib
import mechanize,sys

url = sys.argv[1]

print("""
    ###############################################################
                        SQLI VULNERABILITY SCANNER              
    ###############################################################
     """)
def create_report(sqli_data):
    Write_file('sqli_1.txt', sqli_data)

def Write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def Sqli_scanner():
    #Verify if site is vulnerable or not?
    url1 = url+"'"
    html = urllib.urlopen(url+"'")
    bt = BeautifulSoup(html.read(),"lxml")
    if "You have an error in your SQL syntax" in bt.get_text():
        create_report(" URL IS VULNERABLE WITH SQL INJECTION "+url1)
        print('\n')
        exit()
    else:
        create_report(" URL IS NOT VULNERABLE WITH SQL INJECTION "+url1)
        print('\n')
        exit()
    """
    print("Finding Total number of tables..........")
    #Start Exploting SQL vulnerability...
    html = urllib.urlopen(url+"' "+"--+")
    bt = BeautifulSoup(html.read(), "lxml")
    if "You have an error in your SQL syntax" in bt.get_text():
        html2 = urllib.urlopen(url+"--")
        bt2 = BeautifulSoup(html2.read(), "lxml")
        if "You have an error in your SQL syntax" in bt2.get_text():
            print("This sql Vulnerability is can't be exploit by this tool wait for next version to or else try manually.")
            create_report("This sql Vulnerability is can't be exploit by this tool wait for next version to or else try manually.")
        # -- ORDER BY
        else:
            i=1
            while True:
                #Order by testing url type
                order_url = url+" ORDER BY "+str(i)+"--"
                html3 = urllib.urlopen(order_url)
                bt3 = BeautifulSoup(html3.read(), "lxml")
                if "Unknown column" in bt3.get_text():
                    break
                else:
                    i = i+1
            No_of_columns = i-1
            print(" Number of Columns: "+No_of_columns)
            #lets find vulnerable columns from total number of tables
            #vuln_column_url = url[:url.find('=')+1] + '-' + url[url.find('=')+1:] + " UNION SELECT "+ str(range(1,NO_of_tables+1)) + "--"
            #vuln_column_url = url + " UNION SELECT "+"--"
            #html4 = urllib.urlopen(vuln_column_url)
            #bt4 = BeautifulSoup(html4.read(), "lxml")
            #if "Not Acceptable! This error was generated by Mod_Security." in bt4.get_text():
             #   print("Above Given Url Have Mod Security Enable Please Wait for our next Version of this tool or else try manually.")
    
    # --+ ORDER BY
    else:
        i=1
        while True:
            #Order by testing url type
            order_url = url+" ORDER BY "+str(i)+"--"
            html3 = urllib.urlopen(order_url)
            bt3 = BeautifulSoup(html3.read(), "lxml")
            if "Unknown column" in bt3.get_text():
                break
            else:
                i = i+1
        No_of_columns = i-1
        print(" Number of Columns: "+No_of_columns)        
    """
try:        
    Sqli_scanner()
except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
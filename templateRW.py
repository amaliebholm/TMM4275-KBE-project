f = open("K:\\Biblioteker\\Dokumenter\\Skole\\Automatisering\\TMM4275-KBE-project\\DFAs\\templates\\My_Chair_template.dfa", "r")
fileContent = f.read()
f.close()


#Set in parameters.
fileContent = fileContent.replace("<PARAM_SIDE>", "1234")
fileContent = fileContent.replace("<PARAM_DEPTH>", "1000")
fileContent = fileContent.replace("<PARAM_WIDTH>", "900")
fileContent = fileContent.replace("<PARAM_HEIGHT>", "800")


#Let's write the file
f = open("K:\\Biblioteker\\Dokumenter\\Skole\\Automatisering\\TMM4275-KBE-project\\DFAs\\My_Chair_210213.dfa", "w")
f.write(fileContent)
f.close()


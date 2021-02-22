# Reading the template file
f = open("C:\\Users\\Amalie\\Documents\\GitHub\\TMM4275-KBE-project\\DFAs\\templates\\Colored_Block_DYN_210200.dfa", "r")
txt = f.read()
print("before:", txt)

#Request from KB for the cube side
# Take length from cube_1
param1_val = data['results']['bindings'][0]['side']['value']
# Take height from cube_2
param2_val = data['results']['bindings'][1]['side']['value']
# Take width from cube_3
param3_val = data['results']['bindings'][2]['side']['value']


#Replacement section for L_PARAM, W_PARAM, H_PARAM acording to cube side
txt = txt.replace("<L_PARAM>", param1_val)
txt = txt.replace("<W_PARAM>", param2_val)
txt = txt.replace("<H_PARAM>", param3_val)

#Writing to the correct location
f = open("C:\\Users\\Amalie\\Documents\\GitHub\\TMM4275-KBE-project\\DFAs\\templates\\Colored_Block_DYN_210200.dfa", "w")
f.write(txt)
f.close()

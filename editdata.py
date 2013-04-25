#!/usr/bin/env python
#This program updates the data file based on user preference
import json
inp_json = {"felicity": {
            "text": "felicity is the annual cultural-technical festival of iiit-hyderabad. With more than 65 countries participating in the events and competitions makes this one of the largest festivals around", 
            "meta": "some fest,south asia,college fest", 
            "tagset":"fest,college fest,felicity",
            "location": {
                "text": "iiit-h", 
                "tagset":  "location,place,where",    
                },  
                "time": {
                "text": "tba", 
                "tagset":"when,time"
            }   
    
             }   
}
   
def read_json():
  json_data = open ("Data_json", "r").read().strip('\n')
  dic_json = json.loads(json_data)
  return dic_json

def get_tags (tagset):
  tagset = str(tagset)
  lst =  tagset.split(',')
  for i in range(len(lst)):
    lst[i].strip()
  return lst

def check_in_tagset (item, dic):
  present = False
  tag_list = []
  head_tag = None
  d_comp = {}
  for elm in dic:
    if type(dic[elm]) == type(d_comp):
      if 'tagset' in dic[elm]:
        tag_list =  get_tags (dic[elm]['tagset'])
        if item in tag_list:
          present = True
          head_tag = elm
          break
  return (present, head_tag)


def update(dic_source, dic_dest):
  exists = True
  head_key = None

  d_comp = {} #just a sample dictionary to compare the type with
  if type(dic_source) !=  type(d_comp):
    return

  for item in dic_source:
    if item in dic_dest:
      exists = True
      head_key = item
    else:
      (exists, head_key) = check_in_tagset (item, dic_dest) #called when the name of the items doesn't match directly in source and destination

    if exists == False:
      dic_dest[item] = dic_source[item]
    else:
      if type(dic_dest[head_key]) != type(d_comp):
        dic_dest[head_key] += "," + str(dic_source[item]) 

	temp_list1 = dic_dest[head_key].split(',')
	temp_list2 = dic_source[item].split(',')
	temp_list1 += temp_list2
	for i in range(len(temp_list1)):
	  temp_list1[i].strip()
	  temp_list1[i] = str(temp_list1[i])

	dic_dest[head_key] = (',').join(set(temp_list1))
	
      update (dic_source[item], dic_dest[head_key]) #recursive call


  
	  
def init():
 return 

def main():
  init()
  dic_json = read_json()
  update (inp_json, dic_json['logical'])
  fp=open('Data_json','w')
	
  fp.write(json.dumps (dic_json, sort_keys=True, indent=4))

if __name__ == "__main__":
  main()

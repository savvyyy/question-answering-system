import json
import requests

data_path = '/home/itadmin/Desktop/reviews_data.txt'

# with open(data_path, 'r') as outfile:
#     data = json.load(outfile)

fh = open(data_path, errors='ignore')
formatted_data = []
final_data = []
data = {}
index = 0
for line in fh:
    formatted_data.append(line)
fh.close()

for i in range(0, len(formatted_data)):
    data['id'] = index
    data['snippet'] = formatted_data[i]
    index += 1
    final_data.append(data.copy())


    

# print('data', formatted_data)

# headers = {('Content-Type', 'application/json')}

r = requests.post('http://localhost:8983/solr/techproducts/update?commit=true', json=final_data)


# d = requests.get('http://localhost:8983/solr/techproducts/select?q=*excellent*&wt=json')

# dt = d.json()['response']['docs']

# for i in range(0, len(dt)):
#     print('data', dt[i]['snippet'])































# solr = SolrClient('http://localhost:8983/solr')
# res = solr.query('sample_techproducts_configs', {
#     'q': 'Thief',
#     'facet':True,
#     'facet.field':'facet_test',
# })
# res.get_results_count()
# print('ok')
# res.docs
# print('okok')

# jsonFile = '/home/itadmin/Desktop/sample.json'


# r = requests.post('http://localhost:8983/solr/sample_techproducts_configs/update?commit=true', data = jsonFile, headers={'Content-Type: application/json'})
# print (response.status_code)



# connection = urlopen('http://localhost:8983/solr/sample_techproducts_configs/select?q=Aditya&wt=json')
# response = json.load(connection)
# data = json.dumps(response['response']['docs'])
# print(data)
# print(type(data))
# print (response['response']['numFound'], "documents found.")

# for document in response['response']['docs']:
#     print ("Name =", document['name'])

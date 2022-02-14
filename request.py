import requests

post1 = requests.post('http://localhost:8080')
print(post1.text)
out = post1.text
start_idx = out.find('{')+2
end_idx = out.rfind(':')-1
delete_value = out[start_idx: end_idx]
print("delete_value", delete_value)

post2 = requests.post('http://localhost:8080')
print(post2.text)

get1 = requests.get('http://localhost:8080')
print(get1.text)

delete_out = requests.delete('http://localhost:8080/' + delete_value)
print(delete_out.text)

get2 = requests.get('http://localhost:8080')
print(get2.text)

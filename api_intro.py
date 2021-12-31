import requests

count = input('How many CAT facts would you like? ')

response = requests.get("https://catfact.ninja/facts?max_length=60&limit=",count)
data = response.json()

a = 0

while a < int(count):
    print(a+1, ': ', data['data'][a]['fact'])
    a += 1

# a = 10
# b = 0

# while b<10:
#     print(b+1, ': ', data['data'][b]['fact'])
#     b+=1
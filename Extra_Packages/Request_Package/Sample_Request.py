import urllib.request

url = "https://www.cnn.com"  # Replace with your actual URL
try:
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()
        print(data)  # This will print the HTML content of the page
except urllib.error.HTTPError:
    print('HTTP request failed')
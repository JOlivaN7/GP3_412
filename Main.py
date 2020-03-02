### Import data and read,...


import urllib.request


### Pull data from AWS database
def main():
  webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
  print("result: " + str(webUrl.getcode()))
  data = webUrl.read()
  print(data)

if __name__ == "__main__":
  main()

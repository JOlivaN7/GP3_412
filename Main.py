### Import data and read,...


from urllib.request import urlopen


### Pull data from AWS database

AWSurl = "https://s3.amazonaws.com/tcmg476/http_access_log"
data1 = urlopen(AWSurl)
strData = data1.read()
s1 = str(strData, encoding = 'utf-8')
OutP = open("AWSoutput.txt", "w")

#for line in s1:
 #   fields = line.split("local")
  #  OutP.write(type)

#m = s1.split("local", 2)
OutP.write(s1)


OutP.close()


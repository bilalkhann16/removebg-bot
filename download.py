
image_url= "https://o.remove.bg/downloads/6e118512-00d3-4f22-a79a-239bb0efdab9/andrew_selfie-removebg-preview.png"
import urllib.request

# Adding information about user agent
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0')]
urllib.request.install_opener(opener)


# setting filename and image URL
filename = image_url.split("/")[-1]
# image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"

# calling urlretrieve function to get resource
urllib.request.urlretrieve(image_url,filename)
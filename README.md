# PyYtX
[PyYtX](https://pypi.org/project/PyYtX) Simple Python Library to Get Details About a Youtube Video.

# Installation
Installation is pretty easy. Run the following command to install PyYtX
```
pip3 install PyYtX
```

## Currently Supporting Features,
- Get Thumbnail Urls From a Youtube Video
- Downlaod Thumbnails From Youtube Video or Thumbnail Url

More Features Coming Soon...

# Examples
Here are some examples to get started.
#### To Get Thumbnail Urls
```python
from PyYtX import PyYtX

# Your Youtube Url here
url = "https://youtu.be/VaybjAk3dEY"

# max_thumb = Thumbnail with the maximum quality
# standered_thumb = Thumbnail with the standard quality
max_thumb, standered_thumb = PyYtX.get_thumb(url)

print(f"Best Thumbnail Url: {max_thumb} \nStandard quality: {standered_thumb}")
```
#### Download Youtube Thumbnail Urls
**Example 1.1 - Download Thumbnail by It's Url,**
```python
from PyYtX import PyYtX

# Your Youtube Thumbnail Url here
url = "https://img.youtube.com/vi/O9UgaCWN2Ag/maxresdefault.jpg"
# Create a url list
url = [url]

# Now Download the thumbnails in "url" list
# Default path is 'pyytx_img'. You can change it, see Example 2
PyYtX.download_thumbs(url)
```
**Example 1.2 - Download Thumbnail by It's Url to a Specific Folder,**
```python
from PyYtX import PyYtX

# Enter Your Youtube Thumbnail Url here
url = "https://img.youtube.com/vi/O9UgaCWN2Ag/maxresdefault.jpg"
# Enter Your Folder Here
path = "/home/itzfork/PyYtX_Images"
# Create a url list
url = [url]

# Now Download the thumbnails in "url" list to 'PyYtX_Images' Folder
PyYtX.download_thumbs(url, path=path)
```

</br>

**Example 2.1 - Download Thumbnails by Youtube Video Url**
```python
from PyYtX import PyYtX

# Your Youtube Video Url here
url = "https://www.youtube.com/watch?v=O9UgaCWN2Ag&pp=sAQA"
# Now get thumbnial urls. To Know about resolutions see 'Example 1.1'
max_thumb, standered_thumb = PyYtX.get_thumb(url)
# Create a url list You can choose which one you want to download
# I'll choose 'max_thumb'. You can download both if you want
url = [max_thumb]

# Now Download the thumbnails in "url" list
# Default path is 'pyytx_img'. You can change it, see Example 2
PyYtX.download_thumbs(url)
```
**Example 2.2 - Download Thumbnail by Youtube Video Ur to a Specific Folder,**
```python
from PyYtX import PyYtX

# Your Youtube Video Url here
url = "https://www.youtube.com/watch?v=O9UgaCWN2Ag&pp=sAQA"
# Now get thumbnial urls. To Know about resolutions see 'Example 1.1'
max_thumb, standered_thumb = PyYtX.get_thumb(url)
# Create a url list You can choose which one you want to download
# I'll choose 'max_thumb'. You can download both if you want
url = [max_thumb]
# Enter Your Folder Here
path = "/home/itzfork/PyYtX_Images"

# Now Download the thumbnails in "url" list to 'PyYtX_Images' Folder
PyYtX.download_thumbs(url, path=path)
```

</br>

**Example 3 - Download Thumbnails while extracting Thumbnail Urls,**
</br>Don't try to Extract thumbnail urls with this!
```python
from PyYtX import PyYtX

# Your Youtube Url hee
url = "https://youtu.be/VaybjAk3dEY"

# Now download Thumbnails. This will download both
# For Custom Paths See Above Examples
PyYtX.get_thumb(url, download=True)
```

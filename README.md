# PyYtX
[PyYtX](https://pypi.org/project/PyYtX) Simple Python Library to Get Details About a Youtube Video.

# Installation
Installation is pretty easy. Run the following command to install PyYtX
```
pip3 install PyYtX
```

## Currently Supporting Features,
- Get Thumbnail Urls From a Youtube Video

More Features Coming Soon...

# Examples
Here are some examples to get started.
#### To Get Thumbnail Urls
```python
from PyYtX import PyYtX

# Your Youtube Url hee
url = "https://youtu.be/VaybjAk3dEY"

# max_thumb = Thumbnail with the maximum quality
# standered_thumb = Thumbnail with the standard quality
max_thumb, standered_thumb = PyYtX.get_thumb(url)

print(f"Best Thumbnail Url: {max_thumb} \nStandard quality: {standered_thumb}")
```

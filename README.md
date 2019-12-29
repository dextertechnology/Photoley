# Introduction
Photoley is an [Unsplash](https://unsplash.com/) random image grabbing cli based application.

# Installation
## Using pip
```
pip install https://github.com/dextertechnology/Photoley/archive/photoley-1.0.0.tar.gz
```
## Using source
```
git clone https://github.com/dextertechnology/Photoley.git \
&& cd Photoley \
&& make build \
&& make install \
&& make clean
```
Pyinstaller is also configured, if required to install using pyinstaller.
# Usage
```photoley [options] [options]```  

__Random Image without parameter__
```
photoley
```

__Image from specific user__
```
photoley -u <username>
```

__Image from specific collection__
```
photoley -c <collection_id>
```

__Image of specific resolution__
```
photoley -r <WIDTHxHEIGHT>
```

__Search term__  
Narrow down random by comma-separated random search-term
```
photoley -q <term>,<term>
```

__Use multiple options__
```
photoley -q nature,animals -u mischievous_penguins
```

# Contribution
This is an open source project and all the contribution will be accepted with warm heart. Happy Coding :)
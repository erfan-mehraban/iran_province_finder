# Iran Province Finder

python3 library for finding province of iran correspond to latitude and longtitude

currently supporting 31 province.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

```bash
$ pip3 install git+https://github.com/erfan-mehraban/iran_province_founder
```

### Configure

Change ```provinces_polygons.py``` and ```province``` array and modify second item of tuple to return that item if correspond province found

### Usage

Import it by:

```python3
from iran_province_finder.province_finder import find_province
```

And use ```find_province``` funtion whenever you want:

```python3
print(find_province(39.534530, 44.592775))
```

## Built With

* [Python3](http://www.dropwizard.io/1.0.2/docs/)
* [Shapely](https://pypi.org/project/Shapely/) - BSD-licensed Python package for manipulation and analysis of planar geometric objects

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## TODO

* class based instead of module based
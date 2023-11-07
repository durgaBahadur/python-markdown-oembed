# Python Markdown oEmbed

## Installation

    pip install from python_markdown-oembed_extension

## Links

- [python_markdown-oembed_extension](https://github.com/Hopiu/python-markdown-oembed)
- [Markdown](http://daringfireball.net/projects/markdown/)
- [oEmbed](http://www.oembed.com/)
- [python-oembed](https://github.com/abarmat/python-oembed)

## Development

This project uses flit as packaging tool.

### Install flit

```
pip install flit
```

### Build needed packages for project

```
flit install
```

## Changelog

### 0.2.1

- add Slideshare endpoint (thanks to [anantshri](https://github.com/anantshri))

### 0.2.0

- backwards incompatible changes
    - allows arbitrary endpoints ([commit](https://github.com/Wenzil/python-markdown-oembed/commit/1e89de9db5e63677e071c36503e2499bbe0792da))
    - works with modern Markdown (>=2.6)
    - dropped support for python 2.6
- added support python 3.x

### 0.3.0

- Updated version of [python-markdown-oembed](https://github.com/rennat/python-markdown-oembed)
- Various small fixes and code modernizations.


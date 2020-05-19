## Please follow the guide below

- You will be asked some questions, please read them **carefully** and answer honestly
- Put an `x` into all the boxes [ ] relevant to your *pull request* (like that [x])
- Use *Preview* tab to see how your *pull request* will actually look like

---

### Before submitting a *pull request* make sure you have:
- [x] At least skimmed through [adding new extractor tutorial](https://github.com/ytdl-org/youtube-dl#adding-support-for-a-new-site) and [youtube-dl coding conventions](https://github.com/ytdl-org/youtube-dl#youtube-dl-coding-conventions) sections
- [x] [Searched](https://github.com/ytdl-org/youtube-dl/search?q=is%3Apr&type=Issues) the bugtracker for similar pull requests
- [x] Checked the code with [flake8](https://pypi.python.org/pypi/flake8)

### In order to be accepted and merged into youtube-dl each piece of code must be in public domain or released under [Unlicense](http://unlicense.org/). Check one of the following options:
- [x] I am the original author of this code and I am willing to release it under [Unlicense](http://unlicense.org/)
- [ ] I am not the original author of this code but it is in public domain or released under [Unlicense](http://unlicense.org/) (provide reliable evidence)

### What is the purpose of your *pull request*?
- [x] Bug fix
- [ ] Improvement
- [ ] New extractor
- [ ] New feature

---

### Description of your *pull request* and other information

This request fixes the problem identified in [issue #25311](https://github.com/ytdl-org/youtube-dl/issues/25311).

It changes the redtube.py extractor to correctly locate the json expression for mediaDescription on the webpage.

The referenced issue has more information.
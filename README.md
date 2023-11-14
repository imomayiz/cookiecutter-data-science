## cookiecutter-data-science
**A general template for any data science project.**

## Setup
```bash
pip install cookiecutter
```

## Use this template
```bash
cookiecutter https://github.com/imomayiz/cookiecutter-data-science.git
```
This template comes with configured precommits. Once you run the command above, pre-commit will automatically be installed if necessary. Any commit afterwards will trigger multiple checks (pylint, black, mypy, interrogate, isort..) related to your code.

## Template structure
```plain text
|   .env
|   .gitignore
|   README.md
|   requirements.txt
|   tree.txt
|   
+---data         <- gitignored
|   +---processed
|   \---raw
+---docs
+---models 
+---notebooks     <- Naming convention e.g. `1.0-initial-data-exploration`.
+---results
|   +---plots
|   +---reports
|   \---scores
+---secrets       <- gitignored
|       credentials.yaml
|       
+---src
        build_features.py
        make_dataset.py
        predict.py
        train.py
        utils.py
        __init__.py
\---tests         <- unit tests
```
# nlp_paraphrase

## About

This application takes syntax tree from GET request parameter "tree" and optionally parameter "limit". It return to you a list of paraphrased syntax trees in JSON format. Optional parameter "limit" used to limit the count of returned syntax trees, by default it's 20.

## Requirements

* Clone this git repository to your pc

* Open this project with your interpreter or IDE

* Run this command in your terminal to install required packages:
```
pip install -r requirements.txt
```

## How to run

* Run file "flask_api.py" in your interpreter or IDE, by default it uses 5000 port.
* Or you can type this command in your terminal:
```
flask --app flask_api run
```

* Copy this link to your browser: 
http://localhost:5000/paraphrase?tree=(S (NP (NP (DT The)(JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )

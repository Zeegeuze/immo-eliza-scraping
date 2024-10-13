# Immo Eliza

## Description
The real estate company "Immo Eliza" wants to develop a machine learning model to make price predictions on real estate sales in Belgium. They wnant help with the entire pipeline. Immoweb is a commonly used website for Belgian properties.

The task is to build a dataset that gathers information about at least 10000 properties all over Belgium. 

##  Repo structure
.
├── scraper/
│   ├── features.py
│   ├── optimiser.py
│   └── scraping.py
├── .gitignore
├── main.py
├── requirements.txt
└── README.md

## Usage
1. Clone the repository to your local machine.
2. To run the script, you can execute the main.py file from your command line:

```
python main.py
```

Due to the issues with Selenium, I have decided to start from a csv containing all needed links. 
The script reads the csv, after which we'll scrape the info from Immoweb. Later on it will be saved to a csv file in your data map.

## Personal situation
I had some issues doing this exercise. First at all, due to my computer being split with a separate Linux disk, we didn't manage to get Selenium working. I had a look with the coach which also didn't get it to work.

The second issue I had was trying to run the different pipelines in a separate file, the optimiser.py. I didn't manage to give an empty dataframe. The full dataframe with the urls passed without issues. As time run out, I just run it in the main.py.

## Timeline
It took me a week to finish this project, mainly due to issues with my split drive.

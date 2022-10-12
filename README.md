# combine-word-documents-with-docxtpl-workplan-in-python
Need To Create 100’s Of Workplan (word) Documents Automatically?
This article will show you how to create multiple docx documents at once at the click of a finger using python.


## Installation

To follow this project, go to your terminal or command line and type in.

```python3
pip install docxtpl
```


##  Default workplan template

Our default workplan template will look like this.


![my_workplan_template](https://user-images.githubusercontent.com/22924800/195295668-7a172b9d-8694-43e8-9c9f-aee0dc6ac87a.png)



## DEFAULT CODE using our default workplan template

```
from docxtpl import DocxTemplate

doc = DocxTemplate("my_word_template.docx")
context={'company_name':"World company"}
doc.render(context)
doc.save("generated_doc.docx")
```




## Real World Sample Usage 

```
from docxtpl import DocxTemplate

doc = DocxTemplate("my_workplan_template.docx")
context = {'workplan_number': "100", 'name':"John", 'location':"london"}
doc.render(context)
doc.save("hash_workplan_doc.docx")
```



### The result - Real World Sample Usage

![hash_workplan_doc docx](https://user-images.githubusercontent.com/22924800/195303101-618ff424-89b5-4322-90d8-dbdbaac013db.png)


## CREATING 200 WORKPLANS AT ONCE USING A CSV FILE




**CSV file will look like this**
![csv file workplan template](https://user-images.githubusercontent.com/22924800/195306289-7974a53b-bca9-4b11-afa7-56abb60a21d4.png)


**workplan template will look like this**
![200 csv documents](https://user-images.githubusercontent.com/22924800/195309098-36a14f34-88bf-4286-99dd-aa9e5a78e267.png)





# our 200 workplan done automatically with python….

![200 workplans done with python](https://user-images.githubusercontent.com/22924800/195309475-0c86d8a9-5251-4b00-b3c2-9c9025af56a5.png)


![200 workplans done with python 2](https://user-images.githubusercontent.com/22924800/195309545-0b6daef4-d871-44b6-af40-4ab856a2a0d2.png)




## How to use the API
**1) Install the requirements:**

    pip install -r requirements.txt
\
**2) Run the server in local:**

    uvicorn main:app --reload
\
**3) To make predictions:**
Send a POST request to **localhost:8000/predict** with a JSON in the body of the style:

    {'fecha_dia_de_la_semana':6, 'dcto':0.0, 'fecha_hora':3, 'dispositivo_os':'ANDROID', 'ID_USER':5}
   - "fecha_dia_de_la_semana": Int number. It represents the day of the week. Monday is denoted by 0 and ends on Sunday which is denoted by 6.
   - "dcto": Float number. It represents the discount.
   - "fecha_hora": Int number between 0 and 23. It's the hour without minutes.
   - "dispositivo_os": String variable. Contains the operating system, for example ANDROID or WEB.
   - "ID_USER": Int number. Unique customer code.
   
   Response:

    {"code": 200,
    "status": "success",
    "data": {
        "prediction": "1"}
    }

"1" represents Fraud. A postman collection is included which can be imported and made easy to consult.

\
**4) Replication of the exploratory and training process:**
To replicate the exploratory, clustering and classification process, the notebook called **"final_notebook.ipynb"** included in the folder **"replicate"** of the repository must be executed. The notebook is also available at the following link: [Notebook in Google Colab](https://drive.google.com/file/d/1X0gGIm7X4RLTt0UYNgLlMspTIL1CU5Wl/view?usp=sharing)
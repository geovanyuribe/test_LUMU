# **How to use the API** #

There are three ways to test the API:

1. **Cloud**: Testing the endoint deployed on GCP (*Google Cloud Run* especifically).
2. **Local**: Installing the requirements and running Uvicorn.
3. **Local**: Building the Docker image and running it on local.

&nbsp;

# **1.1.** Testing in **Cloud** : #

To test the endpoint deployed in Google Cloud Platform, you only have to send a POST request to the URL **https://test-lumu-ia7m4ghnua-uc.a.run.app/predict** with a body like:

    "{'fecha_dia_de_la_semana':6, 'dcto':0.0, 'fecha_hora':3, 'dispositivo_os':'ANDROID', 'ID_USER':5}"

   - "fecha_dia_de_la_semana": Int number. It represents the day of the week. Monday is denoted by 0 and ends on Sunday which is denoted by 6.
   - "dcto": Float number. It represents the discount.
   - "fecha_hora": Int number between 0 and 23. It's the hour without minutes.
   - "dispositivo_os": String variable. Contains the operating system, for example ANDROID or WEB.
   - "ID_USER": Int number. Unique customer code.

\
Inside the **folder called postman** is the **collection called test_LUMU.postman_collection.json**. You can also use the **request called test_CLOUD** that is included in it to test the endpoint with Postman.

&nbsp;

# **1.2.** Testing in **Local** (Uvicorn) : #

For this method you need to have **Python 3.7** or higher installed.

\
**1.2.1. Install the requirements:**

    pip install -r requirements.txt
\
**1.2.2. Run the server in local:**

    uvicorn main:app --port 8080 --reload
\
**1.2.3. To make predictions:**
Send a POST request to **http://localhost:8080/predict** with a JSON in the body of the style:

    "{'fecha_dia_de_la_semana':6, 'dcto':0.0, 'fecha_hora':3, 'dispositivo_os':'ANDROID', 'ID_USER':5}"

   - "fecha_dia_de_la_semana": Int number. It represents the day of the week. Monday is denoted by 0 and ends on Sunday which is denoted by 6.
   - "dcto": Float number. It represents the discount.
   - "fecha_hora": Int number between 0 and 23. It's the hour without minutes.
   - "dispositivo_os": String variable. Contains the operating system, for example ANDROID or WEB.
   - "ID_USER": Int number. Unique customer code.

\
Inside the **folder called postman** is the **collection called test_LUMU.postman_collection.json**. You can also use the **request called test_LOCAL** that is included in it to test the endpoint with Postman.

&nbsp;

# **1.3.** Testing in **Local** (Docker) : #

For this method you need to have **Docker 20.10.12** installed.

\
**1.3.1. Create the Docker image:**

    docker build -t test-lumu .
\
**1.3.2. Run the image in local:**

    docker run -p 8080:8080 test-lumu
\
**1.3.3. To make predictions:**
Send a POST request to **http://localhost:8080/predict** with a JSON in the body of the style:

    "{'fecha_dia_de_la_semana':6, 'dcto':0.0, 'fecha_hora':3, 'dispositivo_os':'ANDROID', 'ID_USER':5}"

   - "fecha_dia_de_la_semana": Int number. It represents the day of the week. Monday is denoted by 0 and ends on Sunday which is denoted by 6.
   - "dcto": Float number. It represents the discount.
   - "fecha_hora": Int number between 0 and 23. It's the hour without minutes.
   - "dispositivo_os": String variable. Contains the operating system, for example ANDROID or WEB.
   - "ID_USER": Int number. Unique customer code.

\
Inside the **folder called postman** is the **collection called test_LUMU.postman_collection.json**. You can also use the **request called test_LOCAL** that is included in it to test the endpoint with Postman.

&nbsp;
# **2.** Responses: #
   
A **good response** looks like:

    {"code": 200,
    "status": "success",
    "data": {
        "prediction": "1"}
    }
"1" represents fraud. A postman collection is included which can be imported and made easy to consult.

\
A **bad response** (in this case, 'dcto' variable doesn't have any value) looks like:

    {
        "code": 503,
        "message": {
            "INVALID REQUEST": "{'fecha_dia_de_la_semana':6, 'dcto':, 'fecha_hora':3, 'dispositivo_os':'ANDROID', 'ID_USER':5}",
            "TRY WITH A VALID REQUEST LIKE": "{'fecha_dia_de_la_semana':6, 'dcto':0.0, 'fecha_hora':3, 'dispositivo_os':'ANDROID', 'ID_USER':5}",
            "NOTE:": "The variables are fecha_dia_de_la_semana, dcto, fecha_hora, dispositivo_os and ID_USER (capital letter). All the variables should have values."
        }
    }


&nbsp;
# **3.** Replication of the exploratory and training process: #
To replicate the exploratory, clustering and classification process, the notebook called **"final_notebook.ipynb"** included in the folder **"replicate"** of the repository must be executed. The notebook is also available at the following link: [Notebook in Google Colab](https://drive.google.com/file/d/1X0gGIm7X4RLTt0UYNgLlMspTIL1CU5Wl/view?usp=sharing)
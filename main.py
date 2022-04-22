from fastapi import FastAPI, Request
import joblib
import pandas as pd

app = FastAPI()

@app.post("/predict")
async def get_body(request: Request):

    new_request = await request.json()

    try:
        new_request = eval(new_request)

        model = joblib.load("models/model.joblib")
        dummies_columns = joblib.load("models/dummies_columns.joblib")

        for i in new_request:
            new_request[i] = [new_request[i]]

        new_request = pd.DataFrame(new_request)

        new_request['fecha_dia_de_la_semana'] = new_request['fecha_dia_de_la_semana'].astype('category')
        new_request['fecha_hora'] = new_request['fecha_hora'].astype('category')
        new_request['dispositivo_os'] = new_request['dispositivo_os'].astype('category')
        new_request['ID_USER'] = new_request['ID_USER'].astype('category')

        new_request_dummies = pd.get_dummies(new_request)

        new_request_dummies = new_request_dummies.reindex(labels = dummies_columns, axis = 1, fill_value = 0)
        prediction = model.predict(new_request_dummies)

        return {"prediction":str(prediction[0])}
    
    except:
        return {"INVALID REQUEST": new_request,
        "TRY WITH A VALID REQUEST LIKE": "{'fecha_dia_de_la_semana':6, 'dcto':0.0, 'fecha_hora':3, 'dispositivo_os':'ANDROID', 'ID_USER':5}",
        "NOTE:":"The variables are fecha_dia_de_la_semana, dcto, fecha_hora, dispositivo_os and ID_USER (capital letter). All the variables should have values."}
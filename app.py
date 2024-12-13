from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from us_visa.pipline.prediction_pipeline import USvisaData, USvisaClassifier
from us_visa.pipline.training_pipeline import TrainPipeline
from uvicorn import run as app_run
from us_visa.constants import APP_HOST, APP_PORT
app = FastAPI()

# CORS settings
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body schema
class VisaPredictionRequest(BaseModel):
    continent: str
    education_of_employee: str
    has_job_experience: str
    requires_job_training: str
    no_of_employees: int
    region_of_employment: str
    prevailing_wage: float
    unit_of_wage: str
    full_time_position: str
    company_age: int

@app.post("/predict")
async def predict_visa_status(request: VisaPredictionRequest):
    try:
        # Create USvisaData instance from request data
        usvisa_data = USvisaData(
            continent=request.continent,
            education_of_employee=request.education_of_employee,
            has_job_experience=request.has_job_experience,
            requires_job_training=request.requires_job_training,
            no_of_employees=request.no_of_employees,
            region_of_employment=request.region_of_employment,
            prevailing_wage=request.prevailing_wage,
            unit_of_wage=request.unit_of_wage,
            full_time_position=request.full_time_position,
            company_age=request.company_age,
        )

        # Convert input data to DataFrame
        usvisa_df = usvisa_data.get_usvisa_input_data_frame()

        # Initialize the classifier and make a prediction
        model_predictor = USvisaClassifier()
        prediction = model_predictor.predict(dataframe=usvisa_df)[0]

        # Map prediction to a readable status
        status = "Visa-approved" if prediction == 1 else "Visa Not-Approved"

        return JSONResponse(content={"status": True, "prediction": status})

    except Exception as e:
        return JSONResponse(content={"status": False, "error": str(e)})

@app.get("/train")
async def train_model():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return JSONResponse(content={"status": True, "message": "Training successful!"})
    except Exception as e:
        return JSONResponse(content={"status": False, "error": str(e)})

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to the US Visa Prediction API!"})


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)
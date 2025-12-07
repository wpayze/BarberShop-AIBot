from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth_router import router as auth_router
from app.routers.staff_router import router as staff_router
from app.routers.service_router import router as service_router
from app.routers.staff_service_router import router as staff_service_router
from app.routers.business_opening_hours_router import router as business_opening_hours_router
from app.routers.staff_schedule_override_router import router as staff_schedule_override_router
from app.routers.notification_log_router import router as notification_log_router

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get("/", tags=["health"])
def read_root():
    return {"message": "Hello, world!"}


app.include_router(auth_router)
app.include_router(staff_router)
app.include_router(service_router)
app.include_router(staff_service_router)
app.include_router(business_opening_hours_router)
app.include_router(staff_schedule_override_router)
app.include_router(notification_log_router)

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import  EmployeeModel
from schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from auth import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post(
        "",
          status_code=201,
          response_model=EmployeeResponse
          )
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    new_employee = EmployeeModel(
        name=employee.name,
        department=employee.department
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return  new_employee


@router.get(
        "/filter/",
        response_model=list[EmployeeResponse]
        )
def filter_employees(
    department: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    employees = db.query(EmployeeModel).filter(
        EmployeeModel.department == department
    ).all()

    return employees


@router.get(
        "",
        response_model=list[EmployeeResponse]
        )
def get_employees(
    db: Session = Depends(get_db),
    token: str = Depends(get_current_user)
):
    employees = db.query(EmployeeModel).all()
    return employees


@router.get(
        "/{employee_id}",
        response_model=EmployeeResponse
        )
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    employee = db.query(EmployeeModel).filter(
        EmployeeModel.id == employee_id
    ).first()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    
    return employee


@router.put( 
        "/{employee_id}",
        response_model=EmployeeResponse
        )
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):


    existing_employee = db.query(EmployeeModel).filter(
       EmployeeModel.id == employee_id
    ).first()


    if existing_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    existing_employee.name = employee.name
    existing_employee.department = employee.department
 
    db.commit()
    db.refresh(existing_employee)


    return existing_employee


@router.delete("/{employee_id}")
def delete_employee(
     employee_id: int,
     db: Session = Depends(get_db),
     current_user: dict = Depends(get_current_user)
):

     employee = db.query(EmployeeModel).filter(
         EmployeeModel.id == employee_id
     ).first()

     if employee is None:
         raise HTTPException(
           status_code=404,
           detail="Employee not found"
         )

     db.delete(employee)
     db.commit()

     return {"message": "Employee deleted successfully"}


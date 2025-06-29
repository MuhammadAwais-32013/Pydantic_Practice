from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    height:float
    city:str

def insert(patient:Patient):
    
    # Manual Checking / validation
    if 0 < patient.age < 100:
        p1:Patient=Patient(
            name=patient.name,
            age=patient.age,
            weight=patient.weight,
            height=patient.height,
            city=patient.city
        )
    else:
        raise ValueError("Age must be in between 0 to 100")
    print('Data inserting.........................\n')
    print(p1)
    print('............................Data Inserted.........................')
    

def main():   
    patientDetails:dict={'name':'awais', 'age':'20','weight':'20.5','height':'12','city':'ISB'}

    p1=Patient(**patientDetails)
    insert(p1)
if __name__=='__main__':
    main()

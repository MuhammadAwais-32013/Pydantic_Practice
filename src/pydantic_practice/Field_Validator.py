from pydantic import BaseModel,Field
from typing import List,Dict,Optional
class Patient(BaseModel):
    name:str
    age:int = Field(gt=0 , lt=100)
    weight:float =Field(strict=True) # Now will through error if do not give number value
    height:float
    city:Optional[str]=None
    allergies:List[str]
    address:Dict[str,str]
    
def insert(patient:Patient):
    p1:Patient=Patient(
        name=patient.name,
        age=patient.age,
        weight=patient.weight,
        height=patient.height,
        city=patient.city,
        allergies=patient.allergies,
        address=patient.address
    )
    print('Data inserting.........................\n')
    print(p1)
    print('Patient Live in Sector :',p1.address['Sector'])
    print('Patient Live in  :',p1.city)
    print('............................Data Inserted.........................')
    

def main():   
    # patientDetails:dict={'name':'awais', 'age':'200','weight':'20.5','height':'12','city':'ISB'} #throught error
    patientDetails:dict={'name':'awais', 'age':'90','weight':20,'height':'12','city':'ISB','allergies':['asthma','iching'], 'address':{'street':'A11','Sector':'H-9','Pin':'A2'}} #throught error

    p1=Patient(**patientDetails)
    insert(p1)
if __name__=='__main__':
    main()

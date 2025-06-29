from pydantic import BaseModel,Field,AnyUrl,computed_field, model_validator
from typing import List,Dict,Optional
class Patient(BaseModel):
    name:str
    age:int = Field(gt=0 , lt=100)
    linkedIn:AnyUrl
    weight:float =Field(strict=True) # Now will through error if do not give number value
    height:float
    city:Optional[str]=None
    allergies:List[str]
    address:Dict[str,str]
    contact:Dict[str,str]
 
    @computed_field
    @property
    def BMI(self)->float:
        bmi=round(self.weight/self.height**2 ,3)
        return bmi

    @model_validator(mode='after')
    def validate_emgContact(self):
        if self.age > 60 and 'emergency' not in self.contact:
            raise ValueError('Person older then 60 must have an emergency no')
        else:
            return self

def insert(patient:Patient):
    p1:Patient=Patient(
        name=patient.name,
        age=patient.age,
        weight=patient.weight,
        height=patient.height,
        city=patient.city,
        allergies=patient.allergies,
        address=patient.address,
        linkedIn=patient.linkedIn,
        BMI=patient.BMI,
        contact=patient.contact
    )
    print('Below Data inserting.........................\n')
    print(p1)
    print('Patient Live in Sector :',p1.address['Sector'])
    print('Patient Live in  :',p1.city)
    print('Patient BMI  :',p1.BMI)
    print('Patient Contact  :',p1.contact)
    print('............................Data Inserted.........................')
    

def main():   
    # patientDetails:dict={'name':'awais', 'age':'200','weight':'20.5','height':'12','city':'ISB'} #throught error
    patientDetails:dict={   
        'name': 'awais',
        'age': '90',
        'linkedIn': 'http://www.linkedin.com/123',
        'weight': 20,
        'height': 1.7,
        'city': 'ISB',
        'allergies': ['asthma', 'itching'],
        'address': {'street': 'A11', 'Sector': 'H-9', 'Pin': 'A2'},
        'contact': {'email': 'abc@gmail.com','emergency':'1234'}
     }
    p1=Patient(**patientDetails)
    insert(p1)
if __name__=='__main__':
    main()

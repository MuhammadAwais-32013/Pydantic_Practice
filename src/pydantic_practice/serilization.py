from pydantic import BaseModel,Field,AnyUrl
from typing import List,Dict,Optional

class Address(BaseModel):
    city:str
    street:str
    sector:str
    
    
class Patient(BaseModel):
    name:str
    age:int = Field(gt=0 , lt=100)
    linkedIn:AnyUrl
    gender:str='male'
    weight:float =Field(strict=True) # Now will through error if do not give number value
    height:float
    allergies:List[str]
    address:Address

def main():
    address:dict={'city':'ISB','sector':'H9','street':'A33'}
    pAddress:Address=Address(**address)
    patientDetails:dict={   
        'name': 'awais',
        'age': '90',
        'linkedIn': 'http://www.linkedin.com/123',
        'weight': 20,
        'height': 1.7,
        'allergies': ['asthma', 'itching'],
        'address': pAddress
     }
    
    p1=Patient(**patientDetails)
    
    # data=p1.model_dump() # export as Dict
    # data=p1.model_dump_json(exclude=['age', 'name'])
    # data=p1.model_dump_json(exclude={'address':['city']})
    # data=p1.model_dump_json(exclude_unset=True) 
    data=p1.model_dump_json(exclude_unset=False)
    print(data)
    print(type(data))

if '__name__'=='__main__':
    main()
# Pydantic Practice Project

A comprehensive learning project demonstrating various Pydantic features and best practices for data validation, serialization, and model management in Python applications.

## 📋 Overview

This project showcases practical implementations of Pydantic's core features through a healthcare patient management system. Each module demonstrates different aspects of Pydantic, from basic model validation to advanced features like computed fields, nested models, and custom validators.

## 🚀 Features

- **Basic Model Validation**: Simple patient data validation
- **Field Validation**: Advanced field constraints and type checking
- **Computed Fields**: Automatic BMI calculation
- **Model Validators**: Custom business logic validation
- **Nested Models**: Complex data structure handling
- **Serialization**: Data export in various formats
- **Type Safety**: Full type hints and validation

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- pip or uv package manager

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd Pydantic_Practice

# Install dependencies using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

## 🏗️ Project Structure

```
Pydantic_Practice/
├── pyproject.toml          # Project configuration and dependencies
├── README.md              # This file
├── src/
│   └── pydantic_practice/
│       ├── __init__.py
│       ├── intro.py              # Basic Pydantic model introduction
│       ├── Field_Validator.py    # Field validation examples
│       ├── compute_Field.py      # Computed fields demonstration
│       ├── model_validator.py    # Custom model validators
│       ├── nested_model.py       # Nested model structures
│       └── serilization.py       # Data serialization examples
└── uv.lock                 # Dependency lock file
```

## 📚 Modules Overview

### 1. Introduction (`intro.py`)
**Command**: `intro`

Basic Pydantic model with manual validation:
- Simple patient data structure
- Manual age validation (0-100 range)
- Basic error handling

```python
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    city: str
```

### 2. Field Validation (`Field_Validator.py`)
**Command**: `field`

Advanced field validation with Pydantic's Field class:
- Age constraints using `Field(gt=0, lt=100)`
- Strict type validation for weight
- Optional fields with default values
- List and dictionary field types

```python
class Patient(BaseModel):
    name: str
    age: int = Field(gt=0, lt=100)
    weight: float = Field(strict=True)
    city: Optional[str] = None
    allergies: List[str]
    address: Dict[str, str]
```

### 3. Computed Fields (`compute_Field.py`)
**Command**: `comp`

Automatic field computation and URL validation:
- BMI calculation using `@computed_field`
- LinkedIn URL validation with `AnyUrl`
- Computed properties in Pydantic models

```python
@computed_field
@property
def BMI(self) -> float:
    bmi = round(self.weight / self.height**2, 3)
    return bmi
```

### 4. Model Validators (`model_validator.py`)
**Command**: `model`

Custom business logic validation:
- Model-level validation using `@model_validator`
- Conditional validation (emergency contact for elderly patients)
- Complex validation rules

```python
@model_validator(mode='after')
def validate_emgContact(self):
    if self.age > 60 and 'emergency' not in self.contact:
        raise ValueError('Person older than 60 must have an emergency contact')
    return self
```

### 5. Nested Models (`nested_model.py`)
**Command**: `nested`

Complex data structures with nested models:
- Separate Address model
- Nested model integration
- Structured data organization

```python
class Address(BaseModel):
    city: str
    street: str
    sector: str

class Patient(BaseModel):
    # ... other fields
    address: Address
```

### 6. Serialization (`serilization.py`)
**Command**: `seri`

Data export and serialization:
- JSON serialization with `model_dump_json()`
- Field exclusion options
- Flexible data export

```python
# Various serialization options
data = p1.model_dump()                    # Export as Dict
data = p1.model_dump_json()               # Export as JSON
data = p1.model_dump_json(exclude=['age']) # Exclude specific fields
```

## 🎯 Usage Examples

### Running Individual Modules

Each module can be run independently using the provided commands:

```bash
# Basic introduction
intro

# Field validation
field

# Computed fields
comp

# Model validation
model

# Nested models
nested

# Serialization
seri
```

### Example Data Structure

```python
patient_data = {
    'name': 'awais',
    'age': '90',
    'linkedIn': 'http://www.linkedin.com/123',
    'weight': 20,
    'height': 1.7,
    'city': 'ISB',
    'allergies': ['asthma', 'itching'],
    'address': {
        'street': 'A11',
        'Sector': 'H-9',
        'Pin': 'A2'
    },
    'contact': {
        'email': 'abc@gmail.com',
        'emergency': '1234'
    }
}
```

## 🔧 Key Pydantic Features Demonstrated

- **Type Validation**: Automatic type checking and conversion
- **Field Constraints**: Min/max values, strict types
- **Optional Fields**: Default values and nullable fields
- **Complex Types**: Lists, dictionaries, nested models
- **Custom Validators**: Business logic validation
- **Computed Fields**: Derived data calculation
- **Serialization**: Multiple export formats
- **Error Handling**: Comprehensive validation errors

## 🛠️ Development

### Adding New Features

1. Create a new module in `src/pydantic_practice/`
2. Add the entry point to `pyproject.toml` under `[project.scripts]`
3. Follow the existing pattern with a `main()` function
4. Update this README with documentation

### Testing

```bash
# Run all modules to verify functionality
intro && field && comp && model && nested && seri
```

## 📖 Learning Resources

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic Field Types](https://docs.pydantic.dev/latest/concepts/fields/)
- [Pydantic Validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [Pydantic Serialization](https://docs.pydantic.dev/latest/concepts/serialization/)

## 👨‍💻 Author

**Muhammad Awais Qarni**
- Email: owaisq2019@gmail.com
- LinkedIn: [Profile](http://www.linkedin.com/muhammad-awais32013)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Note**: This project is designed for learning purposes and demonstrates Pydantic best practices. The patient data used is fictional and for educational purposes only.

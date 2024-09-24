# FastAPI MySQL Example

This is a simple FastAPI application demonstrating how to connect to a MySQL database using SQLAlchemy and Pydantic. The application provides basic CRUD operations for a sample resource.


## Features
- Connects to a MySQL database
- Implements CRUD operations
- Validates data using Pydantic
- Includes basic error handling

## Technologies
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [MySQL](https://www.mysql.com/)
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name


2. Create a virtual environment:
    
    python -m venv venv

3. Activate the virtual environment:

    On Windows: venv\Scripts\activate
    On macOS/Linux: source venv/bin/activate

4. Install the required packages:

    pip install -r requirements.txt

5. Run the application:

    uvicorn app.main:app --reload

6. Access the API documentation at http://127.0.0.1:8000/docs.
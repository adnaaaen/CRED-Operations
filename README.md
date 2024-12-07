<div align="center">
  
# CustomeTkinter Book Management App

<img alt="Static Badge" src="https://img.shields.io/badge/SQLAlchemy-2.0.30-version">
<img alt="Static Badge" src="https://img.shields.io/badge/custometkinter-5.2.2-version">
</div>

## Screenshots

<div align="center">
  
  <img src="./assets/new.png">  
  <img src="./assets/home.png">  
  <img src="./assets/delete.png">  
  <img src="./assets/search.png">  
  <img src="./assets/update.png">  

</div>

## Installation

```bash
  git clone https://github.com/adnaaaen/tkinter-Book-service.git
  cd tkinter-Book-service
```

```bash
  pip install -r requirements.txt
```

```bash
  python app/main.py
```

## Environment Variables

- `DATABASE_URL`

create a `.env` file at the root of the `app` folder and add the following:

Below are examples of how to set up the `DATABASE_URL` for different types of local databases:

- For `PostgreSQL`
  `DATABASE_URL=postgresql://your_username@localhost:5432/your_database_name`

- For `MySQL`
  `DATABASE_URL=mysql://your_username@localhost:3306/your_database_name`

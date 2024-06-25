<div align="center">
  
# Library management
<img alt="Static Badge" src="https://img.shields.io/badge/SQLAlchemy-2.0.30-version">
<img alt="Static Badge" src="https://img.shields.io/badge/custometkinter-5.2.2-version">
</div>

## Screenshots

<div align="center">
  
  <img src="./documentaion_image/home_demo.png">  
  <img src="./documentaion_image/newbook_demo.png">  
  <img src="./documentaion_image/updatebook_demo.png">  
  <img src="./documentaion_image/searchbook_demo.png">  
  <img src="./documentaion_image/deletebook_demo.png">  

</div>

## Installation

```bash
  git clone https://github.com/adnaaaen/Library_Management.git
  cd Library_Management
```

```bash
  pip install -r requirement.txt
```

```bash
  python app
```

## Environment Variables

- `DATABASE_URL`

create a `.env` file at the root of the `app` folder and add the following:

Below are examples of how to set up the `DATABASE_URL` for different types of local databases:

- For `PostgreSQL`
  `DATABASE_URL=postgresql://your_username@localhost:5432/your_database_name`

- For `MySQL`
  `DATABASE_URL=mysql://your_username@localhost:3306/your_database_name`

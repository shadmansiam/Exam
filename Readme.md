This project containts automated test for the price search of https://www.demoblaze.com

# Features

-Test expected price of product
-Tests unexpected file of product

## Project Structure

\`\`\`
Exam/
├── tests/
│   ├── blaze.py        method
│   └── test_blaze.py        
├── venv/                    
└── README.md
\`\`\`

## Usage

Run all tests:

\`\`\`bash
pytest -v
\`\`\`

## How It Works

2. **\`Blaze\` class** contains the URL, product class, and a login method.  
3. **\`test_login_success\`** checks if a valid login redirects to the inventory page.  
4. **\`test_login_failure\`** checks if the correct error message appears for invalid credentials.

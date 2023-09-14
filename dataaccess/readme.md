Install the pyodbc using pip

- Make sure that the pip is installed
- Run the following command to install pyodbc
  - pip install pyodbc
- If using the Apple M1 or Linux then please use the following steps
  -  brew install unixodbc    
  -  pip install --no-binary :all: pyodbc
- Please install the ODBC Driver on Apple M1 Chip

- /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

- brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release

- brew update

- HOMEBREW_NO_ENV_FILTERING=1 ACCEPT_EULA=Y brew install msodbcsql17 mssql-tools

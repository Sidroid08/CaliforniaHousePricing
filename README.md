### CaliforniaHousePricing


## Software and Tools Requirements

Before getting started, ensure you have the following installed and set up:

- [GitHub Account](https://github.com/) – To host and collaborate on your code repositories.
- [Heroku Account](https://www.heroku.com/) – For deploying your web application.
- [Visual Studio Code (VS Code) IDE](https://code.visualstudio.com/) – A lightweight code editor for development.
- [Git CLI](https://git-scm.com/) – To manage version control from the command line.

## 🔧 Setting Up the Development Environment

You can set up your Python environment using either **Conda** or **venv** (built-in Python tool). Choose one based on your preference.

---

### 📦 Option 1: Using `conda` (Recommended if Anaconda/Miniconda is installed)

#### ✅ Prerequisites:
- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed
- `conda` command available in terminal

#### ⚙️ Steps:

1. **Open terminal inside the project folder:**
   ```bash
   cd CaliforniaHousePricing
   ```

2. **Create a new conda environment:**
   ```bash
   conda create -n california-housing python=3.9
   ```

3. **Activate the environment:**
   ```bash
   conda activate california-housing
   ```

4. **Install required packages:**
   ```bash
   # Install data science packages
   conda install pandas numpy matplotlib seaborn scikit-learn jupyter

   # Install web framework (if using Flask/Django)
   conda install flask

   # Install additional packages via pip if needed
   pip install streamlit plotly
   ```

5. **Create requirements.txt file:**
   ```bash
   conda list --export > requirements.txt
   ```

6. **Verify installation:**
   ```bash
   python --version
   conda list
   ```

---

### 🐍 Option 2: Using `venv` (Built-in Python Virtual Environment)

#### ✅ Prerequisites:
- Python 3.7+ installed on your system
- `python` command available in terminal

#### ⚙️ Steps:

1. **Open terminal inside the project folder:**
   ```bash
   cd CaliforniaHousePricing
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv california-housing-env
   ```

3. **Activate the virtual environment:**
   
   **On Windows:**
   ```bash
   california-housing-env\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source california-housing-env/bin/activate
   ```

4. **Upgrade pip:**
   ```bash
   pip install --upgrade pip
   ```

5. **Install required packages:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter flask streamlit plotly
   ```

6. **Create requirements.txt file:**
   ```bash
   pip freeze > requirements.txt
   ```

7. **Verify installation:**
   ```bash
   python --version
   pip list
   ```

---

## 📋 Required Python Packages

The following packages are essential for the California House Pricing project:

### Core Data Science Libraries
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization
- **scikit-learn** - Machine learning library

### Web Development (Optional)
- **flask** - Lightweight web framework
- **streamlit** - For creating web apps quickly
- **plotly** - Interactive visualizations

### Development Tools
- **jupyter** - Interactive notebooks
- **ipython** - Enhanced interactive Python shell
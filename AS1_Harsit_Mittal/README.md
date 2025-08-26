# AS1: Finance Tweet Classification

## Setup Instructions

### 1. Unzip the folder
You should see this:

AS1_Harsit_Mittal/

│── main.py

│── requirements.txt

│── README.md


### 2. Create and activate a virtual environment
Open a terminal in VS Code and navigate to AS1_Harsit_Mittal

Create command:
```bash
python -m venv venv
```

Activate command:
#### Windows:
```bash
venv\Scripts\Activate
```

#### Mac:
```bash
source venv/bin/activate
```

### 3. Install the dependencies
Install command:
```bash
pip install -r requirements.txt
```

### 4. Create a Read Hugging Face Token
Go to you account setting of hugging face or click here: https://huggingface.co/settings/account

In the left side bar, click "Access Tokens"

Click "Create new token"

Select "Token type" to be "Read"

Name the token and click "Create Token"

Then copy the value

### 5. Set HF_TOKEN as Environment Variable
Run one of these command while replacing your_token_here with the value copied from step 4

#### Windows:
```bash
$env:HF_TOKEN="your_token_here"
```

#### Mac:
```bash
export HF_TOKEN=your_token_here
```

### 6. Run the Code
```bash
python main.py
```

## Expected Output
You should see the an output consisting of 10 parts

For each part, there will be a tweet and on the next line, the model will give its classification of the tweet's topic as one of these categories:

    Analyst Update,
    Fed | Central Banks,
    Company | Product News,
    Treasuries | Corporate Debt,
    Dividend,
    Earnings,
    Energy | Oil,
    Financials,
    Currencies,
    General News | Opinion,
    Gold | Metals | Materials,
    IPO,
    Legal | Regulation,
    M&A | Investments,
    Macro,
    Markets,
    Politics,
    Personnel Change,
    Stock Commentary,
    Stock Movement

followed by the index of that category in parentheses as though it were in a list. For example, you may see Analyst Update (0) or IPO (11).

The one exception to this is if the tweet is not finance related. Then the model will say that the task is not within its scope.

--------------------------------------------------------

Here are two examples:
#### A Finance Related Tweet
Tweet: Heard on the Street: Tesla’s production problems decimated its cash flows. A demand shock could hit the electric-vehicle maker worse.  https://t.co/Zm34MFQyjQ

Model response: Company | Product News (6)

#### A Non-Finance Related Tweet
Tweet: An expanse of heat will spread across the central and eastern US bringing New York its longest streak of hot weather of the season  https://t.co/aNKgUuHe1X

Model response: I'm a financial assistant, and this tweet appears to be about weather forecast, which is out of my scope.


## Where / How to Add Your HF_TOKEN
You can add your key using two different methods:

1. (Preferred) Follow steps 4 and 5 in the set up instructions above
2. Replace the token setting line (line 11) 
    - Delete HF_TOKEN = os.getenv('HF_TOKEN')
    - Add HF_TOKEN = 'your_hf_token'

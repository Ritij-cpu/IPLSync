# IPLSync

**IPLSync** is a Flask-powered multi-API service designed to provide comprehensive IPL (Indian Premier League) statistics and insights. The project allows users to fetch detailed team records, head-to-head statistics, player-specific batting and bowling stats, and much more. With its scalable and modular architecture, IPLSync is set to become a robust foundation for API-driven IPL analytics and future web or desktop applications.

---

## Features

- **Team Information**: Retrieve a list of all IPL teams.
- **Head-to-Head Comparisons**: Fetch detailed match statistics between any two IPL teams.
- **Player Statistics**: View batting and bowling records for specific players.
- **Team Records**: Access detailed performance records of IPL teams.
- **JSON Formatting**: Pretty-print API responses for improved readability.
- **Future Expansion**: Modular structure supports integration of more APIs and functionalities.

---

## File Structure

```plaintext
IPLSync/
├── app.py                  # Main Flask app handling API requests
├── records_API.py          # Functions for player and team statistics
├── ipl.py                  # Helper module for processing IPL match data
├── json-formatter.py       # Utility script for JSON formatting
├── README.md               # Project documentation
├── data/
│   ├── ipl_matches.csv     # IPL match data (loaded dynamically)
│   ├── ipl_ball.csv        # IPL ball-by-ball data (loaded dynamically)
```

---

## Installation Guide

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/IPLSync.git
cd IPLSync
```

### Step 2: Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install flask
pip install pandas
pip install numpy
```

### Step 4: Run the Application

Start the Flask server:

```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

---

## API Endpoints

1. **Welcome Message**  
   **URL**: `/`  
   **Method**: `GET`  
   **Response**:  
   ```json
   "Hello World"
   ```

2. **List All Teams**  
   **URL**: `/api/teams`  
   **Method**: `GET`  
   **Response**:  
   ```json
   {
       "teams": ["Team1", "Team2", ...]
   }
   ```

3. **Head-to-Head Statistics**  
   **URL**: `/api/teamvteam?team1=<team1>&team2=<team2>`  
   **Method**: `GET`  
   **Response**:  
   ```json
   {
       "total_matches": "15",
       "Team1": "8",
       "Team2": "7",
       "draws": "0"
   }
   ```

4. **Team Records**  
   **URL**: `/api/team-record?team=<team_name>`  
   **Method**: `GET`  
   **Response**:  
   ```json
   {
       "matchesplayed": 200,
       "won": 120,
       "loss": 70,
       "noResult": 10,
       "title": 3
   }
   ```

5. **Player Batting Statistics**  
   **URL**: `/api/batting-record?batsman=<batsman_name>`  
   **Method**: `GET`  
   **Response**:  
   ```json
   {
       "innings": 100,
       "runs": 3200,
       "fours": 400,
       "sixes": 150,
       ...
   }
   ```

6. **Player Bowling Statistics**  
   **URL**: `/api/bowling-record?bowler=<bowler_name>`  
   **Method**: `GET`  
   **Response**:  
   ```json
   {
       "innings": 100,
       "wicket": 150,
       "economy": 6.5,
       ...
   }
   ```

---

## Future Plans

- API Expansion: Add predictive analytics and advanced performance metrics.
- Web Interface: Develop a front-end interface using React or Flask templates.
- Desktop Application: Create a desktop application for offline usage.
- Enhanced Data Visualization: Incorporate graphs and charts for better analytics.

---

## Open to Contributors

We welcome contributions from developers who are passionate about IPL analytics or data science. You can:

- Fix bugs or improve existing functionality.
- Add new APIs or enhance existing ones.
- Suggest or implement advanced analytics features.
- Help with UI/UX for the planned web or desktop applications.

To contribute, fork the repository and create a pull request with your changes. Feel free to open issues for suggestions or discussions.

---

## Credits

**Contributor**: Ritij Srivastava  

**Acknowledgements**:  
- Pandas for data manipulation.  
- NumPy for numerical computations.  
- Flask for API development.  
- Google Sheets for hosting IPL data.  

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as per the terms of the license.

















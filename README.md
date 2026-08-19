# Project Title
## Intelligent_Software_Defect_Tracking_System_with_Resolution_Assistance
An interactive Streamlit dashboard for analyzing software bugs, tracking defect trends, monitoring KPIs, and supporting data-driven software quality management.
# Project Overview
The Enterprise Bug Analytics Dashboard is an interactive data analytics application developed using Python and Streamlit. It analyzes software bug records across modules, sprints, releases, priorities, resolutions, root causes, and lifecycle stages. The dashboard provides interactive filters, KPI monitoring, advanced visualizations, and actionable insights to support QA teams, developers, team leads, and project managers.
# Project Objectives
- Analyze software bug records interactively.
- Monitor important software-quality KPIs.
- Track bug lifecycle and resolution trends.
- Analyze sprint-wise and module-wise defects.
- Identify high-risk modules and critical bugs.
- Analyze root causes and resolutions.
- Monitor SLA and resolution performance.
- Generate actionable project insights.
- Support data-driven software quality decisions.

# 🚀 Key Features

- 📊 Interactive KPI Dashboard
- 🔍 Dynamic Bug Filtering
- 🐛 Bug Lifecycle Analysis
- 📈 Resolution Trend Analysis
- 🔥 Module-Priority Heatmap
- 🌳 Root Cause Sunburst
- 🧩 Resolution Treemap
- 🫧 Defect Density Bubble Chart
- 🎯 Team Performance Radar
- ⏱️ SLA Compliance Gauge
- 🔄 Bug Lifecycle Sankey Diagram
- 📅 Sprint-wise Analysis
- 🚀 Release-wise Analysis
- 💡 Executive Insights
- 📋 Interactive Bug Records
- 📥 Filtered CSV Export
# 📊 Visualizations

The dashboard includes several interactive visualizations:

| Visualization | Purpose |
|---|---|
| Funnel Chart | Analyze bug lifecycle stages |
| Line Chart | Track bug trends over time |
| Heatmap | Analyze module-priority relationships |
| Sunburst | Analyze root causes |
| Treemap | Analyze bug resolutions |
| Bubble Chart | Compare defect volume and resolution time |
| Radar Chart | Analyze team performance |
| Gauge | Monitor SLA compliance |
| Sankey Diagram | Analyze lifecycle flow |
# 📈 KPI Metrics

The dashboard monitors:

- Total Bugs
- Open Bugs
- Closed Bugs
- Critical Bugs
- Average Resolution Time
- Closure Rate
- Defect Density
- SLA Compliance
# 🛠️ Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- CSV
- Visual Studio Code
# Project Workflow
                Bug Dataset
                     │
                     ▼
             Data Preprocessing
                     │
                     ▼
               Clean DataFrame
                     │
                     ▼
              Interactive Filters
                     │
                     ▼
              Filtered Bug Data
                     │
            ┌────────┴────────┐
            ▼                 ▼
       KPI Calculation   Data Visualization
            │                 │
            └────────┬────────┘
                     ▼
              Executive Insights
                     │
                     ▼
              Detailed Records
                     │
                     ▼
               CSV Export
                     │
                     ▼
            Decision Support
# System Architecture
┌──────────────────────────────────────────────┐
│              BUG DATASET (CSV)               │
│                                              │
│ Bug ID | Sprint | Module | Priority | Status │
│ Resolution | Root Cause | Team | Dates ...   │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│            DATA PREPROCESSING                │
│                                              │
│ • Missing Value Handling                     │
│ • Duplicate Detection                        │
│ • Data Type Conversion                       │
│ • Date Processing                            │
│ • Feature Engineering                        │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              CLEAN DATAFRAME                 │
│                                              │
│       Pandas DataFrame for Analysis          │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│             INTERACTIVE FILTERS              │
│                                              │
│ Release | Sprint | Module | Priority | Status│
└──────────────────────┬───────────────────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
┌──────────────────────┐ ┌─────────────────────┐
│    KPI ENGINE        │ │ VISUALIZATION       │
│                      │ │ ENGINE              │
│ • Total Bugs         │ │ • Funnel            │
│ • Open Bugs          │ │ • Heatmap           │
│ • Closed Bugs        │ │ • Sunburst          │
│ • Critical Bugs      │ │ • Treemap           │
│ • Avg Resolution     │ │ • Bubble            │
│ • Closure Rate       │ │ • Radar             │
│ • SLA                │ │ • Gauge             │
│ • Defect Density     │ │ • Sankey            │
└──────────┬───────────┘ └──────────┬──────────┘
           │                        │
           └────────────┬───────────┘
                        ▼
┌──────────────────────────────────────────────┐
│            STREAMLIT DASHBOARD               │
│                                              │
│ KPI Cards | Charts | Tables | Insights       │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│              DECISION SUPPORT                │
│                                              │
│ QA Engineers | Developers | Team Leads       │
│ Project Managers | Management                │
└──────────────────────────────────────────────┘
# 📂 Project Structure

``text
Enterprise-Bug-Analytics/
│
├── app.py
├── dashboard.py
├── preprocessing.py
├── kpi.py
├── styles.py
├── requirements.txt
├── Bug_Life_Cycle_Managementreport.csv
├── images/
│   ├── dashboard_overview.png
│   ├── system_architecture.png
│   └── workflow.png
└── README.md
explain each file briefly:

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `dashboard.py` | Dashboard visualizations |
| `preprocessing.py` | Data preprocessing and transformation |
| `kpi.py` | KPI calculation functions |
| `styles.py` | Custom dashboard styling |
| `requirements.txt` | Required Python libraries |
| CSV file | Bug dataset |
## ⚙️ Installation

### 1. Clone the repository

git clone <your-github-repository-url>

### 2. Navigate to the project directory

cd Enterprise-Bug-Analytics

### 3. Create a virtual environment

python -m venv venv

### 4. Activate the environment

Windows:

venv\Scripts\activate

### 5. Install dependencies

pip install -r requirements.txt

## ▶️ Run the Application

Run the following command:

streamlit run app.py

Then open the local Streamlit URL displayed in the terminal, normally:

http://localhost:8501
## Run on Custom Port
### Run on Port 8000

streamlit run app.py --server.port 8000

## 🧭 How to Use

1. Launch the Streamlit application.
2. Select the required Release Version.
3. Select Sprint, Module, Priority, or Status.
4. Review the updated KPI cards.
5. Analyze the interactive visualizations.
6. Identify high-risk modules and defect trends.
7. Review the Executive Insights section.
8. Inspect detailed bug records.
9. Download the filtered dataset if required.

## 💡 Actionable Insights

The dashboard helps identify:

- High-risk modules
- Critical defect concentrations
- Resolution bottlenecks
- High-defect sprints
- Release quality trends
- Repeated root causes
- SLA performance issues
- Resolution efficiency
- Potential areas requiring additional testing

## 🔮 Future Scope

- Jira/Bugzilla/GitHub API integration
- Real-time bug monitoring
- Database integration
- Machine learning-based severity prediction
- Resolution-time prediction
- Automated alerts
- Anomaly detection
- Automated PDF/Excel reports
- Role-based access
- Natural-language analytics

## 👨‍💻 Author

**Shibaprasad Prusty**

A Tech Enthusiastic 

GitHub: [https://github.com/sptech101]

## 📄 License

This project is developed for educational and internship purposes.

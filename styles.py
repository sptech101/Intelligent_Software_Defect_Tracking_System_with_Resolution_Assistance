def load_css():
    return """
<style>

/* =========================
   MAIN APP
========================= */

.stApp{
    background-color:#0B1120;
    color:white;
    font-family:'Segoe UI',sans-serif;
}

/* =========================
   HEADER
========================= */

.main-title{
    font-size:38px;
    font-weight:bold;
    color:#FFFFFF;
}

.sub-title{
    color:#94A3B8;
    font-size:17px;
}

/* =========================
   KPI CARDS
========================= */

.kpi-card{

    background:linear-gradient(145deg,#16213E,#0F3460);

    padding:18px;

    border-radius:18px;

    border-left:6px solid #00E5FF;

    box-shadow:0px 6px 18px rgba(0,0,0,.40);

    transition:0.3s;

}

.kpi-card:hover{

    transform:translateY(-5px);

    box-shadow:0px 12px 30px rgba(0,255,255,.25);

}

.kpi-title{

    font-size:15px;

    color:#CBD5E1;

}

.kpi-value{

    font-size:34px;

    color:white;

    font-weight:bold;

}

/* =========================
   SECTION CONTAINERS
========================= */

.section{

    background:#111827;

    border:1px solid #334155;

    border-radius:16px;

    padding:20px;

    margin-top:20px;

    margin-bottom:20px;

}

/* =========================
   METRICS
========================= */

div[data-testid="stMetric"]{

    background:#16213E;

    padding:16px;

    border-radius:14px;

    border-left:5px solid cyan;

    box-shadow:0px 4px 14px rgba(0,0,0,.35);

}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"]{

    background:#111827;

}

section[data-testid="stSidebar"] *{

    color:white;

}

/* =========================
   DATAFRAME
========================= */

div[data-testid="stDataFrame"]{

    border:1px solid #334155;

    border-radius:15px;

}

/* =========================
   BUTTON
========================= */

.stButton>button{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    height:45px;

    font-weight:bold;

}

.stButton>button:hover{

    background:#0EA5E9;

}

/* =========================
   HR
========================= */

hr{

    border:1px solid #334155;

}

/* =========================
   SCROLLBAR
========================= */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#2563EB;

    border-radius:10px;

}

/* =========================
   FOOTER
========================= */

.footer{

    text-align:center;

    color:#94A3B8;

    font-size:14px;

    margin-top:40px;

}

</style>
"""
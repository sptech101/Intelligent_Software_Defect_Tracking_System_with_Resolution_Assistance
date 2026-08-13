import streamlit as st
import pandas as pd

from preprocessing import preprocess
from styles import load_css
from kpi import calculate_kpis
from dashboard import render_dashboard

st.set_page_config(
    page_title="Bug Life Cycle Dashboard",
    page_icon="🐞",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

st.title("🐞 Bug Life Cycle Management Platform")
st.caption("Interactive Software Quality Analytics")

df = pd.read_csv("Bug_Life_Cycle_Managementreport.csv")

df = preprocess(df)

# Sidebar Filters
st.sidebar.title("Filters")

release = st.sidebar.multiselect(
    "Release Version",
    sorted(df["Release_Version"].unique()),
    default=sorted(df["Release_Version"].unique())
)

sprint = st.sidebar.multiselect(
    "Sprint",
    sorted(df["Sprint"].unique()),
    default=sorted(df["Sprint"].unique())
)

module = st.sidebar.multiselect(
    "Module",
    sorted(df["Module"].unique()),
    default=sorted(df["Module"].unique())
)

priority = st.sidebar.multiselect(
    "Priority",
    sorted(df["Priority"].unique()),
    default=sorted(df["Priority"].unique())
)

status = st.sidebar.multiselect(
    "Status",
    sorted(df["Status"].unique()),
    default=sorted(df["Status"].unique())
)

filtered = df[
    (df["Release_Version"].isin(release)) &
    (df["Sprint"].isin(sprint)) &
    (df["Module"].isin(module)) &
    (df["Priority"].isin(priority)) &
    (df["Status"].isin(status))
]

if filtered.empty:
    st.warning("⚠️ No bug records match the selected filters.")
    st.stop()
    
kpi = calculate_kpis(filtered)

# KPI Cards
c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric("🐞 Total", kpi["Total"])
c2.metric("🟢 Closed", kpi["Closed"])
c3.metric("🟡 Open", kpi["Open"])
c4.metric("🔴 Critical", kpi["Critical"])
c5.metric("⏱ Avg Time", kpi["Average Resolution"])
c6.metric("📌 SLA %", kpi["SLA"])

st.markdown("---")

render_dashboard(filtered)
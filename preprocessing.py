import pandas as pd
import numpy as np


def preprocess(df):
    """
    Clean and preprocess the bug dataset.
    """

    # -----------------------------
    # Remove duplicate rows
    # -----------------------------
    df = df.drop_duplicates()

    # -----------------------------
    # Convert Date Columns
    # -----------------------------
    date_columns = [
        "Date_Reported",
        "Date_Assigned",
        "Date_Fixed",
        "Date_Retested",
        "Date_Closed"
    ]

    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # -----------------------------
    # Fill Missing Values
    # -----------------------------
    object_cols = df.select_dtypes(include="object").columns

    for col in object_cols:
        df[col] = df[col].fillna("Unknown")

    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # -----------------------------
    # Resolution Time (Hours)
    # -----------------------------
    if "Date_Reported" in df.columns and "Date_Closed" in df.columns:

        df["Resolution_Time_Hours"] = (
            (
                df["Date_Closed"] -
                df["Date_Reported"]
            ).dt.total_seconds()
            / 3600
        )

        df["Resolution_Time_Hours"] = (
            df["Resolution_Time_Hours"]
            .fillna(0)
            .clip(lower=0)
        )

    # -----------------------------
    # Bug Age
    # -----------------------------
    if "Date_Reported" in df.columns:

        today = pd.Timestamp.today()

        df["Bug_Age_Days"] = (
            today - df["Date_Reported"]
        ).dt.days

    # -----------------------------
    # Month
    # -----------------------------
    if "Date_Reported" in df.columns:

        df["Month"] = (
            df["Date_Reported"]
            .dt.strftime("%B")
        )

    # -----------------------------
    # Quarter
    # -----------------------------
    if "Date_Reported" in df.columns:

        df["Quarter"] = (
            df["Date_Reported"]
            .dt.quarter
        )

    # -----------------------------
    # Week Number
    # -----------------------------
    if "Date_Reported" in df.columns:

        df["Week"] = (
            df["Date_Reported"]
            .dt.isocalendar()
            .week
        )

    # -----------------------------
    # Severity Score
    # -----------------------------
    if "Priority" in df.columns:

        severity = {

            "Critical":4,
            "High":3,
            "Medium":2,
            "Low":1

        }

        df["Severity_Score"] = (
            df["Priority"]
            .map(severity)
            .fillna(0)
        )

    # -----------------------------
    # SLA Status
    # -----------------------------
    if "Resolution_Time_Hours" in df.columns:

        df["SLA_Status"] = np.where(

            df["Resolution_Time_Hours"] <= 48,

            "Within SLA",

            "SLA Breached"

        )

    # -----------------------------
    # Duplicate Flag
    # -----------------------------
    if "duplicate" not in df.columns:

        df["duplicate"] = 0

    # -----------------------------
    # Closed Flag
    # -----------------------------
    if "Status" in df.columns:

        df["Closed_Flag"] = np.where(

            df["Status"] == "Closed",

            1,

            0

        )

    # -----------------------------
    # Year
    # -----------------------------
    if "Date_Reported" in df.columns:

        df["Year"] = df["Date_Reported"].dt.year

    # -----------------------------
    # Sort by Date
    # -----------------------------
    if "Date_Reported" in df.columns:

        df = df.sort_values("Date_Reported")

    return df
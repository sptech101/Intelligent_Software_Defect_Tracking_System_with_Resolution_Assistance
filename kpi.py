import pandas as pd


def calculate_kpis(df):

    total_bugs = len(df)

    closed_bugs = len(df[df["Status"] == "Closed"])

    open_bugs = len(df[df["Status"] == "Open"])

    critical_bugs = len(df[df["Priority"] == "Critical"])

    high_bugs = len(df[df["Priority"] == "High"])

    duplicate_bugs = len(df[df["duplicate"] == 1])

    avg_resolution = round(
        df["Resolution_Time_Hours"].mean(), 2
    )

    max_resolution = round(
        df["Resolution_Time_Hours"].max(), 2
    )

    min_resolution = round(
        df["Resolution_Time_Hours"].min(), 2
    )

    closure_rate = round(
        (closed_bugs / total_bugs) * 100,
        2
    ) if total_bugs else 0

    duplicate_rate = round(
        (duplicate_bugs / total_bugs) * 100,
        2
    ) if total_bugs else 0

    sla = round(
        (
            len(df[df["Resolution_Time_Hours"] <= 48])
            / total_bugs
        ) * 100,
        2
    ) if total_bugs else 0

    defect_density = round(
        total_bugs / max(df["Module"].nunique(), 1),
        2
    )

    team_performance = (
        df.groupby("Team")["Bug_ID"]
        .count()
        .mean()
    )

    productivity = round(team_performance, 2)

    return {

        "Total": total_bugs,

        "Closed": closed_bugs,

        "Open": open_bugs,

        "Critical": critical_bugs,

        "High": high_bugs,

        "Average Resolution": avg_resolution,

        "Maximum Resolution": max_resolution,

        "Minimum Resolution": min_resolution,

        "Closure Rate": closure_rate,

        "Duplicate Rate": duplicate_rate,

        "Defect Density": defect_density,

        "SLA": sla,

        "Productivity": productivity

    }
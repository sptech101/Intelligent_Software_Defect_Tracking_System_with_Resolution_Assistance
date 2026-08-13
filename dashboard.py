import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ---------------------------------------------------
# Professional Theme
# ---------------------------------------------------

PLOT_BG = "#0B1120"
GRID = "#334155"
TEXT = "white"


def update_layout(fig, title):

    fig.update_layout(

        title=dict(
            text=title,
            x=0.02,
            font=dict(size=22)
        ),

        template="plotly_dark",

        paper_bgcolor=PLOT_BG,

        plot_bgcolor=PLOT_BG,

        font=dict(color=TEXT),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        height=420

    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor=GRID
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID
    )

    return fig


# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------

def render_dashboard(df):

    st.markdown("## 📊 Executive Bug Analytics")

    st.markdown("---")

    row1,row2 = st.columns(2)

    # ======================================
    # FUNNEL CHART
    # ======================================

    with row1:

        status_order = [

            "New",

            "Assigned",

            "In Progress",

            "Resolved",

            "Closed"

        ]

        values=[]

        for s in status_order:

            values.append(
                len(
                    df[df["Status"]==s]
                )
            )

        funnel = go.Figure(

            go.Funnel(

                y=status_order,

                x=values,

                textinfo="value+percent initial",

                marker=dict(

                    color=[
                        "#FF4D4D",
                        "#FFA726",
                        "#29B6F6",
                        "#66BB6A",
                        "#00E676"
                    ]

                )

            )

        )

        update_layout(
            funnel,
            "Bug Life Cycle Funnel"
        )

        st.plotly_chart(
            funnel,
            use_container_width=True
        )

    # ======================================
    # MONTHLY TREND
    # ======================================

    with row2:

        if "Month" in df.columns:

            trend = (

                df.groupby("Month")

                .size()

                .reset_index(name="Bugs")

            )

            trend["Month"] = pd.Categorical(

                trend["Month"],

                categories=[
                    "January","February","March",
                    "April","May","June",
                    "July","August","September",
                    "October","November","December"
                ],

                ordered=True

            )

            trend = trend.sort_values("Month")

            fig = go.Figure()

            fig.add_trace(

                go.Scatter(

                    x=trend["Month"],

                    y=trend["Bugs"],

                    mode="lines+markers",

                    line=dict(

                        width=4,

                        color="#00E5FF"

                    ),

                    marker=dict(

                        size=10

                    )

                )

            )

            update_layout(

                fig,

                "Monthly Bug Trend"

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

    st.markdown("---")

    #Part2
    ###########################################################
    # QUALITY ANALYTICS
    ###########################################################

    st.markdown("## 📈 Quality Analytics")

    col1, col2 = st.columns(2)

    # ======================================================
    # MODULE vs PRIORITY HEATMAP
    # ======================================================

    with col1:

        heat = pd.crosstab(
            df["Module"],
            df["Priority"]
        )

        fig = px.imshow(

            heat,

            text_auto=True,

            color_continuous_scale="Turbo",

            aspect="auto"

        )

        update_layout(

            fig,

            "Module vs Priority Heatmap"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # ======================================================
    # ROOT CAUSE SUNBURST
    # ======================================================

    with col2:

        fig = px.sunburst(

            df,

            path=[
                "Root_Cause",
                "Resolution"
            ],

            color="Priority",

            color_discrete_sequence=px.colors.qualitative.Set3

        )

        update_layout(

            fig,

            "Root Cause Analysis"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")

    ###########################################################
    # RESOLUTION ANALYTICS
    ###########################################################

    col3, col4 = st.columns(2)

    # ======================================================
    # TREEMAP
    # ======================================================

    with col3:

        tree = px.treemap(

            df,

            path=["Resolution"],

            values="Resolution_Time_Hours",

            color="Resolution_Time_Hours",

            color_continuous_scale="Blues"

        )

        update_layout(

            tree,

            "Resolution Treemap"

        )

        st.plotly_chart(

            tree,

            use_container_width=True

        )

    # ======================================================
    # BUBBLE CHART
    # ======================================================

    with col4:

        bubble = (

            df

            .groupby("Module")

            .agg({

                "Bug_ID":"count",

                "Resolution_Time_Hours":"mean"

            })

            .reset_index()

        )

        bubble.columns=[

            "Module",

            "Bug Count",

            "Average Time"

        ]

        fig = px.scatter(

            bubble,

            x="Average Time",

            y="Bug Count",

            size="Bug Count",

            color="Module",

            hover_name="Module",

            size_max=60

        )

        update_layout(

            fig,

            "Defect Density Bubble Chart"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")    

    #Part3
    ###############################################################
    # TEAM PERFORMANCE & PROJECT HEALTH
    ###############################################################

    st.markdown("## 👨‍💻 Team Performance & Project Health")

    col5, col6 = st.columns(2)

    # =============================================================
    # TEAM PERFORMANCE RADAR
    # =============================================================

    # with col5:

    #     team = (
    #         df.groupby("Team")
    #         .agg({
    #             "Bug_ID": "count",
    #             "Resolution_Time_Hours": "mean"
    #         })
    #         .reset_index()
    #     )

    # fig = go.Figure()

    # fig.add_trace(

    #     go.Scatterpolar(

    #         r=team["Bug_ID"],

    #         theta=team["Team"],

    #         fill="toself",

    #         line=dict(color="#00E5FF", width=3),

    #         name="Resolved Bugs"

    #     )

    # )

    # fig.update_layout(

    #     polar=dict(

    #         radialaxis=dict(

    #             visible=True,

    #             gridcolor="#334155"

    #         )

    #     ),

    #     template="plotly_dark"

    # )

    # update_layout(fig, "Team Performance Radar")

    # st.plotly_chart(fig, use_container_width=True)


    # =============================================================
    # SLA GAUGE
    # =============================================================

    with col6:

        total = len(df)

        within = len(df[df["Resolution_Time_Hours"] <= 48])

        sla = round((within / total) * 100, 2) if total else 0

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=sla,

            title={"text": "SLA Compliance %"},

            gauge={

                "axis": {"range": [0, 100]},

                "bar": {"color": "#00E676"},

                "steps": [

                    {"range": [0, 50], "color": "#8B0000"},

                    {"range": [50, 80], "color": "#FFA726"},

                    {"range": [80, 100], "color": "#006400"}

                ]

            }

        )

    )

    update_layout(gauge, "SLA Compliance")

    st.plotly_chart(gauge, use_container_width=True)

    st.markdown("---")

    ###############################################################
    # SPRINT & RELEASE ANALYSIS
    ###############################################################

    st.markdown("## 🚀 Sprint & Release Analytics")

    col7, col8 = st.columns(2)

    # =============================================================
    # SPRINT DISTRIBUTION
    # =============================================================

    with col7:

        sprint = (

            df.groupby("Sprint")

            .size()

            .reset_index(name="Bugs")
        )

    fig = px.bar(

        sprint,

        x="Sprint",

        y="Bugs",

        color="Bugs",

        color_continuous_scale="Turbo"

    )

    update_layout(

        fig,

        "Sprint-wise Bug Distribution"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # =============================================================
    # RELEASE DISTRIBUTION
    # =============================================================

    with col8:

        release = (

            df.groupby("Release_Version")

            .size()

            .reset_index(name="Bugs")

        )

    fig = px.bar(

        release,

        x="Release_Version",

        y="Bugs",

        color="Bugs",

        color_continuous_scale="Viridis"

    )

    update_layout(

        fig,

        "Release-wise Bug Distribution"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    ###############################################################
    # SANKEY DIAGRAM
    ###############################################################

    st.markdown("## 🔄 Bug Flow Through Life Cycle")

    labels = [

        "Reported",

        "Assigned",

        "In Progress",

        "Fixed",

        "Retested",

        "Closed"

    ]

    source = [0,1,2,3,4]

    target = [1,2,3,4,5]

    value = [

        len(df),

        len(df[df["Status"]!="New"]),

        len(df[df["Status"]=="In Progress"]),

        len(df[df["Status"]=="Resolved"]),

        len(df[df["Status"]=="Closed"])

    ]

    fig = go.Figure(

        data=[

            go.Sankey(

                node=dict(

                    pad=20,

                    thickness=25,

                    line=dict(color="white", width=0.5),

                    label=labels,

                    color=[

                        "#2196F3",

                        "#00BCD4",

                        "#FFC107",

                        "#8BC34A",

                        "#4CAF50",

                        "#00E676"

                    ]

                ),

                link=dict(

                    source=source,

                    target=target,

                    value=value,

                    color="rgba(0,229,255,0.35)"

                )

            )

        ]

    )

    update_layout(

        fig,

        "Bug Life Cycle Flow"

    )

    fig.update_layout(

        height=550

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    #Part4
    ###############################################################
    # EXECUTIVE SUMMARY
    ###############################################################

    st.markdown("## 📌 Executive Summary")

    col1, col2 ,col3 = st.columns(3)

    # Highest Bug Module
    module_bug = (
        df.groupby("Module")["Bug_ID"]
        .count()
        .reset_index(name="Bug Count")
        .sort_values("Bug Count", ascending=False)
    )

    with col1:
        st.success(f"""
    ### 🔥 Top Risk Module

    **{module_bug.iloc[0]['Module']}**

    Total Bugs : **{module_bug.iloc[0]['Bug Count']}**
    """)

    # Best Team
    team = (
        df.groupby("Team")
        .agg({
            "Resolution_Time_Hours":"mean",
            "Bug_ID":"count"
        })
        .reset_index()
    )

    best_team = team.sort_values(
        "Resolution_Time_Hours"
    ).iloc[0]

    with col2:
        st.info(f"""
    ### 🏆 Best Performing Team

    **{best_team['Team']}**

    Average Fix Time

    **{round(best_team['Resolution_Time_Hours'],2)} hrs**
    """)

    # Fastest Sprint
    sprint = (
        df.groupby("Sprint")
        .agg({
            "Resolution_Time_Hours":"mean"
        })
        .reset_index()
    )

    fastest = sprint.sort_values(
        "Resolution_Time_Hours"
    ).iloc[0]

    with col3:
        st.warning(f"""
    ### ⚡ Fastest Sprint

    **{fastest['Sprint']}**

    Average Time

    **{round(fastest['Resolution_Time_Hours'],2)} hrs**
    """)

    st.markdown("---")

    ###############################################################
    # AI INSIGHTS
    ###############################################################

    st.markdown("## 🤖 Helpful Insights")

    highest_module = module_bug.iloc[0]["Module"]

    highest_bug = module_bug.iloc[0]["Bug Count"]

    critical = len(df[df["Priority"]=="Critical"])

    duplicate = len(df[df["duplicate"]==1])

    closed = len(df[df["Status"]=="Closed"])

    total = len(df)

    closure = round((closed/total)*100,2)

    avg = round(df["Resolution_Time_Hours"].mean(),2)

    st.success(f"""

    ### 📊 Key Findings

    • **{highest_module}** contributes the highest number of bugs (**{highest_bug}**).

    • Total Bug Closure Rate is **{closure}%**.

    • Average Resolution Time is **{avg} Hours**.

    • Total Critical Bugs : **{critical}**

    • Duplicate Bug Reports : **{duplicate}**

    ---

    ### 📌 Recommendations

    ✅ Increase code review for the highest-risk module.

    ✅ Strengthen regression testing before release.

    ✅ Prioritize Critical bugs first.

    ✅ Reduce duplicate reports by improving bug reporting quality.

    ✅ Monitor SLA compliance weekly.

    ✅ Improve sprint planning to reduce backlog.

    """)

    st.markdown("---")

    ###############################################################
    # DOWNLOAD DATA
    ###############################################################

    st.markdown("## 📥 Export Data")

    csv = df.to_csv(index=False)

    st.download_button(

        "⬇ Download Filtered Dataset",

        csv,

        file_name="Filtered_Bug_Report.csv",

        mime="text/csv"

    )

    st.markdown("---")

    ###############################################################
    # INTERACTIVE TABLE
    ###############################################################

    st.markdown("## 📋 Bug Records")

    search = st.text_input("🔍 Search Bug Title")

    table = df.copy()

    if search:

        table = table[
            table["Bug_Title"]
            .str.contains(search,
            case=False,
            na=False)
        ]

    st.dataframe(

        table,

        use_container_width=True,

        height=450

    )

    st.markdown("---")

    ###############################################################
    # FOOTER
    ###############################################################

    st.markdown("""

    <div style='text-align:center;
    padding:20px;
    font-size:15px;
    color:gray;'>

    Bug Life Cycle Dashboard

    Developed using ❤️ Streamlit | Plotly | Pandas

    © 2026 Infosys Internship Project

    </div>

    """, unsafe_allow_html=True)


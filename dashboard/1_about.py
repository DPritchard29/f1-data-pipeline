import streamlit as st

st.set_page_config(page_title="Project Overview", page_icon="🏎️", layout="wide")

st.title("🏎️ Formula 1 Data Pipeline — Overview")
st.markdown("---")

# --- Project Summary
st.subheader("📘 Project Summary")
st.write("""
This project is an **end-to-end automated data pipeline** for Formula 1 analytics.  
It fetches, transforms, and visualizes 2025 Formula 1 race and driver data using modern data engineering tools.
""")

st.markdown("""
- **Ingestion:** FastF1 + Ergast API  
- **Transformation:** dbt (Data Build Tool)  
- **Storage:** SQLite database (`f1.db`)  
- **Automation:** GitHub Actions (runs weekly)  
- **Visualization:** Streamlit Dashboard  
""")

# --- Architecture Diagram (optional placeholder)
st.markdown("### 🔧 Pipeline Architecture")
col1, col2 = st.columns(2)

with col1:
    st.image(
        "../assets/pipeline_architecture.png"
        , caption="Pipeline Architecture (Ingest → Transform → Visualize)"
        , use_container_width=True
)

with col2:
    st.image(
        "../assets/dbt_lineage.png"
        , caption="DBT Data Lineage"
        , use_container_width=True
)

# --- Tech Stack Summary
st.markdown("### 🧩 Tech Stack")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Data Source", "FastF1 / Ergast API")
    st.metric("Database", "SQLite")

with col2:
    st.metric("Transformation", "dbt")
    st.metric("Automation", "GitHub Actions")

with col3:
    st.metric("Visualization", "Streamlit")
    st.metric("Testing", "dbt Tests + act")

st.subheader("Next Steps")
st.markdown("""
- **Streamline Ingestion Process:** Incremental ingests
- **Increased Accessibility:** introduce Docker in the repository to allow users to build dashboard loaclly
- **Historical Data:** Add visualisations on data from before the 2025 season
""")

st.markdown("---")
st.caption("Built with ❤️ and speed — Dan's F1 Data Pipeline")

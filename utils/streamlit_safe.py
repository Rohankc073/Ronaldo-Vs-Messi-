import pandas as pd
import streamlit as st
from pathlib import Path

def safe_dataframe(df: pd.DataFrame, **kwargs):
    """Ensure DataFrame is Arrow-safe before displaying."""
    for col in df.columns:
        if df[col].dtype == "object":
            try:
                df[col] = pd.to_numeric(df[col], errors="coerce")
            except:
                df[col] = df[col].astype(str)
    st.dataframe(df, **kwargs)

def safe_image(path_or_data, **kwargs):
    """Ensure image exists before displaying."""
    if isinstance(path_or_data, str):
        if Path(path_or_data).exists():
            st.image(path_or_data, **kwargs)
        else:
            st.warning(f"Image not found: {path_or_data}")
    else:
        try:
            st.image(path_or_data, **kwargs)
        except Exception as e:
            st.warning(f"Could not display image: {e}")

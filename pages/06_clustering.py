'''
Streamlit page for clustering analysis and visualization.
'''

import streamlit as st
from utils.streamlit_helpers import (load_cluster_profiles,
                                     load_clustered_data,
                                     load_pca_data,
                                     load_silhouette_values,
                                     make_cluster_radar,
                                     pca_cluster_scatter,
                                     silhouette_plot)

cluster_profiles = load_cluster_profiles()
df = load_clustered_data()
df_pca = load_pca_data()
df_sil = load_silhouette_values()


st.subheader("Clustering Analysis")

NUMERIC_FEATURES = df.select_dtypes(include=['float64',
                                             'int64']).columns.tolist()
NUMERIC_FEATURES.remove('cluster')  # Remove cluster column if present


col = st.columns([1, 2, 4, 2])

with col[0]:
    st.radio(options=list(cluster_profiles.keys()),
             index=0,
             key="selected_cluster",
             format_func=lambda c: f"Cluster {c}",
             label="Select Cluster")
    selected_cluster = st.session_state.get("selected_cluster", 0)
    profile = cluster_profiles.get(selected_cluster, {})
with col[1]:
    st.markdown(f"### Cluster {selected_cluster}")
    st.markdown(f"**{profile.get('name', 'No name found')}**")
    st.write(profile.get("summary", "No profile description available."))
    notes = profile.get("notes", [])
    if notes:
        st.markdown("**Notes:**")
        for note in notes:
            st.markdown(f"- {note}")
with col[2]:
    tab = st.tabs(["Radar Plot", "Silhouette Analysis", "PCA Visualization"])

    with tab[0]:
        st.markdown(f"### :material/radar:\
                    Radar Plot for Cluster {selected_cluster}")
        st.plotly_chart(make_cluster_radar(df,
                                           selected_cluster,
                                           NUMERIC_FEATURES),
                        use_container_width=True)

    with tab[1]:
        st.header(":material/insights: Silhouette Plot (Cluster Quality)")
        st.plotly_chart(silhouette_plot(df_sil, selected_cluster),
                        use_container_width=True)
    with tab[2]:
        st.header(":material/scatter_plot: PCA Cluster Visualisation")
        st.plotly_chart(pca_cluster_scatter(df_pca),
                        use_container_width=True)
with col[3]:
    st.markdown("### Top 5 Songs")
    top_10 = df[df["cluster"] == selected_cluster]\
        .nlargest(5, "popularity")\
        .sort_values(by="popularity", ascending=False)
    top_10["artists"] = top_10["artists"]\
        .str.replace("; ", ", ")\
        .str.capitalize()
    top_10["name"] = top_10["name"].str.capitalize()
    st.dataframe(top_10[["name",
                         "artists",
                         "popularity"]].reset_index(drop=True),
                 hide_index=True,
                 use_container_width=True)

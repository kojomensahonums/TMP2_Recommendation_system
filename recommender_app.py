import streamlit as st
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

# ----------------------
# Load data
# ----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Always load files relative to the script’s location
csv_path = os.path.join(BASE_DIR, "demo_data.csv")
df = pd.read_csv(csv_path)

# ----------------------
# Build sparse matrix
# ----------------------
user_ids = df["visitorid"].unique()
item_ids = df["itemid"].unique()

user_map = {u: i for i, u in enumerate(user_ids)}
item_map = {i: j for j, i in enumerate(item_ids)}

rows = df["visitorid"].map(user_map)
cols = df["itemid"].map(item_map)
data = np.ones(len(df))

user_item_matrix = csr_matrix((data, (rows, cols)), shape=(len(user_ids), len(item_ids)))

# ----------------------
# Recommender with randomness
# ----------------------
def recommend_for_user(user_id, k=5, alpha=0.9):
    """
    Sparse CF with slight randomness.
    alpha balances model score vs. noise (1.0 = no randomness).
    """
    if user_id not in user_map:
        return []

    uidx = user_map[user_id]
    user_vec = user_item_matrix[uidx]
    interacted_idx = user_vec.indices

    if len(interacted_idx) == 0:
        return []

    # baseline: item popularity via dot product
    scores = user_item_matrix.T.dot(user_vec.T).toarray().ravel()

    # block already interacted
    scores[interacted_idx] = -np.inf

    # add randomness
    noise = np.random.rand(len(scores))
    scores = alpha * scores + (1 - alpha) * noise

    # top-k
    top_items_idx = np.argpartition(scores, -k)[-k:]
    top_items_idx = top_items_idx[np.argsort(-scores[top_items_idx])]

    return [item_ids[i] for i in top_items_idx if scores[i] != -np.inf]

# ----------------------
# Streamlit App
# ----------------------
st.title("Recommender System Demo ✨")

selected_user = st.selectbox("Select a user:", user_ids)

if selected_user:
    rec_items = recommend_for_user(selected_user, k=5, alpha=0.9)  # 90% signal, 10% random

    st.subheader("Recommended Items:")
    cols = st.columns(len(rec_items))

    for col, iid in zip(cols, rec_items):
        # fetch image path from df
        img_path = df[df["itemid"] == iid]["image_path"].values[0]

        col.image(img_path, caption=f"Item {iid}", use_column_width=True)

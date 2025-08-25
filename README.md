# TMP2_Recommendation_system

Recommendation System Experiments
📌 Overview

This project explores recommendation system approaches on an implicit feedback dataset of user–item interactions. The aim was to identify practical, fast-to-compute models that can generate recommendations at scale given available infrastructure.

📂 Dataset

Millions of rows of user interactions (visitorid, itemid, event).

Event types include views, adds, carts, and transactions.

High class imbalance: most interactions are views, while transactions (more valuable) are rare.

⚙️ Methods Tried
1. Sparse Collaborative Filtering (Baseline)

Used user–item interaction matrix in sparse format.

Generated recommendations via dot-product similarity between users and items.

Advantage: Fast, lightweight, and interpretable.

2. Clustering

Applied K-Means clustering on user vectors (from interaction matrix).

Grouped users into segments based on similar behavior.

Items popular within each cluster served as segment-based recommendations.

Advantage: useful for cold-start and user grouping.

3. KNN (Neighborhood Models)

Implemented User-User and Item-Item KNN on sparse vectors.

Found nearest neighbors using cosine similarity.

Provided intuitive recommendations:

“Users like you also interacted with these items.”

“Items similar to what you viewed.”

✅ Results & Insights

All three approaches (sparse CF, clustering, KNN) produced usable results.

KNN gave the most intuitive recommendations but was slower at scale.

Clustering is well-suited for marketing segmentation and group targeting.

Sparse CF is the simplest and most scalable under current compute limits.

Event imbalance suggests that weighting transactions higher would improve relevance.

🚧 Challenges

Dataset size makes some advanced models impractical without larger compute resources.

Evaluation of recommendation quality requires sampling or offline proxy metrics due to scale.

Users/items are highly imbalanced: a small percentage drive most interactions.

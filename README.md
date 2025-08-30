# :mag_right: Recommendation System Experiments

This project explores **recommendation system approaches** on an **implicit feedback dataset** of user–item interactions.  
The aim was to identify **practical, fast-to-compute models** that can generate recommendations at scale, given available infrastructure and deployment constraints.  

---

## 📂 Dataset

- **Scale**: Millions of rows of user interactions (`visitorid`, `itemid`, `event`)  
- **Event types**: Views, add-to-carts, and transactions  
- **Imbalance**: Most events are *views*, while transactions (the most valuable) are rare  

---

## ⚙️ Methods Tried

### 🔹 1. Sparse Collaborative Filtering (Baseline)
- Built a **user–item interaction matrix** in sparse format  
- Recommendations computed via **dot-product similarity** between users and items  
- **Advantage**: Fast, lightweight, interpretable  

---

### 🔹 2. Clustering
- Applied **K-Means** on user vectors derived from the interaction matrix  
- Grouped users into **behavioral segments**  
- Items popular within each cluster served as **segment-based recommendations**  
- **Advantage**: Useful for **cold-start users** and marketing segmentation  

---

### 🔹 3. KNN (Neighborhood Models)
- Implemented **User–User** and **Item–Item KNN** on sparse vectors  
- Found nearest neighbors using **cosine similarity**  
- Delivered intuitive recommendations:  
  - “Users like you also interacted with these items”  
  - “Items similar to what you viewed”  
- **Advantage**: Most intuitive recommendations, but slower at scale  

---

### 🔹 4. Randomised Recommendation (Deployment Extension)
During **deployment**, several challenges arose:  
- The **scale of the dataset** made some models (eg. LightFM) impractical under current compute limits  
- Certain methods (eg., KNN) became **too repetitive** in recommendations, recommending the same items for different users.
- To ensure recommendations felt **fresh and responsive**, a **randomisation component** was added to the baseline CF output  

This approach:  
- Preserves **relevance** while introducing **diversity**  
- Prevents recommendations from being identical on every run  
- Offers a more engaging user experience despite infrastructure constraints  

---

## ✅ Results & Insights

- **Sparse CF**: Most scalable under current compute limits  
- **Clustering**: Strong for segmentation and group targeting  
- **KNN**: Best interpretability but slow for large-scale deployment  
- **Randomised extension**: Practical fix for deployment, balancing **speed + diversity**  
- Event imbalance suggests **weighting transactions higher** could improve relevance  

---

## 🚧 Challenges

- **Large dataset size**: Limited advanced models without bigger compute resources  
- **Evaluation**: Measuring recommendation quality required sampling/offline proxy metrics  
- **Skewed distributions**: A small set of users/items drove most of the interactions  
- **Deployment constraints**: Led to inclusion of a **randomisation step** to improve UX  

---

# :mag_right: Recommendation System Experiments

📢 **Live Demo**: [Try the App on Streamlit Cloud 🚀](https://ecommerce-recommendation-system-001.streamlit.app/)

### Run Locally:
1. Clone the repo  
   ```bash
   git clone https://github.com/kojomensahonums/tmp2_recommendation_system.git
   cd tmp2_recommendation_system
2. pip install -r requirements.txt
3. streamlit run recommender_app.py
4. Open in browser: 👉 http://localhost:8501
---

This project explores **recommendation system approaches** on an **implicit feedback dataset** of user–item interactions.  
The aim was to identify **practical, fast-to-compute models** that can generate recommendations at scale, given available infrastructure and deployment constraints.  

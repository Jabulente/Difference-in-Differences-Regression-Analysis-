<h1 align='center'> Impact Evaluation of Marketing Campaign </h1>

### **Overview**  
This project evaluates the effectiveness of the **Summer Blitz 2024** marketing campaign on sales revenue using **simulated sales data**. The analysis employs **A/B testing and Difference-in-Differences (DiD) regression** to measure the campaign’s incremental impact while controlling for external factors.  

### **Objective**  
Determine whether the campaign drove a statistically significant increase in sales revenue by comparing **Pilot Launch Regions (treatment group)** against **Business-as-Usual Regions (control group)**.  

---  

### **Methodology**  

**1. Exploratory Data Analysis (EDA)**  
- Assessed distributions, trends, and anomalies in sales data.  
- Compared pre- and post-campaign performance across store sizes and regions.  

**2. Hypothesis Testing (A/B Testing)**  
- **Null Hypothesis (H₀):** The campaign had no effect on sales.  
- **Alternative Hypothesis (H₁):** The campaign increased sales.  
- Used **t-tests and DiD regression** to validate significance.  

**3. Regression Analysis (Difference-in-Differences)**  
- Model:  
  ```  
  Sales ~ Intercept + Store_Size + is_campaign_group + post_campaign_period + (is_campaign_group × post_campaign_period)  
  ```  
- Key Metrics:  
  - **Post-campaign effect** (time trend).  
  - **Interaction term** (campaign’s incremental lift).  

---  

### **Results**  

**Key Tables & Figures**  
- **Figure 1:** *Sales Revenue Lift Following Summer Blitz 2024 Launch* – Visualizes treatment vs. control trends.  
- **Table 1:** *Regression Results* – Displays coefficients, p-values, and percentage effects.  

### **Findings**  

- The campaign **increased sales by 11.06%** in pilot regions beyond natural market growth.  
- **Larger stores outperformed smaller ones**, confirming store size as a key revenue driver.  
- No pre-existing differences between groups, ensuring reliable comparisons.  

**Business Implication:** The campaign was successful and should be expanded, with adjustments for smaller stores.  

---  

### **Tools & Skills Demonstrated**  
- **Programming:** Python (Pandas, Statsmodels, Matplotlib/Seaborn).  
- **Statistical Methods:** A/B Testing, DiD Regression, Hypothesis Testing.  
- **Data Visualization:** Trend analysis, effect size presentation.  
- **Business Insight:** Translating statistical results into actionable strategies.  

---  

### **Folder Structure**  
```  
project/  
├── data/              # Simulated sales dataset  
├── notebooks/         # Jupyter notebooks (EDA, regression, visualization)  
├── results/           # Outputs (tables, plots, reports)  
└── README.md  
```  

---  

### **How to Use This Project**  
1. **Explore Data:** Run `EDA.ipynb` to review trends and preprocessing.  
2. **Test Hypotheses:** Execute `hypothesis_testing.ipynb` for A/B tests.  
3. **Run Regression:** Use `DID_regression.ipynb` for the full DiD analysis.  
4. **Generate Reports:** Outputs are saved in `/results`.  

---  

### **Conclusion**  
The **Summer Blitz 2024 campaign significantly boosted sales**, with a **net 11.06% lift** attributable to the intervention. Future efforts should scale the campaign while optimizing for store size variations.  

---  

### **Contact & Call to Action**  
- **Questions?** Reach out via [email/LinkedIn].  
- **Want to replicate or extend?** Fork the repository and customize the analysis.  

**Next Steps:**  
- Apply the same methodology to future campaigns.  
- Investigate strategies to improve small-store performance.  

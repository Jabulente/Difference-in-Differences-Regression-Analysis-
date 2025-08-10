import numpy as np
import pandas as pd
from datetime import datetime

def construct_dataset(
    n_stores=120,
    n_periods=60,                # 5 years monthly data
    treat_frac=0.5,               # fraction of stores in campaign group
    campaign_start_period=12,     # month index when campaign starts (e.g., Aug 2026)
    seed=42,
    baseline_sales_mean_tzs=1_200_000,
    baseline_sales_trend_tzs=12_000,
    seasonal_amplitude_tzs=10_000,
    treatment_effect_tzs=200_000,
    treatment_ramp_months=3,
    noise_sd_tzs=80_000
):
    np.random.seed(seed)
    
    store_ids = np.arange(1, n_stores + 1)
    
    # Assign stores to groups
    campaign_group_mask = np.zeros(n_stores, dtype=int)
    campaign_indices = np.random.choice(n_stores, size=int(treat_frac * n_stores), replace=False)
    campaign_group_mask[campaign_indices] = 1
    
    store_size_category = np.random.choice(['Small', 'Medium', 'Large'], size=n_stores, p=[0.4, 0.45, 0.15])
    avg_order_value_tzs_store = np.clip(np.random.normal(loc=35_000, scale=5_000, size=n_stores), 10_000, 80_000)
    
    rows = []
    start_date = datetime(2023, 1, 1)
    
    for i, sid in enumerate(store_ids):
        for t in range(1, n_periods + 1):
            date = pd.to_datetime(start_date) + pd.DateOffset(months=t - 1)
            
            size_multiplier = {'Small': 0.75, 'Medium': 1.0, 'Large': 1.3}[store_size_category[i]]
            
            # Parallel trends: same baseline pattern for both groups pre-treatment
            trend = baseline_sales_trend_tzs * (t - 1)
            seasonal = seasonal_amplitude_tzs * np.sin(2 * np.pi * (t / 12))
            store_base = baseline_sales_mean_tzs * size_multiplier
            
            sales_no_treat = store_base + trend + seasonal + np.random.normal(0, noise_sd_tzs)
            
            campaign_group = campaign_group_mask[i]
            post = 1 if t >= campaign_start_period else 0
            
            treatment_effect = 0.0
            if campaign_group and post:
                months_since_start = t - campaign_start_period + 1
                ramp_factor = min(1.0, months_since_start / treatment_ramp_months)
                treatment_effect = ramp_factor * (treatment_effect_tzs * np.random.uniform(0.85, 1.15))
            
            final_sales_tzs = sales_no_treat + treatment_effect
            
            rows.append({
                'Store_ID': sid,
                'Date': date,
                'Month Index': t,
                'Store Size': store_size_category[i],
                'Marketing Strategy': 'Pilot Launch Regions' if campaign_group else 'Business-as-Usual (BAU) Regions',
                'Average Order Values (Tsh)': int(avg_order_value_tzs_store[i]),
                'Post Campaign Period': post,
                'Sales Revenue (Tsh)': final_sales_tzs
            })
    
    df = pd.DataFrame(rows)
    return df
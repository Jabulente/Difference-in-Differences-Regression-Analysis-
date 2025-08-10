import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

def did_regression(df: pd.DataFrame, formula: str):
    model = smf.ols(formula=formula, data=df).fit()
    return model


def formart_result(model):
    result = model.summary2().tables[1].copy()  
    result = result.reset_index().rename(columns={'index': 'Variable'})
    baseline = model.params['Intercept']
    result['Percent Effect (%)'] = (result['Coef.'] / baseline) * 100
    result['Percent Diff. (%)'] = result['Percent Effect (%)'].round(2)
    result['Coef.'] = result['Coef.'].round(3)
    result['Std.Err.'] = result['Std.Err.'].round(3)
    result['t'] = result['t'].round(3)
    result['P>|t|'] = result['P>|t|'].round(4)
    result['[0.025'] = result['[0.025'].round(3)
    result['0.975]'] = result['0.975]'].round(3)
    return result
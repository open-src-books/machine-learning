# Mean Absolute Percentage Error (MAPE)

Mean Absolute Percentage Error (MAPE) is a widely used metric for evaluating the accuracy of regression models, particularly in forecasting and prediction tasks. It expresses the prediction error as a percentage of the actual values, providing an intuitive measure of accuracy. MAPE is especially useful when the scale of the target variable varies significantly.

---

## Formula

The formula for MAPE is:

$$
\text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right| \times 100
$$

Where:

- $n$: Number of observations,
- $y_i$: Actual value of the target variable,
- $\hat{y}_i$: Predicted value,
- $\left| \frac{y_i - \hat{y}_i}{y_i} \right|$: Absolute percentage error for each observation.

---

## Characteristics

1. **Expressed as a Percentage:**  
    - MAPE is unitless and provides a percentage error, making it easily interpretable and suitable for comparison across datasets with different scales.

2. **Sensitivity to Small Actual Values:**  
    - When $y_i$ is close to zero, the percentage error can become excessively large, distorting the overall MAPE value.

3. **Non-Symmetric:**  
    - MAPE treats over-predictions and under-predictions equally in magnitude but does not capture the direction of errors.

---

## Advantages

1. **Intuitive Interpretation:**  
    - The percentage representation makes MAPE easy to understand and communicate.

2. **Scale-Invariance:**  
    - MAPE is not affected by the scale of the target variable, allowing comparisons across different datasets.

3. **Commonly Used in Forecasting:**  
    - Popular in industries like finance, retail, and supply chain management due to its straightforward nature.

---

## Disadvantages

1. **Issues with Small Actual Values:**  
    - When actual values ($y_i$) are near zero, MAPE can produce extremely high or undefined errors, leading to misleading results.

2. **Overweighting Small Errors:**  
    - Observations with smaller actual values contribute disproportionately to the overall MAPE, even if the absolute errors are small.

3. **No Symmetry:**  
    - Overestimations and underestimations are treated equally in magnitude but ignore error direction.

4. **Non-Differentiable:**  
    - The absolute value makes it non-differentiable, complicating its use in optimization processes.

---

## When to Use MAPE

1. **Forecasting Accuracy:**  
    - Commonly used in time series analysis and demand forecasting.

2. **Relative Error Assessment:**  
    - When the relative size of errors matters more than absolute errors.

3. **Comparative Studies:**  
    - For comparing model accuracy across datasets with different scales.

---

## Comparison with Other Metrics

1. **MAPE vs. Mean Absolute Error (MAE):**  
    - MAE measures absolute errors in the same unit as the target variable, while MAPE represents errors as a percentage of actual values.  
    - MAPE is scale-invariant; MAE is not.

2. **MAPE vs. RMSE:**  
    - RMSE penalizes larger errors more heavily due to squaring, while MAPE treats all errors equally as a percentage.

3. **MAPE vs. Symmetric MAPE (SMAPE):**  
    - SMAPE addresses MAPE's issue with small actual values by normalizing the error using both actual and predicted values.

---

## Example Calculation

Suppose we have the following actual ($y_i$) and predicted ($\hat{y}_i$) values:

- Actual: [50, 60, 70]
- Predicted: [55, 58, 65]

1. Calculate the absolute percentage errors:
    - $\left| \frac{50 - 55}{50} \right| \times 100 = 10\%$,
    - $\left| \frac{60 - 58}{60} \right| \times 100 = 3.33\%$,
    - $\left| \frac{70 - 65}{70} \right| \times 100 = 7.14\%$.

2. Calculate MAPE:

$$
\text{MAPE} = \frac{1}{3} (10 + 3.33 + 7.14) \approx 6.16\%
$$

---

## Interpretation

A MAPE of 6.16% indicates that, on average, the model's predictions are 6.16% off from the actual values. Lower MAPE values signify higher accuracy.

---

## Use Cases

1. **Demand Forecasting:**  
    - Measuring the accuracy of sales, inventory, or production forecasts.

2. **Energy and Finance:**  
    - Evaluating prediction models for energy consumption, stock prices, or financial metrics.

3. **Supply Chain Optimization:**  
    - Ensuring accurate predictions for logistics and inventory management.

---

## Addressing MAPE Limitations

1. **Handling Small Actual Values:**  
    - Replace $y_i = 0$ with a small constant or use alternative metrics like RMSE or SMAPE.

2. **Alternative Metrics:**  
    - Use metrics such as Mean Absolute Scaled Error (MASE) or Mean Squared Percentage Error (MSPE) for specific scenarios.

3. **Error Weighting:**  
    - Adjust weighting for observations with small actual values to balance their influence on the final MAPE score.

MAPE is a simple and interpretable metric, making it highly suitable for regression and forecasting tasks. However, its limitations with small actual values and error weighting should be considered when applying it to real-world scenarios.

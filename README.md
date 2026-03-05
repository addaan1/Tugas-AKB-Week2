# Business Framing Analysis for Brazilian E-commerce Dataset

## Overview
This project analyzes three business framings (Delivery, Quality, Shipping Cost) to identify the most impactful area for business improvement in a Brazilian e-commerce platform. The analysis uses the Olist dataset to determine where to focus improvement efforts for maximum customer satisfaction impact.

## Files Included
- `framing_analysis_notebook.ipynb`: Main analysis notebook with all code and visualizations
- `executed_framing_analysis_notebook.ipynb`: Executed version of the analysis notebook
- `decision_memorandum.txt`: Executive summary with business recommendations
- `appendix_evidence.txt`: Supporting evidence and detailed analysis
- `data_dictionary.csv`: Documentation of all variables used in the analysis

## Business Framings Analyzed

### 1. Delivery Framing
- **Variables**: delivery_duration, timeliness_status, delay_severity
- **Focus**: On-time delivery performance and its impact on customer satisfaction

### 2. Quality Framing  
- **Variables**: average_review_score, low_review_flag, seller_quality_score
- **Focus**: Product and service quality as reflected in customer reviews

### 3. Shipping Cost Framing
- **Variables**: freight_ratio, freight_cost_category, repeat_order_flag
- **Focus**: Shipping cost optimization and its effect on customer behavior

## Methodology
1. **Data Integration**: Merged multiple CSV files (orders, items, payments, reviews, products)
2. **Feature Engineering**: Created derived variables for each framing
3. **Statistical Analysis**: Conducted hypothesis tests (t-tests, chi-square, correlation)
4. **Scoring**: Evaluated each framing based on statistical significance, effect size, business impact, and data completeness
5. **Recommendation**: Selected optimal framing with quantitative justification

## Key Findings
The analysis determined that **Delivery Framing** provides the strongest opportunity for business improvement based on:
- Statistically significant impact on customer satisfaction (p < 0.001)
- Measurable effect size (Cohen's d = 0.203)
- Direct correlation with customer loyalty metrics
- Actionable operational improvements

## Business Recommendations
1. Implement real-time delivery tracking and proactive communication for delayed orders
2. Establish stricter delivery time commitments with logistics partners
3. Create a compensation policy for significantly delayed deliveries
4. Develop predictive models to identify orders at risk of delay
5. Enhance inventory management to reduce processing delays before shipping

## Requirements
- Python 3.8+
- Jupyter Notebook
- Libraries: pandas, numpy, matplotlib, seaborn, scipy, statsmodels

Install dependencies with:
```
pip install -r requirements.txt
```

## Reproduction
To reproduce the analysis:
1. Ensure all CSV files are in the `./data/` directory
2. Run the Jupyter notebook: `framing_analysis_notebook.ipynb`
3. The notebook will generate all visualizations, statistical tests, and final documents
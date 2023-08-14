from dash import Dash, dcc, html, Input, Output,callback
from src.components import ids

def render(app):
    dropdown = html.Div([
        dcc.Dropdown(
        ['Business_Ethics',
        'Data_Security',
        'Access_And_Affordability',
        'Business_Model_Resilience',
        'Competitive_Behavior',
        'Critical_Incident_Risk_Management',
        'Customer_Welfare',
        'Director_Removal',
        'Employee_Engagement_Inclusion_And_Diversity',
        'Employee_Health_And_Safety',
        'Human_Rights_And_Community_Relations',
        'Labor_Practices',
        'Management_Of_Legal_And_Regulatory_Framework',
        'Physical_Impacts_Of_Climate_Change',
        'Product_Quality_And_Safety',
        'Product_Design_And_Lifecycle_Management',
        'Selling_Practices_And_Product_Labeling',
        'Supply_Chain_Management',
        'Systemic_Risk_Management',
        'Waste_And_Hazardous_Materials_Management',
        'Water_And_Wastewater_Management',
        'Air_Quality',
        'Customer_Privacy',
        'Ecological_Impacts',
        'Energy_Management',
        'GHG_Emissions'], id=ids.DROPDOWN_INPUT)
            ])
    
    return dropdown

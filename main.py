from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
'this is a test'
def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = 'ESG Insights'
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()
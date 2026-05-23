import plotly.express as px

# Lists to hold structured data for the chart axes
repo_links, stars, hover_texts = [], [], []

# Assume 'top_repos' is the list extracted from the example above
for repo in top_repos[:30]:  # Limit to top 30 items
    # Create HTML anchor tags for the x-axis labels
    name = repo['name']
    web_url = repo['html_url']
    repo_links.append(f"<a href='{web_url}'>{name}</a>")

    # Store y-axis heights
    stars.append(repo['stargazers_count'])

    # Generate interactive HTML tooltips (Hover text)
    owner = repo['owner']['login']
    desc = repo['description']
    hover_texts.append(f"{owner}<br />{desc}")

# Define metadata and generate the Plotly bar chart
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_links, y=stars, title=title,
            labels=labels, hover_name=hover_texts)

# Update layout fonts and marker properties (Color and Opacity)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                    yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

# Launch the interactive chart in your browser
fig.show()

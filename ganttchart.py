import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Read relevant material", start="2021-11-15", finish="2022-01-21", Resource="Reading"),
    dict(Task="Work on collostructional analysis", start="2021-11-15", finish="2021-12-06", Resource="Programming"),
    dict(Task="Work on transformers", start="2021-11-15", finish="2021-12-06", Resource="Programming"),
    dict(Task="Train own transformer (MAYBE)", start="2021-12-12", finish="2021-12-26", Resource="Programming"),
    dict(Task="Perform collostructional analysis on transformer trained corpus (MAYBE)", start="2021-12-12", finish="2021-12-26", Resource="Programming"),
    dict(Task="Write introduction and methods used", start="2021-11-27", finish="2021-12-12", Resource="Writing"),
    dict(Task="Write on the received results", start="2021-12-12", finish="2021-12-26", Resource="Writing"),
    dict(Task="Write more on possible new results and improve other parts of thesis", start="2021-12-26", finish="2022-01-07", Resource="Writing"),
    dict(Task="Writing the evaluation & conclusion of the research", start="2022-01-07", finish="2022-01-21", Resource="Writing"),
    dict(Task="Finalize writing of the thesis", start="2022-01-21", finish="2022-02-04", Resource="Writing"),
    dict(Task="Make and present the final presentation", start="2022-01-21", finish="2022-02-04", Resource="Presenting"),
    dict(Task="Make and record mid-term presentation", start="2021-12-06", finish="2021-12-12", Resource="Presenting"),
])

fig = px.timeline(df, x_start="start", x_end="finish", y="Task", color="Resource")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.write_html("ganttchart.html")
from dash import Dash, html, dash_table, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from . import data
import plotly.express as px

dash2 = Dash(
    requests_pathname_prefix="/dash/app2/", external_stylesheets=[dbc.themes.BOOTSTRAP]
)
dash2.title = "信用卡消費樣態"
lastest_data = data.search_data(dataName="職業類別",tableName="job")


lastest_df = pd.DataFrame(
    lastest_data, columns=["年", "月", "地區", "產業別", "職業類別", "信用卡交易筆數", "信用卡交易金額"]
)


dash2.layout = html.Div(
    [
        dbc.Container(
            [
                html.Div(
                    [
                        html.Div(
                            [html.H1("各職業類別信用卡消費樣態")],
                            className="col text-center",
                        )
                    ],
                    className="row",
                    style={"paddingTop": "2rem"},
                ),
                html.Div(
                    [
                        dbc.DropdownMenu(
                            label="資料類別",
                            children=[
                                dbc.DropdownMenuItem(
                                    "首頁", href="/dash/index/", external_link=True
                                ),
                                dbc.DropdownMenuItem(
                                    "教育程度", href="/dash/app/", external_link=True
                                ),
                                dbc.DropdownMenuItem(
                                    "年齡層", href="/dash/app1/", external_link=True
                                ),
                                dbc.DropdownMenuItem(
                                    "性別", href="/dash/app3/", external_link=True
                                ),
                                dbc.DropdownMenuItem(
                                    "年收入", href="/dash/app4/", external_link=True
                                ),
                            ],
                            color="success",
                            style={"marginRight": "1rem"},
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupText("月份"),
                                dbc.Select(
                                    id="month",
                                    value="ALL",
                                    options=[
                                        {"label": "1月", "value": "1"},
                                        {"label": "2月", "value": "2"},
                                        {"label": "3月", "value": "3"},
                                        {"label": "4月", "value": "4"},
                                        {"label": "5月", "value": "5"},
                                        {"label": "6月", "value": "6"},
                                        {"label": "7月", "value": "7"},
                                        {"label": "8月", "value": "8"},
                                        {"label": "9月", "value": "9"},
                                        {"label": "10月", "value": "10"},
                                        {"label": "11月", "value": "11"},
                                        {"label": "12月", "value": "12"},
                                        {"label": "ALL", "value": "ALL"},
                                    ],
                                    style={"marginRight": "1rem"},
                                ),
                            ],
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupText("地區"),
                                dbc.Select(
                                    id="area",
                                    value="ALL",
                                    options=[
                                        {"label": "臺北市", "value": "臺北市"},
                                        {"label": "新北市", "value": "新北市"},
                                        {"label": "桃園市", "value": "桃園市"},
                                        {"label": "臺中市", "value": "臺中市"},
                                        {"label": "臺南市", "value": "臺南市"},
                                        {"label": "高雄市", "value": "高雄市"},
                                        {"label": "ALL", "value": "ALL"},
                                    ],
                                    style={"marginRight": "1rem"},
                                ),
                            ],
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupText("產業別"),
                                dbc.Select(
                                    id="industry",
                                    value="ALL",
                                    options=[
                                        {"label": "食", "value": "食"},
                                        {"label": "衣", "value": "衣"},
                                        {"label": "住", "value": "住"},
                                        {"label": "行", "value": "行"},
                                        {"label": "文教康樂", "value": "文教康樂"},
                                        {"label": "百貨", "value": "百貨"},
                                        {"label": "ALL", "value": "ALL"},
                                    ],
                                    style={"marginRight": "1rem"},
                                ),
                            ],
                        ),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupText("職業類別"),
                                dbc.Select(
                                    id="job",
                                    value="ALL",
                                    options=[
                                        {"label": "軍警人員一", "value": "軍警人員一"},
                                        {"label": "軍警人員二", "value": "軍警人員二"},
                                        {
                                            "label": "其他公共行政類",
                                            "value": "其他公共行政類",
                                        },
                                        {"label": "教育類", "value": "教育類"},
                                        {
                                            "label": "工商及服務類",
                                            "value": "工商及服務類",
                                        },
                                        {
                                            "label": "專業及技術服務類",
                                            "value": "專業及技術服務類",
                                        },
                                        {"label": "ALL", "value": "ALL"},
                                    ],
                                ),
                            ],
                        ),
                    ],
                    className="d-flex justify-content-center",
                    style={"paddingTop": "2rem"},
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                dash_table.DataTable(
                                    id="data",
                                    data=lastest_df.to_dict("records"),
                                    columns=[
                                        {"id": column, "name": column}
                                        for column in lastest_df.columns
                                    ],
                                    page_size=20,
                                    fixed_rows={"headers": True},
                                    style_table={
                                        "height": "300px",
                                        "overflowY": "auto",
                                    },
                                    style_cell={
                                        "text_align": "center",
                                    },
                                ),
                            ],
                            className="col text-center",
                        )
                    ],
                    className="row",
                    style={"paddingTop": "2rem"},
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                dcc.Graph(id="graph", style={"flex": "5"}),
                                dcc.Graph(id="graph_sunburst", style={"flex": "5"}),
                            ],
                            style={
                                "display": "flex",
                                "flexWrap": "wrap",
                                "paddingTop": "2rem",
                            },
                        ),
                        dcc.Graph(id="graph_line"),
                        dcc.Graph(id="graph_bar"),
                    ],
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.P("來源："),
                                html.P("Data： 聯合信用卡處理中心Open API"),
                                html.P("Icon： Image by toffeomurice from Pixabay"),
                            ],
                            className="col",
                        )
                    ],
                    className="row",
                    style={
                        "paddingTop": "2rem",
                        "fontSize": "0.8rem",
                        "lineHeight": "0.3rem",
                    },
                ),
            ]
        )
    ],
    className="container-lg",
)


@dash2.callback(
    Output("data", "data"),
    [Input("area", "value"), Input("month", "value"), Input("industry", "value"), Input("job", "value")],
)
def update_table(selected_area, selected_month, selected_industry, selected_job):
    filtered_data = [
        row
        for row in lastest_data
        if (selected_area == "ALL" or row[2] == selected_area)
        and (selected_month == "ALL" or str(row[1]) == selected_month)
        and (selected_industry == "ALL" or row[3] == selected_industry)
        and (selected_job == "ALL" or row[4] == selected_job)
    ]

    update_df = pd.DataFrame(
        filtered_data, columns=["年", "月", "地區", "產業別", "職業類別", "信用卡交易筆數", "信用卡交易金額"]
    )
    return update_df.to_dict("records")

@dash2.callback(
    Output("graph", "figure"),
    [Input("industry","value"),Input("job","value")]
)
def update_pie_chart(selected_value, selected_job_value):
    global lastest_df
    if selected_value == "ALL":
        industry_sum = lastest_df.groupby('產業別')['信用卡交易金額'].sum().reset_index()
        fig = px.pie(industry_sum, values='信用卡交易金額', names='產業別', title='各產業別信用卡交易金額分布', height=500)
    else:
        if selected_job_value != 'ALL':
            filtered_df = lastest_df[lastest_df['產業別'] == f'{selected_value}']
            fig = px.pie(filtered_df, values='信用卡交易金額', names='職業類別',title=f'{selected_value} / {selected_job_value} 信用卡交易金額占比', height=500)
            highlight_job = selected_job_value
            fig.update_traces(
                marker=dict(colors=['rgba(1,87,155,0.2)' if edu != highlight_job else '' for edu in fig.data[0]['labels']]),
            )
        else:
            filtered_df = lastest_df[lastest_df['產業別'] == f'{selected_value}']
            fig = px.pie(filtered_df, values='信用卡交易金額', names='職業類別', title=f'{selected_value} / 各職業類別信用卡交易金額分布', height=500)
    return fig

@dash2.callback(
    Output("graph_line", "figure"),
    Input("job","value")
)
def update_line_chart(selected_job):
    global lastest_df
    if selected_job == "ALL":
        monthly_total = lastest_df.groupby(['年', '月', '職業類別'])['信用卡交易金額'].sum().reset_index()
        fig = px.line(monthly_total, x="月", y="信用卡交易金額", color="職業類別", title='各職業類別每月信用卡交易金額趨勢', markers=True, height=450)
    else:
        monthly_total = lastest_df.groupby(['年', '月', '職業類別'])['信用卡交易金額'].sum().reset_index()
        filtered_df = monthly_total[monthly_total['職業類別'] == f'{selected_job}']
        fig = px.line(filtered_df, x="月", y="信用卡交易金額", color="職業類別", title=f'{selected_job}每月信用卡交易金額趨勢', markers=True, height=450)
    return fig

@dash2.callback(
    Output("graph_bar", "figure"),
    Input("area","value")
)
def update_bar_chart(selected_area):
    global lastest_df
    if selected_area == "ALL":
        region_sum = lastest_df.groupby('地區')['信用卡交易金額'].sum().reset_index()
        fig = px.bar(region_sum, x='地區', y='信用卡交易金額', title='各地區信用卡交易金額', height=450)
    else:
        region_sum = lastest_df.groupby('地區')['信用卡交易金額'].sum().reset_index()
        fig = px.bar(region_sum, x='地區', y='信用卡交易金額', title=f'{selected_area}信用卡交易金額', height=450)
        highlighted_region = selected_area
        fig.update_traces(marker_color=['rgba(1,87,155,0.2)' if region != highlighted_region else 'blue' for region in region_sum['地區']])
    return fig

@dash2.callback(
    Output("graph_sunburst", "figure"),
    [Input("month","value"),Input("area","value"),Input("industry","value")]
)
def update_sunburst_chart(selected_mon,selected_ar,selected_ind):
    global lastest_df
    if selected_mon == "ALL" and selected_ar == "ALL" and selected_ind == "ALL":
        fig = px.sunburst(lastest_df, path=['年', '月', '地區', '產業別', '職業類別'], values='信用卡交易金額', title='2023年各職業類別信用卡交易分布', height=500)
    elif selected_mon != "ALL" and selected_ar == "ALL" and selected_ind == "ALL":
        filtered_df = lastest_df[lastest_df['月'].astype(str) == selected_mon]
        fig = px.sunburst(filtered_df, path=['月', '地區', '產業別', '職業類別'], values='信用卡交易金額',title=f'{selected_mon}月信用卡交易分布', height=500)
    elif (selected_mon == "ALL" and selected_ar != "ALL" and selected_ind == "ALL"):
        filtered_df = lastest_df[lastest_df['地區'] == selected_ar]
        fig = px.sunburst(filtered_df, path=['地區', '產業別', '職業類別'], values='信用卡交易金額',title=f'{selected_ar}信用卡交易分布', height=500)
    elif (selected_mon == "ALL" and selected_ar != "ALL" and selected_ind != "ALL"):
        filtered_df = lastest_df[(lastest_df['地區'] == selected_ar) & (lastest_df['產業別'] == selected_ind)]
        fig = px.sunburst(filtered_df, path=['地區', '產業別', '職業類別'], values='信用卡交易金額',title=f'{selected_ar} / {selected_ind} 信用卡交易分布', height=500)
    elif selected_mon != "ALL" and selected_ar != "ALL" and selected_ind == "ALL":
        filtered_df = lastest_df[(lastest_df['月'].astype(str) == selected_mon) & (lastest_df['地區'] == selected_ar)]
        fig = px.sunburst(filtered_df, path=['地區', '產業別', '職業類別'], values='信用卡交易金額',title=f'{selected_mon}月 / {selected_ar} 信用卡交易分布', height=500)
    elif selected_mon != "ALL" and selected_ar == "ALL" and selected_ind != "ALL":
        filtered_df = lastest_df[(lastest_df['月'].astype(str) == selected_mon) & (lastest_df['產業別'] == selected_ind)]
        fig = px.sunburst(filtered_df, path=['月', '產業別', '職業類別'], values='信用卡交易金額',title=f'{selected_mon}月 / {selected_ind} 信用卡交易分布', height=500)
    elif selected_mon != "ALL" and selected_ar != "ALL" and selected_ind != "ALL":
        filtered_df = lastest_df[(lastest_df['月'].astype(str) == selected_mon) & (lastest_df['地區'] == selected_ar) & (lastest_df['產業別'] == selected_ind)]
        fig = px.sunburst(filtered_df, path=['地區', '產業別', '職業類別'], values='信用卡交易金額',title=f'{selected_mon}月 / {selected_ar} / {selected_ind} / 各職業類別信用卡交易分布', height=500)
    return fig

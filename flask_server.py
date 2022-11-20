from flask import Flask, render_template, jsonify, redirect, url_for, request, session
from insights import getAllPost, getPostInsights, getCreds
from posting_content import post_image, post_video

app = Flask(__name__)


@app.route('/get_barchart_data')
def get_barchart_data():
    barChartData = []

    eachBarChart = {}
    eachBarChart['group'] = "Class I"
    eachBarChart['category'] = "Car"
    eachBarChart['measure'] = 10
    barChartData.append(eachBarChart)

    eachBarChart = {}
    eachBarChart['group'] = "Class I"
    eachBarChart['category'] = "Car"
    eachBarChart['measure'] = 20
    barChartData.append(eachBarChart)

    eachBarChart = {}
    eachBarChart['group'] = "Class II"
    eachBarChart['category'] = "Truck"
    eachBarChart['measure'] = 25
    barChartData.append(eachBarChart)

    eachBarChart = {}
    eachBarChart['group'] = "Class III"
    eachBarChart['category'] = "Bus"
    eachBarChart['measure'] = 30
    barChartData.append(eachBarChart)
    j = jsonify(barChartData)
    return jsonify(barChartData)


@app.route('/', methods=['GET', 'POST'])
def index():
    credential_params = getCreds()
    posts = getAllPost()
    post_insight = getPostInsights('18325478134037207', 'IMAGE')
    return render_template('index.html',
                           instagram_username=credential_params['ig_username'],
                           posts=posts,
                           message='social media automation server is running')


if __name__ == '__main__':
    app.run(debug=True)

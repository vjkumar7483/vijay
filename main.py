# Copyright 2019 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, request, make_response, jsonify
import pandas as pd

final_list=pd.read_excel('gs://sunday-msayty.appspot.com/final_list.xlsx')
var_list=final_list.set_index('Variable')['Defination'].to_dict()

# initialize the flask app
app = Flask(__name__)

# create a route for webhook
@app.route('/', methods=['POST'])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    # return response
    return make_response(jsonify(results(req)))
# function for responses
def results(req):
    # fetch action from json
    action = req.get('queryResult').get('action')
    #if req.get("queryResult").get("action") != "Defination":
     #   return {}
    result = req.get("queryResult")
    parameter = result.get("parameters")
    variable = parameter.get("variable")
    variable=tuple(variable)
    defination = var_list
    speech =  str(defination[variable[0]])
    print(speech)
    # return a fulfillment response
    return {'fulfillmentText': speech }

# run the app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)

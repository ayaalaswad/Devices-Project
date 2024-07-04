from flask import Flask, request, jsonify, Response
import pandas as pd
import pickle

app = Flask(__name__)
df = pd.read_csv('./test - test.csv')

@app.route('/api/devices', methods=['GET'])
def getAllDevices():
    return Response(df.to_json(orient="records"), mimetype='application/json')

@app.route('/api/devices/<id>', methods=['GET'])
def getSingleDevice(id):
    device = df.query(f'id == {id}')
    return Response(device.to_json(orient="records"), mimetype='application/json')

@app.route('/api/devices', methods=['POST'])
def addDevice():
    global df
    data = request.json
    newRecord = pd.DataFrame([data])
    df = pd.concat([newRecord, df])
    df.to_csv('./test - test.csv')
    df = pd.read_csv('./test - test.csv')
    return Response(newRecord.to_json(orient="records"), mimetype='application/json')
    
@app.route('/api/predict/<device_id>', methods=['POST'])
def predictDevice(device_id):
    device = df.query(f'id == {device_id}')
    device = device.drop(['id', 'Unnamed: 0'], axis=1)
    with open('model2.pkl', 'rb') as f:
        clf = pickle.load(f)
    result = clf.predict(device)
    return jsonify({'Price': f'{result}'})

if __name__ == '__main__':
    app.run(debug=True)
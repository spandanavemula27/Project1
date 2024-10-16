import csv
import numpy
from elasticnet.models.ElasticNet import ElasticNetModel

def test_predict():
    model = ElasticNetModel()
    data = []
    with open("auto-mpg.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    X = numpy.array([[v for k,v in datum.items() if k.startswith('x')] for datum in data])
    y = numpy.array([[v for k,v in datum.items() if k=='y'] for datum in data])
    results = model.fit(X,y)
    preds = results.predict(X)
    assert preds == 0.5

import joblib
from .features_extraction import look_url
import sys
import numpy as np

# from .features_extraction import LOCALHOST_PATH, DIRECTORY_NAME
import pickle
import os
def get_prediction_from_url(test_url):
    features_test = look_url(test_url)

    features_test = np.array(features_test).reshape((1, -1))
    print('=============get_prediction_from_url======================')
    print(features_test)
    ll = os.path.dirname(__file__)
    print(ll)
    clf = joblib.load(ll+'/classifier/random_forest.pkl')

    pred = clf.predict(features_test)
    print(pred)
    return pred


def main():
    # url = sys.argv[1]
    url = 'http://bongatoken.ru/index.php?do=feedback'

    pred = get_prediction_from_url(url)
    print('-----------------------')
    print(pred)

    if int(pred[0]) == 1:

        print("SAFE")
    elif int(pred[0]) == -1:
        print("PHISHING")



        # print 'Error -', features_test


if __name__ == "__main__":
    pass
    # main()
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
    #
    #
    # import requests
    # res =requests.get('https://classificadovitoria.com.br/shalom/ab_/home.php?email=',allow_redirects=False,headers=headers)
    # print(res.text)
    # print(res.status_code)
    # print(res.headers)
    # print(res.is_redirect)
    # print(res.request)
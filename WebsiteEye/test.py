import joblib
from WebsiteEye.features_extraction import look_url
import sys
import numpy as np

# from .features_extraction import LOCALHOST_PATH, DIRECTORY_NAME
import pickle

def get_prediction_from_url(test_url):
    features_test = look_url(test_url)
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))
    print('===================================')
    print(features_test)

    # clf = joblib.load('./classifier/random_forest.pkl')
    # with open('./classifier/random_forest.pkl') as f:
    #     clf = pickle.load(f, encoding='latin1')
    # clf = pickle.load(open("./classifier/random_forest.pkl", 'rb'), encoding='utf-8')
    clf = joblib.load('./classifier/random_forest.pkl')

    pred = clf.predict(features_test)
    print(pred)
    return pred


def main():
    # url = sys.argv[1]
    url = 'http://bongatoken.ru/index.php?do=feedback'

    pred = get_prediction_from_url(url)
    print('-----------------------')
    print(pred)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if int(pred[0]) == 1:
        # print "The website is safe to browse"
        print("SAFE")
    elif int(pred[0]) == -1:
        # print "The website has phishing features. DO NOT VISIT!"
        print("PHISHING")



        # print 'Error -', features_test


if __name__ == "__main__":
    main()
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
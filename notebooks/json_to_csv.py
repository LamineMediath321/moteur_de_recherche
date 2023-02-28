import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import json


def json_csv(path):
    json_list = []
    for jsonfile in glob.glob(path + '/*.json'):
        with open(jsonfile, encoding='utf-8') as f:
            data = json.load(f)
            value = (data['identifiantArticle'], data['urlArticle'],
                     data['sourceArticle'], data['thematiqueArticle'],
                     data['imagesArticle'], data['titreArticle'],
                     data['resumeArticle'], data['auteurArticle'],
                     data['datePublicationArticle'], data['contenuArticle'])
        json_list.append(value)
    column_name = ['identifiantArticle', 'urlArticle',
                   'sourceArticle', 'thematiqueArticle',
                   'imagesArticle', 'titreArticle',
                   'resumeArticle', 'auteurArticle',
                   'datePublicationArticle', 'contenuArticle']
    json_df = pd.DataFrame(json_list, columns=column_name)
    return json_df


def main():
    json_path = os.path.join(os.getcwd(), ('articles'))
    json_df = json_csv(json_path)
    json_df.to_csv(('articles/articles.csv'), index=None)
    print('Successfully converted xml to csv.')


main()

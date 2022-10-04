# -*- encoding: utf-8 -*-
'''
@File    :   数据格式互转.py
@Author  :   北极星光 
@Contact :   light22@126.com
'''
import pandas as pd
from pandas import DataFrame


def read_data(src_path: str):
    try:
        if src_path.split('.')[-1] == 'xlsx':
            data = pd.read_excel(src_path)
        elif src_path.split('.')[-1] == 'xml':
            data = pd.read_xml(src_path)
        elif src_path.split('.')[-1] == 'json':
            data = pd.read_json(src_path)
        elif src_path.split('.')[-1] == 'csv':
            data = pd.read_csv(src_path)
        elif src_path.split('.')[-1] == 'html':
            data = pd.read_html(src_path)
        else:
            print('源文件格式错误')
            return
    except:
        print('源文件格式错误')
        return
    return data


def save_data(data: DataFrame, tag_path: str):
    try:
        if tag_path.split('.')[-1] == 'xlsx':
            data.to_excel(tag_path, index=False)
        elif tag_path.split('.')[-1] == 'xml':
            data.to_xml(tag_path, index=False)
        elif tag_path.split('.')[-1] == 'json':
            data.to_json(tag_path, force_ascii=False)
        elif tag_path.split('.')[-1] == 'csv':
            data.to_csv(tag_path, index=False)
        elif tag_path.split('.')[-1] == 'html':
            data.to_html(tag_path, index=False)
        else:
            print('输出文件格式错误')
            return 'E'
    except:
        print('输出文件格式错误')
        return 'E'


def main(src_path, tag_path):
    data = read_data(src_path)
    if str(data) != 'None':
        result = save_data(data, tag_path)
        if result != 'E':
            print(
                f"已成功将{src_path.split('.')[-1]}文件转换为{tag_path.split('.')[-1]}文件，并保存至{tag_path}")


if __name__ == '__main__':
    src_path = r"D:\Desktop\示例.xlsx"
    json_path = 'D:/Desktop/json.json'
    excel_path = 'D:/Desktop/excel.xlsx'
    xml_path = 'D:/Desktop/xml.xml'
    csv_path = 'D:/Desktop/csv.csv'
    html_path = 'D:/Desktop/html.html'
    main(src_path, json_path)

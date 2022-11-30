# 人工智能
# 开发人：高云龙
# 开发时间：2022/11/29 上午10:08
import numpy as np
"""
0 ：节约标准煤
（万吨）
1：减排二氧化碳当量（万吨）
2：温室气体
3：办公用纸
4：用纸量
5：绿色信贷
6：普惠金融
7：每股
8：员工总数
9：女性员工数量
10：涉农
11：公益
12：总资产
13：纳税
"""
import pandas as pd
import os

def predict(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    data = pd.read_csv('/home/barry_gyl/fata_data/ESG_homo_eval.csv')
    # print(data)
    dt = pd.DataFrame([a,b,c,d,e,f,g,h,i,j,k,l,m,n,0]).T
    dt.columns = data.columns
    df_new = pd.concat([data,dt],ignore_index=True)
    # print(df_new)
    df_new.to_csv('/home/barry_gyl/fata_data/ESG_homo_eval.csv')

os.system('echo %s | sudo -S %s'% ('1635500367', 'docker restart standalone_fate && docker exec -i $(docker ps -aqf "name=standalone_fate") bash && source bin/init_env.sh && flow job submit -c ./examples/dsl/v2/homo_secureboost/test_predict_conf.json'))
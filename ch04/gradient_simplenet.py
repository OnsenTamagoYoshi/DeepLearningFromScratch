# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.pardir) #親ディレクトリのファイルをインポートするための設定
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient  import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3) #ガウス分布(正規分布)で初期化
        
    #予測するためのメソッド
    def predict(self, x):
        return np.dot(x, self.W)
    
    #損失関数の値を求めるメソッド
    #x:入力データ
    #t:正解ラベル
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        
        return loss
        

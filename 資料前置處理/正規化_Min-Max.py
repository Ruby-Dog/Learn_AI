from __future__ import division


def width(lst):  #獲得矩陣column數量
  i=0
  for j in lst[0]:
    i=i+1
  return i  


def AutoNorm(mat):   #mat為矩陣(二維陣列)
  row_count=len(mat)  #矩陣row數量from __future__ import division
  column_count=width(mat) #矩陣column數量
  MinNum =[999999999]*column_count  #先將MinNum裡的數都設為最大值,等等比較時只要比他小就取代他的值成為最小值,再繼續比下去
  MaxNum =[0]*column_count      #先將MaxNum裡的數都設為最小值,等等比較時只要比他大就取代他的值成為最大值,再繼續比下去
  
  # 找出每一欄位(column)的最大值
  for r in mat:       # r為row c為column 
    for c in range(0,column_count):
      if r[c]>MaxNum[c]:
        MaxNum[c]=r[c]
  
  # 找出每一欄位(column)最小值
  for r in mat:
    for c in range(0,column_count):
      if r[c]<MinNum[c]:
        MinNum[c]=r[c]


  section=list(map(lambda x:x[0]-x[1],zip(MaxNum,MinNum)))
  
  NormMat=[]

  for k in mat:

    distance=list(map(lambda x: x[0]-x[1], zip(k,MinNum)))
    value=list(map(lambda x: x[0]/x[1], zip(distance,section)))
    NormMat.append(value)

  return NormMat    
  
  
  

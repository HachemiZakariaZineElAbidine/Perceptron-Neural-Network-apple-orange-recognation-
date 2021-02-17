from sklearn.linear_model import Perceptron



#features = [[140,'smooth'],[130,'smooth'],[150,'bumpy'],[170,'bumpy'],[200,'bumpy'],[120,'smooth']]
final_features = [[140,1],[130,1],[150,1],[170,1],[200,1],[120,0]]

#lables = ['apple','apple','orange','orange''orange','apple']
final_lables = [0,0,1,1,1,0]

clf = Perceptron()
clf.fit(final_features,final_lables)
width = int(input("Give me the width : "))
adj = int(input("Give me the state :\n1-smooth\n2-bumpy"))

if adj == 2 :
    adj = 0

result = clf.predict([[width,adj]])
if result == 0 :
    print('predict apple')
if result == 1 :
    print('predict orange')    

print(f'score {clf.score(final_features,final_lables)}')

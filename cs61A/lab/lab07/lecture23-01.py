class Restaurant:
    all=[]
    def __init__(self,name,stars):
        self.name = name
        self.stars = stars
        Restaurant.all.append(self)

    def similiar(self,k , similarity):
        """
     "Return the K most similar restaurants to SELF"
     similarity 是个函数，比如我们通过星星找相似
     >>>g=Restaurant('Ramen House',4)
     >>>g.similiar(1,lambda k: k.stars)
     Restaurant: Vietnam resturant
        """
        others=[restaurant  for restaurant in Restaurant.all if restaurant!=self]
        others.sort(key=lambda r:abs(similarity(self)-similarity(r)))#根据similarity
        return others[:k]
    
    def __repr__(self):
        return f"{self.name},{self.stars}✨"
g=Restaurant('Vietnam resturant',4)
Restaurant('Mac Donald',3)
Restaurant('Ramen House',4)

print(g.similiar(2,lambda r:r.stars))


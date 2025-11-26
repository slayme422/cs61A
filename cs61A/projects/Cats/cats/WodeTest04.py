player1_score=[60,20,90]
player2_score=[70,30,50]
player3_score=[80,90,40]
scores=[]
def scores_append(player_score,scores):
    scores.append(player_score)
    return scores

scores_append(player1_score,scores)
scores_append(player2_score,scores)
scores_append(player3_score,scores)

#[[60, 20, 90], [70, 30, 50], [80, 90, 40]]
player_list=[]

ids=['1','2','3']

def player_append(ids,scores):
    
    player_list=[]
    for i in range(len(ids)):
        player_dictionary={
            'id': ids[i],
            'score':scores[i]
        }
        player_list.append(player_dictionary)
    return player_list

players_list=player_append(ids,scores)


def search_player_score(id ,players_list):
    for player_list in players_list:
        if player_list['id']== id :
            scores=player_list['score']
            return scores
    
    print(f"未找到id为{id}的player的分数")
        

scores=search_player_score('1',players_list)
print(scores)
player_index= list(range(len(scores)))
print(player_index)

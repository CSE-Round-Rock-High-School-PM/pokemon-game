# @author iedgeley
# @date 7.22.14
# @title Pokemon game
# Tries to string together a sequence of Pokemon using the last letter of one pokemon to the first letter of another!
# It does not work like you'd expect!! Because I am a bad programmer!!

pokemon = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

pokeList = pokemon.split(" ")

def pokeRecur(words):
    word = words[len(words)-1]
    lastLetter = word[word.__len__()-1]
    if len(words) == 70:
         return words  
    for item in pokeList:
        if item[0] == lastLetter:
            if item not in words:
                words.append(item)
                return pokeRecur(words)
    return words

for p in pokeList:
    lst = [p]
    #print lst
    ans = pokeRecur(lst)
    print ans            

    
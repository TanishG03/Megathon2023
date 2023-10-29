for i in range(100):
    conscientiousness = float(input())
    neuroticism = float(input())
    agreeableness = float(input())
    extroversion = float(input())
    openness = float(input())

    neuro = 5 - neuroticism
    def tech():
        tech_score = (conscientiousness*7) + (neuro*5) + (agreeableness *2) + (extroversion*1) + (openness *6)
        tech_score=tech_score/105
        tech_score = tech_score *100
        # print(tech_score)
        return tech_score
    
    def sale():
        sale_score = (conscientiousness*7) + (neuro*5) + (agreeableness *2) + (extroversion*6) + (openness *1)
        sale_score=sale_score/105
        sale_score = sale_score *100
        # print(sale_score)   
        return sale_score

    def check():
        if((tech()> sale()) and (tech()>50 or openness >2)):
            print("suitable for tech job")
        elif(tech()<sale() and ((sale()>50) or (extroversion >=3 ))):
            print("suitable for sales job")
        elif(tech()==sale() and tech() >50 and (extroversion > openness)):
            print("suitable for sales")
        elif(tech()==sale() and tech() >50 and (extroversion < openness)):
            print("suitable for tech")
        elif(tech()==sale() and tech() >50):
            print("suitable for both")
        else:
            print("suitable for none")
            
    print(tech())
    print(sale())   
    check()
    
    
    
    
    
    
    # C N A E O
    
    # How meticulous are you when it comes to quality and accuracy in your work?
    # How well do you collaborate with team members to achieve common goals?
    # put your own point forward
    # conducted/organized events
    # public speaking
    # participated in discussions
    
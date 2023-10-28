def assess_job_suitability(conscientiousness, neuroticism, agreeableness, extroversion, openness):
    neuro = 5 - neuroticism

    def tech():
        tech_score = (conscientiousness * 7) + (neuro * 5) + (agreeableness * 2) + (extroversion * 1) + (openness * 6)
        tech_score = (tech_score / 105) * 100
        return tech_score

    def sale():
        sale_score = (conscientiousness * 7) + (neuro * 5) + (agreeableness * 2) + (extroversion * 6) + (openness * 1)
        sale_score = (sale_score / 105) * 100
        return sale_score

    def check():
        if tech() > sale() and (tech() > 60 or openness > 2):
            return "suitable for tech job"
        elif tech() < sale() and (sale() > 60 or extroversion >= 3):
            return "suitable for sales job"
        elif tech() == sale() and tech() > 50:
            if extroversion > openness:
                return "suitable for sales"
            elif extroversion < openness:
                return "suitable for tech"
            else:
                return "suitable for both"
        else:
            return "suitable for none"

    tech_score = tech()
    sale_score = sale()
    suitability = check()

    return tech_score, sale_score, suitability

for i in range(1000):
    inputs = input().split(",")
    conscientiousness, neuroticism, agreeableness, extroversion, openness = map(float, inputs)
    tech_score, sale_score, suitability = assess_job_suitability(conscientiousness, neuroticism, agreeableness, extroversion, openness)
    # print("Tech Score:", tech_score)
    # print("Sales Score:", sale_score)
    print(suitability)

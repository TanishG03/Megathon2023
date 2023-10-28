### THIS LIBRARY IGNORES ARTICLES, PREPOSITIONS ETC
from empath import Empath
lexicon = Empath()
# custom_categories = {
#     'time': ['today', 'tomorrow', 'yesterday', 'now', 'later']
# }
# lexicon.create_category("custom_time", custom_categories['time'])

### INTROVERT:
# text = "I’ve been waking up on time so far. What has it been, 5 days? Dear me, I'll never keep it up, being such not a morning person and all. But maybe i'll adjust, or not. i want internet access in my room, i don't have it yet, but i will on Wednesday? I think. but that ain't soon enough, cause i got calculus homework."

### EXTROVERT:
# text = "I have some really random thoughts. I want to get the best things out of life. but i fear that i want too much! what if i fall flat on my face and don't amount to anything. but i feel like i was born to do BIG things on this earth. but who knows, there is this persian party today."

### NEUROTIC:
# text = "One of my friends just barged in, and I jumped in my seat. This is crazy. I should tell him not to do that again. I’m not that fastidious actually. But certain things annoy me. The things that would annoy me would actually annoy any normal human being, so I know I’m not a freak."
# text = "Oh my goodness, I can't believe I forgot to double-check the stove before leaving the house today! What if it's still on, and the entire place goes up in flames? And did I lock the front door properly? What if someone breaks in? I knew I should have taken a different route to work, this traffic is just too risky! And what if I mess up that presentation later? It's going to be a disaster, and everyone will notice, and I'll lose my job for sure. Why does everything have to be so stressful and uncertain all the time?"

### EMOTIONALY STABLE:
# text = "I should excel in this sport because I know how to push my body harder than anyone I know, no matter what the test I always push my body harder than everyone else. I want to be the best no matter what the sport or event. I should also be good at this because I love to ride my bike."
# text = " find that maintaining emotional stability is key to a fulfilling life. It's essential to keep a calm and level head, even when things get challenging. Emotions are part of being human, but it's important not to let them control our decisions. By staying emotionally steady, I can navigate both the highs and lows of life with grace and resilience. I've learned to adapt and find a sense of inner peace, no matter the circumstances. This stability not only benefits my own well-being but also allows me to be a source of support for those around me."

### UNCONSCIENTIOUS:
# text = "I tried to yell at you through the window. Oh. xxxx’s fucking a dumb ass. Look at him. Look at him, dude. Look at him. I wish we had a camera. He’s fucking brushing his t-shirt with a tooth brush. Get a kick of it. Don’t steal nothing."
# text = "You know, I've never been one for strict routines or overthinking things. Life is too short to be bogged down by rules and expectations. I prefer to go with the flow, embrace spontaneity, and enjoy the journey without too much planning. Sure, I might miss a deadline here and there, but I believe in the freedom to explore, make mistakes, and learn along the way. Sometimes, it's the unexpected twists and turns that lead to the most exciting experiences. So, I'll keep taking life as it comes and making the most of every moment, whether it fits a schedule or not."

### CONSCIENTIOUS:
# text = "I don’t, I don’t know for a fact but I would imagine that historically women who have entered prostitution have done so, not everyone, but for the majority out of extreme desperation and I think. I don’t know, i think people understand that desperation and they don’t don’t see"
# text = "I firmly believe in the power of conscientiousness. It's about setting clear goals, planning meticulously, and staying committed to excellence in all aspects of life. Attention to detail is crucial, and I strive to meet and often exceed the high standards I set for myself. My sense of duty drives me to fulfill my responsibilities and obligations with unwavering dedication. I believe in being dependable and consistent, and I take pride in delivering quality work. Conscientiousness is not just a trait; it's a way of life, a path to personal growth, and a commitment to making a positive impact in everything I do."

### OPENNESS:
# text = "I'm really excited about this new opportunity to explore different perspectives and ideas. It's amazing how diverse the world is, and I genuinely enjoy learning from people with unique experiences. I believe that the more open-minded we are, the richer our lives become. I'm always up for trying something new or going on an adventure; you never know what you might discover! Being open to change and embracing new experiences is, in my opinion, the best way to grow and find true fulfillment in life."

### UNOPENNESS:
# text = "I don't see the point in all this change and exploration. Life's already complicated enough as it is. I prefer sticking to what I know and trust, and I've never been a fan of stepping out of my comfort zone. New things are often just more trouble than they're worth, and I'd rather avoid unnecessary complications. Why mess with the familiar when you can maintain a stable, predictable routine? That's what works for me."

### SATYA NADELLA:
# text = "I always enjoy learning about the innovative ways our employees are already applying this next generation of AI across their work and life, in ways big and small. Here's my annual letter to shareholders, a look at how we're reimagining every layer of our tech stack in this new age of AI—and our growing opportunity ahead. Today is a great day for gamers everywhere. Together with Activision Blizzard, we will deliver on our vision to help people connect and play great games wherever, whenever, and however they want. Heartbroken by the horrific terrorist attacks on Israel and the escalating conflict. My deepest condolences are with all those killed and impacted. Our focus remains on ensuring the safety of our employees and their families. Below is a message we shared with Microsoft employees today about our response."

### #war:
text = "Putin is killing his soldiers and littering Ukraine with corpses. Russians, when will you understand that you are dying for a thief in a foreign land? EVIDENCE OF BEHEADED BABY BUT ITS PALESTINIAN Where is the humanity? (Sensitive content) *NSFW BREAKING: Biden vows to go to war against China to defend The Philippines after The Philippines coast guard ship and supply boat were rammed by Chinese vessels at disputed Shoal in the South China Sea.  Be ready boys the draft is about to kick in."

### test hashtags:
# text = "#war #kill #bill 'ramesh'"
ans = (lexicon.analyze(text))
words = (text.lower().replace(",", "").replace("!", "").replace("?", "")
         .replace("*", "").replace("@", "").replace("&", "")
         .replace("$", "").replace("%", "").replace(".", "").replace("\'", "")
         .replace("\"", "").replace("\\", "").replace(":", "").replace("/", "")
         .replace("<", "").replace(">", "").replace(";", "").split(" "))
print(words)
hashtags = ""
for word in words:
    if word[0] == '#':
        hashtags += word[1:]
        hashtags += " "
# ans['self'] = words.count("i") + words.count("me") + words.count("my")
ans['swearing_terms'] += words.count("fucking")
useful_words = 0
score = [0.0, 0.0, 0.0, 0.0, 0.0]
check = dict(sleep=[-.01, -.03, -.02, .03, -.08], anger=[-.03, -.08, -.16, -.14, .06],
             achievement=[.03, .01, -.01, .02, -.07], affection=[.03, -.07, -.04, -.06, .04],
             fear=[-.01, -.14, .03, .05, -.04], body=[-.05, -.04, -.04, -.04, .02], death=[-.02, -.04, -.02, -.06, .05],
             family=[.05, -.05, .09, .04, -.07], friends=[.06, -.04, .02, .01, -.12],
             wedding=[-.02, -.02, .01, .01, -.05], hearing=[-.03, .00, -.01, -.04, .04],
             home=[-.01, -.02, .04, .06, -.15], blue_collar_job=[.02, .01, .01, .05, -.05],
             white_collar_job=[.02, .01, .01, .05, -.05], leisure=[-.03, .07, .03, -.01, -.05],
             musical=[-.04, .06, -.01, -.07, .10], negative_emotion=[-.03, -.18, -.11, -.11, .04],
             occupation=[.03, .05, .04, .09, -.18], optimism=[.03, .04, .01, .08, -.07],
             positive_emotion=[.07, .07, .05, .02, .02], divine=[.00, .03, .00, -.06, .07],
             worship=[.00, .03, .00, -.06, .07], religion=[.00, .03, .00, -.06, .07], sad=[.00, -.12, .00, .01, -.01],
             school=[.03, .05, .06, .10, -.20], sexual=[.07, -.02, .00, -.04, .09],
             social_media=[.08, .00, .02, -.02, .02], sports=[.01, .09, .02, .00, -.05],
             swearing_terms=[-.01, .00, -.14, -.11, .08], superhero=[-.04, .04, -.02, -.04, .04],
             party=[-.02,-.05,-.03,-.03,.01], self=[.07,-.14,.06,.04,-.14], ridicule=[-.03, -.18, -.11, -.11, .04],
             )

text = text.split(" ")
total_words = len(text)
for item in ans:
    # print(item)
    if ans[item] > 0:
        useful_words = useful_words + ans[item]
        print(item, ans[item])
        if item in check.keys():
            for i in range(0, 5):
                score[i] = score[i] + ans[item]*check[item][i]

ans = lexicon.analyze(hashtags)
for item in ans:
    # print(item)
    if ans[item] > 0:
        useful_words = useful_words + ans[item]
        print(item, ans[item])
        if item in check.keys():
            for i in range(0, 5):
                score[i] = score[i] + 2*ans[item]*check[item][i]

for i in range(0, 5):
    score[i] = -score[i]
    if useful_words > 0:
        score[i]/useful_words
    score[i] *= 80

score[1] = -score[1]
score[2] = -score[2]
score[3] = -score[3]
print(total_words, useful_words)
print(score)


### dictionary and Big5 correlation:
# Sleep,-.01,-.03,-.02,.03,-.08**
# Anger,-.03,-.08**,-.16**,-.14**,.06**
# Achievement,.03,.01,-.01,.02,-.07**
# Affection,.03,-.07**,-.04,-.06**,.04*
# fear,-.01,-.14**,.03,.05*,-.04
# Body,-.05**,-.04,-.04*,-.04*,.02
# Death,-.02,-.04,-.02,-.06**,.05*
# Exclam,.00,-.05*,.06**,.00,-.03            (ADD THIS: EXCLAMATION MARK)
# Family,.05*,-.05*,.09**,.04*,-.07**
# Friends,.06**,-.04*,.02,.01,-.12**
# Wedding,-.02,-.02,.01,.01,-.05**
# Hearing,-.03,.00,-.01,-.04*,.04*
# Home,-.01,-.02,.04*,.06**,-.15**
# blue_collar_job,.02,.01,.01,.05**,-.05**
# white_collar_job,.02,.01,.01,.05**,-.05**
# Leisure,-.03,.07**,.03,-.01,-.05**
# Musical,-.04*,.06**,-.01,-.07**,.10**
# Negative_emotion,-.03,-.18**,-.11**,-.11**,.04
# Number,-.03,.05*,-.03,-.02,-.06**         (ADD THIS: NUMBERS)
# Occupation,.03,.05*,.04,.09**,-.18**
# Optimism,.03,.04,.01,.08**,-.07**
# Positive_emotion,.07**,.07**,.05*,.02,.02
# Qmark-.06**-.05*-.04-.06**.08**           (ADD THIS: QUESTIONMARK)
# Pronoun,.07**,-.12**,.04*,.02-,.06**      (ADD THIS: PRONOUNS (ALSO CATAGORISE INTO FIRST, SECOND, THIRD PERSON))
# divine,.00,.03,.00,-.06**,.07**
# worship,.00,.03,.00,-.06**,.07**
# religion,.00,.03,.00,-.06**,.07**
# Sad,.00,-.12**,.00,.01,-.01
# School,.03,.05**,.06**,.10**,-.20**
# Self,.07**,-.14**,.06**,.04*,-.14**       (ADD THIS: I, ME, MY, ETC)
# Sexual,.07**,-.02.00,-.04,.09**
# Social_media,.08**,.00,.02,-.02,.02
# Sports,.01,.09**,.02,.00,-.05**
# Swearing_terms,-.01,.00,-.14**,-.11**,.08**
# Tentat,-.06**,-.01,-.03,-.06**,.05*       (ADD THIS: MAYBE, MIGHT, ETC)
# Time,-.02,.02,.07**,.09**,-.15**          (ADD THIS: TODAY, TOMORROW, YESTERDAY, ETC)
# superhero,-.04,.04*,-.02,-.04,*.04


# WC.03-.06**.01.02.05*         --- average length of tweet
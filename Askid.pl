:- dynamic curr/1.
:- dynamic yes/1.
:- dynamic no/1.
:- dynamic asked/1.

ask(X, Y):-
    yes(X), follow_up(X, Y).

ask(X, Y):-
    no(X), random_question(Y).

follow_up(X, Y):- curr(eat), eat(L), member(X, L), member(Y, L), \+asked(Y).
follow_up(X, Y):- curr(play), play(L), member(X, L), member(Y, L), \+asked(Y).
follow_up(X, Y):- curr(learn), learn(L), member(X, L), member(Y, L), \+asked(Y).
follow_up(X, Y):- curr(rest), rest(L), member(X, L), member(Y, L), \+asked(Y).
follow_up(X, Y):- curr(sports), sports(L), member(X, L), member(Y, L), \+asked(Y).

random_question(X):- curr(eat), eat(L), random_member(X, L), \+asked(X).
random_question(X):- curr(play), play(L), random_member(X, L), \+asked(X).
random_question(X):- curr(learn), learn(L), random_member(X, L), \+asked(X).
random_question(X):- curr(rest), rest(L), random_member(X, L), \+asked(X).
random_question(X):- curr(sports), sports(L), random_member(X, L), \+asked(X).

activity([eat, play, learn, rest]).
eat(['Does your food taste good? I really hope you have a good meal at school.', 
    'Is it your food tasty? I really hope you have a good meal at school.', 
    'Is your food sweet? Please do not eat too much sweet food, they are bad for yout teeth:(', 
    'Is your food salty? You should not eat very salty food, they are bad for you.', 
    'Is your food too spicy? You should not eat too much spicy food!', 
    'Did you wash your hands before eating your food? Hygiene is very important! I do not want you to get sick.', 
    'Did you share your food with your friends? It is always good to share with your firends. Remember that sharing is caring', 
    'Is the food portion enough for you? You are growing right now, so you should need more:)']).
play(['Did you have fun at school today? I wish you spent a wonderful day at school', 
    'Did you play with your friends? I hope you are getting along well with your friends at school.', 
    'Did you enjoy yourself at shcool today? I really wish everything goes well.',
    'Did you play your favourite chess game at school today?',
    'Did you meet any new friends today at school?']).
learn(['Did you find that you have learned a lot of new things today?',
    'Did you find anything thing you still do not understand? You can always ask me!',
    'Did you find what you have learned in school useful?', 
    'Did you gain any new knowledge today? I hope you can learn something new every day!', 
    'Is learning new things fun for you?',
    'Do you like to learn new things or new skills everyday?']).
rest(['Did you have a good rest at school today? Having a good rest is key to a healthy lifestyle.',
    'Did you take a nap at school today? I hope you make full use of your recess.',
    'Do you feel tired going to school? It is alright, people feel tired sometimes! It is normal!']).
sports(['Did you do any sports today at school? You really need to get more exercises!',
    'Did you play your favourite basketball game at school today? I think it is a really good sports and it helps you to grow taller.', 
    'Do you like to swim at your schools swimming pool? It is a really amazing place!']).
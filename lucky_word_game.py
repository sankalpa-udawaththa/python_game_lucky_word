import random


guess_count = 0
guess_limit = 3


words = ["ability", "able", "about", "above", "accept", "according", "abbreviate", "abattoir", "abolition","ambassador",
         "ancillary", "account","across","action","activity","actually","address","administration","angstrom","angular",
         "admit", "adult", "affect", "after", "again","against","agency","agent","agreement","anguished","astronautics",
         "ahead", "allow", "almost", "alone", "already", "although", "astound","asthenia","astrocyte","atherosclerosis",
         "American", "analysis", "animal", "another", "autotoxin", "answer", "anyone", "beautiful", "because", "become",
         "before", "begin", "behavior", "behind", "believe", "benefit", "beyond", "blood", "bachelor", "babytalk",
         "backwardation", "backstory", "baltic", "balneology", "bamboozle", "banausic","beefcake","beryllium","beseech",
         "bewilderment", "bezoar", "bivouac", "bivalve","bleeder","blighter","blunder","blowhard","bluetit","bodacious",
         "camera", "campaign", "cancer", "candidate", "capital", "career", "century", "certain","challenge","character",
         "charter", "chauvinist", "cheekbone", "chequer", "chernozem","childless","chimpanzee","chiromancy","chiseller",
         "condition","conference","Congress","consider","consumer","continue","daughter","chlorophyll",
         "cholecystectomy",
         "chore","christen","chronicle","churchman","cinder","chutzpah","cleavage","clergyman","climatology", "clinker",
         "debate","decade","decide","decision","dampen","dapper","darkness", "dartboard", "dauntless", "daylong", "day",
         "deep","defense","degree","Democrat","democratic", "development", "dazzle", "deaf", "dealership", "debauchery",
         "decade","decametre","decapod","decency","decipher", "declared", "decisive", "declaw", "decompress", "decorum",
         "decontrol", "decretal", "dedicated", "deepen", "defamiliarize", "default", "disorder", "disinvestment",
         "eaglet", "ecumenical", "emulate", "encomiast", "encore","encrypt","endowment","enforcer","engaging","engrain",
         "farthing", "fascia", "fealty", "federation", "fimbria", "fingerprint", "fireball",
         "firebug", "fistic", "fixate",
         "gasholder", "gastroscope", "gatekeeper", "ghost", "gesture", "glabella", "glaucoma", "globule", "godfather",
         "hagiology", "hairpiece", "halberd", "halitosis", "hallucination", "hamitic", "handbrake", "handpump",
         "harmonize",
         "implore", "impose", "inanimate", "inadequacy", "incandesce", "incognito", "incommode", "indraught",
         "inelegant",
         "kitchenware", "knockabout", "knucklehead", "krypton",
         "laboratory", "laden", "lambaste", "lampblack", "landscape", "laparoscope", "lassitude", "launch", "lavage",
         "madness", "magenta", "magician", "mailer", "mainstream", "majesty", "majority", "malefactor", "malware",
         "narrowly", "nation", "navigable", "naughty", "nonchalant", "nyctalopia", "nutrition", "numeral", "nuclear",
         "obstacle", "occupled", "oceanology", "octopus", "offensive", "oilskin", "palladium", "palmyra", "purpose",
         "ramble", "range", "readopt", "regard", "regency", "rhythmic", "saltation", "scotch", "seecorn", "semester",
         "showdown", "showery", "shredder", "tergiversate", "terrain", "terrifically", "thankful", "theatre",
         "thematic", "underline", "unicity", "uniflow", "upturn", "usucaption", "utopia", "uxorial", "utilize",
         "vanguard", "vascular", "vaulting", "vehement", "velocity", "veneration", "ventifact", "verification",
         "watch", "waterbed", "watercress", "waveform", "weakness", "wearing", "weathercock", "website", "weight",
         "xanthoma", "xeriscape", "xylophone", "yatter", "yearbook", "youngish", "youthful", "yorker", "yonder",
         "zeitgeist", "zombie", "zoomorphic", "zymurgy"]


random_words = ["fgjvAtribtue", "fweyrweyrwi", "e8293cq20q", "rv48Re64w%^@ad*$^@", "upgjdfggena", "!@^jksdhksewa0eiy",
                "ewvyvtvhwrb5tbjyb"]
rand_word = ["vsvhvwvewbjdclfg", "78wt7ewyufwv7453tv75tvgreb53v", "vw8tvyw3434"]


se_word = str(random.choice(words))
ra_wo_front = str(random.choice(random_words))
ra_wo_back = str(random.choice(rand_word))
print('''
w            w  EEEEEE  0        0000000     000    00    00  EEEEEE 
 w    w     w   E       0        0         0     0  0 0  0 0  E
  w   w   w     EEE     0        0         0     0  0  00  0  EEE
   www www      E       0        0         0     0  0      0  E
    W   W       EEEEEE  0000000  0OOOOOO     000    0      0  EEEEEE
''')
name = input("Enter your Name:  ")
print(f"Hello {name.upper()}, Your game has started")
print('''
We will give to you unknown English word with random letters .
now you can see letters like a secret code. so your word is in that code .
You have 3 Attempts to win this game
good luck 
find your lucky word.
''')
print("'"+ se_word[3] + "'"'  ➡➡➡➡➡ This is a Middle letter of your lucky word')
print("Your word-->  " + ra_wo_front + se_word+ra_wo_back)

while guess_count<guess_limit:
  guess_count += 1
  guess = str(input(">>word:  "))


  if str(guess) == se_word:

      print(f"congratulations {name.upper()} you won the GAME")
      print('''
                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
  ---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.   ''')
      break

  else:
      print(f"sorry {name.upper()}  Try your Next attempt ")
      print('''
               _..._
             ,'     `.
           ,'         `.
         ,'    _   ,-.  `.
         |    (_)  `-'   |
         |        >      |
         |     ,----.    |
         |    /,-""-.\   |
         `.  |/      "  ,'
           `.         ,'
             `._____,'
''')



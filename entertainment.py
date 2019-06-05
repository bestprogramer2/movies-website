import media
import fresh_tomatoes
open_season=media.Movie("Open Season","Boog, a 900-pound grizzly bear, is content entertaining tourists and living in park ranger Beth's barn. His life takes a drastic turn when he rescues a one-horned mule deer named Elliot from a hunter , and is subsequently tranquilized and returned to the wild. Elliot and Boog recruit the other animals, notably a Scottish squirrel and a beaver foreman, to help turn the tables on the hunters to make the woods safe.",
"https://upload.wikimedia.org/wikipedia/en/9/9e/Open_Season.jpg",'https://www.youtube.com/watch?v=TxuILCOrnSE')

spider_man_far_from_home=media.Movie("Spider-man:Far from home","Following the events of Avengers: Endgame, Spider-Man must step up to take on new threats in a world that has changed forever.",
"https://upload.wikimedia.org/wikipedia/en/8/84/SpiderManFarFromHomeTheatrical.jpg","https://www.youtube.com/watch?v=Nt9L1jCKGnE")

iron_man_2008=media.Movie("Iron man","A billionaire industrialist and genius inventor, Tony Stark , is conducting weapons tests overseas, but terrorists kidnap him to force him to build a devastating weapon. Instead, he builds an armored suit and upends his captors. Returning to America, Stark refines the suit and uses it to combat crime and terrorism.",
"https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG","https://www.youtube.com/watch?v=8hYlB38asDY")

up=media.Movie("up","Carl Fredricksen, a 78-year-old balloon salesman, is about to fulfill a lifelong dream. Tying thousands of balloons to his house, he flies away to the South American wilderness. But curmudgeonly Carl's worst nightmare comes true when he discovers a little boy named Russell is a stowaway aboard the balloon-powered house. A Pixar animation.",
"https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg","https://www.youtube.com/watch?v=ORFWdXl_zJ4")
movies=[open_season, spider_man_far_from_home,iron_man_2008,up]
fresh_tomatoes.open_movies_page(movies)


from datetime import date
posts_blog = [
    {
        'slug' : 'practic-coding-daily',
        'image' : 'coding.jpg',
        'author' : 'Hammad Khan',
        'date' : date(2024, 9, 1),
        'title' : 'how to become a pro in programming',
        'excerpt' : 'The Power of Daily Coding: Why Consistency Matters for Developers',
        'content' : """ In the fast-paced world of technology, the most successful developers aren't necessarily the ones who know the most programming languages or have the flashiest resumes. Instead, they're often the ones who code every single day, practicing their craft consistently and building their skills brick by brick. Daily coding isn't just a routine—it's a mindset. Whether you’re a beginner or an experienced coder, developing a habit of coding daily can be transformative.
        Here’s why daily coding is such a game-changer and how you can make it work for you."""
    },
    {
        'slug' : 'practic-not-coding-daily',
        'image' : 'landscap2.jpg',
        'author' : 'Hammad Khan',
        'date' : date(2024, 12, 19),
        'title' : 'how to become a loser in programming',
        'excerpt' : 'The Case for Not Coding Daily: Why Balance is Key for Developers',
        'content' : """ One of the biggest dangers of coding daily is the risk of burnout. Coding is a mentally intensive activity that requires focus, problem-solving, and creativity. When you push yourself to code every single day without adequate rest, you run the risk of burning out, losing your passion for programming, and feeling exhausted.
        Example: Imagine working on a complex project late into the night, only to wake up the next day and force yourself to code again. The result? Mental fatigue, frustration, and diminished productivity.
        Taking time off from coding, even for just a day or two, gives your brain a chance to recharge. Breaks allow you to return to coding with fresh energy and renewed creativity."""
    },{
        'slug' : 'practic-coding-daily',
        'image' : 'coding.jpg',
        'author' : 'Hammad Khan',
        'date' : date(2022, 3, 8),
        'title' : 'how to become a pro in programming',
        'excerpt' : 'The Power of Daily Coding: Why Consistency Matters for Developers',
        'content' : """ In the fast-paced world of technology, the most successful developers aren't necessarily the ones who know the most programming languages or have the flashiest resumes. Instead, they're often the ones who code every single day, practicing their craft consistently and building their skills brick by brick. Daily coding isn't just a routine—it's a mindset. Whether you’re a beginner or an experienced coder, developing a habit of coding daily can be transformative.
        Here’s why daily coding is such a game-changer and how you can make it work for you."""
    },
    {
        'slug' : 'practic-coding-daily',
        'image' : 'coding.jpg',
        'author' : 'Hammad Khan',
        'date' : date(2021, 3, 1),
        'title' : 'how to become a pro in programming',
        'excerpt' : 'The Power of Daily Coding: Why Consistency Matters for Developers',
        'content' : """ In the fast-paced world of technology, the most successful developers aren't necessarily the ones who know the most programming languages or have the flashiest resumes. Instead, they're often the ones who code every single day, practicing their craft consistently and building their skills brick by brick. Daily coding isn't just a routine—it's a mindset. Whether you’re a beginner or an experienced coder, developing a habit of coding daily can be transformative.
        Here’s why daily coding is such a game-changer and how you can make it work for you."""
    }
]
a = next(post for post in posts_blog if post['slug'] == 'practic-not-coding-daily' )
# print(a)

def post_details(slug):
    identified_post = next(post for post in posts_blog if post['slug'] == slug )
    print(identified_post)
# post_details('practice-not-coding-daily')

# lst =(for item in range(10))
# print(next(lst))
age = 36
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
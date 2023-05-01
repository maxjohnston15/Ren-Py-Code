# Declare characters used by this game.
define s = Character(_("Professor Sylvie"), color="#c8fcc8")
define m = Character(_("Max"), color="#c8c8cf")

image HallwayBG = "HallwayBG.jpg"
image LibraryBG = "LibraryBG.jpg"
image Splashscreen = "Splashscreen.jpg"
image OfficeBG = "OfficeBG.jpg"

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

label splashscreen:
    show Splashscreen with dissolve:
        xzoom 2.25 yzoom 2.25
    $ renpy.pause()
    return
# The game starts here.
label start:
    scene HallwayBG:
        xzoom 0.5 yzoom 0.5
    
    show sylvie blue normal

    "I see my professor coming from down the hallway. I am worried that they'll say something to me"
    
    show sylvie blue smile

    "Professor Sylvie is a great Python Professor, but now I am working on the final project and it's quite different from what I used to work on"

    s "Hi Max! How is your final project coming along?"

    "Shoot! I was hoping she wouldn't ask me about my project as I have been really struggling on it and haven't made much progress"
    show sylvie blue normal
    menu:
        "In the heat of the moment, I decide"

        "To lie.":
            jump lie
        
        "To tell the truth.":
            jump truth

label lie:
    m "It's coming along really well!"
    show sylvie blue smile
    m "I am almost finished!"
    s "Great I am looking forward to seeing it!"
    hide sylvie blue smile
    "It is really time to make some progress, she thinks I am doing well so I need a great project to submit."
    "I think I should go to the library and work on it until I am done."
    jump library

label library:
    scene LibraryBG:
        xzoom 2 yzoom 1.3
    "If I am going to work hard on this, I should probably listen to my study music..."
    menu:
        "Should I work in silence or listen to music?"
        "Silence":
            jump silence
        "Music":
            jump music
    label music:
    "If I'm going to focus, it'll have to be to our beloved National Anthem"
    play music "audio/SSB.mp3"
    "Ah, that's perfect! Time to finish this project and get an A+!"
    stop music fadeout 3.0

    jump turnItInNoHelp

    label silence:
    "Ah, nice and quiet. Time to finish this project and get an A+!"
    jump turnItInNoHelp


label truth:
    m "Honestly, I am really struggling to make some progress."
    show sylvie blue surprised
    m "I still haven't figured out how to ask the user to make a choice on Ren'Py, and I am confused about how to upload music, images, and backgrounds."
    show sylvie blue normal
    s "Uh Oh! I am glad you were honest, swing by my office hours and we can figure it out!"
    m "Will do, thanks!"
    jump officehours

label officehours:
    scene OfficeBG:
        xzoom 2.5 yzoom 2.5
    show sylvie blue normal
    m "Hi Professor, this office is fantastic!"
    show sylvie blue smile
    s "Thank you, let's get to work, how can I help you?"
    "I showed Professor Sylvie my issues, and she was able to help"
    "We spent about an hour working through some Ren'Py issues, and I was all set to finish on my own."
    "I knew I would have it done by tomorrow, so I could turn it in when I see her at school."
    jump turnItInWithHelp



label turnItInNoHelp:
    scene HallwayBG:
        xzoom 0.5 yzoom 0.5
    show sylvie blue normal
    m "Hi Professor! Finished my project up in the library, here is my finished product!"
    show sylvie blue smile
    s "Thank you Max!"
    
    "The end."
    return

label turnItInWithHelp:
    scene HallwayBG:
        xzoom 0.5 yzoom 0.5
    show sylvie blue normal
    m "Hi Professor! Thank you so much for you help! Here is my finished product!"
    show sylvie blue smile
    s "No problem, thank you Max!"
    
    "The end."
    return
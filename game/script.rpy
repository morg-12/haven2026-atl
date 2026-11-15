# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define fad = Fade(0.5,0.0,0.5,color = "#ffffff")
define false = False
define true = True 
define none = None 
define a = Character("Aveline")
define c = Character("Commissioner")
define dis = dissolve
image Aveline = "/images/Aveline.png"
image bg_house = "/images/House.jpg"
image bg_park = "/images/Park.jpg"
image bg_clouds = "/images/Clouds.jpg"
image badEnd = "/images/BadEnd.jpg"
image goodEnd = "/images/AvelineGoodEnd.jpg"
image end = "/images/AvelineEnd.jpg"
image void = "/images/staying_up_late.png"
transform genpos:
    xalign 0.5
    yalign 0.125
transform lefpos:
    xalign 0
    yalign 0.125
transform ripos:
    xalign 1.0
    yalign 0.125
define nar = nvl_narrator
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_house
    with dis

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Aveline at genpos
    with dis
    "{i}Another day, another commission.{/i}"
    "{i}I don't know how I've kept up so far. None of my commissions so far have looked right.{/i}"
    "{i}They haven't looked right for a few months, either. The customers keep eating it up, though.{/i}"
    "{i}... Is this seriously how my life is going to be for the forseeable future?{/i}"
    play sound "notif.wav"
    pause 0.5
    "{i}Oh, a message from the commissioner. What is it?{/i}"
    c "Are you going to finish my commission? It's been weeks."
    "{i}I forgot someone's request?!{/i}"
    a "Oh my! I'm so sorry for the long delay."
    c "Did you forget about my commission?"
    "{i}In reality, I completely forgot about it.{/i}"
    "{i}I can't just say that, though.{/i}"
    a "No, no. I have been overloaded with work recently."
    c "... I expect a refund, you know?! And you have to finish the damn thing, too."
    a "I can provide a refund, but I won't be able to give a project after that."
    c "Give me the refund, then."
    a "It'll be processed in the coming days. Again, I'm sorry for the inconvenience."
    c "Ugh."
    "{i}... That's bad. I left a customer completely hanging.{/i}"
    "{i}I hope they don't leave a bad revie-"
    play sound "notif.wav"
    pause 0.5
    "{i}Eh?{/i}"
    "{i}It's a new notification...{/i}"
    "{i}... Wait, they...{/i}"
    c "This account scams people. They take money, then never send a project. Reported."
    "{i}They reported my account?{/i}"
    "{i}... I don't think anything will come of it, but...{/i}"
    "{i}Ugh.{/i}"
    jump park
label park:
    scene bg_park
    with fade
    show Aveline at genpos
    with dis
    "{i}Sitting in a park with absolutely nobody to talk to. Fun.{/i}"
    "{i}This day could not get worse. Well, it probably cou-{/i}"
    play sound notif
    pause 0.5
    "{i}My email? What in the world is-{/i}"
    "\"Your account, AvelineHaven, has been permanently suspended from PerilConglomerate. Reason: Fraud. This decision is final, and no appeals will be accepted.\""
    "{i}... What.{/i}"
    a "My account was suspended? And it’s unappealable? Is this a phishing scam?"
    "{i}I attempt to log into my XXXXXXXX account, only to see the worst thing ever.{/i}"
    "Banned permanently… Banned?"
    jump house2
label house2:
    scene bg_house
    with fade
    "{i}That day in the park was the last time I was fully aware. After all, I had my only financial lifeline pulled out from under me.{/i}"
    "{i}Stolen, like a console from a house.{/i}"
    "{i}I even refunded the dude. The one who reported me for fraud. But, I suppose that wasn’t enough.{/i}"
    "{i}I’ve just been living off my savings, floating through the void. Looking for something to do until I eventually get evicted.{/i}"
    "{i}… I don’t want to be like this, but I can’t escape it. The crushing void of unemployment, am I right?{/i}"
    "{i}... Not funny, I know.{/i}"
    "{i}... No escape. No lifeline. Just pure despair.{/i}"
    "{i}I don't think I want to-{/i}"
    play sound notif
    pause 0.5
    "{i}My email...?{/i}"
    "\"After further investigation, we have decided to reinstate your account. Your credentials are the same.\""
    "{i}That… that has to be a lie. They banned me permanently with no parole, how am I supposed to believe this?{/i}"
    "{i}It’s a phishing email, like it always is. Looking to get my information.{/i}"
    pause 0.5
    "{i}I can't just ignore it, though.{/i}"
    "{i}Therefore, I should try logging in.{/i}"
    play sound click
    pause 0.5
    "{i}... What?{/i}"
    "{i}It... worked? How?{/i}"
    "{i}I mean, my rating is still a crisp 1.1 stars, though.{/i}"
    jump choice
label choice:
    menu:
        "{i}... So, doesn't that mean-{/i}"
        "I can start over?":
            jump goodend
        "It's still over?":
            jump badend
label goodend:
    scene bg_clouds
    with fade
    a "I chose to dig back up from my six feet hole. Fought my way back up to the top."
    a "And well, it’s quite hard to do that. Very hard, in fact."
    a "I’ve only gotten myself back to about 3.2 stars. Nowhere near my original 4.7 stars, but there is a silver lining."
    a "I’m no longer in the dumps. I’ve gotten myself back on my feet."
    a "And maybe, at some point in the future…"
    scene goodEnd
    with fade
    a "I'll have bounced back."
    scene end
    pause 2
    return
label badend:
    scene badEnd
    with dis 
    nar "{i}In the end, I didn't do anything about it. After all, my rating was abysmally low. There was nothing I could do about it.{/i}"
    nar "{i}And, eventually,{/i}"
    nar "{i}I was swallowed up by my despair. I lost my apartment, my friends, and eventually myself.{/i}"
    scene void
    nar "{i}There's nothing I could do about it.{/i}"
    nar "{i}Nothing I could've done about it.{/i}"
    nar "{i}Absolutely nothing{/i}"
    nar "{i}Nothing{/i}"
    nar "{i}Nothing{/i}"
    pause 0.25
    nar "{i}NOTHING!{/i}"
    scene bg_house
    with fad
    jump choice

titles={

#Source: Danshive.Tumblr.Com (selected where would work as a title)

1856: u'A comic with green hair, but not necessarily ABOUT green hair?', 1707: u'Indeed!', 1708: u'Ze questioning continues!', 1709: u'"They asked WHAT?!"', 1713: u'SUDDEN NEW Q&A ATTACK!', 1715: u'Default Grace! ...Wait, what?', 1721: u'last comic of the Q&A!', 1722: u'AAAA I THOUGHT WE WERE DONE WITH THIS CAMERA ANGLE', 1723: u"What'choo talkin' bout, Sarah?", 1724: u'No really! There is!', 1726: u'BAM! STATISTICS! GET HYPED!', 1727: u'Featuring the new star of El Goonish Shive! (not really)', 1728: u"It's Susan. Do you really need any more incentive to click than that?", 1732: u"That huge one that you're standing on right now.", 1733: u"You don't have infinity time to get to class, guys!", 1734: u'The most brilliant mind of our generation returns', 1869: u'What do your Sarah eyes see?', 1872: u'In which Sarah contemplates the exact nature of the mental condition that results in her talking to various versions of herself.', 1874: u'CARD GAAAAAAAAMES OMG...!!!', 1879: u'AAAAA Nearly forgot to post this or more accurately I did forget and then later remembered AAAAAA', 1884: u'It is a message from the North! "Bring back <em>Wagon Train?</em>" What?', 1888: u'To card game or not to card game, that is the question.', 1891: u"<em>Donnnnnnn't say if I were you, or tell me what you'd do, how things would be if you were in my shoes, 'cause you're not me</em>", 1894: u'NERRRRRRRD...!', 1895: u'"Hi Tedd! Did your opponent think you\'re a girl again?"',

}
megatitles={

#Source: Titles on the strips themselves

1818:"Identity - The end",1819:"Summer Moments #1 - Bad Influence",1820:"Summer Moments #2 - Guess Which Of Us Is Who",1821:"Summer Moments #3 - At The Movies",1822:"Previous Summer Moments #4 - A Perfect Plan",1823:"Previous Summer Moments #5 - Hazards Of Clone Form Pranking"

}

sbmegatitles={

#Source: Titles on the strips themselves

713:"Not-Tengu size guide (minus wings)",756:"Eye Science! (with eyes)"

}

modes={
"story":[
    (1824,"Pandora's Box: Squirrel Prophet - Part 1"),
    (1837,"Pandora's Box: Squirrel Prophet - Part 2"),
    (1964,"Pandora's Box: Squirrel Prophet - The Final Battle [part 3]"),
    (2023,"Pandora's Box: So a date at the mall - Part 1"),
    (2067,"Pandora's Box: So a date at the mall - Part 2"),
    (2078,"Pandora's Box: So a date at the mall - Part 3"),
],"sketch":[
    (708,"Post Ookii"), #will be redone by megadb_indextransforms anyway
],"np":[
    (180,"Back"),
    (181,"Playing with Dolls"),
    (254,"Assorted 2015 01"),
    (259,"Zombie Plans"),
    (268,"Question Mark - Part 1"),
    (283,"Question Mark - Part 2"),
    (287,"Question Mark - Part 3"),
    (305,"Assorted 2015 02"),
    (310,"Gaming Webcomic"),
    (325,"Assorted 2015 03"),
    (358,"MV5"),
]}

def handle_titles_ookii_sketch_addendum(strip):
    #Titles from Dan's DeviantArt
    if strip["Id"]==444:
        strip["Titles"]["DeviantArt"]="Grace at the Booth"
    if strip["Id"]==522:
        strip["Titles"]["DeviantArt"]="El Goonish Easter"
    if strip["Id"]==528:
        strip["Titles"]["DeviantArt"]="APRONS"
    if strip["Id"]==586:
        strip["Titles"]["DeviantArt"]="Deleted Scene"
    if strip["Id"]==601:
        strip["Titles"]["DeviantArt"]="El Goonish Holiday 2010"
    if strip["Id"]==77:
        strip["Titles"]["DeviantArt"]="El Goonish X-Mas 2011"

haylo_errorlinks=["[S.T.O.R.Y. March 8, 2004] Crap!-y writing"]


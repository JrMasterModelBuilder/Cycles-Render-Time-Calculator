#!/usr/local/bin/python3

# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


# Cycles Render Time Calculator V1.1 Stable
# Copyright 2013 le717
# http://triangle717.wordpress.com
# and rioforce
# http://rioforce.wordpress.com

import sys, time, webbrowser

app = "Cycles Render Time Calculator"
majver = "Version 1.1"
minver = "Stable"
creator = "le717 and rioforce"

def preload():
    '''Python 3.2 version check'''
    # You need to have at least Python 3.2 to run this program.
    if sys.version_info < (3,2):
        print("You need to download Python 3.2 or greater to run {0} {1}.".format(app, majver))
         # Don't open browser immediately
        time.sleep(2)
        webbrowser.open("http://python.org/download", new=2, autoraise=True) # Open in new tab, raise browser window (if possible)
        # It automatically closes after this
        time.sleep(5) 
    # If you are running Python 3.2     
    else:
        main()

def main():
    '''Menu Layout'''
    print() # Blank space helps keep it all nice and neat
    print("{0}\nCopyright 2013 {1}".format(app, creator))
    print('''\nPlease make a selection:\n
[a] Animation Render
[t] Render Using Tiles
[p] Render Using Progressive Refine
[q] Quit''')
    menuopt = input("\n> ")
    while True:
        if menuopt.lower() == "t":
            tilerender()
        elif menuopt.lower() == "a":
            videorender()
        elif menuopt.lower() == "p":
            layerrender()
        elif menuopt.lower() == "q":
            print("\nGoodbye!")
            time.sleep(2)
            raise SystemExit
        else:
            main()

def videorender():
    '''Generic Animation Render Time'''
    try:
        videoframes = int(input("\nHow many frames are in your animation? "))
        videoframetime = float(input("How long does a single frame take to render (in seconds)? "))
        # Calculate the seconds, minutes, and hours
        videoseconds = (videoframes * videoframetime)
        videominutes = (videoseconds / 60)
        videohours = (videoseconds / 3600)
        # It will take over an hour to render
        if videoseconds >= 3600.0:
            time.sleep(0.2)
            print("\nIt will take approximately {0} hours to render your animation.\n".format(round(videohours, 2)))
            time.sleep(1)
            main()
        # It will take over a minute but less than an hour to render
        elif videoseconds >= 60.0 and videoseconds < 3599.9:
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your animation.\n".format(round(videominutes, 2)))
            time.sleep(1)
            main()
        #It will take only seconds to render  
        else:
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your animation.\n".format(round(videoseconds, 2)))
            time.sleep(1)
            main()
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        videorender()

def tilerender():
    '''Calculates Image Render Time (Using Tiles)'''
    try:
        numtiles = int(input("\nHow many tiles are in your render? "))
        tilerendertime = float(input("How long does a single tile take to render (in seconds)? "))
        # Mathamatical functions
        global tileseconds
        tileseconds = (numtiles * tilerendertime)
        tileminutes = (tileseconds / 60)
        tilehours = (tileseconds / 3600)
        # It will take over an hour
        if tileseconds >= 3600.0:
            time.sleep(0.2)
            print("\nIt will take approximately {0} hours to render your image.\n".format(round(tilehours, 2)))
        # It will take over a minute but less than an hour
        elif tileseconds >= 60.0 and tileseconds < 3599.9:
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your image.\n".format(round(tileminutes, 2)))
        #It will take only seconds    
        else:
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your image.\n".format(round(tileseconds, 2)))
    # Catch any non-numerical input        
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        tilerender()
    print("Are you rendering an animation? " + r"(y\N)") # AKA video or "multi-frame" animation
    tilevideo = input("\n> ")
    if tilevideo.lower() != "y": # No, I am not
        time.sleep(1)
        main()
    else: 
        tilevideorender(tileseconds) # Yes, I am
            

def tilevideorender(tileseconds):
    '''Calculates Animation Render Time (Using Tiles)'''
    try:
        time.sleep(0.2) # Sleep for a tiny bit so the text doesn't "jump" at you (and same everywhere else)
        tileframenumber = int(input("\nHow many frames are in your animation? "))
        # More mathamatical functions
        tilevideoseconds = (tileseconds * tileframenumber)
        tilevideominutes = (tilevideoseconds / 60)
        tilevideohours = (tilevideoseconds / 3600)
        # It will take over an hour
        if tilevideoseconds >= 3600.0:
            time.sleep(0.2)
            print("\nIt will take approximately {0} hours to render your animation.\n".format(round(tilevideohours, 2)))
        # It will take over a minute but less than an hour 
        elif tilevideoseconds >= 60.0 and tilevideoseconds < 3599.9:
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your animation.\n".format(round(tilevideominutes, 2)))
        else:   
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your animation.\n".format(round(tilevideoseconds, 2)))
        time.sleep(1)
        main()
    # Catch any non-numerical input     
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        tilevideorender(tileseconds)

def layerrender():
    '''Calculates Image Render Time (Using Progessive Refine)'''
    '''Progressive Refine Image and Animation render is just the Tile render code adapted to
support the Progressive Refine method. Therefore, I've omitted the comments.'''
    try:
        layernum = int(input("\nHow many samples are in your render? "))
        layerrendertime = float(input("How long does a single sample take to render (in seconds)? "))
        # Even more Mathamatical functions
        global layerseconds
        layerseconds = (layernum * layerrendertime)
        layerminutes = (layerseconds / 60)
        layerhours = (layerseconds / 3600)
        if layerseconds >= 3600.0:
            time.sleep(0.2)
            print("\nIt will take approximately {0} hours to render your image.\n".format(round(layerhours, 2)))
        elif layerseconds >= 60.0 and layerseconds < 3599.9:
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your image.\n".format(round(layerminutes, 2)))
        else:
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your image.\n".format(round(layerseconds, 2)))
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        layerrender()
    print("Are you rendering an animation? " + r"(y\N)")
    layervideo = input("\n> ")
    if layervideo.lower() != "y":
        time.sleep(1)
        main()
    else: 
        layervideorender(layerseconds)
        
def layervideorender(layerseconds):
    '''Calculates Animation Render Time (Using Progessive Refine)'''
    try:
        time.sleep(0.2)
        layerframenumber = int(input("\nHow many frames are in your animation? "))
        # Math is FUN!
        layervideoseconds = (layerseconds * layerframenumber)
        layervideominutes = (layervideoseconds / 60)
        layervideohours = (layervideoseconds / 3600)
        if layervideoseconds >= 3600.0:
            time.sleep(0.2)
            print("\nIt will take approximately {0} hours to render your animation.\n".format(round(layervideohours, 2)))
        elif layervideoseconds >= 60.0 and layervideoseconds < 3599.9:
            time.sleep(0.2)
            print("\nIt will take approximately {0} minutes to render your animation.\n".format(round(layervideominutes, 2)))
        else:
            time.sleep(0.2)
            print("\nIt will take approximately {0} seconds to render your animation.\n".format(round(layervideoseconds, 2)))
        time.sleep(1)
        main()
    except ValueError:
        print("That is an invalid input. Please try again.\n")
        layervideorender(layerseconds)            
        
        
if __name__ == "__main__":
    preload()
# Display complete app info if imported as a module    
else:
    print()
    print("{0} {1} {2}\nCopyright 2013 {3}".format(app, majver, minver, creator))
    

# runarcn dotfiles
Dotfiles is how you customize and personalize my systems. These are mine. 

This repository functions as a backup for me incase I ever brick my system (oopsies), to share with everyone should anyone else want to use, study or modify them and should I need to link to them on a forum or similar.

You may use the dotfiles as you want as long as they follow the terms and conditions of the GPL-3 license. Read the [LICENSE](https://github.com/runarcn/dotfiles/blob/main/LICENSE)-file for more information about this.

Should you ever have any questions about this repository, contact me on Mastodon! [@runarcn@mstdn.social](https://mstdn.social/@runarcn).

***DISCLAIMER***
I don't know how to use git at all. If stuff here looks weird, that's probably why. 

## i3
To install my dotfiles, clone them either through `git` with `git clone https://github.com/runarcn/dotfiles.git` or download them manually before moving them into the folders where they belong. For i3wm, this would be `~/.config/i3/`. I've chosen not to write any shellscripts to install them automatically in case anyone here uses custom locations, and frankly, because I don't see the need to as of right now.

I will add a list of the different software I use with i3wm at some point. For now, I'd recommend reading through the config file. 

## .bashrc
The .bashrc file is exactly the same as the default one with a few custom aliases at the bottom. These are some I use for simplicity's sake, and some for dumb typos I make.

You should make sure you've installed all the packages at the bottom of .bashrc to so that you don't get any weird breakages, such as micro and btop

### bashrc-scripts
A folder where I store the scripts I've written for .bashrc. Install this in your home folder.

## dunstrc
Nothing special here, just moving the notifications to top right corner

## btop
Changed theme to a new default theme

## micro
Plugins and theming

## xorg.conf.d
Natural scrolling for touchpad (not for mouse and trackpoint)


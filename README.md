This simple program uses Python and [PyObjC](http://pyobjc.sourceforge.net/) to
parse OS X [Preview.app](http://en.wikipedia.org/wiki/Preview_%28software%29)'s
bookmarks, stored in
`${HOME}/Library/Preferences/com.apple.Preview.bookmarks.plist`.

How did I figure this out?

1. Install [class-dump](http://www.codethecode.com/projects/class-dump/).

    $ brew install class-dump

2. Run it. The `awk` is just to filter the output to show just the `PVBookmark` class.

    $ class-dump /Applications/Preview.app | awk '/@interface PVBookmark/, /@end/ { print; }'

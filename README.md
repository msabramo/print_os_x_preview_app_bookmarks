This simple program uses Python and [PyObjC](http://pyobjc.sourceforge.net/) to
parse OS X [Preview.app](http://en.wikipedia.org/wiki/Preview_%28software%29)'s
bookmarks, stored in
`${HOME}/Library/Preferences/com.apple.Preview.bookmarks.plist`.

How did I figure this out?

### Install [class-dump](http://www.codethecode.com/projects/class-dump/).
    $ brew install class-dump
### Run it. The `awk` is just to filter the output to show just the `PVBookmark` class.
    $ class-dump /Applications/Preview.app | awk '/@interface PVBookmark/, /@end/ { print; }'
    @interface PVBookmark : NSObject
    {
        NSString *_UUID;
        NSString *_parentUUID;
        PVFileReference *_file;
        NSDate *_fileModDate;
        NSString *_label;
        int _pageIndex;
    }
    
    - (id)initWithFilePath:(id)arg1 label:(id)arg2 pageIndex:(unsigned long long)arg3;
    - (void)dealloc;
    - (id)initWithCoder:(id)arg1;
    - (void)encodeWithCoder:(id)arg1;
    - (id)description;
    - (id)UUID;
    - (id)filePath;
    - (id)fileModificationDate;
    - (id)label;
    - (void)setLabel:(id)arg1;
    - (unsigned long long)pageIndex;
    - (id)targetExists;
    - (BOOL)targetIsOnNetworkVolume;
    - (id)displayPath;
    - (unsigned long long)pageNumber;
    
    @end

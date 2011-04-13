#!/usr/bin/env python

import os
from Cocoa import *

def getPlistFilename():
    return '%s/Library/Preferences/com.apple.Preview.bookmarks.plist' % os.getenv('HOME')


def getData(bytes):
    return NSData.alloc().initWithBytes_length_(bytes, len(bytes))


class PVBookmark(NSObject):
    """
    @interface PVBookmark : NSObject
    {
        NSString         *_UUID;
        NSString         *_parentUUID;
        PVFileReference  *_file;
        NSDate           *_fileModDate;
        NSString         *_label;
        unsigned int      _pageIndex;
    }
    """

    def initWithCoder_(self, coder):
        schema = (
            ('_UUID',          coder.decodeObjectForKey_),
            ('_parentUUID',    coder.decodeObjectForKey_),
            ('_file',          coder.decodeObjectForKey_),
            ('_fileModDate',   coder.decodeObjectForKey_),
            ('_label',         coder.decodeObjectForKey_),
            ('_pageIndex',     coder.decodeIntForKey_),
            )

        for key, func in schema:
            setattr(self, key, func(key))

        return self


class PVFileReference(NSObject):
    """
    @interface PVFileReference : NSObject
    {
        struct AliasRecord   **_fileAlias;
    }

    struct AliasRecord {
        OSType                 userType;
        unsigned short         aliasSize;
    };
    """

    def initWithCoder_(self, coder):
        """
        schema = (
            ('_fileAlias',        coder.decodeObjectForKey_),
            )

        for key, func in schema:
            setattr(self, key, func(key))
        """

        fileAliasData, fileAliasDataLength = coder.decodeBytesForKey_returnedLength_('_fileAlias', None)
        self.filename = fileAliasData[fileAliasData.index('Users/'):]
        self.filename = '/' + self.filename[:self.filename.index('\x00')]
    
        return self


plistFilename     = getPlistFilename()
print('Reading plist: "%s"' % plistFilename)

plist             = NSDictionary.dictionaryWithContentsOfFile_(plistFilename)
bookmarksArray    = plist['bookmarksArray']
data              = getData(bookmarksArray.bytes())
bookmarks         = NSKeyedUnarchiver.unarchiveObjectWithData_(data)

for bookmark in bookmarks:
    print("{")
    print("    'label': %r," % bookmark._label)
    print("    'pageIndex': %r," % bookmark._pageIndex)
    print("    'file': %r," % bookmark._file.__dict__)
    print("},")

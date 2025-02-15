# `stat` — Interpreting `stat()` results

> [!WARNING]
> The text, although it almost duplicates the official documentation, still differs from it. Be
> careful what you use!

The `stat` module defines constants and functions for interpreting the results of [os.stat()][os],
[os.fstat()][os] and [os.lstat()][os] (if they exist). For complete details about the `stat()`,
`fstat()` and `lstat()` calls, consult the documentation for your system.

The `stat` module defines the following functions to test for specific file types:

### \* stat.**S_ISDIR**(*mode*)

Return non-zero if the mode is from a directory.

### \* stat.**S_ISCHR**(*mode*)

Return non-zero if the mode is from a character special device file.

### \* stat.**S_ISBLK**(*mode*)

Return non-zero if the mode is from a block special device file.

### \* stat.**S_ISREG**(*mode*)

Return non-zero if the mode is from a regular file.

### \* stat.**S_ISFIFO**(*mode*)

Return non-zero if the mode is from a FIFO (named pipe).

### \* stat.**S_ISLNK**(*mode*)

Return non-zero if the mode is from a symbolic link.

### \* stat.**S_ISSOCK**(*mode*)

Return non-zero if the mode is from a socket.

### \* stat.**S_ISDOOR**(*mode*)

Return non-zero if the mode is from a door.

### \* stat.**S_ISPORT**(*mode*)

Return non-zero if the mode is from an event port.

### \* stat.**S_ISWHT**(*mode*)

Return non-zero if the mode is from a whiteout.

### \* stat.**S_IMODE**(*mode*)

Return the portion of the file's mode that can be set by [os.chmod()][os] — that is, the file's
permission bits, plus the sticky bit, set-group-id, and set-user-id bits (on systems that support
them).

### \* stat.**S_IFMT**(*mode*)

Return the portion of the file's mode that describes the file type (used by the `S_IS*()` functions
above).

###

Normally, you would use the `os.path.is*()` functions for testing the type of a file; the functions
here are useful when you are doing multiple tests of the same file and wish to avoid the overhead of
the `stat()` system call for each test. These are also useful when checking for information about a
file that isn’t handled by [os.path][os.path], like the tests for block and character devices.

Example:

```python
from backlib.py313.os import curdir, listdir, lstat
from backlib.py313.ospath import join
from backlib.py313.stat import S_ISDIR, S_ISREG


def walktree(root: str) -> None:
    """Walk the file system tree."""
    for filename in listdir(root):
        path = join(root, filename)
        st = lstat(path)

        if S_ISDIR(st.st_mode):
            walktree(path)

        elif S_ISREG(st.st_mode):
            print(path)


def main() -> None:
    """Run the program."""
    walktree(curdir)


if __name__ == "__main__":
    main()
```

An additional utility function is provided to convert a file's mode in a human readable string:

### \* stat.**filemode**(*mode*)

Convert a file's mode to a string of the form `'-rwxrwxrwx'`.

###

All the variables below are simply symbolic indexes into the 10-tuple returned by [os.stat()][os],
[os.fstat()][os] or [os.lstat()][os].

### \* stat.**ST_MODE**

Inode protection mode.

### \* stat.**ST_INO**

Inode number.

### \* stat.**ST_DEV**

Device inode resides on.

### \* stat.**ST_NLINK**

Number of links to the inode.

### \* stat.**ST_UID**

User id of the owner.

### \* stat.**ST_GID**

Group id of the owner.

### \* stat.**ST_SIZE**

Size in bytes of a plain file; amount of data waiting on some special files.

### \* stat.**ST_ATIME**

Time of last access.

### \* stat.**ST_MTIME**

Time of last modification.

### \* stat.**ST_CTIME**

The "ctime" as reported by the operating system. On some systems (like Unix) is the time of the last
metadata change, and, on others (like Windows), is the creation time (see platform documentation for
details).

###

The interpretation of "file size" changes according to the file type. For plain files this is the
size of the file in bytes. For FIFOs and sockets under most flavors of Unix (including Linux in
particular), the "size" is the number of bytes waiting to be read at the time of the call to
[os.stat()][os], [os.fstat()][os], or [os.lstat()][os]; this can sometimes be useful, especially for
polling one of these special files after a non-blocking open. The meaning of the size field for
other character and block devices varies more, depending on the implementation of the underlying
system call.

The variables below define the flags used in the `ST_MODE` field.

Use of the functions above is more portable than use of the first set of flags:

### \* stat.**S_IFSOCK**

Socket.

### \* stat.**S_IFLNK**

Symbolic link.

### \* stat.**S_IFREG**

Regular file.

### \* stat.**S_IFBLK**

Block device.

### \* stat.**S_IFDIR**

Directory.

### \* stat.**S_IFCHR**

Character device.

### \* stat.**S_IFIFO**

FIFO.

### \* stat.**S_IFDOOR**

Door.

### \* stat.**S_IFPORT**

Event port.

### \* stat.**S_IFWHT**

Whiteout.

###

> [!NOTE]
> `S_IFDOOR`, `S_IFPORT` or `S_IFWHT` are defined as `0` when the platform does not have support for
> the file types.

The following flags can also be used in the mode argument of [os.chmod()][os]:

### \* stat.**S_ISUID**

Set UID bit.

### \* stat.**S_ISGID**

Set-group-ID bit. This bit has several special uses. For a directory it indicates that BSD semantics
is to be used for that directory: files created there inherit their group ID from the directory, not
from the effective group ID of the creating process, and directories created there will also get the
`S_ISGID` bit set. For a file that does not have the group execution bit (`S_IXGRP`) set, the
set-group-ID bit indicates mandatory file/record locking (see also `S_ENFMT`).

### \* stat.**S_ISVTX**

Sticky bit. When this bit is set on a directory it means that a file in that directory can be
renamed or deleted only by the owner of the file, by the owner of the directory, or by a privileged
process.

### \* stat.**S_IRWXU**

Mask for file owner permissions.

### \* stat.**S_IRUSR**

Owner has read permission.

### \* stat.**S_IWUSR**

Owner has write permission.

### \* stat.**S_IXUSR**

Owner has execute permission.

### \* stat.**S_IRWXG**

Mask for group permissions.

### \* stat.**S_IRGRP**

Group has read permission.

### \* stat.**S_IWGRP**

Group has write permission.

### \* stat.**S_IXGRP**

Group has execute permission.

### \* stat.**S_IRWXO**

Mask for permissions for others (not in group).

### \* stat.**S_IROTH**

Others have read permission.

### \* stat.**S_IWOTH**

Others have write permission.

### \* stat.**S_IXOTH**

Others have execute permission.

### \* stat.**S_ENFMT**

System V file locking enforcement. This flag is shared with `S_ISGID`: file / record locking is
enforced on files that do not have the group execution bit (`S_IXGRP`) set.

### \* stat.**S_IREAD**

Unix V7 synonym for `S_IRUSR`.

### \* stat.**S_IWRITE**

Unix V7 synonym for `S_IWUSR`.

### \* stat.**S_IEXEC**

Unix V7 synonym for `S_IXUSR`.

The following flags can be used in the flags argument of `os.chflags()`:

### \* stat.**UF_SETTABLE**

All user settable flags.

### \* stat.**UF_NODUMP**

Do not dump the file.

### \* stat.**UF_IMMUTABLE**

The file may not be changed.

### \* stat.**UF_APPEND**

The file may only be appended to.

### \* stat.**UF_OPAQUE**

The directory is opaque when viewed through a union stack.

### \* stat.**UF_NOUNLINK**

The file may not be renamed or deleted.

### \* stat.**UF_COMPRESSED**

The file is stored compressed (macOS 10.6+).

### \* stat.**UF_TRACKED**

Used for handling document IDs (macOS)

### \* stat.**UF_DATAVAULT**

The file needs an entitlement for reading or writing (macOS 10.13+)

### \* stat.**UF_HIDDEN**

The file should not be displayed in a GUI (macOS 10.5+).

### \* stat.**SF_SETTABLE**

All super-user changeable flags

### \* stat.**SF_SUPPORTED**

All super-user supported flags

### \* stat.**SF_SYNTHETIC**

All super-user read-only synthetic flags

### \* stat.**SF_ARCHIVED**

The file may be archived.

### \* stat.**SF_IMMUTABLE**

The file may not be changed.

### \* stat.**SF_APPEND**

The file may only be appended to.

### \* stat.**SF_RESTRICTED**

The file needs an entitlement to write to (macOS 10.13+)

### \* stat.**SF_NOUNLINK**

The file may not be renamed or deleted.

### \* stat.**SF_SNAPSHOT**

The file is a snapshot file.

### \* stat.**SF_FIRMLINK**

The file is a firmlink (macOS 10.15+)

### \* stat.**SF_DATALESS**

The file is a dataless object (macOS 10.15+)

###

The following constants are available for use when testing bits in the `st_file_attributes` member
returned by [os.stat()][os]:

### \* stat.**FILE_ATTRIBUTE_ARCHIVE**

A file or directory that is an archive file or directory. Applications typically use this attribute
to mark files for backup or removal. (Windows).

### \* stat.**FILE_ATTRIBUTE_COMPRESSED**

A file or directory that is compressed. For a file, all of the data in the file is compressed. For a
directory, compression is the default for newly created files and subdirectories. (Windows).

### \* stat.**FILE_ATTRIBUTE_DEVICE**

This value is reserved for system use. (Windows).

### \* stat.**FILE_ATTRIBUTE_DIRECTORY**

The handle that identifies a directory. (Windows).

### \* stat.**FILE_ATTRIBUTE_ENCRYPTED**

A file or directory that is encrypted. For a file, all data streams in the file are encrypted. For a
directory, encryption is the default for newly created files and subdirectories. (Windows).

### \* stat.**FILE_ATTRIBUTE_HIDDEN**

The file or directory is hidden. It is not included in an ordinary directory listing. (Windows).

### \* stat.**FILE_ATTRIBUTE_INTEGRITY_STREAM**

The directory or user data stream is configured with integrity (only supported on ReFS volumes). It
is not included in an ordinary directory listing. The integrity setting persists with the file if
it's renamed. If a file is copied the destination file will have integrity set if either the source
file or destination directory have integrity set. (Windows).

### \* stat.**FILE_ATTRIBUTE_NORMAL**

A file that does not have other attributes set. This attribute is valid only when used alone.
(Windows).

### \* stat.**FILE_ATTRIBUTE_NOT_CONTENT_INDEXED**

The file or directory is not to be indexed by the content indexing service. (Windows).

### \* stat.**FILE_ATTRIBUTE_NO_SCRUB_DATA**

The user data stream not to be read by the background data integrity scanner (AKA scrubber). When
set on a directory it only provides inheritance. This flag is only supported on Storage Spaces and
ReFS volumes. It is not included in an ordinary directory listing. (Windows).

### \* stat.**FILE_ATTRIBUTE_OFFLINE**

The data of a file is not available immediately. This attribute indicates that the file data is
physically moved to offline storage. This attribute is used by Remote Storage, which is the
hierarchical storage management software. Applications should not arbitrarily change this attribute.
(Windows).

### \* stat.**FILE_ATTRIBUTE_READONLY**

A file that is read-only. Applications can read the file, but cannot write to it or delete it. This
attribute is not honored on directories. (Windows).

### \* stat.**FILE_ATTRIBUTE_REPARSE_POINT**

A file or directory that has an associated reparse point, or a file that is a symbolic link.
(Windows).

### \* stat.**FILE_ATTRIBUTE_SPARSE_FILE**

A file that is a sparse file. (Windows).

### \* stat.**FILE_ATTRIBUTE_SYSTEM**

A file or directory that the operating system uses a part of, or uses exclusively. (Windows).

### \* stat.**FILE_ATTRIBUTE_TEMPORARY**

A file that is being used for temporary storage. File systems avoid writing data back to mass
storage if sufficient cache memory is available, because typically, an application deletes a
temporary file after the handle is closed. In that scenario, the system can entirely avoid writing
the data. Otherwise, the data is written after the handle is closed. (Windows).

### \* stat.**FILE_ATTRIBUTE_VIRTUAL**

This value is reserved for system use. (Windows).

###

The following constants are available for comparing against the `st_reparse_tag` member returned by
[os.lstat()][os]:

### \* stat.**IO_REPARSE_TAG_SYMLINK**

Used for symbolic link support. (Windows).

### \* stat.**IO_REPARSE_TAG_MOUNT_POINT**

Used for mount point support. (Windows).

### \* stat.**IO_REPARSE_TAG_APPEXECLINK**

Used by Universal Windows Platform (UWP) packages to encode information that allows the application
to be launched by CreateProcess. Server-side interpretation only, not meaningful over the wire.
(Windows).

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[os]: ./os.md
[os.path]: ./os.path.md

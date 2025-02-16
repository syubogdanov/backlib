"""Error codes for Solaris 10.0+.

See Also
--------
* https://www.ioplex.com/~miallen/errcmp.html
"""

from typing import Final


__all__: list[str] = [
    "E2BIG",
    "EACCES",
    "EADDRINUSE",
    "EADDRNOTAVAIL",
    "EADV",
    "EAFNOSUPPORT",
    "EAGAIN",
    "EALREADY",
    "EBADE",
    "EBADF",
    "EBADFD",
    "EBADMSG",
    "EBADR",
    "EBADRQC",
    "EBADSLT",
    "EBFONT",
    "EBUSY",
    "ECANCELED",
    "ECHILD",
    "ECHRNG",
    "ECOMM",
    "ECONNABORTED",
    "ECONNREFUSED",
    "ECONNRESET",
    "EDEADLK",
    "EDEADLOCK",
    "EDESTADDRREQ",
    "EDOM",
    "EDQUOT",
    "EEXIST",
    "EFAULT",
    "EFBIG",
    "EHOSTDOWN",
    "EHOSTUNREACH",
    "EIDRM",
    "EILSEQ",
    "EINPROGRESS",
    "EINTR",
    "EINVAL",
    "EIO",
    "EISCONN",
    "EISDIR",
    "EL2HLT",
    "EL2NSYNC",
    "EL3HLT",
    "EL3RST",
    "ELIBACC",
    "ELIBBAD",
    "ELIBEXEC",
    "ELIBMAX",
    "ELIBSCN",
    "ELNRNG",
    "ELOCKUNMAPPED",
    "ELOOP",
    "EMFILE",
    "EMLINK",
    "EMSGSIZE",
    "EMULTIHOP",
    "ENAMETOOLONG",
    "ENETDOWN",
    "ENETRESET",
    "ENETUNREACH",
    "ENFILE",
    "ENOANO",
    "ENOBUFS",
    "ENOCSI",
    "ENODATA",
    "ENODEV",
    "ENOENT",
    "ENOEXEC",
    "ENOLCK",
    "ENOLINK",
    "ENOMEM",
    "ENOMSG",
    "ENONET",
    "ENOPKG",
    "ENOPROTOOPT",
    "ENOSPC",
    "ENOSR",
    "ENOSTR",
    "ENOSYS",
    "ENOTACTIVE",
    "ENOTBLK",
    "ENOTCONN",
    "ENOTDIR",
    "ENOTEMPTY",
    "ENOTRECOVERABLE",
    "ENOTSOCK",
    "ENOTSUP",
    "ENOTTY",
    "ENOTUNIQ",
    "ENXIO",
    "EOPNOTSUPP",
    "EOVERFLOW",
    "EOWNERDEAD",
    "EPERM",
    "EPFNOSUPPORT",
    "EPIPE",
    "EPROTO",
    "EPROTONOSUPPORT",
    "EPROTOTYPE",
    "ERANGE",
    "EREMCHG",
    "EREMOTE",
    "ERESTART",
    "EROFS",
    "ESHUTDOWN",
    "ESOCKTNOSUPPORT",
    "ESPIPE",
    "ESRCH",
    "ESRMNT",
    "ESTALE",
    "ESTRPIPE",
    "ETIME",
    "ETIMEDOUT",
    "ETOOMANYREFS",
    "ETXTBSY",
    "EUNATCH",
    "EUSERS",
    "EWOULDBLOCK",
    "EXDEV",
    "EXFULL",
]


E2BIG: Final[int] = 7
EACCES: Final[int] = 13
EADDRINUSE: Final[int] = 125
EADDRNOTAVAIL: Final[int] = 126
EADV: Final[int] = 68
EAFNOSUPPORT: Final[int] = 124
EAGAIN: Final[int] = 11
EALREADY: Final[int] = 149
EBADE: Final[int] = 50
EBADF: Final[int] = 9
EBADFD: Final[int] = 81
EBADMSG: Final[int] = 77
EBADR: Final[int] = 51
EBADRQC: Final[int] = 54
EBADSLT: Final[int] = 55
EBFONT: Final[int] = 57
EBUSY: Final[int] = 16
ECANCELED: Final[int] = 47
ECHILD: Final[int] = 10
ECHRNG: Final[int] = 37
ECOMM: Final[int] = 70
ECONNABORTED: Final[int] = 130
ECONNREFUSED: Final[int] = 146
ECONNRESET: Final[int] = 131
EDEADLK: Final[int] = 45
EDEADLOCK: Final[int] = 56
EDESTADDRREQ: Final[int] = 96
EDOM: Final[int] = 33
EDQUOT: Final[int] = 49
EEXIST: Final[int] = 17
EFAULT: Final[int] = 14
EFBIG: Final[int] = 27
EHOSTDOWN: Final[int] = 147
EHOSTUNREACH: Final[int] = 148
EIDRM: Final[int] = 36
EILSEQ: Final[int] = 88
EINPROGRESS: Final[int] = 150
EINTR: Final[int] = 4
EINVAL: Final[int] = 22
EIO: Final[int] = 5
EISCONN: Final[int] = 133
EISDIR: Final[int] = 21
EL2HLT: Final[int] = 44
EL2NSYNC: Final[int] = 38
EL3HLT: Final[int] = 39
EL3RST: Final[int] = 40
ELIBACC: Final[int] = 83
ELIBBAD: Final[int] = 84
ELIBEXEC: Final[int] = 87
ELIBMAX: Final[int] = 86
ELIBSCN: Final[int] = 85
ELNRNG: Final[int] = 41
ELOCKUNMAPPED: Final[int] = 72
ELOOP: Final[int] = 90
EMFILE: Final[int] = 24
EMLINK: Final[int] = 31
EMSGSIZE: Final[int] = 97
EMULTIHOP: Final[int] = 74
ENAMETOOLONG: Final[int] = 78
ENETDOWN: Final[int] = 127
ENETRESET: Final[int] = 129
ENETUNREACH: Final[int] = 128
ENFILE: Final[int] = 23
ENOANO: Final[int] = 53
ENOBUFS: Final[int] = 132
ENOCSI: Final[int] = 43
ENODATA: Final[int] = 61
ENODEV: Final[int] = 19
ENOENT: Final[int] = 2
ENOEXEC: Final[int] = 8
ENOLCK: Final[int] = 46
ENOLINK: Final[int] = 67
ENOMEM: Final[int] = 12
ENOMSG: Final[int] = 35
ENONET: Final[int] = 64
ENOPKG: Final[int] = 65
ENOPROTOOPT: Final[int] = 99
ENOSPC: Final[int] = 28
ENOSR: Final[int] = 63
ENOSTR: Final[int] = 60
ENOSYS: Final[int] = 89
ENOTACTIVE: Final[int] = 73
ENOTBLK: Final[int] = 15
ENOTCONN: Final[int] = 134
ENOTDIR: Final[int] = 20
ENOTEMPTY: Final[int] = 93
ENOTRECOVERABLE: Final[int] = 59
ENOTSOCK: Final[int] = 95
ENOTSUP: Final[int] = 48
ENOTTY: Final[int] = 25
ENOTUNIQ: Final[int] = 80
ENXIO: Final[int] = 6
EOPNOTSUPP: Final[int] = 122
EOVERFLOW: Final[int] = 79
EOWNERDEAD: Final[int] = 58
EPERM: Final[int] = 1
EPFNOSUPPORT: Final[int] = 123
EPIPE: Final[int] = 32
EPROTO: Final[int] = 71
EPROTONOSUPPORT: Final[int] = 120
EPROTOTYPE: Final[int] = 98
ERANGE: Final[int] = 34
EREMCHG: Final[int] = 82
EREMOTE: Final[int] = 66
ERESTART: Final[int] = 91
EROFS: Final[int] = 30
ESHUTDOWN: Final[int] = 143
ESOCKTNOSUPPORT: Final[int] = 121
ESPIPE: Final[int] = 29
ESRCH: Final[int] = 3
ESRMNT: Final[int] = 69
ESTALE: Final[int] = 151
ESTRPIPE: Final[int] = 92
ETIME: Final[int] = 62
ETIMEDOUT: Final[int] = 145
ETOOMANYREFS: Final[int] = 144
ETXTBSY: Final[int] = 26
EUNATCH: Final[int] = 42
EUSERS: Final[int] = 94
EWOULDBLOCK: Final[int] = 11
EXDEV: Final[int] = 18
EXFULL: Final[int] = 52

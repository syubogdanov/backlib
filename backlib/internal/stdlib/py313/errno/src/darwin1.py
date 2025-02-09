from typing import Final


__all__: list[str] = [
    "E2BIG",
    "EACCES",
    "EADDRINUSE",
    "EADDRNOTAVAIL",
    "EAFNOSUPPORT",
    "EAGAIN",
    "EALREADY",
    "EAUTH",
    "EBADARCH",
    "EBADEXEC",
    "EBADF",
    "EBADMACHO",
    "EBADMSG",
    "EBADRPC",
    "EBUSY",
    "ECANCELED",
    "ECHILD",
    "ECONNABORTED",
    "ECONNREFUSED",
    "ECONNRESET",
    "EDEADLK",
    "EDESTADDRREQ",
    "EDEVERR",
    "EDOM",
    "EDQUOT",
    "EEXIST",
    "EFAULT",
    "EFBIG",
    "EFTYPE",
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
    "ELOOP",
    "EMFILE",
    "EMLINK",
    "EMSGSIZE",
    "EMULTIHOP",
    "ENAMETOOLONG",
    "ENEEDAUTH",
    "ENETDOWN",
    "ENETRESET",
    "ENETUNREACH",
    "ENFILE",
    "ENOATTR",
    "ENOBUFS",
    "ENODATA",
    "ENODEV",
    "ENOENT",
    "ENOEXEC",
    "ENOLCK",
    "ENOLINK",
    "ENOMEM",
    "ENOMSG",
    "ENOPOLICY",
    "ENOPROTOOPT",
    "ENOSPC",
    "ENOSR",
    "ENOSTR",
    "ENOSYS",
    "ENOTBLK",
    "ENOTCONN",
    "ENOTDIR",
    "ENOTEMPTY",
    "ENOTRECOVERABLE",
    "ENOTSOCK",
    "ENOTSUP",
    "ENOTTY",
    "ENXIO",
    "EOPNOTSUPP",
    "EOVERFLOW",
    "EOWNERDEAD",
    "EPERM",
    "EPFNOSUPPORT",
    "EPIPE",
    "EPROCLIM",
    "EPROCUNAVAIL",
    "EPROGMISMATCH",
    "EPROGUNAVAIL",
    "EPROTO",
    "EPROTONOSUPPORT",
    "EPROTOTYPE",
    "EPWROFF",
    "EQFULL",
    "ERANGE",
    "EREMOTE",
    "ERESTART",
    "EROFS",
    "ERPCMISMATCH",
    "ESHLIBVERS",
    "ESHUTDOWN",
    "ESOCKTNOSUPPORT",
    "ESPIPE",
    "ESRCH",
    "ESTALE",
    "ETIME",
    "ETIMEDOUT",
    "ETOOMANYREFS",
    "ETXTBSY",
    "EUSERS",
    "EWOULDBLOCK",
    "EXDEV",
]


E2BIG: Final[int] = 7
EACCES: Final[int] = 13
EADDRINUSE: Final[int] = 48
EADDRNOTAVAIL: Final[int] = 49
EAFNOSUPPORT: Final[int] = 47
EAGAIN: Final[int] = 35
EALREADY: Final[int] = 37
EAUTH: Final[int] = 80
EBADF: Final[int] = 9
EBADRPC: Final[int] = 72
EBUSY: Final[int] = 16
ECANCELED: Final[int] = 89
ECHILD: Final[int] = 10
ECONNABORTED: Final[int] = 53
ECONNREFUSED: Final[int] = 61
ECONNRESET: Final[int] = 54
EDEADLK: Final[int] = 11
EDESTADDRREQ: Final[int] = 39
EDEVERR: Final[int] = 83
EDOM: Final[int] = 33
EDQUOT: Final[int] = 69
EEXIST: Final[int] = 17
EFAULT: Final[int] = 14
EFBIG: Final[int] = 27
EFTYPE: Final[int] = 79
EHOSTDOWN: Final[int] = 64
EHOSTUNREACH: Final[int] = 65
EINPROGRESS: Final[int] = 36
EINTR: Final[int] = 4
EINVAL: Final[int] = 22
EIO: Final[int] = 5
EISCONN: Final[int] = 56
EISDIR: Final[int] = 21
ELOOP: Final[int] = 62
EMFILE: Final[int] = 24
EMLINK: Final[int] = 31
EMSGSIZE: Final[int] = 40
ENAMETOOLONG: Final[int] = 63
ENEEDAUTH: Final[int] = 81
ENETDOWN: Final[int] = 50
ENETRESET: Final[int] = 52
ENETUNREACH: Final[int] = 51
ENFILE: Final[int] = 23
ENOBUFS: Final[int] = 55
ENODATA: Final[int] = 96
ENODEV: Final[int] = 19
ENOENT: Final[int] = 2
ENOEXEC: Final[int] = 8
ENOLCK: Final[int] = 77
ENOMEM: Final[int] = 12
ENOPROTOOPT: Final[int] = 42
ENOSPC: Final[int] = 28
ENOSYS: Final[int] = 78
ENOTBLK: Final[int] = 15
ENOTCONN: Final[int] = 57
ENOTDIR: Final[int] = 20
ENOTEMPTY: Final[int] = 66
ENOTSOCK: Final[int] = 38
ENOTTY: Final[int] = 25
ENXIO: Final[int] = 6
EOPNOTSUPP: Final[int] = 102
EOVERFLOW: Final[int] = 84
EPERM: Final[int] = 1
EPFNOSUPPORT: Final[int] = 46
EPIPE: Final[int] = 32
EPROCLIM: Final[int] = 67
EPROCUNAVAIL: Final[int] = 76
EPROGMISMATCH: Final[int] = 75
EPROGUNAVAIL: Final[int] = 74
EPROTO: Final[int] = 100
EPROTONOSUPPORT: Final[int] = 43
EPROTOTYPE: Final[int] = 41
EPWROFF: Final[int] = 82
EQFULL: Final[int] = 106
ERANGE: Final[int] = 34
EREMOTE: Final[int] = 71
ERESTART: Final[int] = -1
EROFS: Final[int] = 30
ERPCMISMATCH: Final[int] = 73
ESHUTDOWN: Final[int] = 58
ESOCKTNOSUPPORT: Final[int] = 44
ESPIPE: Final[int] = 29
ESRCH: Final[int] = 3
ESTALE: Final[int] = 70
ETIMEDOUT: Final[int] = 60
ETOOMANYREFS: Final[int] = 59
ETXTBSY: Final[int] = 26
EUSERS: Final[int] = 68
EWOULDBLOCK: Final[int] = 35
EXDEV: Final[int] = 18
EBADARCH: Final[int] = 86
EBADEXEC: Final[int] = 85
EBADMACHO: Final[int] = 88
EBADMSG: Final[int] = 94
EIDRM: Final[int] = 90
EILSEQ: Final[int] = 92
EMULTIHOP: Final[int] = 95
ENOATTR: Final[int] = 93
ENOLINK: Final[int] = 97
ENOMSG: Final[int] = 91
ENOPOLICY: Final[int] = 103
ENOSR: Final[int] = 98
ENOSTR: Final[int] = 99
ENOTRECOVERABLE: Final[int] = 104
ENOTSUP: Final[int] = 45
EOWNERDEAD: Final[int] = 105
ESHLIBVERS: Final[int] = 87
ETIME: Final[int] = 101

"""Error codes for POSIX 88.

See Also
--------
* https://docs.rust-embedded.org/rust-i2cdev/libc/consts/os/posix88/index.html
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
    "EDOTDOT",
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
    "EISNAM",
    "EKEYEXPIRED",
    "EKEYREJECTED",
    "EKEYREVOKED",
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
    "ELOOP",
    "EMEDIUMTYPE",
    "EMFILE",
    "EMLINK",
    "EMSGSIZE",
    "EMULTIHOP",
    "ENAMETOOLONG",
    "ENAVAIL",
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
    "ENOKEY",
    "ENOLCK",
    "ENOLINK",
    "ENOMEDIUM",
    "ENOMEM",
    "ENOMSG",
    "ENONET",
    "ENOPKG",
    "ENOPROTOOPT",
    "ENOSPC",
    "ENOSR",
    "ENOSTR",
    "ENOSYS",
    "ENOTBLK",
    "ENOTCONN",
    "ENOTDIR",
    "ENOTEMPTY",
    "ENOTNAM",
    "ENOTRECOVERABLE",
    "ENOTSOCK",
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
    "EREMOTEIO",
    "ERESTART",
    "ERFKILL",
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
    "EUCLEAN",
    "EUNATCH",
    "EUSERS",
    "EWOULDBLOCK",
    "EXDEV",
    "EXFULL",
]


E2BIG: Final[int] = 7
EACCES: Final[int] = 13
EADDRINUSE: Final[int] = 98
EADDRNOTAVAIL: Final[int] = 99
EADV: Final[int] = 68
EAFNOSUPPORT: Final[int] = 97
EAGAIN: Final[int] = 11
EALREADY: Final[int] = 114
EBADE: Final[int] = 52
EBADF: Final[int] = 9
EBADFD: Final[int] = 77
EBADMSG: Final[int] = 74
EBADR: Final[int] = 53
EBADRQC: Final[int] = 56
EBADSLT: Final[int] = 57
EBFONT: Final[int] = 59
EBUSY: Final[int] = 16
ECANCELED: Final[int] = 125
ECHILD: Final[int] = 10
ECHRNG: Final[int] = 44
ECOMM: Final[int] = 70
ECONNABORTED: Final[int] = 103
ECONNREFUSED: Final[int] = 111
ECONNRESET: Final[int] = 104
EDEADLK: Final[int] = 35
EDEADLOCK: Final[int] = 35
EDESTADDRREQ: Final[int] = 89
EDOM: Final[int] = 33
EDOTDOT: Final[int] = 73
EDQUOT: Final[int] = 122
EEXIST: Final[int] = 17
EFAULT: Final[int] = 14
EFBIG: Final[int] = 27
EHOSTDOWN: Final[int] = 112
EHOSTUNREACH: Final[int] = 113
EIDRM: Final[int] = 43
EILSEQ: Final[int] = 84
EINPROGRESS: Final[int] = 115
EINTR: Final[int] = 4
EINVAL: Final[int] = 22
EIO: Final[int] = 5
EISCONN: Final[int] = 106
EISDIR: Final[int] = 21
EISNAM: Final[int] = 120
EKEYEXPIRED: Final[int] = 127
EKEYREJECTED: Final[int] = 129
EKEYREVOKED: Final[int] = 128
EL2HLT: Final[int] = 51
EL2NSYNC: Final[int] = 45
EL3HLT: Final[int] = 46
EL3RST: Final[int] = 47
ELIBACC: Final[int] = 79
ELIBBAD: Final[int] = 80
ELIBEXEC: Final[int] = 83
ELIBMAX: Final[int] = 82
ELIBSCN: Final[int] = 81
ELNRNG: Final[int] = 48
ELOOP: Final[int] = 40
EMEDIUMTYPE: Final[int] = 124
EMFILE: Final[int] = 24
EMLINK: Final[int] = 31
EMSGSIZE: Final[int] = 90
EMULTIHOP: Final[int] = 72
ENAMETOOLONG: Final[int] = 36
ENAVAIL: Final[int] = 119
ENETDOWN: Final[int] = 100
ENETRESET: Final[int] = 102
ENETUNREACH: Final[int] = 101
ENFILE: Final[int] = 23
ENOANO: Final[int] = 55
ENOBUFS: Final[int] = 105
ENOCSI: Final[int] = 50
ENODATA: Final[int] = 61
ENODEV: Final[int] = 19
ENOENT: Final[int] = 2
ENOEXEC: Final[int] = 8
ENOKEY: Final[int] = 126
ENOLCK: Final[int] = 37
ENOLINK: Final[int] = 67
ENOMEDIUM: Final[int] = 123
ENOMEM: Final[int] = 12
ENOMSG: Final[int] = 42
ENONET: Final[int] = 64
ENOPKG: Final[int] = 65
ENOPROTOOPT: Final[int] = 92
ENOSPC: Final[int] = 28
ENOSR: Final[int] = 63
ENOSTR: Final[int] = 60
ENOSYS: Final[int] = 38
ENOTBLK: Final[int] = 15
ENOTCONN: Final[int] = 107
ENOTDIR: Final[int] = 20
ENOTEMPTY: Final[int] = 39
ENOTNAM: Final[int] = 118
ENOTRECOVERABLE: Final[int] = 131
ENOTSOCK: Final[int] = 88
ENOTTY: Final[int] = 25
ENOTUNIQ: Final[int] = 76
ENXIO: Final[int] = 6
EOPNOTSUPP: Final[int] = 95
EOVERFLOW: Final[int] = 75
EOWNERDEAD: Final[int] = 130
EPERM: Final[int] = 1
EPFNOSUPPORT: Final[int] = 96
EPIPE: Final[int] = 32
EPROTO: Final[int] = 71
EPROTONOSUPPORT: Final[int] = 93
EPROTOTYPE: Final[int] = 91
ERANGE: Final[int] = 34
EREMCHG: Final[int] = 78
EREMOTE: Final[int] = 66
EREMOTEIO: Final[int] = 121
ERESTART: Final[int] = 85
ERFKILL: Final[int] = 132
EROFS: Final[int] = 30
ESHUTDOWN: Final[int] = 108
ESOCKTNOSUPPORT: Final[int] = 94
ESPIPE: Final[int] = 29
ESRCH: Final[int] = 3
ESRMNT: Final[int] = 69
ESTALE: Final[int] = 116
ESTRPIPE: Final[int] = 86
ETIME: Final[int] = 62
ETIMEDOUT: Final[int] = 110
ETOOMANYREFS: Final[int] = 109
ETXTBSY: Final[int] = 26
EUCLEAN: Final[int] = 117
EUNATCH: Final[int] = 49
EUSERS: Final[int] = 87
EWOULDBLOCK: Final[int] = 11
EXDEV: Final[int] = 18
EXFULL: Final[int] = 54

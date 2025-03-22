import errno as py_errno

from typing import Final

from backlib.internal.backports.py310.errno.internal import (
    darwin1,
    freebsd13,
    msvc22,
    posix88,
    solaris10,
)
from backlib.internal.utils import alias


__all__: list[str] = [
    "E2BIG",
    "EACCES",
    "EADDRINUSE",
    "EADDRNOTAVAIL",
    "EADV",
    "EAFNOSUPPORT",
    "EAGAIN",
    "EALREADY",
    "EAUTH",
    "EBADARCH",
    "EBADE",
    "EBADEXEC",
    "EBADF",
    "EBADFD",
    "EBADMACHO",
    "EBADMSG",
    "EBADR",
    "EBADRPC",
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
    "EDEVERR",
    "EDOM",
    "EDOTDOT",
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
    "ELOCKUNMAPPED",
    "ELOOP",
    "EMEDIUMTYPE",
    "EMFILE",
    "EMLINK",
    "EMSGSIZE",
    "EMULTIHOP",
    "ENAMETOOLONG",
    "ENAVAIL",
    "ENEEDAUTH",
    "ENETDOWN",
    "ENETRESET",
    "ENETUNREACH",
    "ENFILE",
    "ENOANO",
    "ENOATTR",
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
    "ENOPOLICY",
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
    "ENOTNAM",
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
    "EPROCLIM",
    "EPROCUNAVAIL",
    "EPROGMISMATCH",
    "EPROGUNAVAIL",
    "EPROTO",
    "EPROTONOSUPPORT",
    "EPROTOTYPE",
    "EPWROFF",
    "ERANGE",
    "EREMCHG",
    "EREMOTE",
    "EREMOTEIO",
    "ERESTART",
    "ERFKILL",
    "EROFS",
    "ERPCMISMATCH",
    "ESHLIBVERS",
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
    "errorcode",
]


E2BIG: Final[int] = alias.or_platform(
    py_errno,
    "E2BIG",
    darwin=darwin1.E2BIG,
    freebsd=freebsd13.E2BIG,
    nt=msvc22.E2BIG,
    posix=posix88.E2BIG,
    solaris=solaris10.E2BIG,
    otherwise=posix88.E2BIG,
)

EACCES: Final[int] = alias.or_platform(
    py_errno,
    "EACCES",
    darwin=darwin1.EACCES,
    freebsd=freebsd13.EACCES,
    nt=msvc22.EACCES,
    posix=posix88.EACCES,
    solaris=solaris10.EACCES,
    otherwise=posix88.EACCES,
)

EADDRINUSE: Final[int] = alias.or_platform(
    py_errno,
    "EADDRINUSE",
    darwin=darwin1.EADDRINUSE,
    freebsd=freebsd13.EADDRINUSE,
    nt=msvc22.EADDRINUSE,
    posix=posix88.EADDRINUSE,
    solaris=solaris10.EADDRINUSE,
    otherwise=posix88.EADDRINUSE,
)

EADDRNOTAVAIL: Final[int] = alias.or_platform(
    py_errno,
    "EADDRNOTAVAIL",
    darwin=darwin1.EADDRNOTAVAIL,
    freebsd=freebsd13.EADDRNOTAVAIL,
    nt=msvc22.EADDRNOTAVAIL,
    posix=posix88.EADDRNOTAVAIL,
    solaris=solaris10.EADDRNOTAVAIL,
    otherwise=posix88.EADDRNOTAVAIL,
)

EADV: Final[int] = alias.or_platform(
    py_errno,
    "EADV",
    posix=posix88.EADV,
    solaris=solaris10.EADV,
    otherwise=posix88.EADV,
)

EAFNOSUPPORT: Final[int] = alias.or_platform(
    py_errno,
    "EAFNOSUPPORT",
    darwin=darwin1.EAFNOSUPPORT,
    freebsd=freebsd13.EAFNOSUPPORT,
    nt=msvc22.EAFNOSUPPORT,
    posix=posix88.EAFNOSUPPORT,
    solaris=solaris10.EAFNOSUPPORT,
    otherwise=posix88.EAFNOSUPPORT,
)

EAGAIN: Final[int] = alias.or_platform(
    py_errno,
    "EAGAIN",
    darwin=darwin1.EAGAIN,
    freebsd=freebsd13.EAGAIN,
    nt=msvc22.EAGAIN,
    posix=posix88.EAGAIN,
    solaris=solaris10.EAGAIN,
    otherwise=posix88.EAGAIN,
)

EALREADY: Final[int] = alias.or_platform(
    py_errno,
    "EALREADY",
    darwin=darwin1.EALREADY,
    freebsd=freebsd13.EALREADY,
    nt=msvc22.EALREADY,
    posix=posix88.EALREADY,
    solaris=solaris10.EALREADY,
    otherwise=posix88.EALREADY,
)

EAUTH: Final[int] = alias.or_platform(
    py_errno,
    "EAUTH",
    darwin=darwin1.EAUTH,
    freebsd=freebsd13.EAUTH,
    otherwise=darwin1.EAUTH,
)

EBADARCH: Final[int] = alias.or_platform(
    py_errno,
    "EBADARCH",
    darwin=darwin1.EBADARCH,
    otherwise=darwin1.EBADARCH,
)

EBADE: Final[int] = alias.or_platform(
    py_errno,
    "EBADE",
    posix=posix88.EBADE,
    solaris=solaris10.EBADE,
    otherwise=posix88.EBADE,
)

EBADEXEC: Final[int] = alias.or_platform(
    py_errno,
    "EBADEXEC",
    darwin=darwin1.EBADEXEC,
    otherwise=darwin1.EBADEXEC,
)

EBADF: Final[int] = alias.or_platform(
    py_errno,
    "EBADF",
    darwin=darwin1.EBADF,
    freebsd=freebsd13.EBADF,
    nt=msvc22.EBADF,
    posix=posix88.EBADF,
    solaris=solaris10.EBADF,
    otherwise=posix88.EBADF,
)

EBADFD: Final[int] = alias.or_platform(
    py_errno,
    "EBADFD",
    posix=posix88.EBADFD,
    solaris=solaris10.EBADFD,
    otherwise=posix88.EBADFD,
)

EBADMACHO: Final[int] = alias.or_platform(
    py_errno,
    "EBADMACHO",
    darwin=darwin1.EBADMACHO,
    otherwise=darwin1.EBADMACHO,
)

EBADMSG: Final[int] = alias.or_platform(
    py_errno,
    "EBADMSG",
    darwin=darwin1.EBADMSG,
    freebsd=freebsd13.EBADMSG,
    nt=msvc22.EBADMSG,
    posix=posix88.EBADMSG,
    solaris=solaris10.EBADMSG,
    otherwise=posix88.EBADMSG,
)

EBADR: Final[int] = alias.or_platform(
    py_errno,
    "EBADR",
    posix=posix88.EBADR,
    solaris=solaris10.EBADR,
    otherwise=posix88.EBADR,
)

EBADRPC: Final[int] = alias.or_platform(
    py_errno,
    "EBADRPC",
    darwin=darwin1.EBADRPC,
    freebsd=freebsd13.EBADRPC,
    otherwise=darwin1.EBADRPC,
)

EBADRQC: Final[int] = alias.or_platform(
    py_errno,
    "EBADRQC",
    posix=posix88.EBADRQC,
    solaris=solaris10.EBADRQC,
    otherwise=posix88.EBADRQC,
)

EBADSLT: Final[int] = alias.or_platform(
    py_errno,
    "EBADSLT",
    posix=posix88.EBADSLT,
    solaris=solaris10.EBADSLT,
    otherwise=posix88.EBADSLT,
)

EBFONT: Final[int] = alias.or_platform(
    py_errno,
    "EBFONT",
    posix=posix88.EBFONT,
    solaris=solaris10.EBFONT,
    otherwise=posix88.EBFONT,
)

EBUSY: Final[int] = alias.or_platform(
    py_errno,
    "EBUSY",
    darwin=darwin1.EBUSY,
    freebsd=freebsd13.EBUSY,
    nt=msvc22.EBUSY,
    posix=posix88.EBUSY,
    solaris=solaris10.EBUSY,
    otherwise=posix88.EBUSY,
)

ECANCELED: Final[int] = alias.or_platform(
    py_errno,
    "ECANCELED",
    darwin=darwin1.ECANCELED,
    freebsd=freebsd13.ECANCELED,
    nt=msvc22.ECANCELED,
    posix=posix88.ECANCELED,
    solaris=solaris10.ECANCELED,
    otherwise=posix88.ECANCELED,
)

ECHILD: Final[int] = alias.or_platform(
    py_errno,
    "ECHILD",
    darwin=darwin1.ECHILD,
    freebsd=freebsd13.ECHILD,
    nt=msvc22.ECHILD,
    posix=posix88.ECHILD,
    solaris=solaris10.ECHILD,
    otherwise=posix88.ECHILD,
)

ECHRNG: Final[int] = alias.or_platform(
    py_errno,
    "ECHRNG",
    posix=posix88.ECHRNG,
    solaris=solaris10.ECHRNG,
    otherwise=posix88.ECHRNG,
)

ECOMM: Final[int] = alias.or_platform(
    py_errno,
    "ECOMM",
    posix=posix88.ECOMM,
    solaris=solaris10.ECOMM,
    otherwise=posix88.ECOMM,
)

ECONNABORTED: Final[int] = alias.or_platform(
    py_errno,
    "ECONNABORTED",
    darwin=darwin1.ECONNABORTED,
    freebsd=freebsd13.ECONNABORTED,
    nt=msvc22.ECONNABORTED,
    posix=posix88.ECONNABORTED,
    solaris=solaris10.ECONNABORTED,
    otherwise=posix88.ECONNABORTED,
)

ECONNREFUSED: Final[int] = alias.or_platform(
    py_errno,
    "ECONNREFUSED",
    darwin=darwin1.ECONNREFUSED,
    freebsd=freebsd13.ECONNREFUSED,
    nt=msvc22.ECONNREFUSED,
    posix=posix88.ECONNREFUSED,
    solaris=solaris10.ECONNREFUSED,
    otherwise=posix88.ECONNREFUSED,
)

ECONNRESET: Final[int] = alias.or_platform(
    py_errno,
    "ECONNRESET",
    darwin=darwin1.ECONNRESET,
    freebsd=freebsd13.ECONNRESET,
    nt=msvc22.ECONNRESET,
    posix=posix88.ECONNRESET,
    solaris=solaris10.ECONNRESET,
    otherwise=posix88.ECONNRESET,
)

EDEADLK: Final[int] = alias.or_platform(
    py_errno,
    "EDEADLK",
    darwin=darwin1.EDEADLK,
    freebsd=freebsd13.EDEADLK,
    nt=msvc22.EDEADLK,
    posix=posix88.EDEADLK,
    solaris=solaris10.EDEADLK,
    otherwise=posix88.EDEADLK,
)

EDEADLOCK: Final[int] = alias.or_platform(
    py_errno,
    "EDEADLOCK",
    nt=msvc22.EDEADLOCK,
    posix=posix88.EDEADLOCK,
    solaris=solaris10.EDEADLOCK,
    otherwise=posix88.EDEADLOCK,
)

EDESTADDRREQ: Final[int] = alias.or_platform(
    py_errno,
    "EDESTADDRREQ",
    darwin=darwin1.EDESTADDRREQ,
    freebsd=freebsd13.EDESTADDRREQ,
    nt=msvc22.EDESTADDRREQ,
    posix=posix88.EDESTADDRREQ,
    solaris=solaris10.EDESTADDRREQ,
    otherwise=posix88.EDESTADDRREQ,
)

EDEVERR: Final[int] = alias.or_platform(
    py_errno,
    "EDEVERR",
    darwin=darwin1.EDEVERR,
    otherwise=darwin1.EDEVERR,
)

EDOM: Final[int] = alias.or_platform(
    py_errno,
    "EDOM",
    darwin=darwin1.EDOM,
    freebsd=freebsd13.EDOM,
    nt=msvc22.EDOM,
    posix=posix88.EDOM,
    solaris=solaris10.EDOM,
    otherwise=posix88.EDOM,
)

EDOTDOT: Final[int] = alias.or_platform(
    py_errno,
    "EDOTDOT",
    posix=posix88.EDOTDOT,
    otherwise=posix88.EDOTDOT,
)

EDQUOT: Final[int] = alias.or_platform(
    py_errno,
    "EDQUOT",
    darwin=darwin1.EDQUOT,
    freebsd=freebsd13.EDQUOT,
    posix=posix88.EDQUOT,
    solaris=solaris10.EDQUOT,
    otherwise=posix88.EDQUOT,
)

EEXIST: Final[int] = alias.or_platform(
    py_errno,
    "EEXIST",
    darwin=darwin1.EEXIST,
    freebsd=freebsd13.EEXIST,
    nt=msvc22.EEXIST,
    posix=posix88.EEXIST,
    solaris=solaris10.EEXIST,
    otherwise=posix88.EEXIST,
)

EFAULT: Final[int] = alias.or_platform(
    py_errno,
    "EFAULT",
    darwin=darwin1.EFAULT,
    freebsd=freebsd13.EFAULT,
    nt=msvc22.EFAULT,
    posix=posix88.EFAULT,
    solaris=solaris10.EFAULT,
    otherwise=posix88.EFAULT,
)

EFBIG: Final[int] = alias.or_platform(
    py_errno,
    "EFBIG",
    darwin=darwin1.EFBIG,
    freebsd=freebsd13.EFBIG,
    nt=msvc22.EFBIG,
    posix=posix88.EFBIG,
    solaris=solaris10.EFBIG,
    otherwise=posix88.EFBIG,
)

EFTYPE: Final[int] = alias.or_platform(
    py_errno,
    "EFTYPE",
    darwin=darwin1.EFTYPE,
    freebsd=freebsd13.EFTYPE,
    otherwise=darwin1.EFTYPE,
)

EHOSTDOWN: Final[int] = alias.or_platform(
    py_errno,
    "EHOSTDOWN",
    darwin=darwin1.EHOSTDOWN,
    freebsd=freebsd13.EHOSTDOWN,
    posix=posix88.EHOSTDOWN,
    solaris=solaris10.EHOSTDOWN,
    otherwise=posix88.EHOSTDOWN,
)

EHOSTUNREACH: Final[int] = alias.or_platform(
    py_errno,
    "EHOSTUNREACH",
    darwin=darwin1.EHOSTUNREACH,
    freebsd=freebsd13.EHOSTUNREACH,
    nt=msvc22.EHOSTUNREACH,
    posix=posix88.EHOSTUNREACH,
    solaris=solaris10.EHOSTUNREACH,
    otherwise=posix88.EHOSTUNREACH,
)

EIDRM: Final[int] = alias.or_platform(
    py_errno,
    "EIDRM",
    darwin=darwin1.EIDRM,
    freebsd=freebsd13.EIDRM,
    nt=msvc22.EIDRM,
    posix=posix88.EIDRM,
    solaris=solaris10.EIDRM,
    otherwise=posix88.EIDRM,
)

EILSEQ: Final[int] = alias.or_platform(
    py_errno,
    "EILSEQ",
    darwin=darwin1.EILSEQ,
    freebsd=freebsd13.EILSEQ,
    nt=msvc22.EILSEQ,
    posix=posix88.EILSEQ,
    solaris=solaris10.EILSEQ,
    otherwise=posix88.EILSEQ,
)

EINPROGRESS: Final[int] = alias.or_platform(
    py_errno,
    "EINPROGRESS",
    darwin=darwin1.EINPROGRESS,
    freebsd=freebsd13.EINPROGRESS,
    nt=msvc22.EINPROGRESS,
    posix=posix88.EINPROGRESS,
    solaris=solaris10.EINPROGRESS,
    otherwise=posix88.EINPROGRESS,
)

EINTR: Final[int] = alias.or_platform(
    py_errno,
    "EINTR",
    darwin=darwin1.EINTR,
    freebsd=freebsd13.EINTR,
    nt=msvc22.EINTR,
    posix=posix88.EINTR,
    solaris=solaris10.EINTR,
    otherwise=posix88.EINTR,
)

EINVAL: Final[int] = alias.or_platform(
    py_errno,
    "EINVAL",
    darwin=darwin1.EINVAL,
    freebsd=freebsd13.EINVAL,
    nt=msvc22.EINVAL,
    posix=posix88.EINVAL,
    solaris=solaris10.EINVAL,
    otherwise=posix88.EINVAL,
)

EIO: Final[int] = alias.or_platform(
    py_errno,
    "EIO",
    darwin=darwin1.EIO,
    freebsd=freebsd13.EIO,
    nt=msvc22.EIO,
    posix=posix88.EIO,
    solaris=solaris10.EIO,
    otherwise=posix88.EIO,
)

EISCONN: Final[int] = alias.or_platform(
    py_errno,
    "EISCONN",
    darwin=darwin1.EISCONN,
    freebsd=freebsd13.EISCONN,
    nt=msvc22.EISCONN,
    posix=posix88.EISCONN,
    solaris=solaris10.EISCONN,
    otherwise=posix88.EISCONN,
)

EISDIR: Final[int] = alias.or_platform(
    py_errno,
    "EISDIR",
    darwin=darwin1.EISDIR,
    freebsd=freebsd13.EISDIR,
    nt=msvc22.EISDIR,
    posix=posix88.EISDIR,
    solaris=solaris10.EISDIR,
    otherwise=posix88.EISDIR,
)

EISNAM: Final[int] = alias.or_platform(
    py_errno,
    "EISNAM",
    posix=posix88.EISNAM,
    otherwise=posix88.EISNAM,
)

EKEYEXPIRED: Final[int] = alias.or_platform(
    py_errno,
    "EKEYEXPIRED",
    posix=posix88.EKEYEXPIRED,
    otherwise=posix88.EKEYEXPIRED,
)

EKEYREJECTED: Final[int] = alias.or_platform(
    py_errno,
    "EKEYREJECTED",
    posix=posix88.EKEYREJECTED,
    otherwise=posix88.EKEYREJECTED,
)

EKEYREVOKED: Final[int] = alias.or_platform(
    py_errno,
    "EKEYREVOKED",
    posix=posix88.EKEYREVOKED,
    otherwise=posix88.EKEYREVOKED,
)

EL2HLT: Final[int] = alias.or_platform(
    py_errno,
    "EL2HLT",
    posix=posix88.EL2HLT,
    solaris=solaris10.EL2HLT,
    otherwise=posix88.EL2HLT,
)

EL2NSYNC: Final[int] = alias.or_platform(
    py_errno,
    "EL2NSYNC",
    posix=posix88.EL2NSYNC,
    solaris=solaris10.EL2NSYNC,
    otherwise=posix88.EL2NSYNC,
)

EL3HLT: Final[int] = alias.or_platform(
    py_errno,
    "EL3HLT",
    posix=posix88.EL3HLT,
    solaris=solaris10.EL3HLT,
    otherwise=posix88.EL3HLT,
)

EL3RST: Final[int] = alias.or_platform(
    py_errno,
    "EL3RST",
    posix=posix88.EL3RST,
    solaris=solaris10.EL3RST,
    otherwise=posix88.EL3RST,
)

ELIBACC: Final[int] = alias.or_platform(
    py_errno,
    "ELIBACC",
    posix=posix88.ELIBACC,
    solaris=solaris10.ELIBACC,
    otherwise=posix88.ELIBACC,
)

ELIBBAD: Final[int] = alias.or_platform(
    py_errno,
    "ELIBBAD",
    posix=posix88.ELIBBAD,
    solaris=solaris10.ELIBBAD,
    otherwise=posix88.ELIBBAD,
)

ELIBEXEC: Final[int] = alias.or_platform(
    py_errno,
    "ELIBEXEC",
    posix=posix88.ELIBEXEC,
    solaris=solaris10.ELIBEXEC,
    otherwise=posix88.ELIBEXEC,
)

ELIBMAX: Final[int] = alias.or_platform(
    py_errno,
    "ELIBMAX",
    posix=posix88.ELIBMAX,
    solaris=solaris10.ELIBMAX,
    otherwise=posix88.ELIBMAX,
)

ELIBSCN: Final[int] = alias.or_platform(
    py_errno,
    "ELIBSCN",
    posix=posix88.ELIBSCN,
    solaris=solaris10.ELIBSCN,
    otherwise=posix88.ELIBSCN,
)

ELNRNG: Final[int] = alias.or_platform(
    py_errno,
    "ELNRNG",
    posix=posix88.ELNRNG,
    solaris=solaris10.ELNRNG,
    otherwise=posix88.ELNRNG,
)

ELOCKUNMAPPED: Final[int] = alias.or_platform(
    py_errno,
    "ELOCKUNMAPPED",
    solaris=solaris10.ELOCKUNMAPPED,
    otherwise=solaris10.ELOCKUNMAPPED,
)

ELOOP: Final[int] = alias.or_platform(
    py_errno,
    "ELOOP",
    darwin=darwin1.ELOOP,
    freebsd=freebsd13.ELOOP,
    nt=msvc22.ELOOP,
    posix=posix88.ELOOP,
    solaris=solaris10.ELOOP,
    otherwise=posix88.ELOOP,
)

EMEDIUMTYPE: Final[int] = alias.or_platform(
    py_errno,
    "EMEDIUMTYPE",
    posix=posix88.EMEDIUMTYPE,
    otherwise=posix88.EMEDIUMTYPE,
)

EMFILE: Final[int] = alias.or_platform(
    py_errno,
    "EMFILE",
    darwin=darwin1.EMFILE,
    freebsd=freebsd13.EMFILE,
    nt=msvc22.EMFILE,
    posix=posix88.EMFILE,
    solaris=solaris10.EMFILE,
    otherwise=posix88.EMFILE,
)

EMLINK: Final[int] = alias.or_platform(
    py_errno,
    "EMLINK",
    darwin=darwin1.EMLINK,
    freebsd=freebsd13.EMLINK,
    nt=msvc22.EMLINK,
    posix=posix88.EMLINK,
    solaris=solaris10.EMLINK,
    otherwise=posix88.EMLINK,
)

EMSGSIZE: Final[int] = alias.or_platform(
    py_errno,
    "EMSGSIZE",
    darwin=darwin1.EMSGSIZE,
    freebsd=freebsd13.EMSGSIZE,
    nt=msvc22.EMSGSIZE,
    posix=posix88.EMSGSIZE,
    solaris=solaris10.EMSGSIZE,
    otherwise=posix88.EMSGSIZE,
)

EMULTIHOP: Final[int] = alias.or_platform(
    py_errno,
    "EMULTIHOP",
    darwin=darwin1.EMULTIHOP,
    freebsd=freebsd13.EMULTIHOP,
    posix=posix88.EMULTIHOP,
    solaris=solaris10.EMULTIHOP,
    otherwise=posix88.EMULTIHOP,
)

ENAMETOOLONG: Final[int] = alias.or_platform(
    py_errno,
    "ENAMETOOLONG",
    darwin=darwin1.ENAMETOOLONG,
    freebsd=freebsd13.ENAMETOOLONG,
    nt=msvc22.ENAMETOOLONG,
    posix=posix88.ENAMETOOLONG,
    solaris=solaris10.ENAMETOOLONG,
    otherwise=posix88.ENAMETOOLONG,
)

ENAVAIL: Final[int] = alias.or_platform(
    py_errno,
    "ENAVAIL",
    posix=posix88.ENAVAIL,
    otherwise=posix88.ENAVAIL,
)

ENEEDAUTH: Final[int] = alias.or_platform(
    py_errno,
    "ENEEDAUTH",
    darwin=darwin1.ENEEDAUTH,
    freebsd=freebsd13.ENEEDAUTH,
    otherwise=darwin1.ENEEDAUTH,
)

ENETDOWN: Final[int] = alias.or_platform(
    py_errno,
    "ENETDOWN",
    darwin=darwin1.ENETDOWN,
    freebsd=freebsd13.ENETDOWN,
    nt=msvc22.ENETDOWN,
    posix=posix88.ENETDOWN,
    solaris=solaris10.ENETDOWN,
    otherwise=posix88.ENETDOWN,
)

ENETRESET: Final[int] = alias.or_platform(
    py_errno,
    "ENETRESET",
    darwin=darwin1.ENETRESET,
    freebsd=freebsd13.ENETRESET,
    nt=msvc22.ENETRESET,
    posix=posix88.ENETRESET,
    solaris=solaris10.ENETRESET,
    otherwise=posix88.ENETRESET,
)

ENETUNREACH: Final[int] = alias.or_platform(
    py_errno,
    "ENETUNREACH",
    darwin=darwin1.ENETUNREACH,
    freebsd=freebsd13.ENETUNREACH,
    nt=msvc22.ENETUNREACH,
    posix=posix88.ENETUNREACH,
    solaris=solaris10.ENETUNREACH,
    otherwise=posix88.ENETUNREACH,
)

ENFILE: Final[int] = alias.or_platform(
    py_errno,
    "ENFILE",
    darwin=darwin1.ENFILE,
    freebsd=freebsd13.ENFILE,
    nt=msvc22.ENFILE,
    posix=posix88.ENFILE,
    solaris=solaris10.ENFILE,
    otherwise=posix88.ENFILE,
)

ENOANO: Final[int] = alias.or_platform(
    py_errno,
    "ENOANO",
    posix=posix88.ENOANO,
    solaris=solaris10.ENOANO,
    otherwise=posix88.ENOANO,
)

ENOATTR: Final[int] = alias.or_platform(
    py_errno,
    "ENOATTR",
    darwin=darwin1.ENOATTR,
    freebsd=freebsd13.ENOATTR,
    otherwise=darwin1.ENOATTR,
)

ENOBUFS: Final[int] = alias.or_platform(
    py_errno,
    "ENOBUFS",
    darwin=darwin1.ENOBUFS,
    freebsd=freebsd13.ENOBUFS,
    nt=msvc22.ENOBUFS,
    posix=posix88.ENOBUFS,
    solaris=solaris10.ENOBUFS,
    otherwise=posix88.ENOBUFS,
)

ENOCSI: Final[int] = alias.or_platform(
    py_errno,
    "ENOCSI",
    posix=posix88.ENOCSI,
    solaris=solaris10.ENOCSI,
    otherwise=posix88.ENOCSI,
)

ENODATA: Final[int] = alias.or_platform(
    py_errno,
    "ENODATA",
    darwin=darwin1.ENODATA,
    nt=msvc22.ENODATA,
    posix=posix88.ENODATA,
    solaris=solaris10.ENODATA,
    otherwise=posix88.ENODATA,
)

ENODEV: Final[int] = alias.or_platform(
    py_errno,
    "ENODEV",
    darwin=darwin1.ENODEV,
    freebsd=freebsd13.ENODEV,
    nt=msvc22.ENODEV,
    posix=posix88.ENODEV,
    solaris=solaris10.ENODEV,
    otherwise=posix88.ENODEV,
)

ENOENT: Final[int] = alias.or_platform(
    py_errno,
    "ENOENT",
    darwin=darwin1.ENOENT,
    freebsd=freebsd13.ENOENT,
    nt=msvc22.ENOENT,
    posix=posix88.ENOENT,
    solaris=solaris10.ENOENT,
    otherwise=posix88.ENOENT,
)

ENOEXEC: Final[int] = alias.or_platform(
    py_errno,
    "ENOEXEC",
    darwin=darwin1.ENOEXEC,
    freebsd=freebsd13.ENOEXEC,
    nt=msvc22.ENOEXEC,
    posix=posix88.ENOEXEC,
    solaris=solaris10.ENOEXEC,
    otherwise=posix88.ENOEXEC,
)

ENOKEY: Final[int] = alias.or_platform(
    py_errno,
    "ENOKEY",
    posix=posix88.ENOKEY,
    otherwise=posix88.ENOKEY,
)

ENOLCK: Final[int] = alias.or_platform(
    py_errno,
    "ENOLCK",
    darwin=darwin1.ENOLCK,
    freebsd=freebsd13.ENOLCK,
    nt=msvc22.ENOLCK,
    posix=posix88.ENOLCK,
    solaris=solaris10.ENOLCK,
    otherwise=posix88.ENOLCK,
)

ENOLINK: Final[int] = alias.or_platform(
    py_errno,
    "ENOLINK",
    darwin=darwin1.ENOLINK,
    freebsd=freebsd13.ENOLINK,
    nt=msvc22.ENOLINK,
    posix=posix88.ENOLINK,
    solaris=solaris10.ENOLINK,
    otherwise=posix88.ENOLINK,
)

ENOMEDIUM: Final[int] = alias.or_platform(
    py_errno,
    "ENOMEDIUM",
    posix=posix88.ENOMEDIUM,
    otherwise=posix88.ENOMEDIUM,
)

ENOMEM: Final[int] = alias.or_platform(
    py_errno,
    "ENOMEM",
    darwin=darwin1.ENOMEM,
    freebsd=freebsd13.ENOMEM,
    nt=msvc22.ENOMEM,
    posix=posix88.ENOMEM,
    solaris=solaris10.ENOMEM,
    otherwise=posix88.ENOMEM,
)

ENOMSG: Final[int] = alias.or_platform(
    py_errno,
    "ENOMSG",
    darwin=darwin1.ENOMSG,
    freebsd=freebsd13.ENOMSG,
    nt=msvc22.ENOMSG,
    posix=posix88.ENOMSG,
    solaris=solaris10.ENOMSG,
    otherwise=posix88.ENOMSG,
)

ENONET: Final[int] = alias.or_platform(
    py_errno,
    "ENONET",
    posix=posix88.ENONET,
    solaris=solaris10.ENONET,
    otherwise=posix88.ENONET,
)

ENOPKG: Final[int] = alias.or_platform(
    py_errno,
    "ENOPKG",
    posix=posix88.ENOPKG,
    solaris=solaris10.ENOPKG,
    otherwise=posix88.ENOPKG,
)

ENOPOLICY: Final[int] = alias.or_platform(
    py_errno,
    "ENOPOLICY",
    darwin=darwin1.ENOPOLICY,
    otherwise=darwin1.ENOPOLICY,
)

ENOPROTOOPT: Final[int] = alias.or_platform(
    py_errno,
    "ENOPROTOOPT",
    darwin=darwin1.ENOPROTOOPT,
    freebsd=freebsd13.ENOPROTOOPT,
    nt=msvc22.ENOPROTOOPT,
    posix=posix88.ENOPROTOOPT,
    solaris=solaris10.ENOPROTOOPT,
    otherwise=posix88.ENOPROTOOPT,
)

ENOSPC: Final[int] = alias.or_platform(
    py_errno,
    "ENOSPC",
    darwin=darwin1.ENOSPC,
    freebsd=freebsd13.ENOSPC,
    nt=msvc22.ENOSPC,
    posix=posix88.ENOSPC,
    solaris=solaris10.ENOSPC,
    otherwise=posix88.ENOSPC,
)

ENOSR: Final[int] = alias.or_platform(
    py_errno,
    "ENOSR",
    darwin=darwin1.ENOSR,
    nt=msvc22.ENOSR,
    posix=posix88.ENOSR,
    solaris=solaris10.ENOSR,
    otherwise=posix88.ENOSR,
)

ENOSTR: Final[int] = alias.or_platform(
    py_errno,
    "ENOSTR",
    darwin=darwin1.ENOSTR,
    nt=msvc22.ENOSTR,
    posix=posix88.ENOSTR,
    solaris=solaris10.ENOSTR,
    otherwise=posix88.ENOSTR,
)

ENOSYS: Final[int] = alias.or_platform(
    py_errno,
    "ENOSYS",
    darwin=darwin1.ENOSYS,
    freebsd=freebsd13.ENOSYS,
    nt=msvc22.ENOSYS,
    posix=posix88.ENOSYS,
    solaris=solaris10.ENOSYS,
    otherwise=posix88.ENOSYS,
)

ENOTACTIVE: Final[int] = alias.or_platform(
    py_errno,
    "ENOTACTIVE",
    solaris=solaris10.ENOTACTIVE,
    otherwise=solaris10.ENOTACTIVE,
)

ENOTBLK: Final[int] = alias.or_platform(
    py_errno,
    "ENOTBLK",
    darwin=darwin1.ENOTBLK,
    freebsd=freebsd13.ENOTBLK,
    posix=posix88.ENOTBLK,
    solaris=solaris10.ENOTBLK,
    otherwise=posix88.ENOTBLK,
)

ENOTCONN: Final[int] = alias.or_platform(
    py_errno,
    "ENOTCONN",
    darwin=darwin1.ENOTCONN,
    freebsd=freebsd13.ENOTCONN,
    nt=msvc22.ENOTCONN,
    posix=posix88.ENOTCONN,
    solaris=solaris10.ENOTCONN,
    otherwise=posix88.ENOTCONN,
)

ENOTDIR: Final[int] = alias.or_platform(
    py_errno,
    "ENOTDIR",
    darwin=darwin1.ENOTDIR,
    freebsd=freebsd13.ENOTDIR,
    nt=msvc22.ENOTDIR,
    posix=posix88.ENOTDIR,
    solaris=solaris10.ENOTDIR,
    otherwise=posix88.ENOTDIR,
)

ENOTEMPTY: Final[int] = alias.or_platform(
    py_errno,
    "ENOTEMPTY",
    darwin=darwin1.ENOTEMPTY,
    freebsd=freebsd13.ENOTEMPTY,
    nt=msvc22.ENOTEMPTY,
    posix=posix88.ENOTEMPTY,
    solaris=solaris10.ENOTEMPTY,
    otherwise=posix88.ENOTEMPTY,
)

ENOTNAM: Final[int] = alias.or_platform(
    py_errno,
    "ENOTNAM",
    posix=posix88.ENOTNAM,
    otherwise=posix88.ENOTNAM,
)

ENOTRECOVERABLE: Final[int] = alias.or_platform(
    py_errno,
    "ENOTRECOVERABLE",
    darwin=darwin1.ENOTRECOVERABLE,
    freebsd=freebsd13.ENOTRECOVERABLE,
    nt=msvc22.ENOTRECOVERABLE,
    posix=posix88.ENOTRECOVERABLE,
    solaris=solaris10.ENOTRECOVERABLE,
    otherwise=posix88.ENOTRECOVERABLE,
)

ENOTSOCK: Final[int] = alias.or_platform(
    py_errno,
    "ENOTSOCK",
    darwin=darwin1.ENOTSOCK,
    freebsd=freebsd13.ENOTSOCK,
    nt=msvc22.ENOTSOCK,
    posix=posix88.ENOTSOCK,
    solaris=solaris10.ENOTSOCK,
    otherwise=posix88.ENOTSOCK,
)

ENOTSUP: Final[int] = alias.or_platform(
    py_errno,
    "ENOTSUP",
    darwin=darwin1.ENOTSUP,
    nt=msvc22.ENOTSUP,
    solaris=solaris10.ENOTSUP,
    otherwise=darwin1.ENOTSUP,
)

ENOTTY: Final[int] = alias.or_platform(
    py_errno,
    "ENOTTY",
    darwin=darwin1.ENOTTY,
    freebsd=freebsd13.ENOTTY,
    nt=msvc22.ENOTTY,
    posix=posix88.ENOTTY,
    solaris=solaris10.ENOTTY,
    otherwise=posix88.ENOTTY,
)

ENOTUNIQ: Final[int] = alias.or_platform(
    py_errno,
    "ENOTUNIQ",
    posix=posix88.ENOTUNIQ,
    solaris=solaris10.ENOTUNIQ,
    otherwise=posix88.ENOTUNIQ,
)

ENXIO: Final[int] = alias.or_platform(
    py_errno,
    "ENXIO",
    darwin=darwin1.ENXIO,
    freebsd=freebsd13.ENXIO,
    nt=msvc22.ENXIO,
    posix=posix88.ENXIO,
    solaris=solaris10.ENXIO,
    otherwise=posix88.ENXIO,
)

EOPNOTSUPP: Final[int] = alias.or_platform(
    py_errno,
    "EOPNOTSUPP",
    darwin=darwin1.EOPNOTSUPP,
    freebsd=freebsd13.EOPNOTSUPP,
    nt=msvc22.EOPNOTSUPP,
    posix=posix88.EOPNOTSUPP,
    solaris=solaris10.EOPNOTSUPP,
    otherwise=posix88.EOPNOTSUPP,
)

EOVERFLOW: Final[int] = alias.or_platform(
    py_errno,
    "EOVERFLOW",
    darwin=darwin1.EOVERFLOW,
    freebsd=freebsd13.EOVERFLOW,
    nt=msvc22.EOVERFLOW,
    posix=posix88.EOVERFLOW,
    solaris=solaris10.EOVERFLOW,
    otherwise=posix88.EOVERFLOW,
)

EOWNERDEAD: Final[int] = alias.or_platform(
    py_errno,
    "EOWNERDEAD",
    darwin=darwin1.EOWNERDEAD,
    freebsd=freebsd13.EOWNERDEAD,
    nt=msvc22.EOWNERDEAD,
    posix=posix88.EOWNERDEAD,
    solaris=solaris10.EOWNERDEAD,
    otherwise=posix88.EOWNERDEAD,
)

EPERM: Final[int] = alias.or_platform(
    py_errno,
    "EPERM",
    darwin=darwin1.EPERM,
    freebsd=freebsd13.EPERM,
    nt=msvc22.EPERM,
    posix=posix88.EPERM,
    solaris=solaris10.EPERM,
    otherwise=posix88.EPERM,
)

EPFNOSUPPORT: Final[int] = alias.or_platform(
    py_errno,
    "EPFNOSUPPORT",
    darwin=darwin1.EPFNOSUPPORT,
    freebsd=freebsd13.EPFNOSUPPORT,
    posix=posix88.EPFNOSUPPORT,
    solaris=solaris10.EPFNOSUPPORT,
    otherwise=posix88.EPFNOSUPPORT,
)

EPIPE: Final[int] = alias.or_platform(
    py_errno,
    "EPIPE",
    darwin=darwin1.EPIPE,
    freebsd=freebsd13.EPIPE,
    nt=msvc22.EPIPE,
    posix=posix88.EPIPE,
    solaris=solaris10.EPIPE,
    otherwise=posix88.EPIPE,
)

EPROCLIM: Final[int] = alias.or_platform(
    py_errno,
    "EPROCLIM",
    darwin=darwin1.EPROCLIM,
    freebsd=freebsd13.EPROCLIM,
    otherwise=darwin1.EPROCLIM,
)

EPROCUNAVAIL: Final[int] = alias.or_platform(
    py_errno,
    "EPROCUNAVAIL",
    darwin=darwin1.EPROCUNAVAIL,
    freebsd=freebsd13.EPROCUNAVAIL,
    otherwise=darwin1.EPROCUNAVAIL,
)

EPROGMISMATCH: Final[int] = alias.or_platform(
    py_errno,
    "EPROGMISMATCH",
    darwin=darwin1.EPROGMISMATCH,
    freebsd=freebsd13.EPROGMISMATCH,
    otherwise=darwin1.EPROGMISMATCH,
)

EPROGUNAVAIL: Final[int] = alias.or_platform(
    py_errno,
    "EPROGUNAVAIL",
    darwin=darwin1.EPROGUNAVAIL,
    freebsd=freebsd13.EPROGUNAVAIL,
    otherwise=darwin1.EPROGUNAVAIL,
)

EPROTO: Final[int] = alias.or_platform(
    py_errno,
    "EPROTO",
    darwin=darwin1.EPROTO,
    freebsd=freebsd13.EPROTO,
    nt=msvc22.EPROTO,
    posix=posix88.EPROTO,
    solaris=solaris10.EPROTO,
    otherwise=posix88.EPROTO,
)

EPROTONOSUPPORT: Final[int] = alias.or_platform(
    py_errno,
    "EPROTONOSUPPORT",
    darwin=darwin1.EPROTONOSUPPORT,
    freebsd=freebsd13.EPROTONOSUPPORT,
    nt=msvc22.EPROTONOSUPPORT,
    posix=posix88.EPROTONOSUPPORT,
    solaris=solaris10.EPROTONOSUPPORT,
    otherwise=posix88.EPROTONOSUPPORT,
)

EPROTOTYPE: Final[int] = alias.or_platform(
    py_errno,
    "EPROTOTYPE",
    darwin=darwin1.EPROTOTYPE,
    freebsd=freebsd13.EPROTOTYPE,
    nt=msvc22.EPROTOTYPE,
    posix=posix88.EPROTOTYPE,
    solaris=solaris10.EPROTOTYPE,
    otherwise=posix88.EPROTOTYPE,
)

EPWROFF: Final[int] = alias.or_platform(
    py_errno,
    "EPWROFF",
    darwin=darwin1.EPWROFF,
    otherwise=darwin1.EPWROFF,
)

ERANGE: Final[int] = alias.or_platform(
    py_errno,
    "ERANGE",
    darwin=darwin1.ERANGE,
    freebsd=freebsd13.ERANGE,
    nt=msvc22.ERANGE,
    posix=posix88.ERANGE,
    solaris=solaris10.ERANGE,
    otherwise=posix88.ERANGE,
)

EREMCHG: Final[int] = alias.or_platform(
    py_errno,
    "EREMCHG",
    posix=posix88.EREMCHG,
    solaris=solaris10.EREMCHG,
    otherwise=posix88.EREMCHG,
)

EREMOTE: Final[int] = alias.or_platform(
    py_errno,
    "EREMOTE",
    darwin=darwin1.EREMOTE,
    freebsd=freebsd13.EREMOTE,
    posix=posix88.EREMOTE,
    solaris=solaris10.EREMOTE,
    otherwise=posix88.EREMOTE,
)

EREMOTEIO: Final[int] = alias.or_platform(
    py_errno,
    "EREMOTEIO",
    posix=posix88.EREMOTEIO,
    otherwise=posix88.EREMOTEIO,
)

ERESTART: Final[int] = alias.or_platform(
    py_errno,
    "ERESTART",
    darwin=darwin1.ERESTART,
    posix=posix88.ERESTART,
    solaris=solaris10.ERESTART,
    otherwise=posix88.ERESTART,
)

ERFKILL: Final[int] = alias.or_platform(
    py_errno,
    "ERFKILL",
    posix=posix88.ERFKILL,
    otherwise=posix88.ERFKILL,
)

EROFS: Final[int] = alias.or_platform(
    py_errno,
    "EROFS",
    darwin=darwin1.EROFS,
    freebsd=freebsd13.EROFS,
    nt=msvc22.EROFS,
    posix=posix88.EROFS,
    solaris=solaris10.EROFS,
    otherwise=posix88.EROFS,
)

ERPCMISMATCH: Final[int] = alias.or_platform(
    py_errno,
    "ERPCMISMATCH",
    darwin=darwin1.ERPCMISMATCH,
    freebsd=freebsd13.ERPCMISMATCH,
    otherwise=darwin1.ERPCMISMATCH,
)

ESHLIBVERS: Final[int] = alias.or_platform(
    py_errno,
    "ESHLIBVERS",
    darwin=darwin1.ESHLIBVERS,
    otherwise=darwin1.ESHLIBVERS,
)

ESHUTDOWN: Final[int] = alias.or_platform(
    py_errno,
    "ESHUTDOWN",
    darwin=darwin1.ESHUTDOWN,
    freebsd=freebsd13.ESHUTDOWN,
    posix=posix88.ESHUTDOWN,
    solaris=solaris10.ESHUTDOWN,
    otherwise=posix88.ESHUTDOWN,
)

ESOCKTNOSUPPORT: Final[int] = alias.or_platform(
    py_errno,
    "ESOCKTNOSUPPORT",
    darwin=darwin1.ESOCKTNOSUPPORT,
    freebsd=freebsd13.ESOCKTNOSUPPORT,
    posix=posix88.ESOCKTNOSUPPORT,
    solaris=solaris10.ESOCKTNOSUPPORT,
    otherwise=posix88.ESOCKTNOSUPPORT,
)

ESPIPE: Final[int] = alias.or_platform(
    py_errno,
    "ESPIPE",
    darwin=darwin1.ESPIPE,
    freebsd=freebsd13.ESPIPE,
    nt=msvc22.ESPIPE,
    posix=posix88.ESPIPE,
    solaris=solaris10.ESPIPE,
    otherwise=posix88.ESPIPE,
)

ESRCH: Final[int] = alias.or_platform(
    py_errno,
    "ESRCH",
    darwin=darwin1.ESRCH,
    freebsd=freebsd13.ESRCH,
    nt=msvc22.ESRCH,
    posix=posix88.ESRCH,
    solaris=solaris10.ESRCH,
    otherwise=posix88.ESRCH,
)

ESRMNT: Final[int] = alias.or_platform(
    py_errno,
    "ESRMNT",
    posix=posix88.ESRMNT,
    solaris=solaris10.ESRMNT,
    otherwise=posix88.ESRMNT,
)

ESTALE: Final[int] = alias.or_platform(
    py_errno,
    "ESTALE",
    darwin=darwin1.ESTALE,
    freebsd=freebsd13.ESTALE,
    posix=posix88.ESTALE,
    solaris=solaris10.ESTALE,
    otherwise=posix88.ESTALE,
)

ESTRPIPE: Final[int] = alias.or_platform(
    py_errno,
    "ESTRPIPE",
    posix=posix88.ESTRPIPE,
    solaris=solaris10.ESTRPIPE,
    otherwise=posix88.ESTRPIPE,
)

ETIME: Final[int] = alias.or_platform(
    py_errno,
    "ETIME",
    darwin=darwin1.ETIME,
    nt=msvc22.ETIME,
    posix=posix88.ETIME,
    solaris=solaris10.ETIME,
    otherwise=posix88.ETIME,
)

ETIMEDOUT: Final[int] = alias.or_platform(
    py_errno,
    "ETIMEDOUT",
    darwin=darwin1.ETIMEDOUT,
    freebsd=freebsd13.ETIMEDOUT,
    nt=msvc22.ETIMEDOUT,
    posix=posix88.ETIMEDOUT,
    solaris=solaris10.ETIMEDOUT,
    otherwise=posix88.ETIMEDOUT,
)

ETOOMANYREFS: Final[int] = alias.or_platform(
    py_errno,
    "ETOOMANYREFS",
    darwin=darwin1.ETOOMANYREFS,
    freebsd=freebsd13.ETOOMANYREFS,
    posix=posix88.ETOOMANYREFS,
    solaris=solaris10.ETOOMANYREFS,
    otherwise=posix88.ETOOMANYREFS,
)

ETXTBSY: Final[int] = alias.or_platform(
    py_errno,
    "ETXTBSY",
    darwin=darwin1.ETXTBSY,
    freebsd=freebsd13.ETXTBSY,
    nt=msvc22.ETXTBSY,
    posix=posix88.ETXTBSY,
    solaris=solaris10.ETXTBSY,
    otherwise=posix88.ETXTBSY,
)

EUCLEAN: Final[int] = alias.or_platform(
    py_errno,
    "EUCLEAN",
    posix=posix88.EUCLEAN,
    otherwise=posix88.EUCLEAN,
)

EUNATCH: Final[int] = alias.or_platform(
    py_errno,
    "EUNATCH",
    posix=posix88.EUNATCH,
    solaris=solaris10.EUNATCH,
    otherwise=posix88.EUNATCH,
)

EUSERS: Final[int] = alias.or_platform(
    py_errno,
    "EUSERS",
    darwin=darwin1.EUSERS,
    freebsd=freebsd13.EUSERS,
    posix=posix88.EUSERS,
    solaris=solaris10.EUSERS,
    otherwise=posix88.EUSERS,
)

EWOULDBLOCK: Final[int] = alias.or_platform(
    py_errno,
    "EWOULDBLOCK",
    darwin=darwin1.EWOULDBLOCK,
    nt=msvc22.EWOULDBLOCK,
    posix=posix88.EWOULDBLOCK,
    solaris=solaris10.EWOULDBLOCK,
    otherwise=posix88.EWOULDBLOCK,
)

EXDEV: Final[int] = alias.or_platform(
    py_errno,
    "EXDEV",
    darwin=darwin1.EXDEV,
    freebsd=freebsd13.EXDEV,
    nt=msvc22.EXDEV,
    posix=posix88.EXDEV,
    solaris=solaris10.EXDEV,
    otherwise=posix88.EXDEV,
)

EXFULL: Final[int] = alias.or_platform(
    py_errno,
    "EXFULL",
    posix=posix88.EXFULL,
    solaris=solaris10.EXFULL,
    otherwise=posix88.EXFULL,
)


errorcode = {
    E2BIG: "E2BIG",
    EACCES: "EACCES",
    EADDRINUSE: "EADDRINUSE",
    EADDRNOTAVAIL: "EADDRNOTAVAIL",
    EADV: "EADV",
    EAFNOSUPPORT: "EAFNOSUPPORT",
    EAGAIN: "EAGAIN",
    EALREADY: "EALREADY",
    EAUTH: "EAUTH",
    EBADARCH: "EBADARCH",
    EBADE: "EBADE",
    EBADEXEC: "EBADEXEC",
    EBADF: "EBADF",
    EBADFD: "EBADFD",
    EBADMACHO: "EBADMACHO",
    EBADMSG: "EBADMSG",
    EBADR: "EBADR",
    EBADRPC: "EBADRPC",
    EBADRQC: "EBADRQC",
    EBADSLT: "EBADSLT",
    EBFONT: "EBFONT",
    EBUSY: "EBUSY",
    ECANCELED: "ECANCELED",
    ECHILD: "ECHILD",
    ECHRNG: "ECHRNG",
    ECOMM: "ECOMM",
    ECONNABORTED: "ECONNABORTED",
    ECONNREFUSED: "ECONNREFUSED",
    ECONNRESET: "ECONNRESET",
    EDEADLK: "EDEADLK",
    EDEADLOCK: "EDEADLOCK",
    EDESTADDRREQ: "EDESTADDRREQ",
    EDEVERR: "EDEVERR",
    EDOM: "EDOM",
    EDOTDOT: "EDOTDOT",
    EDQUOT: "EDQUOT",
    EEXIST: "EEXIST",
    EFAULT: "EFAULT",
    EFBIG: "EFBIG",
    EFTYPE: "EFTYPE",
    EHOSTDOWN: "EHOSTDOWN",
    EHOSTUNREACH: "EHOSTUNREACH",
    EIDRM: "EIDRM",
    EILSEQ: "EILSEQ",
    EINPROGRESS: "EINPROGRESS",
    EINTR: "EINTR",
    EINVAL: "EINVAL",
    EIO: "EIO",
    EISCONN: "EISCONN",
    EISDIR: "EISDIR",
    EISNAM: "EISNAM",
    EKEYEXPIRED: "EKEYEXPIRED",
    EKEYREJECTED: "EKEYREJECTED",
    EKEYREVOKED: "EKEYREVOKED",
    EL2HLT: "EL2HLT",
    EL2NSYNC: "EL2NSYNC",
    EL3HLT: "EL3HLT",
    EL3RST: "EL3RST",
    ELIBACC: "ELIBACC",
    ELIBBAD: "ELIBBAD",
    ELIBEXEC: "ELIBEXEC",
    ELIBMAX: "ELIBMAX",
    ELIBSCN: "ELIBSCN",
    ELNRNG: "ELNRNG",
    ELOCKUNMAPPED: "ELOCKUNMAPPED",
    ELOOP: "ELOOP",
    EMEDIUMTYPE: "EMEDIUMTYPE",
    EMFILE: "EMFILE",
    EMLINK: "EMLINK",
    EMSGSIZE: "EMSGSIZE",
    EMULTIHOP: "EMULTIHOP",
    ENAMETOOLONG: "ENAMETOOLONG",
    ENAVAIL: "ENAVAIL",
    ENEEDAUTH: "ENEEDAUTH",
    ENETDOWN: "ENETDOWN",
    ENETRESET: "ENETRESET",
    ENETUNREACH: "ENETUNREACH",
    ENFILE: "ENFILE",
    ENOANO: "ENOANO",
    ENOATTR: "ENOATTR",
    ENOBUFS: "ENOBUFS",
    ENOCSI: "ENOCSI",
    ENODATA: "ENODATA",
    ENODEV: "ENODEV",
    ENOENT: "ENOENT",
    ENOEXEC: "ENOEXEC",
    ENOKEY: "ENOKEY",
    ENOLCK: "ENOLCK",
    ENOLINK: "ENOLINK",
    ENOMEDIUM: "ENOMEDIUM",
    ENOMEM: "ENOMEM",
    ENOMSG: "ENOMSG",
    ENONET: "ENONET",
    ENOPKG: "ENOPKG",
    ENOPOLICY: "ENOPOLICY",
    ENOPROTOOPT: "ENOPROTOOPT",
    ENOSPC: "ENOSPC",
    ENOSR: "ENOSR",
    ENOSTR: "ENOSTR",
    ENOSYS: "ENOSYS",
    ENOTACTIVE: "ENOTACTIVE",
    ENOTBLK: "ENOTBLK",
    ENOTCONN: "ENOTCONN",
    ENOTDIR: "ENOTDIR",
    ENOTEMPTY: "ENOTEMPTY",
    ENOTNAM: "ENOTNAM",
    ENOTRECOVERABLE: "ENOTRECOVERABLE",
    ENOTSOCK: "ENOTSOCK",
    ENOTSUP: "ENOTSUP",
    ENOTTY: "ENOTTY",
    ENOTUNIQ: "ENOTUNIQ",
    ENXIO: "ENXIO",
    EOPNOTSUPP: "EOPNOTSUPP",
    EOVERFLOW: "EOVERFLOW",
    EOWNERDEAD: "EOWNERDEAD",
    EPERM: "EPERM",
    EPFNOSUPPORT: "EPFNOSUPPORT",
    EPIPE: "EPIPE",
    EPROCLIM: "EPROCLIM",
    EPROCUNAVAIL: "EPROCUNAVAIL",
    EPROGMISMATCH: "EPROGMISMATCH",
    EPROGUNAVAIL: "EPROGUNAVAIL",
    EPROTO: "EPROTO",
    EPROTONOSUPPORT: "EPROTONOSUPPORT",
    EPROTOTYPE: "EPROTOTYPE",
    EPWROFF: "EPWROFF",
    ERANGE: "ERANGE",
    EREMCHG: "EREMCHG",
    EREMOTE: "EREMOTE",
    EREMOTEIO: "EREMOTEIO",
    ERESTART: "ERESTART",
    ERFKILL: "ERFKILL",
    EROFS: "EROFS",
    ERPCMISMATCH: "ERPCMISMATCH",
    ESHLIBVERS: "ESHLIBVERS",
    ESHUTDOWN: "ESHUTDOWN",
    ESOCKTNOSUPPORT: "ESOCKTNOSUPPORT",
    ESPIPE: "ESPIPE",
    ESRCH: "ESRCH",
    ESRMNT: "ESRMNT",
    ESTALE: "ESTALE",
    ESTRPIPE: "ESTRPIPE",
    ETIME: "ETIME",
    ETIMEDOUT: "ETIMEDOUT",
    ETOOMANYREFS: "ETOOMANYREFS",
    ETXTBSY: "ETXTBSY",
    EUCLEAN: "EUCLEAN",
    EUNATCH: "EUNATCH",
    EUSERS: "EUSERS",
    EWOULDBLOCK: "EWOULDBLOCK",
    EXDEV: "EXDEV",
    EXFULL: "EXFULL",
}

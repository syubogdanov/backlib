from backlib.internal.stdlib.py313.errno.src.core import (
    E2BIG,
    EACCES,
    EADDRINUSE,
    EADDRNOTAVAIL,
    EADV,
    EAFNOSUPPORT,
    EAGAIN,
    EALREADY,
    EAUTH,
    EBADARCH,
    EBADE,
    EBADEXEC,
    EBADF,
    EBADFD,
    EBADMACHO,
    EBADMSG,
    EBADR,
    EBADRPC,
    EBADRQC,
    EBADSLT,
    EBFONT,
    EBUSY,
    ECANCELED,
    ECHILD,
    ECHRNG,
    ECOMM,
    ECONNABORTED,
    ECONNREFUSED,
    ECONNRESET,
    EDEADLK,
    EDEADLOCK,
    EDESTADDRREQ,
    EDEVERR,
    EDOM,
    EDOTDOT,
    EDQUOT,
    EEXIST,
    EFAULT,
    EFBIG,
    EFTYPE,
    EHOSTDOWN,
    EHOSTUNREACH,
    EIDRM,
    EILSEQ,
    EINPROGRESS,
    EINTR,
    EINVAL,
    EIO,
    EISCONN,
    EISDIR,
    EISNAM,
    EKEYEXPIRED,
    EKEYREJECTED,
    EKEYREVOKED,
    EL2HLT,
    EL2NSYNC,
    EL3HLT,
    EL3RST,
    ELIBACC,
    ELIBBAD,
    ELIBEXEC,
    ELIBMAX,
    ELIBSCN,
    ELNRNG,
    ELOCKUNMAPPED,
    ELOOP,
    EMEDIUMTYPE,
    EMFILE,
    EMLINK,
    EMSGSIZE,
    EMULTIHOP,
    ENAMETOOLONG,
    ENAVAIL,
    ENEEDAUTH,
    ENETDOWN,
    ENETRESET,
    ENETUNREACH,
    ENFILE,
    ENOANO,
    ENOATTR,
    ENOBUFS,
    ENOCSI,
    ENODATA,
    ENODEV,
    ENOENT,
    ENOEXEC,
    ENOKEY,
    ENOLCK,
    ENOLINK,
    ENOMEDIUM,
    ENOMEM,
    ENOMSG,
    ENONET,
    ENOPKG,
    ENOPOLICY,
    ENOPROTOOPT,
    ENOSPC,
    ENOSR,
    ENOSTR,
    ENOSYS,
    ENOTACTIVE,
    ENOTBLK,
    ENOTCAPABLE,
    ENOTCONN,
    ENOTDIR,
    ENOTEMPTY,
    ENOTNAM,
    ENOTRECOVERABLE,
    ENOTSOCK,
    ENOTSUP,
    ENOTTY,
    ENOTUNIQ,
    ENXIO,
    EOPNOTSUPP,
    EOVERFLOW,
    EOWNERDEAD,
    EPERM,
    EPFNOSUPPORT,
    EPIPE,
    EPROCLIM,
    EPROCUNAVAIL,
    EPROGMISMATCH,
    EPROGUNAVAIL,
    EPROTO,
    EPROTONOSUPPORT,
    EPROTOTYPE,
    EPWROFF,
    EQFULL,
    ERANGE,
    EREMCHG,
    EREMOTE,
    EREMOTEIO,
    ERESTART,
    ERFKILL,
    EROFS,
    ERPCMISMATCH,
    ESHLIBVERS,
    ESHUTDOWN,
    ESOCKTNOSUPPORT,
    ESPIPE,
    ESRCH,
    ESRMNT,
    ESTALE,
    ESTRPIPE,
    ETIME,
    ETIMEDOUT,
    ETOOMANYREFS,
    ETXTBSY,
    EUCLEAN,
    EUNATCH,
    EUSERS,
    EWOULDBLOCK,
    EXDEV,
    EXFULL,
    errorcode,
)


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
    "ENOTCAPABLE",
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
    "EQFULL",
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

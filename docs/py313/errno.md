# `errno` — Standard errno system symbols

> [!WARNING]
> The text, although it almost duplicates the official documentation, still differs from it. Be
> careful what you use!

This module makes available standard `errno` system symbols. The value of each symbol is the
corresponding integer value. The names and descriptions are borrowed from `linux/include/errno.h`,
which should be all-inclusive.

## Features

### \* errno.**errorcode**

Dictionary providing a mapping from the errno value to the string name in the underlying system. For
instance, `errno.errorcode[errno.EPERM]` maps to `'EPERM'`.

###

To translate a numeric error code to an error message, use [os.strerror()][os].

### \* errno.**EPERM**

Operation not permitted. This error is mapped to the exception [PermissionError][PermissionError].

### \* errno.**ENOENT**

No such file or directory. This error is mapped to the exception
[FileNotFoundError][FileNotFoundError].

### \* errno.**ESRCH**

No such process. This error is mapped to the exception [ProcessLookupError][ProcessLookupError].

### \* errno.**EINTR**

Interrupted system call. This error is mapped to the exception InterruptedError.

### \* errno.**EIO**

I/O error.

### \* errno.**ENXIO**

No such device or address.

### \* errno.**E2BIG**

Arg list too long.

### \* errno.**ENOEXEC**

Exec format error.

### \* errno.**EBADF**

Bad file number.

### \* errno.**ECHILD**

No child processes. This error is mapped to the exception [ChildProcessError][ChildProcessError].

### \* errno.**EAGAIN**

Try again. This error is mapped to the exception [BlockingIOError][BlockingIOError].

### \* errno.**ENOMEM**

Out of memory.

### \* errno.**EACCES**

Permission denied. This error is mapped to the exception [PermissionError][PermissionError].

### \* errno.**EFAULT**

Bad address.

### \* errno.**ENOTBLK**

Block device required.

### \* errno.**EBUSY**

Device or resource busy.

### \* errno.**EEXIST**

File exists. This error is mapped to the exception [FileExistsError][FileExistsError].

### \* errno.**EXDEV**

Cross-device link.

### \* errno.**ENODEV**

No such device.

### \* errno.**ENOTDIR**

Not a directory. This error is mapped to the exception [NotADirectoryError][NotADirectoryError].

### \* errno.**EISDIR**

Is a directory. This error is mapped to the exception [IsADirectoryError][IsADirectoryError].

### \* errno.**EINVAL**

Invalid argument.

### \* errno.**ENFILE**

File table overflow.

### \* errno.**EMFILE**

Too many open files.

### \* errno.**ENOTTY**

Not a typewriter.

### \* errno.**ETXTBSY**

Text file busy.

### \* errno.**EFBIG**

File too large.

### \* errno.**ENOSPC**

No space left on device.

### \* errno.**ESPIPE**

Illegal seek.

### \* errno.**EROFS**

Read-only file system.

### \* errno.**EMLINK**

Too many links.

### \* errno.**EPIPE**

Broken pipe. This error is mapped to the exception [BrokenPipeError][BrokenPipeError].

### \* errno.**EDOM**

Math argument out of domain of func.

### \* errno.**ERANGE**

Math result not representable.

### \* errno.**EDEADLK**

Resource deadlock would occur.

### \* errno.**ENAMETOOLONG**

File name too long.

### \* errno.**ENOLCK**

No record locks available.

### \* errno.**ENOSYS**

Function not implemented.

### \* errno.**ENOTEMPTY**

Directory not empty.

### \* errno.**ELOOP**

Too many symbolic links encountered.

### \* errno.**EWOULDBLOCK**

Operation would block. This error is mapped to the exception [BlockingIOError][BlockingIOError].

### \* errno.**ENOMSG**

No message of desired type.

### \* errno.**EIDRM**

Identifier removed.

### \* errno.**ECHRNG**

Channel number out of range.

### \* errno.**EL2NSYNC**

Level 2 not synchronized.

### \* errno.**EL3HLT**

Level 3 halted.

### \* errno.**EL3RST**

Level 3 reset.

### \* errno.**ELNRNG**

Link number out of range.

### \* errno.**EUNATCH**

Protocol driver not attached.

### \* errno.**ENOCSI**

No CSI structure available.

### \* errno.**EL2HLT**

Level 2 halted.

### \* errno.**EBADE**

Invalid exchange.

### \* errno.**EBADR**

Invalid request descriptor.

### \* errno.**EXFULL**

Exchange full.

### \* errno.**ENOANO**

No anode.

### \* errno.**EBADRQC**

Invalid request code.

### \* errno.**EBADSLT**

Invalid slot.

### \* errno.**EDEADLOCK**

File locking deadlock error.

### \* errno.**EBFONT**

Bad font file format.

### \* errno.**ENOSTR**

Device not a stream.

### \* errno.**ENODATA**

No data available.

### \* errno.**ETIME**

Timer expired.

### \* errno.**ENOSR**

Out of streams resources.

### \* errno.**ENONET**

Machine is not on the network.

### \* errno.**ENOPKG**

Package not installed.

### \* errno.**EREMOTE**

Object is remote.

### \* errno.**ENOLINK**

Link has been severed.

### \* errno.**EADV**

Advertise error.

### \* errno.**ESRMNT**

Srmount error.

### \* errno.**ECOMM**

Communication error on send.

### \* errno.**EPROTO**

Protocol error.

### \* errno.**EMULTIHOP**

Multihop attempted.

### \* errno.**EDOTDOT**

RFS specific error.

### \* errno.**EBADMSG**

Not a data message.

### \* errno.**EOVERFLOW**

Value too large for defined data type.

### \* errno.**ENOTUNIQ**

Name not unique on network.

### \* errno.**EBADFD**

File descriptor in bad state.

### \* errno.**EREMCHG**

Remote address changed.

### \* errno.**ELIBACC**

Can not access a needed shared library.

### \* errno.**ELIBBAD**

Accessing a corrupted shared library.

### \* errno.**ELIBSCN**

.lib section in a.out corrupted.

### \* errno.**ELIBMAX**

Attempting to link in too many shared libraries.

### \* errno.**ELIBEXEC**

Cannot exec a shared library directly.

### \* errno.**EILSEQ**

Illegal byte sequence.

### \* errno.**ERESTART**

Interrupted system call should be restarted.

### \* errno.**ESTRPIPE**

Streams pipe error.

### \* errno.**EUSERS**

Too many users.

### \* errno.**ENOTSOCK**

Socket operation on non-socket.

### \* errno.**EDESTADDRREQ**

Destination address required.

### \* errno.**EMSGSIZE**

Message too long.

### \* errno.**EPROTOTYPE**

Protocol wrong type for socket.

### \* errno.**ENOPROTOOPT**

Protocol not available.

### \* errno.**EPROTONOSUPPORT**

Protocol not supported.

### \* errno.**ESOCKTNOSUPPORT**

Socket type not supported.

### \* errno.**EOPNOTSUPP**

Operation not supported on transport endpoint.

### \* errno.**ENOTSUP**

Operation not supported.

### \* errno.**EPFNOSUPPORT**.

Protocol family not supported.

### \* errno.**EAFNOSUPPORT**

Address family not supported by protocol.

### \* errno.**EADDRINUSE**

Address already in use.

### \* errno.**EADDRNOTAVAIL**

Cannot assign requested address.

### \* errno.**ENETDOWN**

Network is down.

### \* errno.**ENETUNREACH**

Network is unreachable.

### \* errno.**ENETRESET**

Network dropped connection because of reset.

### \* errno.**ECONNABORTED**

Software caused connection abort. This error is mapped to the exception
[ConnectionAbortedError][ConnectionAbortedError].

### \* errno.**ECONNRESET**

Connection reset by peer. This error is mapped to the exception
[ConnectionResetError][ConnectionResetError].

### \* errno.**ENOBUFS**

No buffer space available.

### \* errno.**EISCONN**

Transport endpoint is already connected.

### \* errno.**ENOTCONN**

Transport endpoint is not connected.

### \* errno.**ESHUTDOWN**

Cannot send after transport endpoint shutdown. This error is mapped to the exception
[BrokenPipeError][BrokenPipeError].

### \* errno.**ETOOMANYREFS**

Too many references: cannot splice.

### \* errno.**ETIMEDOUT**

Connection timed out. This error is mapped to the exception [TimeoutError][TimeoutError].

### \* errno.**ECONNREFUSED**

Connection refused. This error is mapped to the exception
[ConnectionRefusedError][ConnectionRefusedError].

### \* errno.**EHOSTDOWN**

Host is down.

### \* errno.**EHOSTUNREACH**

No route to host.

### \* errno.**EALREADY**

Operation already in progress. This error is mapped to the exception
[BlockingIOError][BlockingIOError].

### \* errno.**EINPROGRESS**

Operation now in progress. This error is mapped to the exception [BlockingIOError][BlockingIOError].

### \* errno.**ESTALE**

Stale NFS file handle.

### \* errno.**EUCLEAN**

Structure needs cleaning.

### \* errno.**ENOTNAM**

Not a XENIX named type file.

### \* errno.**ENAVAIL**

No XENIX semaphores available.

### \* errno.**EISNAM**

Is a named type file.

### \* errno.**EREMOTEIO**

Remote I/O error.

### \* errno.**EDQUOT**

Quota exceeded.

### \* errno.**EQFULL**

Interface output queue is full.

### \* errno.**ENOMEDIUM**

No medium found.

### \* errno.**EMEDIUMTYPE**

Wrong medium type.

### \* errno.**ENOKEY**

Required key not available.

### \* errno.**EKEYEXPIRED**

Key has expired.

### \* errno.**EKEYREVOKED**

Key has been revoked.

### \* errno.**EKEYREJECTED**

Key was rejected by service.

### \* errno.**ERFKILL**

Operation not possible due to RF-kill.

### \* errno.**ELOCKUNMAPPED**

Locked lock was unmapped.

### \* errno.**ENOTACTIVE**

Facility is not active.

### \* errno.**EAUTH**

Authentication error.

### \* errno.**EBADARCH**

Bad CPU type in executable.

### \* errno.**EBADEXEC**

Bad executable (or shared library).

### \* errno.**EBADMACHO**

Malformed Mach-o file.

### \* errno.**EDEVERR**

Device error.

### \* errno.**EFTYPE**

Inappropriate file type or format.

### \* errno.**ENEEDAUTH**

Need authenticator.

### \* errno.**ENOATTR**

Attribute not found.

### \* errno.**ENOPOLICY**

Policy not found.

### \* errno.**EPROCLIM**

Too many processes.

### \* errno.**EPROCUNAVAIL**

Bad procedure for program.

### \* errno.**EPROGMISMATCH**

Program version wrong.

### \* errno.**EPROGUNAVAIL**

RPC prog. not avail.

### \* errno.**EPWROFF**

Device power is off.

### \* errno.**EBADRPC**

RPC struct is bad.

### \* errno.**ERPCMISMATCH**

RPC version wrong.

### \* errno.**ESHLIBVERS**

Shared library version mismatch.

### \* errno.**ENOTCAPABLE**

Capabilities insufficient. This error is mapped to the exception [PermissionError][PermissionError].

### \* errno.**ECANCELED**

Operation canceled.

### \* errno.**EOWNERDEAD**

Owner died.

### \* errno.**ENOTRECOVERABLE**

State not recoverable.

<!-- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- -->

[BlockingIOError]: https://docs.python.org/3.13/library/exceptions.html#BlockingIOError
[BrokenPipeError]: https://docs.python.org/3.13/library/exceptions.html#BrokenPipeError
[ChildProcessError]: https://docs.python.org/3.13/library/exceptions.html#ChildProcessError
[ConnectionAbortedError]: https://docs.python.org/3.13/library/exceptions.html#ConnectionAbortedError
[ConnectionRefusedError]: https://docs.python.org/3.13/library/exceptions.html#ConnectionRefusedError
[ConnectionResetError]: https://docs.python.org/3.13/library/exceptions.html#ConnectionResetError
[FileExistsError]: https://docs.python.org/3.13/library/exceptions.html#FileExistsError
[FileNotFoundError]: https://docs.python.org/3.13/library/exceptions.html#FileNotFoundError
[InterruptedError]: https://docs.python.org/3.13/library/exceptions.html#InterruptedError
[IsADirectoryError]: https://docs.python.org/3.13/library/exceptions.html#IsADirectoryError
[NotADirectoryError]: https://docs.python.org/3.13/library/exceptions.html#NotADirectoryError
[PermissionError]: https://docs.python.org/3.13/library/exceptions.html#PermissionError
[ProcessLookupError]: https://docs.python.org/3.13/library/exceptions.html#ProcessLookupError
[TimeoutError]: https://docs.python.org/3.13/library/exceptions.html#TimeoutError

[os]: ./os.md

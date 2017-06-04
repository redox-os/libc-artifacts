#!/usr/bin/env bash
ROOT="$(cd `dirname $0` && pwd)"

if [ "`uname`" == "Linux" ]
then
	compiler="gcc"
elif [ "`uname`" == "Darwin" ]
then
	compiler="x86_64-elf-gcc"
elif [ "`uname`" == "FreeBSD" ]
then
	compiler="gcc"
else
	echo "$0: `uname` not supported"
	exit 1
fi

C_INCLUDE_PATH="$ROOT/usr/include" \
LIBRARY_PATH="$ROOT/usr/lib" \
"$compiler" \
-static -nostartfiles -nostdlib -nodefaultlibs -ffreestanding \
--sysroot "$ROOT" \
-undef -imacros "$ROOT/define.h" \
"$@" \
-Xlinker "$ROOT/usr/lib/crt0.o" \
-Xlinker "$ROOT/usr/lib/libm.a" \
-Xlinker "$ROOT/usr/lib/libgcc.a" \
-Xlinker "$ROOT/usr/lib/libc.a" \
-specs=$ROOT/gcc.spec

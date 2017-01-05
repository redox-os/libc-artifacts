#!/bin/bash
ROOT="$(cd `dirname $0` && pwd)"

if [ "`uname`" == "Linux" ]
then
	compiler="gcc"
elif [ "`uname`" == "Darwin" ]
then
	compiler="x86_64-elf-gcc"
else
	echo "$0: `uname` not supported"
	exit 1
fi

C_INCLUDE_PATH="$ROOT/usr/include" \
LIBRARY_PATH="$ROOT/usr/lib" \
"$compiler" \
-static -nostartfiles -nostdlib -nodefaultlibs \
--sysroot "$ROOT" \
-undef -imacros "$ROOT/define.h" \
"$@" \
"$ROOT/usr/lib/crt0.o" \
"$ROOT/usr/lib/libm.a" \
"$ROOT/usr/lib/libgcc.a" \
"$ROOT/usr/lib/libc.a"

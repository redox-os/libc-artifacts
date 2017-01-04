#!/bin/bash
ROOT="$(cd `dirname $0` && pwd)"
if [ "`uname`" == "Linux" ]
then
	C_INCLUDE_PATH="$ROOT/usr/include" \
	LIBRARY_PATH="$ROOT/usr/lib" \
	gcc -v \
	-static -nostartfiles -nostdlib -nodefaultlibs \
	-undef -imacros "$ROOT/define.h" \
	"$@" \
	"$ROOT/usr/lib/crt0.o" \
	"$ROOT/usr/lib/libm.a" \
	"$ROOT/usr/lib/libgcc.a" \
	"$ROOT/usr/lib/libc.a"
elif [ "`uname`" == "Darwin" ]
then
	C_INCLUDE_PATH="$ROOT/usr/include" \
	LIBRARY_PATH="$ROOT/usr/lib" \
	x86_64-elf-gcc -v \
	-static -nostartfiles -nostdlib -nodefaultlibs \
	-undef -imacros "$ROOT/define.h" \
	"$@" \
	"$ROOT/usr/lib/crt0.o" \
	"$ROOT/usr/lib/libm.a" \
	"$ROOT/usr/lib/libgcc.a" \
	"$ROOT/usr/lib/libc.a"
else
	echo "$0: `uname` not supported"
	exit 1
fi

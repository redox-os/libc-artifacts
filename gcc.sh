#!/bin/bash
ROOT="$(cd `dirname $0` && pwd)"
if [ "`uname`" == "Linux" ]
then
	C_INCLUDE_PATH="$ROOT/usr/include" \
	LIBRARY_PATH="$ROOT/usr/lib" \
	gcc -v \
	-static -nostartfiles -nostdlib -nodefaultlibs \
	-undef -imacros "$ROOT/define.h" \
	"$ROOT/usr/lib/crt0.o" \
	-fno-stack-protector -U_FORTIFY_SOURCE \
	"$@"
else
	echo "$0: `uname` not supported"
	exit 1
fi

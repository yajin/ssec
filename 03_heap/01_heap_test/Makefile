.PHONY: all notcache tcache

all: compile notcache tcache

compile:
	gcc test.c -g -o test

notcache:
	cp test test.notcache
	patchelf --set-interpreter ./notcache/ld-2.27.so test.notcache
	patchelf --replace-needed libc.so.6 ./notcache/libc.so.6 test.notcache

tcache:
	cp test test.tcache
	patchelf --set-interpreter ./tcache/ld-2.27.so test.tcache
	patchelf --replace-needed libc.so.6 ./tcache/libc.so.6 test.tcache

.PHONY:clean

clean:
	rm -f test test.notcache test.tcache


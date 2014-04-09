
# Also see "include/polarssl/config.h"

#CFLAGS	= -I../include -D_FILE_OFFSET_BITS=64 -Wall -Wdeclaration-after-statement
#OFLAGS	= -O

CFLAGS  = -I../include -Wall -W -Wdeclaration-after-statement
OFLAGS  = -O2 

ifeq ("$(TARGET)", "linux-x86")
        include ../../Makefile-include.linux-x86
endif
ifeq ("$(TARGET)", "linux-x86_64")
        include ../../Makefile-include.linux-x86_64
endif
ifeq ("$(TARGET)", "mikrotik-mips")
        include ../../Makefile-include.mikrotik-mips
endif
ifeq ("$(TARGET)", "mikrotik-mipsel")
        include ../../Makefile-include.mikrotik-mipsel
endif
ifeq ("$(TARGET)", "mikrotik-x86")
        include ../../Makefile-include.mikrotik-x86
endif
ifeq ("$(TARGET)", "mikrotik-ppc")
        include ../../Makefile-include.mikrotik-ppc
endif
ifeq ("$(TARGET)", "arm")
        include ../../Makefile-include.arm
endif
ifeq ("$(TARGET)", "solaris-sparc")
        include ../../Makefile-include.solaris-sparc
endif
ifeq ("$(TARGET)", "solaris-x86")
        include ../../Makefile-include.solaris-x86
endif

ifdef DEBUG
CFLAGS += -g3 
endif
# MicroBlaze specific options:
# CFLAGS += -mno-xl-soft-mul -mxl-barrel-shift

# To compile on Plan9:
# CFLAGS += -D_BSD_EXTENSION

# To compile as a shared library:
# CFLAGS += -fPIC

DLEXT=so
# OSX shared library extension:
# DLEXT=dylib

OBJS=	aes.o		arc4.o		base64.o	\
	bignum.o	certs.o		debug.o		\
	des.o		dhm.o		havege.o	\
	md2.o		md4.o		md5.o		\
	net.o		padlock.o	rsa.o		\
	sha1.o		sha2.o		sha4.o		\
	ssl_cli.o	ssl_srv.o	ssl_tls.o	\
	timing.o	x509parse.o	xtea.o		\
	camellia.o  version.o

.SILENT:

all: static

static: libpolarssl.a

shared: libpolarssl.$(DLEXT)

libpolarssl.a: $(OBJS)
	echo "  AR    $@"
	ar r $@ $(OBJS)
	echo "  RL    $@"
	ranlib $@

libpolarssl.so: libpolarssl.a
	echo "  LD    $@"
	$(CC) -shared -Wl,-soname,$@ -o $@ $(OBJS)

libpolarssl.dylib: libpolarssl.a
	echo "  LD    $@"
	$(CC) -dynamiclib -o $@ $(OBJS)

.c.o:
	echo "  CC    $<"
	$(CC) $(CFLAGS) $(OFLAGS) -c $<

clean:
	rm -f *.o libpolarssl.*


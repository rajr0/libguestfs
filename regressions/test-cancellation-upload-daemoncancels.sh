#!/bin/sh -
# libguestfs
# Copyright (C) 2009 Red Hat Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

# Test upload where the daemon cancels.
#
# This is pretty easy - we just upload a too-large source file.

set -e

rm -f test.img

../fish/guestfish <<'EOF'
alloc test.img 10M
run

sfdiskM /dev/sda ,
mkfs ext2 /dev/sda1
mount /dev/sda1 /

# Upload image, daemon should cancel because the image is too large
# to upload into itself.
echo "Expect: write: /test: No space left on device"
-upload test.img /test

ping-daemon
EOF

rm -f test.img

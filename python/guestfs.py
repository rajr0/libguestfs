# libguestfs generated file
# WARNING: THIS FILE IS GENERATED BY 'src/generator.ml'.
# ANY CHANGES YOU MAKE TO THIS FILE WILL BE LOST.
#
# Copyright (C) 2009 Red Hat Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

u"""Python bindings for libguestfs

import guestfs
g = guestfs.GuestFS ()
g.add_drive ("guest.img")
g.launch ()
g.wait_ready ()
parts = g.list_partitions ()

The guestfs module provides a Python binding to the libguestfs API
for examining and modifying virtual machine disk images.

Amongst the things this is good for: making batch configuration
changes to guests, getting disk used/free statistics (see also:
virt-df), migrating between virtualization systems (see also:
virt-p2v), performing partial backups, performing partial guest
clones, cloning guests and changing registry/UUID/hostname info, and
much else besides.

Libguestfs uses Linux kernel and qemu code, and can access any type of
guest filesystem that Linux and qemu can, including but not limited
to: ext2/3/4, btrfs, FAT and NTFS, LVM, many different disk partition
schemes, qcow, qcow2, vmdk.

Libguestfs provides ways to enumerate guest storage (eg. partitions,
LVs, what filesystem is in each LV, etc.).  It can also run commands
in the context of the guest.  Also you can access filesystems over FTP.

Errors which happen while using the API are turned into Python
RuntimeError exceptions.

To create a guestfs handle you usually have to perform the following
sequence of calls:

# Create the handle, call add_drive at least once, and possibly
# several times if the guest has multiple block devices:
g = guestfs.GuestFS ()
g.add_drive ("guest.img")

# Launch the qemu subprocess and wait for it to become ready:
g.launch ()
g.wait_ready ()

# Now you can issue commands, for example:
logvols = g.lvs ()

"""

import libguestfsmod

class GuestFS:
    """Instances of this class are libguestfs API handles."""

    def __init__ (self):
        """Create a new libguestfs handle."""
        self._o = libguestfsmod.create ()

    def __del__ (self):
        libguestfsmod.close (self._o)

    def launch (self):
        u"""Internally libguestfs is implemented by running a
        virtual machine using qemu(1).
        
        You should call this after configuring the handle (eg.
        adding drives) but before performing any actions.
        """
        return libguestfsmod.launch (self._o)

    def wait_ready (self):
        u"""Internally libguestfs is implemented by running a
        virtual machine using qemu(1).
        
        You should call this after "g.launch" to wait for the
        launch to complete.
        """
        return libguestfsmod.wait_ready (self._o)

    def kill_subprocess (self):
        u"""This kills the qemu subprocess. You should never need to
        call this.
        """
        return libguestfsmod.kill_subprocess (self._o)

    def add_drive (self, filename):
        u"""This function adds a virtual machine disk image
        "filename" to the guest. The first time you call this
        function, the disk appears as IDE disk 0 ("/dev/sda") in
        the guest, the second time as "/dev/sdb", and so on.
        
        You don't necessarily need to be root when using
        libguestfs. However you obviously do need sufficient
        permissions to access the filename for whatever
        operations you want to perform (ie. read access if you
        just want to read the image or write access if you want
        to modify the image).
        
        This is equivalent to the qemu parameter "-drive
        file=filename".
        """
        return libguestfsmod.add_drive (self._o, filename)

    def add_cdrom (self, filename):
        u"""This function adds a virtual CD-ROM disk image to the
        guest.
        
        This is equivalent to the qemu parameter "-cdrom
        filename".
        """
        return libguestfsmod.add_cdrom (self._o, filename)

    def config (self, qemuparam, qemuvalue):
        u"""This can be used to add arbitrary qemu command line
        parameters of the form "-param value". Actually it's not
        quite arbitrary - we prevent you from setting some
        parameters which would interfere with parameters that we
        use.
        
        The first character of "param" string must be a "-"
        (dash).
        
        "value" can be NULL.
        """
        return libguestfsmod.config (self._o, qemuparam, qemuvalue)

    def set_qemu (self, qemu):
        u"""Set the qemu binary that we will use.
        
        The default is chosen when the library was compiled by
        the configure script.
        
        You can also override this by setting the
        "LIBGUESTFS_QEMU" environment variable.
        
        The string "qemu" is stashed in the libguestfs handle,
        so the caller must make sure it remains valid for the
        lifetime of the handle.
        
        Setting "qemu" to "NULL" restores the default qemu
        binary.
        """
        return libguestfsmod.set_qemu (self._o, qemu)

    def get_qemu (self):
        u"""Return the current qemu binary.
        
        This is always non-NULL. If it wasn't set already, then
        this will return the default qemu binary name.
        """
        return libguestfsmod.get_qemu (self._o)

    def set_path (self, path):
        u"""Set the path that libguestfs searches for kernel and
        initrd.img.
        
        The default is "$libdir/guestfs" unless overridden by
        setting "LIBGUESTFS_PATH" environment variable.
        
        The string "path" is stashed in the libguestfs handle,
        so the caller must make sure it remains valid for the
        lifetime of the handle.
        
        Setting "path" to "NULL" restores the default path.
        """
        return libguestfsmod.set_path (self._o, path)

    def get_path (self):
        u"""Return the current search path.
        
        This is always non-NULL. If it wasn't set already, then
        this will return the default path.
        """
        return libguestfsmod.get_path (self._o)

    def set_autosync (self, autosync):
        u"""If "autosync" is true, this enables autosync. Libguestfs
        will make a best effort attempt to run "g.sync" when the
        handle is closed (also if the program exits without
        closing handles).
        """
        return libguestfsmod.set_autosync (self._o, autosync)

    def get_autosync (self):
        u"""Get the autosync flag.
        """
        return libguestfsmod.get_autosync (self._o)

    def set_verbose (self, verbose):
        u"""If "verbose" is true, this turns on verbose messages (to
        "stderr").
        
        Verbose messages are disabled unless the environment
        variable "LIBGUESTFS_DEBUG" is defined and set to 1.
        """
        return libguestfsmod.set_verbose (self._o, verbose)

    def get_verbose (self):
        u"""This returns the verbose messages flag.
        """
        return libguestfsmod.get_verbose (self._o)

    def is_ready (self):
        u"""This returns true iff this handle is ready to accept
        commands (in the "READY" state).
        
        For more information on states, see guestfs(3).
        """
        return libguestfsmod.is_ready (self._o)

    def is_config (self):
        u"""This returns true iff this handle is being configured
        (in the "CONFIG" state).
        
        For more information on states, see guestfs(3).
        """
        return libguestfsmod.is_config (self._o)

    def is_launching (self):
        u"""This returns true iff this handle is launching the
        subprocess (in the "LAUNCHING" state).
        
        For more information on states, see guestfs(3).
        """
        return libguestfsmod.is_launching (self._o)

    def is_busy (self):
        u"""This returns true iff this handle is busy processing a
        command (in the "BUSY" state).
        
        For more information on states, see guestfs(3).
        """
        return libguestfsmod.is_busy (self._o)

    def get_state (self):
        u"""This returns the current state as an opaque integer.
        This is only useful for printing debug and internal
        error messages.
        
        For more information on states, see guestfs(3).
        """
        return libguestfsmod.get_state (self._o)

    def set_busy (self):
        u"""This sets the state to "BUSY". This is only used when
        implementing actions using the low-level API.
        
        For more information on states, see guestfs(3).
        """
        return libguestfsmod.set_busy (self._o)

    def set_ready (self):
        u"""This sets the state to "READY". This is only used when
        implementing actions using the low-level API.
        
        For more information on states, see guestfs(3).
        """
        return libguestfsmod.set_ready (self._o)

    def mount (self, device, mountpoint):
        u"""Mount a guest disk at a position in the filesystem.
        Block devices are named "/dev/sda", "/dev/sdb" and so
        on, as they were added to the guest. If those block
        devices contain partitions, they will have the usual
        names (eg. "/dev/sda1"). Also LVM "/dev/VG/LV"-style
        names can be used.
        
        The rules are the same as for mount(2): A filesystem
        must first be mounted on "/" before others can be
        mounted. Other filesystems can only be mounted on
        directories which already exist.
        
        The mounted filesystem is writable, if we have
        sufficient permissions on the underlying device.
        
        The filesystem options "sync" and "noatime" are set with
        this call, in order to improve reliability.
        """
        return libguestfsmod.mount (self._o, device, mountpoint)

    def sync (self):
        u"""This syncs the disk, so that any writes are flushed
        through to the underlying disk image.
        
        You should always call this if you have modified a disk
        image, before closing the handle.
        """
        return libguestfsmod.sync (self._o)

    def touch (self, path):
        u"""Touch acts like the touch(1) command. It can be used to
        update the timestamps on a file, or, if the file does
        not exist, to create a new zero-length file.
        """
        return libguestfsmod.touch (self._o, path)

    def cat (self, path):
        u"""Return the contents of the file named "path".
        
        Note that this function cannot correctly handle binary
        files (specifically, files containing "\\0" character
        which is treated as end of string). For those you need
        to use the "g.download" function which has a more
        complex interface.
        
        Because of the message protocol, there is a transfer
        limit of somewhere between 2MB and 4MB. To transfer
        large files you should use FTP.
        """
        return libguestfsmod.cat (self._o, path)

    def ll (self, directory):
        u"""List the files in "directory" (relative to the root
        directory, there is no cwd) in the format of 'ls -la'.
        
        This command is mostly useful for interactive sessions.
        It is *not* intended that you try to parse the output
        string.
        """
        return libguestfsmod.ll (self._o, directory)

    def ls (self, directory):
        u"""List the files in "directory" (relative to the root
        directory, there is no cwd). The '.' and '..' entries
        are not returned, but hidden files are shown.
        
        This command is mostly useful for interactive sessions.
        Programs should probably use "g.readdir" instead.
        
        This function returns a list of strings.
        """
        return libguestfsmod.ls (self._o, directory)

    def list_devices (self):
        u"""List all the block devices.
        
        The full block device names are returned, eg. "/dev/sda"
        
        This function returns a list of strings.
        """
        return libguestfsmod.list_devices (self._o)

    def list_partitions (self):
        u"""List all the partitions detected on all block devices.
        
        The full partition device names are returned, eg.
        "/dev/sda1"
        
        This does not return logical volumes. For that you will
        need to call "g.lvs".
        
        This function returns a list of strings.
        """
        return libguestfsmod.list_partitions (self._o)

    def pvs (self):
        u"""List all the physical volumes detected. This is the
        equivalent of the pvs(8) command.
        
        This returns a list of just the device names that
        contain PVs (eg. "/dev/sda2").
        
        See also "g.pvs_full".
        
        This function returns a list of strings.
        """
        return libguestfsmod.pvs (self._o)

    def vgs (self):
        u"""List all the volumes groups detected. This is the
        equivalent of the vgs(8) command.
        
        This returns a list of just the volume group names that
        were detected (eg. "VolGroup00").
        
        See also "g.vgs_full".
        
        This function returns a list of strings.
        """
        return libguestfsmod.vgs (self._o)

    def lvs (self):
        u"""List all the logical volumes detected. This is the
        equivalent of the lvs(8) command.
        
        This returns a list of the logical volume device names
        (eg. "/dev/VolGroup00/LogVol00").
        
        See also "g.lvs_full".
        
        This function returns a list of strings.
        """
        return libguestfsmod.lvs (self._o)

    def pvs_full (self):
        u"""List all the physical volumes detected. This is the
        equivalent of the pvs(8) command. The "full" version
        includes all fields.
        
        This function returns a list of PVs. Each PV is
        represented as a dictionary.
        """
        return libguestfsmod.pvs_full (self._o)

    def vgs_full (self):
        u"""List all the volumes groups detected. This is the
        equivalent of the vgs(8) command. The "full" version
        includes all fields.
        
        This function returns a list of VGs. Each VG is
        represented as a dictionary.
        """
        return libguestfsmod.vgs_full (self._o)

    def lvs_full (self):
        u"""List all the logical volumes detected. This is the
        equivalent of the lvs(8) command. The "full" version
        includes all fields.
        
        This function returns a list of LVs. Each LV is
        represented as a dictionary.
        """
        return libguestfsmod.lvs_full (self._o)

    def read_lines (self, path):
        u"""Return the contents of the file named "path".
        
        The file contents are returned as a list of lines.
        Trailing "LF" and "CRLF" character sequences are *not*
        returned.
        
        Note that this function cannot correctly handle binary
        files (specifically, files containing "\\0" character
        which is treated as end of line). For those you need to
        use the "g.read_file" function which has a more complex
        interface.
        
        This function returns a list of strings.
        """
        return libguestfsmod.read_lines (self._o, path)

    def aug_init (self, root, flags):
        u"""Create a new Augeas handle for editing configuration
        files. If there was any previous Augeas handle
        associated with this guestfs session, then it is closed.
        
        You must call this before using any other "g.aug_*"
        commands.
        
        "root" is the filesystem root. "root" must not be NULL,
        use "/" instead.
        
        The flags are the same as the flags defined in
        <augeas.h>, the logical *or* of the following integers:
        
        "AUG_SAVE_BACKUP" = 1
        Keep the original file with a ".augsave" extension.
        
        "AUG_SAVE_NEWFILE" = 2
        Save changes into a file with extension ".augnew",
        and do not overwrite original. Overrides
        "AUG_SAVE_BACKUP".
        
        "AUG_TYPE_CHECK" = 4
        Typecheck lenses (can be expensive).
        
        "AUG_NO_STDINC" = 8
        Do not use standard load path for modules.
        
        "AUG_SAVE_NOOP" = 16
        Make save a no-op, just record what would have been
        changed.
        
        "AUG_NO_LOAD" = 32
        Do not load the tree in "g.aug_init".
        
        To close the handle, you can call "g.aug_close".
        
        To find out more about Augeas, see <http://augeas.net/>.
        """
        return libguestfsmod.aug_init (self._o, root, flags)

    def aug_close (self):
        u"""Close the current Augeas handle and free up any
        resources used by it. After calling this, you have to
        call "g.aug_init" again before you can use any other
        Augeas functions.
        """
        return libguestfsmod.aug_close (self._o)

    def aug_defvar (self, name, expr):
        u"""Defines an Augeas variable "name" whose value is the
        result of evaluating "expr". If "expr" is NULL, then
        "name" is undefined.
        
        On success this returns the number of nodes in "expr",
        or 0 if "expr" evaluates to something which is not a
        nodeset.
        """
        return libguestfsmod.aug_defvar (self._o, name, expr)

    def aug_defnode (self, name, expr, val):
        u"""Defines a variable "name" whose value is the result of
        evaluating "expr".
        
        If "expr" evaluates to an empty nodeset, a node is
        created, equivalent to calling "g.aug_set" "expr",
        "value". "name" will be the nodeset containing that
        single node.
        
        On success this returns a pair containing the number of
        nodes in the nodeset, and a boolean flag if a node was
        created.
        
        This function returns a tuple (int, bool).
        """
        return libguestfsmod.aug_defnode (self._o, name, expr, val)

    def aug_get (self, path):
        u"""Look up the value associated with "path". If "path"
        matches exactly one node, the "value" is returned.
        """
        return libguestfsmod.aug_get (self._o, path)

    def aug_set (self, path, val):
        u"""Set the value associated with "path" to "value".
        """
        return libguestfsmod.aug_set (self._o, path, val)

    def aug_insert (self, path, label, before):
        u"""Create a new sibling "label" for "path", inserting it
        into the tree before or after "path" (depending on the
        boolean flag "before").
        
        "path" must match exactly one existing node in the tree,
        and "label" must be a label, ie. not contain "/", "*" or
        end with a bracketed index "[N]".
        """
        return libguestfsmod.aug_insert (self._o, path, label, before)

    def aug_rm (self, path):
        u"""Remove "path" and all of its children.
        
        On success this returns the number of entries which were
        removed.
        """
        return libguestfsmod.aug_rm (self._o, path)

    def aug_mv (self, src, dest):
        u"""Move the node "src" to "dest". "src" must match exactly
        one node. "dest" is overwritten if it exists.
        """
        return libguestfsmod.aug_mv (self._o, src, dest)

    def aug_match (self, path):
        u"""Returns a list of paths which match the path expression
        "path". The returned paths are sufficiently qualified so
        that they match exactly one node in the current tree.
        
        This function returns a list of strings.
        """
        return libguestfsmod.aug_match (self._o, path)

    def aug_save (self):
        u"""This writes all pending changes to disk.
        
        The flags which were passed to "g.aug_init" affect
        exactly how files are saved.
        """
        return libguestfsmod.aug_save (self._o)

    def aug_load (self):
        u"""Load files into the tree.
        
        See "aug_load" in the Augeas documentation for the full
        gory details.
        """
        return libguestfsmod.aug_load (self._o)

    def aug_ls (self, path):
        u"""This is just a shortcut for listing "g.aug_match"
        "path/*" and sorting the resulting nodes into
        alphabetical order.
        
        This function returns a list of strings.
        """
        return libguestfsmod.aug_ls (self._o, path)

    def rm (self, path):
        u"""Remove the single file "path".
        """
        return libguestfsmod.rm (self._o, path)

    def rmdir (self, path):
        u"""Remove the single directory "path".
        """
        return libguestfsmod.rmdir (self._o, path)

    def rm_rf (self, path):
        u"""Remove the file or directory "path", recursively
        removing the contents if its a directory. This is like
        the "rm -rf" shell command.
        """
        return libguestfsmod.rm_rf (self._o, path)

    def mkdir (self, path):
        u"""Create a directory named "path".
        """
        return libguestfsmod.mkdir (self._o, path)

    def mkdir_p (self, path):
        u"""Create a directory named "path", creating any parent
        directories as necessary. This is like the "mkdir -p"
        shell command.
        """
        return libguestfsmod.mkdir_p (self._o, path)

    def chmod (self, mode, path):
        u"""Change the mode (permissions) of "path" to "mode". Only
        numeric modes are supported.
        """
        return libguestfsmod.chmod (self._o, mode, path)

    def chown (self, owner, group, path):
        u"""Change the file owner to "owner" and group to "group".
        
        Only numeric uid and gid are supported. If you want to
        use names, you will need to locate and parse the
        password file yourself (Augeas support makes this
        relatively easy).
        """
        return libguestfsmod.chown (self._o, owner, group, path)

    def exists (self, path):
        u"""This returns "true" if and only if there is a file,
        directory (or anything) with the given "path" name.
        
        See also "g.is_file", "g.is_dir", "g.stat".
        """
        return libguestfsmod.exists (self._o, path)

    def is_file (self, path):
        u"""This returns "true" if and only if there is a file with
        the given "path" name. Note that it returns false for
        other objects like directories.
        
        See also "g.stat".
        """
        return libguestfsmod.is_file (self._o, path)

    def is_dir (self, path):
        u"""This returns "true" if and only if there is a directory
        with the given "path" name. Note that it returns false
        for other objects like files.
        
        See also "g.stat".
        """
        return libguestfsmod.is_dir (self._o, path)

    def pvcreate (self, device):
        u"""This creates an LVM physical volume on the named
        "device", where "device" should usually be a partition
        name such as "/dev/sda1".
        """
        return libguestfsmod.pvcreate (self._o, device)

    def vgcreate (self, volgroup, physvols):
        u"""This creates an LVM volume group called "volgroup" from
        the non-empty list of physical volumes "physvols".
        """
        return libguestfsmod.vgcreate (self._o, volgroup, physvols)

    def lvcreate (self, logvol, volgroup, mbytes):
        u"""This creates an LVM volume group called "logvol" on the
        volume group "volgroup", with "size" megabytes.
        """
        return libguestfsmod.lvcreate (self._o, logvol, volgroup, mbytes)

    def mkfs (self, fstype, device):
        u"""This creates a filesystem on "device" (usually a
        partition of LVM logical volume). The filesystem type is
        "fstype", for example "ext3".
        """
        return libguestfsmod.mkfs (self._o, fstype, device)

    def sfdisk (self, device, cyls, heads, sectors, lines):
        u"""This is a direct interface to the sfdisk(8) program for
        creating partitions on block devices.
        
        "device" should be a block device, for example
        "/dev/sda".
        
        "cyls", "heads" and "sectors" are the number of
        cylinders, heads and sectors on the device, which are
        passed directly to sfdisk as the *-C*, *-H* and *-S*
        parameters. If you pass 0 for any of these, then the
        corresponding parameter is omitted. Usually for 'large'
        disks, you can just pass 0 for these, but for small
        (floppy-sized) disks, sfdisk (or rather, the kernel)
        cannot work out the right geometry and you will need to
        tell it.
        
        "lines" is a list of lines that we feed to "sfdisk". For
        more information refer to the sfdisk(8) manpage.
        
        To create a single partition occupying the whole disk,
        you would pass "lines" as a single element list, when
        the single element being the string "," (comma).
        
        This command is dangerous. Without careful use you can
        easily destroy all your data.
        """
        return libguestfsmod.sfdisk (self._o, device, cyls, heads, sectors, lines)

    def write_file (self, path, content, size):
        u"""This call creates a file called "path". The contents of
        the file is the string "content" (which can contain any
        8 bit data), with length "size".
        
        As a special case, if "size" is 0 then the length is
        calculated using "strlen" (so in this case the content
        cannot contain embedded ASCII NULs).
        
        Because of the message protocol, there is a transfer
        limit of somewhere between 2MB and 4MB. To transfer
        large files you should use FTP.
        """
        return libguestfsmod.write_file (self._o, path, content, size)

    def umount (self, pathordevice):
        u"""This unmounts the given filesystem. The filesystem may
        be specified either by its mountpoint (path) or the
        device which contains the filesystem.
        """
        return libguestfsmod.umount (self._o, pathordevice)

    def mounts (self):
        u"""This returns the list of currently mounted filesystems.
        It returns the list of devices (eg. "/dev/sda1",
        "/dev/VG/LV").
        
        Some internal mounts are not shown.
        
        This function returns a list of strings.
        """
        return libguestfsmod.mounts (self._o)

    def umount_all (self):
        u"""This unmounts all mounted filesystems.
        
        Some internal mounts are not unmounted by this call.
        """
        return libguestfsmod.umount_all (self._o)

    def lvm_remove_all (self):
        u"""This command removes all LVM logical volumes, volume
        groups and physical volumes.
        
        This command is dangerous. Without careful use you can
        easily destroy all your data.
        """
        return libguestfsmod.lvm_remove_all (self._o)

    def file (self, path):
        u"""This call uses the standard file(1) command to determine
        the type or contents of the file. This also works on
        devices, for example to find out whether a partition
        contains a filesystem.
        
        The exact command which runs is "file -bsL path". Note
        in particular that the filename is not prepended to the
        output (the "-b" option).
        """
        return libguestfsmod.file (self._o, path)

    def command (self, arguments):
        u"""This call runs a command from the guest filesystem. The
        filesystem must be mounted, and must contain a
        compatible operating system (ie. something Linux, with
        the same or compatible processor architecture).
        
        The single parameter is an argv-style list of arguments.
        The first element is the name of the program to run.
        Subsequent elements are parameters. The list must be
        non-empty (ie. must contain a program name).
        
        The $PATH environment variable will contain at least
        "/usr/bin" and "/bin". If you require a program from
        another location, you should provide the full path in
        the first parameter.
        
        Shared libraries and data files required by the program
        must be available on filesystems which are mounted in
        the correct places. It is the caller's responsibility to
        ensure all filesystems that are needed are mounted at
        the right locations.
        """
        return libguestfsmod.command (self._o, arguments)

    def command_lines (self, arguments):
        u"""This is the same as "g.command", but splits the result
        into a list of lines.
        
        This function returns a list of strings.
        """
        return libguestfsmod.command_lines (self._o, arguments)

    def stat (self, path):
        u"""Returns file information for the given "path".
        
        This is the same as the stat(2) system call.
        
        This function returns a dictionary, with keys matching
        the various fields in the stat structure.
        """
        return libguestfsmod.stat (self._o, path)

    def lstat (self, path):
        u"""Returns file information for the given "path".
        
        This is the same as "g.stat" except that if "path" is a
        symbolic link, then the link is stat-ed, not the file it
        refers to.
        
        This is the same as the lstat(2) system call.
        
        This function returns a dictionary, with keys matching
        the various fields in the stat structure.
        """
        return libguestfsmod.lstat (self._o, path)

    def statvfs (self, path):
        u"""Returns file system statistics for any mounted file
        system. "path" should be a file or directory in the
        mounted file system (typically it is the mount point
        itself, but it doesn't need to be).
        
        This is the same as the statvfs(2) system call.
        
        This function returns a dictionary, with keys matching
        the various fields in the statvfs structure.
        """
        return libguestfsmod.statvfs (self._o, path)

    def tune2fs_l (self, device):
        u"""This returns the contents of the ext2, ext3 or ext4
        filesystem superblock on "device".
        
        It is the same as running "tune2fs -l device". See
        tune2fs(8) manpage for more details. The list of fields
        returned isn't clearly defined, and depends on both the
        version of "tune2fs" that libguestfs was built against,
        and the filesystem itself.
        
        This function returns a dictionary.
        """
        return libguestfsmod.tune2fs_l (self._o, device)

    def blockdev_setro (self, device):
        u"""Sets the block device named "device" to read-only.
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_setro (self._o, device)

    def blockdev_setrw (self, device):
        u"""Sets the block device named "device" to read-write.
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_setrw (self._o, device)

    def blockdev_getro (self, device):
        u"""Returns a boolean indicating if the block device is
        read-only (true if read-only, false if not).
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_getro (self._o, device)

    def blockdev_getss (self, device):
        u"""This returns the size of sectors on a block device.
        Usually 512, but can be larger for modern devices.
        
        (Note, this is not the size in sectors, use
        "g.blockdev_getsz" for that).
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_getss (self._o, device)

    def blockdev_getbsz (self, device):
        u"""This returns the block size of a device.
        
        (Note this is different from both *size in blocks* and
        *filesystem block size*).
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_getbsz (self._o, device)

    def blockdev_setbsz (self, device, blocksize):
        u"""This sets the block size of a device.
        
        (Note this is different from both *size in blocks* and
        *filesystem block size*).
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_setbsz (self._o, device, blocksize)

    def blockdev_getsz (self, device):
        u"""This returns the size of the device in units of 512-byte
        sectors (even if the sectorsize isn't 512 bytes ...
        weird).
        
        See also "g.blockdev_getss" for the real sector size of
        the device, and "g.blockdev_getsize64" for the more
        useful *size in bytes*.
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_getsz (self._o, device)

    def blockdev_getsize64 (self, device):
        u"""This returns the size of the device in bytes.
        
        See also "g.blockdev_getsz".
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_getsize64 (self._o, device)

    def blockdev_flushbufs (self, device):
        u"""This tells the kernel to flush internal buffers
        associated with "device".
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_flushbufs (self._o, device)

    def blockdev_rereadpt (self, device):
        u"""Reread the partition table on "device".
        
        This uses the blockdev(8) command.
        """
        return libguestfsmod.blockdev_rereadpt (self._o, device)

    def upload (self, filename, remotefilename):
        u"""Upload local file "filename" to "remotefilename" on the
        filesystem.
        
        "filename" can also be a named pipe.
        
        See also "g.download".
        """
        return libguestfsmod.upload (self._o, filename, remotefilename)

    def download (self, remotefilename, filename):
        u"""Download file "remotefilename" and save it as "filename"
        on the local machine.
        
        "filename" can also be a named pipe.
        
        See also "g.upload", "g.cat".
        """
        return libguestfsmod.download (self._o, remotefilename, filename)

    def checksum (self, csumtype, path):
        u"""This call computes the MD5, SHAx or CRC checksum of the
        file named "path".
        
        The type of checksum to compute is given by the
        "csumtype" parameter which must have one of the
        following values:
        
        "crc"
        Compute the cyclic redundancy check (CRC) specified
        by POSIX for the "cksum" command.
        
        "md5"
        Compute the MD5 hash (using the "md5sum" program).
        
        "sha1"
        Compute the SHA1 hash (using the "sha1sum" program).
        
        "sha224"
        Compute the SHA224 hash (using the "sha224sum"
        program).
        
        "sha256"
        Compute the SHA256 hash (using the "sha256sum"
        program).
        
        "sha384"
        Compute the SHA384 hash (using the "sha384sum"
        program).
        
        "sha512"
        Compute the SHA512 hash (using the "sha512sum"
        program).
        
        The checksum is returned as a printable string.
        """
        return libguestfsmod.checksum (self._o, csumtype, path)

    def tar_in (self, tarfile, directory):
        u"""This command uploads and unpacks local file "tarfile"
        (an *uncompressed* tar file) into "directory".
        
        To upload a compressed tarball, use "g.tgz_in".
        """
        return libguestfsmod.tar_in (self._o, tarfile, directory)

    def tar_out (self, directory, tarfile):
        u"""This command packs the contents of "directory" and
        downloads it to local file "tarfile".
        
        To download a compressed tarball, use "g.tgz_out".
        """
        return libguestfsmod.tar_out (self._o, directory, tarfile)

    def tgz_in (self, tarball, directory):
        u"""This command uploads and unpacks local file "tarball" (a
        *gzip compressed* tar file) into "directory".
        
        To upload an uncompressed tarball, use "g.tar_in".
        """
        return libguestfsmod.tgz_in (self._o, tarball, directory)

    def tgz_out (self, directory, tarball):
        u"""This command packs the contents of "directory" and
        downloads it to local file "tarball".
        
        To download an uncompressed tarball, use "g.tar_out".
        """
        return libguestfsmod.tgz_out (self._o, directory, tarball)

    def mount_ro (self, device, mountpoint):
        u"""This is the same as the "g.mount" command, but it mounts
        the filesystem with the read-only (*-o ro*) flag.
        """
        return libguestfsmod.mount_ro (self._o, device, mountpoint)

    def mount_options (self, options, device, mountpoint):
        u"""This is the same as the "g.mount" command, but it allows
        you to set the mount options as for the mount(8) *-o*
        flag.
        """
        return libguestfsmod.mount_options (self._o, options, device, mountpoint)

    def mount_vfs (self, options, vfstype, device, mountpoint):
        u"""This is the same as the "g.mount" command, but it allows
        you to set both the mount options and the vfstype as for
        the mount(8) *-o* and *-t* flags.
        """
        return libguestfsmod.mount_vfs (self._o, options, vfstype, device, mountpoint)

    def debug (self, subcmd, extraargs):
        u"""The "g.debug" command exposes some internals of
        "guestfsd" (the guestfs daemon) that runs inside the
        qemu subprocess.
        
        There is no comprehensive help for this command. You
        have to look at the file "daemon/debug.c" in the
        libguestfs source to find out what you can do.
        """
        return libguestfsmod.debug (self._o, subcmd, extraargs)

    def lvremove (self, device):
        u"""Remove an LVM logical volume "device", where "device" is
        the path to the LV, such as "/dev/VG/LV".
        
        You can also remove all LVs in a volume group by
        specifying the VG name, "/dev/VG".
        """
        return libguestfsmod.lvremove (self._o, device)

    def vgremove (self, vgname):
        u"""Remove an LVM volume group "vgname", (for example "VG").
        
        This also forcibly removes all logical volumes in the
        volume group (if any).
        """
        return libguestfsmod.vgremove (self._o, vgname)

    def pvremove (self, device):
        u"""This wipes a physical volume "device" so that LVM will
        no longer recognise it.
        
        The implementation uses the "pvremove" command which
        refuses to wipe physical volumes that contain any volume
        groups, so you have to remove those first.
        """
        return libguestfsmod.pvremove (self._o, device)


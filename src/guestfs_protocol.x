/* libguestfs generated file
 * WARNING: THIS FILE IS GENERATED BY 'src/generator.ml'.
 * ANY CHANGES YOU MAKE TO THIS FILE WILL BE LOST.
 *
 * Copyright (C) 2009 Red Hat Inc.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

typedef string str<>;

struct guestfs_lvm_int_pv {
  string pv_name<>;
  opaque pv_uuid[32];
  string pv_fmt<>;
  hyper pv_size;
  hyper dev_size;
  hyper pv_free;
  hyper pv_used;
  string pv_attr<>;
  hyper pv_pe_count;
  hyper pv_pe_alloc_count;
  string pv_tags<>;
  hyper pe_start;
  hyper pv_mda_count;
  hyper pv_mda_free;
};

typedef struct guestfs_lvm_int_pv guestfs_lvm_int_pv_list<>;

struct guestfs_lvm_int_vg {
  string vg_name<>;
  opaque vg_uuid[32];
  string vg_fmt<>;
  string vg_attr<>;
  hyper vg_size;
  hyper vg_free;
  string vg_sysid<>;
  hyper vg_extent_size;
  hyper vg_extent_count;
  hyper vg_free_count;
  hyper max_lv;
  hyper max_pv;
  hyper pv_count;
  hyper lv_count;
  hyper snap_count;
  hyper vg_seqno;
  string vg_tags<>;
  hyper vg_mda_count;
  hyper vg_mda_free;
};

typedef struct guestfs_lvm_int_vg guestfs_lvm_int_vg_list<>;

struct guestfs_lvm_int_lv {
  string lv_name<>;
  opaque lv_uuid[32];
  string lv_attr<>;
  hyper lv_major;
  hyper lv_minor;
  hyper lv_kernel_major;
  hyper lv_kernel_minor;
  hyper lv_size;
  hyper seg_count;
  string origin<>;
  float snap_percent;
  float copy_percent;
  string move_pv<>;
  string lv_tags<>;
  string mirror_log<>;
  string modules<>;
};

typedef struct guestfs_lvm_int_lv guestfs_lvm_int_lv_list<>;

struct guestfs_int_stat {
  hyper dev;
  hyper ino;
  hyper mode;
  hyper nlink;
  hyper uid;
  hyper gid;
  hyper rdev;
  hyper size;
  hyper blksize;
  hyper blocks;
  hyper atime;
  hyper mtime;
  hyper ctime;
};

struct guestfs_int_statvfs {
  hyper bsize;
  hyper frsize;
  hyper blocks;
  hyper bfree;
  hyper bavail;
  hyper files;
  hyper ffree;
  hyper favail;
  hyper fsid;
  hyper flag;
  hyper namemax;
};

struct guestfs_mount_args {
  string device<>;
  string mountpoint<>;
};

struct guestfs_touch_args {
  string path<>;
};

struct guestfs_cat_args {
  string path<>;
};

struct guestfs_cat_ret {
  string content<>;
};

struct guestfs_ll_args {
  string directory<>;
};

struct guestfs_ll_ret {
  string listing<>;
};

struct guestfs_ls_args {
  string directory<>;
};

struct guestfs_ls_ret {
  str listing<>;
};

struct guestfs_list_devices_ret {
  str devices<>;
};

struct guestfs_list_partitions_ret {
  str partitions<>;
};

struct guestfs_pvs_ret {
  str physvols<>;
};

struct guestfs_vgs_ret {
  str volgroups<>;
};

struct guestfs_lvs_ret {
  str logvols<>;
};

struct guestfs_pvs_full_ret {
  guestfs_lvm_int_pv_list physvols;
};

struct guestfs_vgs_full_ret {
  guestfs_lvm_int_vg_list volgroups;
};

struct guestfs_lvs_full_ret {
  guestfs_lvm_int_lv_list logvols;
};

struct guestfs_read_lines_args {
  string path<>;
};

struct guestfs_read_lines_ret {
  str lines<>;
};

struct guestfs_aug_init_args {
  string root<>;
  int flags;
};

struct guestfs_aug_defvar_args {
  string name<>;
  str *expr;
};

struct guestfs_aug_defvar_ret {
  int nrnodes;
};

struct guestfs_aug_defnode_args {
  string name<>;
  string expr<>;
  string val<>;
};

struct guestfs_aug_defnode_ret {
  int nrnodes;
  bool created;
};

struct guestfs_aug_get_args {
  string path<>;
};

struct guestfs_aug_get_ret {
  string val<>;
};

struct guestfs_aug_set_args {
  string path<>;
  string val<>;
};

struct guestfs_aug_insert_args {
  string path<>;
  string label<>;
  bool before;
};

struct guestfs_aug_rm_args {
  string path<>;
};

struct guestfs_aug_rm_ret {
  int nrnodes;
};

struct guestfs_aug_mv_args {
  string src<>;
  string dest<>;
};

struct guestfs_aug_match_args {
  string path<>;
};

struct guestfs_aug_match_ret {
  str matches<>;
};

struct guestfs_aug_ls_args {
  string path<>;
};

struct guestfs_aug_ls_ret {
  str matches<>;
};

struct guestfs_rm_args {
  string path<>;
};

struct guestfs_rmdir_args {
  string path<>;
};

struct guestfs_rm_rf_args {
  string path<>;
};

struct guestfs_mkdir_args {
  string path<>;
};

struct guestfs_mkdir_p_args {
  string path<>;
};

struct guestfs_chmod_args {
  int mode;
  string path<>;
};

struct guestfs_chown_args {
  int owner;
  int group;
  string path<>;
};

struct guestfs_exists_args {
  string path<>;
};

struct guestfs_exists_ret {
  bool existsflag;
};

struct guestfs_is_file_args {
  string path<>;
};

struct guestfs_is_file_ret {
  bool fileflag;
};

struct guestfs_is_dir_args {
  string path<>;
};

struct guestfs_is_dir_ret {
  bool dirflag;
};

struct guestfs_pvcreate_args {
  string device<>;
};

struct guestfs_vgcreate_args {
  string volgroup<>;
  str physvols<>;
};

struct guestfs_lvcreate_args {
  string logvol<>;
  string volgroup<>;
  int mbytes;
};

struct guestfs_mkfs_args {
  string fstype<>;
  string device<>;
};

struct guestfs_sfdisk_args {
  string device<>;
  int cyls;
  int heads;
  int sectors;
  str lines<>;
};

struct guestfs_write_file_args {
  string path<>;
  string content<>;
  int size;
};

struct guestfs_umount_args {
  string pathordevice<>;
};

struct guestfs_mounts_ret {
  str devices<>;
};

struct guestfs_file_args {
  string path<>;
};

struct guestfs_file_ret {
  string description<>;
};

struct guestfs_command_args {
  str arguments<>;
};

struct guestfs_command_ret {
  string output<>;
};

struct guestfs_command_lines_args {
  str arguments<>;
};

struct guestfs_command_lines_ret {
  str lines<>;
};

struct guestfs_stat_args {
  string path<>;
};

struct guestfs_stat_ret {
  guestfs_int_stat statbuf;
};

struct guestfs_lstat_args {
  string path<>;
};

struct guestfs_lstat_ret {
  guestfs_int_stat statbuf;
};

struct guestfs_statvfs_args {
  string path<>;
};

struct guestfs_statvfs_ret {
  guestfs_int_statvfs statbuf;
};

struct guestfs_tune2fs_l_args {
  string device<>;
};

struct guestfs_tune2fs_l_ret {
  str superblock<>;
};

struct guestfs_blockdev_setro_args {
  string device<>;
};

struct guestfs_blockdev_setrw_args {
  string device<>;
};

struct guestfs_blockdev_getro_args {
  string device<>;
};

struct guestfs_blockdev_getro_ret {
  bool ro;
};

struct guestfs_blockdev_getss_args {
  string device<>;
};

struct guestfs_blockdev_getss_ret {
  int sectorsize;
};

struct guestfs_blockdev_getbsz_args {
  string device<>;
};

struct guestfs_blockdev_getbsz_ret {
  int blocksize;
};

struct guestfs_blockdev_setbsz_args {
  string device<>;
  int blocksize;
};

struct guestfs_blockdev_getsz_args {
  string device<>;
};

struct guestfs_blockdev_getsz_ret {
  hyper sizeinsectors;
};

struct guestfs_blockdev_getsize64_args {
  string device<>;
};

struct guestfs_blockdev_getsize64_ret {
  hyper sizeinbytes;
};

struct guestfs_blockdev_flushbufs_args {
  string device<>;
};

struct guestfs_blockdev_rereadpt_args {
  string device<>;
};

struct guestfs_upload_args {
  string remotefilename<>;
};

struct guestfs_download_args {
  string remotefilename<>;
};

struct guestfs_checksum_args {
  string csumtype<>;
  string path<>;
};

struct guestfs_checksum_ret {
  string checksum<>;
};

struct guestfs_tar_in_args {
  string directory<>;
};

struct guestfs_tar_out_args {
  string directory<>;
};

struct guestfs_tgz_in_args {
  string directory<>;
};

struct guestfs_tgz_out_args {
  string directory<>;
};

struct guestfs_mount_ro_args {
  string device<>;
  string mountpoint<>;
};

struct guestfs_mount_options_args {
  string options<>;
  string device<>;
  string mountpoint<>;
};

struct guestfs_mount_vfs_args {
  string options<>;
  string vfstype<>;
  string device<>;
  string mountpoint<>;
};

struct guestfs_debug_args {
  string subcmd<>;
  str extraargs<>;
};

struct guestfs_debug_ret {
  string result<>;
};

struct guestfs_lvremove_args {
  string device<>;
};

struct guestfs_vgremove_args {
  string vgname<>;
};

struct guestfs_pvremove_args {
  string device<>;
};

enum guestfs_procedure {
  GUESTFS_PROC_MOUNT = 1,
  GUESTFS_PROC_SYNC = 2,
  GUESTFS_PROC_TOUCH = 3,
  GUESTFS_PROC_CAT = 4,
  GUESTFS_PROC_LL = 5,
  GUESTFS_PROC_LS = 6,
  GUESTFS_PROC_LIST_DEVICES = 7,
  GUESTFS_PROC_LIST_PARTITIONS = 8,
  GUESTFS_PROC_PVS = 9,
  GUESTFS_PROC_VGS = 10,
  GUESTFS_PROC_LVS = 11,
  GUESTFS_PROC_PVS_FULL = 12,
  GUESTFS_PROC_VGS_FULL = 13,
  GUESTFS_PROC_LVS_FULL = 14,
  GUESTFS_PROC_READ_LINES = 15,
  GUESTFS_PROC_AUG_INIT = 16,
  GUESTFS_PROC_AUG_CLOSE = 26,
  GUESTFS_PROC_AUG_DEFVAR = 17,
  GUESTFS_PROC_AUG_DEFNODE = 18,
  GUESTFS_PROC_AUG_GET = 19,
  GUESTFS_PROC_AUG_SET = 20,
  GUESTFS_PROC_AUG_INSERT = 21,
  GUESTFS_PROC_AUG_RM = 22,
  GUESTFS_PROC_AUG_MV = 23,
  GUESTFS_PROC_AUG_MATCH = 24,
  GUESTFS_PROC_AUG_SAVE = 25,
  GUESTFS_PROC_AUG_LOAD = 27,
  GUESTFS_PROC_AUG_LS = 28,
  GUESTFS_PROC_RM = 29,
  GUESTFS_PROC_RMDIR = 30,
  GUESTFS_PROC_RM_RF = 31,
  GUESTFS_PROC_MKDIR = 32,
  GUESTFS_PROC_MKDIR_P = 33,
  GUESTFS_PROC_CHMOD = 34,
  GUESTFS_PROC_CHOWN = 35,
  GUESTFS_PROC_EXISTS = 36,
  GUESTFS_PROC_IS_FILE = 37,
  GUESTFS_PROC_IS_DIR = 38,
  GUESTFS_PROC_PVCREATE = 39,
  GUESTFS_PROC_VGCREATE = 40,
  GUESTFS_PROC_LVCREATE = 41,
  GUESTFS_PROC_MKFS = 42,
  GUESTFS_PROC_SFDISK = 43,
  GUESTFS_PROC_WRITE_FILE = 44,
  GUESTFS_PROC_UMOUNT = 45,
  GUESTFS_PROC_MOUNTS = 46,
  GUESTFS_PROC_UMOUNT_ALL = 47,
  GUESTFS_PROC_LVM_REMOVE_ALL = 48,
  GUESTFS_PROC_FILE = 49,
  GUESTFS_PROC_COMMAND = 50,
  GUESTFS_PROC_COMMAND_LINES = 51,
  GUESTFS_PROC_STAT = 52,
  GUESTFS_PROC_LSTAT = 53,
  GUESTFS_PROC_STATVFS = 54,
  GUESTFS_PROC_TUNE2FS_L = 55,
  GUESTFS_PROC_BLOCKDEV_SETRO = 56,
  GUESTFS_PROC_BLOCKDEV_SETRW = 57,
  GUESTFS_PROC_BLOCKDEV_GETRO = 58,
  GUESTFS_PROC_BLOCKDEV_GETSS = 59,
  GUESTFS_PROC_BLOCKDEV_GETBSZ = 60,
  GUESTFS_PROC_BLOCKDEV_SETBSZ = 61,
  GUESTFS_PROC_BLOCKDEV_GETSZ = 62,
  GUESTFS_PROC_BLOCKDEV_GETSIZE64 = 63,
  GUESTFS_PROC_BLOCKDEV_FLUSHBUFS = 64,
  GUESTFS_PROC_BLOCKDEV_REREADPT = 65,
  GUESTFS_PROC_UPLOAD = 66,
  GUESTFS_PROC_DOWNLOAD = 67,
  GUESTFS_PROC_CHECKSUM = 68,
  GUESTFS_PROC_TAR_IN = 69,
  GUESTFS_PROC_TAR_OUT = 70,
  GUESTFS_PROC_TGZ_IN = 71,
  GUESTFS_PROC_TGZ_OUT = 72,
  GUESTFS_PROC_MOUNT_RO = 73,
  GUESTFS_PROC_MOUNT_OPTIONS = 74,
  GUESTFS_PROC_MOUNT_VFS = 75,
  GUESTFS_PROC_DEBUG = 76,
  GUESTFS_PROC_LVREMOVE = 77,
  GUESTFS_PROC_VGREMOVE = 78,
  GUESTFS_PROC_PVREMOVE = 79,
  GUESTFS_PROC_NR_PROCS
};

const GUESTFS_MESSAGE_MAX = 4194304;

/* The communication protocol is now documented in the guestfs(3)
 * manpage.
 */

const GUESTFS_PROGRAM = 0x2000F5F5;
const GUESTFS_PROTOCOL_VERSION = 1;

/* These constants must be larger than any possible message length. */
const GUESTFS_LAUNCH_FLAG = 0xf5f55ff5;
const GUESTFS_CANCEL_FLAG = 0xffffeeee;

enum guestfs_message_direction {
  GUESTFS_DIRECTION_CALL = 0,        /* client -> daemon */
  GUESTFS_DIRECTION_REPLY = 1        /* daemon -> client */
};

enum guestfs_message_status {
  GUESTFS_STATUS_OK = 0,
  GUESTFS_STATUS_ERROR = 1
};

const GUESTFS_ERROR_LEN = 256;

struct guestfs_message_error {
  string error_message<GUESTFS_ERROR_LEN>;
};

struct guestfs_message_header {
  unsigned prog;                     /* GUESTFS_PROGRAM */
  unsigned vers;                     /* GUESTFS_PROTOCOL_VERSION */
  guestfs_procedure proc;            /* GUESTFS_PROC_x */
  guestfs_message_direction direction;
  unsigned serial;                   /* message serial number */
  guestfs_message_status status;
};

const GUESTFS_MAX_CHUNK_SIZE = 8192;

struct guestfs_chunk {
  int cancel;			     /* if non-zero, transfer is cancelled */
  /* data size is 0 bytes if the transfer has finished successfully */
  opaque data<GUESTFS_MAX_CHUNK_SIZE>;
};

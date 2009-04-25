(* libguestfs generated file
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
 *)

type t
exception Error of string
external create : unit -> t = "ocaml_guestfs_create"
external close : t -> unit = "ocaml_guestfs_close"

let () =
  Callback.register_exception "ocaml_guestfs_error" (Error "")

type lvm_pv = {
  pv_name : string;
  pv_uuid : string;
  pv_fmt : string;
  pv_size : int64;
  dev_size : int64;
  pv_free : int64;
  pv_used : int64;
  pv_attr : string;
  pv_pe_count : int64;
  pv_pe_alloc_count : int64;
  pv_tags : string;
  pe_start : int64;
  pv_mda_count : int64;
  pv_mda_free : int64;
}

type lvm_vg = {
  vg_name : string;
  vg_uuid : string;
  vg_fmt : string;
  vg_attr : string;
  vg_size : int64;
  vg_free : int64;
  vg_sysid : string;
  vg_extent_size : int64;
  vg_extent_count : int64;
  vg_free_count : int64;
  max_lv : int64;
  max_pv : int64;
  pv_count : int64;
  lv_count : int64;
  snap_count : int64;
  vg_seqno : int64;
  vg_tags : string;
  vg_mda_count : int64;
  vg_mda_free : int64;
}

type lvm_lv = {
  lv_name : string;
  lv_uuid : string;
  lv_attr : string;
  lv_major : int64;
  lv_minor : int64;
  lv_kernel_major : int64;
  lv_kernel_minor : int64;
  lv_size : int64;
  seg_count : int64;
  origin : string;
  snap_percent : float option;
  copy_percent : float option;
  move_pv : string;
  lv_tags : string;
  mirror_log : string;
  modules : string;
}

type stat = {
  dev : int64;
  ino : int64;
  mode : int64;
  nlink : int64;
  uid : int64;
  gid : int64;
  rdev : int64;
  size : int64;
  blksize : int64;
  blocks : int64;
  atime : int64;
  mtime : int64;
  ctime : int64;
}

type statvfs = {
  bsize : int64;
  frsize : int64;
  blocks : int64;
  bfree : int64;
  bavail : int64;
  files : int64;
  ffree : int64;
  favail : int64;
  fsid : int64;
  flag : int64;
  namemax : int64;
}

external launch : t -> unit = "ocaml_guestfs_launch"
external wait_ready : t -> unit = "ocaml_guestfs_wait_ready"
external kill_subprocess : t -> unit = "ocaml_guestfs_kill_subprocess"
external add_drive : t -> string -> unit = "ocaml_guestfs_add_drive"
external add_cdrom : t -> string -> unit = "ocaml_guestfs_add_cdrom"
external config : t -> string -> string option -> unit = "ocaml_guestfs_config"
external set_qemu : t -> string -> unit = "ocaml_guestfs_set_qemu"
external get_qemu : t -> string = "ocaml_guestfs_get_qemu"
external set_path : t -> string -> unit = "ocaml_guestfs_set_path"
external get_path : t -> string = "ocaml_guestfs_get_path"
external set_autosync : t -> bool -> unit = "ocaml_guestfs_set_autosync"
external get_autosync : t -> bool = "ocaml_guestfs_get_autosync"
external set_verbose : t -> bool -> unit = "ocaml_guestfs_set_verbose"
external get_verbose : t -> bool = "ocaml_guestfs_get_verbose"
external is_ready : t -> bool = "ocaml_guestfs_is_ready"
external is_config : t -> bool = "ocaml_guestfs_is_config"
external is_launching : t -> bool = "ocaml_guestfs_is_launching"
external is_busy : t -> bool = "ocaml_guestfs_is_busy"
external get_state : t -> int = "ocaml_guestfs_get_state"
external set_busy : t -> unit = "ocaml_guestfs_set_busy"
external set_ready : t -> unit = "ocaml_guestfs_set_ready"
external mount : t -> string -> string -> unit = "ocaml_guestfs_mount"
external sync : t -> unit = "ocaml_guestfs_sync"
external touch : t -> string -> unit = "ocaml_guestfs_touch"
external cat : t -> string -> string = "ocaml_guestfs_cat"
external ll : t -> string -> string = "ocaml_guestfs_ll"
external ls : t -> string -> string array = "ocaml_guestfs_ls"
external list_devices : t -> string array = "ocaml_guestfs_list_devices"
external list_partitions : t -> string array = "ocaml_guestfs_list_partitions"
external pvs : t -> string array = "ocaml_guestfs_pvs"
external vgs : t -> string array = "ocaml_guestfs_vgs"
external lvs : t -> string array = "ocaml_guestfs_lvs"
external pvs_full : t -> lvm_pv array = "ocaml_guestfs_pvs_full"
external vgs_full : t -> lvm_vg array = "ocaml_guestfs_vgs_full"
external lvs_full : t -> lvm_lv array = "ocaml_guestfs_lvs_full"
external read_lines : t -> string -> string array = "ocaml_guestfs_read_lines"
external aug_init : t -> string -> int -> unit = "ocaml_guestfs_aug_init"
external aug_close : t -> unit = "ocaml_guestfs_aug_close"
external aug_defvar : t -> string -> string option -> int = "ocaml_guestfs_aug_defvar"
external aug_defnode : t -> string -> string -> string -> int * bool = "ocaml_guestfs_aug_defnode"
external aug_get : t -> string -> string = "ocaml_guestfs_aug_get"
external aug_set : t -> string -> string -> unit = "ocaml_guestfs_aug_set"
external aug_insert : t -> string -> string -> bool -> unit = "ocaml_guestfs_aug_insert"
external aug_rm : t -> string -> int = "ocaml_guestfs_aug_rm"
external aug_mv : t -> string -> string -> unit = "ocaml_guestfs_aug_mv"
external aug_match : t -> string -> string array = "ocaml_guestfs_aug_match"
external aug_save : t -> unit = "ocaml_guestfs_aug_save"
external aug_load : t -> unit = "ocaml_guestfs_aug_load"
external aug_ls : t -> string -> string array = "ocaml_guestfs_aug_ls"
external rm : t -> string -> unit = "ocaml_guestfs_rm"
external rmdir : t -> string -> unit = "ocaml_guestfs_rmdir"
external rm_rf : t -> string -> unit = "ocaml_guestfs_rm_rf"
external mkdir : t -> string -> unit = "ocaml_guestfs_mkdir"
external mkdir_p : t -> string -> unit = "ocaml_guestfs_mkdir_p"
external chmod : t -> int -> string -> unit = "ocaml_guestfs_chmod"
external chown : t -> int -> int -> string -> unit = "ocaml_guestfs_chown"
external exists : t -> string -> bool = "ocaml_guestfs_exists"
external is_file : t -> string -> bool = "ocaml_guestfs_is_file"
external is_dir : t -> string -> bool = "ocaml_guestfs_is_dir"
external pvcreate : t -> string -> unit = "ocaml_guestfs_pvcreate"
external vgcreate : t -> string -> string array -> unit = "ocaml_guestfs_vgcreate"
external lvcreate : t -> string -> string -> int -> unit = "ocaml_guestfs_lvcreate"
external mkfs : t -> string -> string -> unit = "ocaml_guestfs_mkfs"
external sfdisk : t -> string -> int -> int -> int -> string array -> unit = "ocaml_guestfs_sfdisk_byte" "ocaml_guestfs_sfdisk"
external write_file : t -> string -> string -> int -> unit = "ocaml_guestfs_write_file"
external umount : t -> string -> unit = "ocaml_guestfs_umount"
external mounts : t -> string array = "ocaml_guestfs_mounts"
external umount_all : t -> unit = "ocaml_guestfs_umount_all"
external lvm_remove_all : t -> unit = "ocaml_guestfs_lvm_remove_all"
external file : t -> string -> string = "ocaml_guestfs_file"
external command : t -> string array -> string = "ocaml_guestfs_command"
external command_lines : t -> string array -> string array = "ocaml_guestfs_command_lines"
external stat : t -> string -> stat = "ocaml_guestfs_stat"
external lstat : t -> string -> stat = "ocaml_guestfs_lstat"
external statvfs : t -> string -> statvfs = "ocaml_guestfs_statvfs"
external tune2fs_l : t -> string -> (string * string) list = "ocaml_guestfs_tune2fs_l"
external blockdev_setro : t -> string -> unit = "ocaml_guestfs_blockdev_setro"
external blockdev_setrw : t -> string -> unit = "ocaml_guestfs_blockdev_setrw"
external blockdev_getro : t -> string -> bool = "ocaml_guestfs_blockdev_getro"
external blockdev_getss : t -> string -> int = "ocaml_guestfs_blockdev_getss"
external blockdev_getbsz : t -> string -> int = "ocaml_guestfs_blockdev_getbsz"
external blockdev_setbsz : t -> string -> int -> unit = "ocaml_guestfs_blockdev_setbsz"
external blockdev_getsz : t -> string -> int64 = "ocaml_guestfs_blockdev_getsz"
external blockdev_getsize64 : t -> string -> int64 = "ocaml_guestfs_blockdev_getsize64"
external blockdev_flushbufs : t -> string -> unit = "ocaml_guestfs_blockdev_flushbufs"
external blockdev_rereadpt : t -> string -> unit = "ocaml_guestfs_blockdev_rereadpt"
external upload : t -> string -> string -> unit = "ocaml_guestfs_upload"
external download : t -> string -> string -> unit = "ocaml_guestfs_download"
external checksum : t -> string -> string -> string = "ocaml_guestfs_checksum"
external tar_in : t -> string -> string -> unit = "ocaml_guestfs_tar_in"
external tar_out : t -> string -> string -> unit = "ocaml_guestfs_tar_out"
external tgz_in : t -> string -> string -> unit = "ocaml_guestfs_tgz_in"
external tgz_out : t -> string -> string -> unit = "ocaml_guestfs_tgz_out"
external mount_ro : t -> string -> string -> unit = "ocaml_guestfs_mount_ro"
external mount_options : t -> string -> string -> string -> unit = "ocaml_guestfs_mount_options"
external mount_vfs : t -> string -> string -> string -> string -> unit = "ocaml_guestfs_mount_vfs"
external debug : t -> string -> string array -> string = "ocaml_guestfs_debug"
external lvremove : t -> string -> unit = "ocaml_guestfs_lvremove"
external vgremove : t -> string -> unit = "ocaml_guestfs_vgremove"
external pvremove : t -> string -> unit = "ocaml_guestfs_pvremove"

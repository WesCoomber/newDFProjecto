.section	.text
.globl _start
_start:
push ebp
call recheck_start
pop ebp
/*TODO: make sure we follow the calling conventions (preseve eax, edx, ecx when we call recheck-support func)*/
/*first checkpoint necessary addresses and registers*/
/*slice begins*/
call access_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call open_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call stat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call open_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call stat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call open_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call stat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call open_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call stat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call open_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call stat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call open_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call stat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call open_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call stat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call open_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call read_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
/*Eliminated [SLICE_TAINT] fstat64 bfffef68 bfffef70*/
/*Eliminated [SLICE_TAINT] fstat64 bfffef50 bfffef54*/
/*Eliminated [SLICE_TAINT] fstat64 bfffef60 bfffef64*/
/*Eliminated [SLICE_TAINT] fstat64 bfffef58 bfffef5c*/
call fstat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffef68)  //come with b7fe4864 (move upwards)*/
mov edi, dword ptr [0xbfffef68]	       /* [ORIGINAL_SLICE] b7fe4864  [SLICE_INFO] #src_memregreg_mov[5:0:4,bfffef68:1:4,0:0:0] #base_reg_value 3221221256, mem_value 11035190, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffef6c)  //come with b7fe4867 (move upwards)*/
mov ecx, dword ptr [0xbfffef6c]	       /* [ORIGINAL_SLICE] b7fe4867  [SLICE_INFO] #src_memregreg_mov[5:0:4,bfffef6c:1:4,0:0:0] #base_reg_value 3221221256, mem_value 0, index_reg_value 0*/
mov edx, 0  /* [SLICE_EXTRA]//comes with b7fe489c*/
xor edx, ecx	       /* [ORIGINAL_SLICE] b7fe489c  [SLICE_INFO] #src_regreg[8:0:4,9:1:4] #dst_reg_value 0, src_reg_value 0*/
mov eax, 0  /* [SLICE_EXTRA]//comes with b7fe489e*/
xor eax, edi	       /* [ORIGINAL_SLICE] b7fe489e  [SLICE_INFO] #src_regreg[10:0:4,3:1:4] #dst_reg_value 0, src_reg_value 11035190*/
or edx, eax	       /* [ORIGINAL_SLICE] b7fe48a0  [SLICE_INFO] #src_regreg[8:1:4,10:1:4] #dst_reg_value 0, src_reg_value 11035190*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7fe48a2  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov edx, 0  /* [SLICE_EXTRA]//comes with b7fe489c*/
xor edx, ecx	       /* [ORIGINAL_SLICE] b7fe489c  [SLICE_INFO] #src_regreg[8:0:4,9:1:4] #dst_reg_value 0, src_reg_value 0*/
mov eax, 0  /* [SLICE_EXTRA]//comes with b7fe489e*/
xor eax, edi	       /* [ORIGINAL_SLICE] b7fe489e  [SLICE_INFO] #src_regreg[10:0:4,3:1:4] #dst_reg_value 0, src_reg_value 11035190*/
or edx, eax	       /* [ORIGINAL_SLICE] b7fe48a0  [SLICE_INFO] #src_regreg[8:1:4,10:1:4] #dst_reg_value 0, src_reg_value 11035190*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7fe48a2  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov edx, 0  /* [SLICE_EXTRA]//comes with b7fe489c*/
xor edx, ecx	       /* [ORIGINAL_SLICE] b7fe489c  [SLICE_INFO] #src_regreg[8:0:4,9:1:4] #dst_reg_value 0, src_reg_value 0*/
mov eax, 0  /* [SLICE_EXTRA]//comes with b7fe489e*/
xor eax, edi	       /* [ORIGINAL_SLICE] b7fe489e  [SLICE_INFO] #src_regreg[10:0:4,3:1:4] #dst_reg_value 0, src_reg_value 11035190*/
or edx, eax	       /* [ORIGINAL_SLICE] b7fe48a0  [SLICE_INFO] #src_regreg[8:1:4,10:1:4] #dst_reg_value 0, src_reg_value 11035190*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7fe48a2  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffee74)  //come with b7fe95e1 (move upwards)*/
mov  dword ptr [0xbfffee74], edi	       /* [ORIGINAL_SLICE] b7fe95e1  [SLICE_INFO] push instruction (rewrite) #src_reg[3:1:4], dst_mem[bfffee74:0:4] #src_reg_value 11035190, dst_mem_value 3086965498*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffee74)  //come with b7fe9804 (move upwards)*/
mov edi	,  dword ptr [0xbfffee74]       /* [ORIGINAL_SLICE] b7fe9804  [SLICE_INFO] pop instruction(rewrite) #src_mem[bfffee74:1:4] #src_mem_value 11035190*/
call close_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffef68)  //come with b7fe5104 (move upwards)*/
mov eax, dword ptr [0xbfffef68]	       /* [ORIGINAL_SLICE] b7fe5104  [SLICE_INFO] #src_memregreg_mov[5:0:4,bfffef68:1:4,0:0:0] #base_reg_value 3221221256, mem_value 11035190, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffef6c)  //come with b7fe510d (move upwards)*/
mov edx, dword ptr [0xbfffef6c]	       /* [ORIGINAL_SLICE] b7fe510d  [SLICE_INFO] #src_memregreg_mov[5:0:4,bfffef6c:1:4,0:0:0] #base_reg_value 3221221256, mem_value 0, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xb7fdde98)  //come with b7fe5112 (move upwards)*/
mov dword ptr [0xb7fdde98], eax	       /* [ORIGINAL_SLICE] b7fe5112  [SLICE_INFO] #src_regregreg_mov[3:0:4,10:1:4,0:0:0] #base_reg_value 3086867640, reg_value 11035190, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xb7fdde9c)  //come with b7fe5118 (move upwards)*/
mov dword ptr [0xb7fdde9c], edx	       /* [ORIGINAL_SLICE] b7fe5118  [SLICE_INFO] #src_regregreg_mov[3:0:4,8:1:4,0:0:0] #base_reg_value 3086867640, reg_value 0, index_reg_value 0*/
call getpid_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
mov ecx, eax	       /* [ORIGINAL_SLICE] b7eeff20  [SLICE_INFO] #src_reg[10:1:4] #src_reg_value 15216*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xb7e41728)  //come with b7eeff24 (move upwards)*/
mov dword ptr [0xb7e41728], ecx	       /* [ORIGINAL_SLICE] b7eeff24  [SLICE_INFO] #src_regregreg_mov[0:0:0,9:1:4,0:0:0] #base_reg_value 0, reg_value 15216, index_reg_value 0*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7eeff2b  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 15216*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4c8)  //come with 80484ae (move upwards)*/
mov dword ptr [0xbffff4c8], eax	       /* [ORIGINAL_SLICE] 80484ae  [SLICE_INFO] #src_regregreg_mov[6:0:4,10:1:4,0:0:0] #base_reg_value 3221222576, reg_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4c8)  //come with 80484b2 (move upwards)*/
cmp dword ptr [0xbffff4c8], 0x0	       /* [ORIGINAL_SLICE] 80484b2  [SLICE_INFO] #src_mem[bffff4c8:1:4] #src_mem_value 15216*/
js jump_diverge       /* [ORIGINAL_SLICE] 80484b7  [SLICE_INFO] #src_flag[10:1:4] #branch_taken 1*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4c8)  //come with 80484c7 (move upwards)*/
mov eax, dword ptr [0xbffff4c8]	       /* [ORIGINAL_SLICE] 80484c7  [SLICE_INFO] #src_memregreg_mov[6:0:4,bffff4c8:1:4,0:0:0] #base_reg_value 3221222576, mem_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4b4)  //come with 80484cb (move upwards)*/
mov dword ptr [0xbffff4b4], eax	       /* [ORIGINAL_SLICE] 80484cb  [SLICE_INFO] #src_regregreg_mov[6:0:4,10:1:4,0:0:0] #base_reg_value 3221222576, reg_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4a0)  //come with b7ff2970 (move upwards)*/
mov  dword ptr [0xbffff4a0], eax	       /* [ORIGINAL_SLICE] b7ff2970  [SLICE_INFO] push instruction (rewrite) #src_reg[10:1:4], dst_mem[bffff4a0:0:4] #src_reg_value 15216, dst_mem_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff49c)  //come with b7ff2971 (move upwards)*/
mov  dword ptr [0xbffff49c], ecx	       /* [ORIGINAL_SLICE] b7ff2971  [SLICE_INFO] push instruction (rewrite) #src_reg[9:1:4], dst_mem[bffff49c:0:4] #src_reg_value 15216, dst_mem_value 3221222616*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff49c)  //come with b7ff2981 (move upwards)*/
mov ecx, dword ptr [0xbffff49c]	       /* [ORIGINAL_SLICE] b7ff2981  [SLICE_INFO] #src_memregreg_mov[6:0:4,bffff49c:1:4,0:0:0] #base_reg_value 3221222556, mem_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4a0)  //come with b7ff2987 (move upwards)*/
mov eax, dword ptr [0xbffff4a0]	       /* [ORIGINAL_SLICE] b7ff2987  [SLICE_INFO] #src_memregreg_mov[6:0:4,bffff4a0:1:4,0:0:0] #base_reg_value 3221222556, mem_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_TAINT] fstat64 bfffeec8 bfffeed0*/
/*Eliminated [SLICE_TAINT] fstat64 bfffeeb0 bfffeeb4*/
/*Eliminated [SLICE_TAINT] fstat64 bfffeec0 bfffeec4*/
/*Eliminated [SLICE_TAINT] fstat64 bfffeeb8 bfffeebc*/
call fstat64_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4b4)  //come with b7e861b6 (move upwards)*/
mov eax, dword ptr [0xbffff4b4]	       /* [ORIGINAL_SLICE] b7e861b6  [SLICE_INFO] #src_memregreg_mov[10:0:4,bffff4b4:1:4,0:0:0] #base_reg_value 3221222580, mem_value 15216, index_reg_value 0*/
mov ecx, eax	       /* [ORIGINAL_SLICE] b7e86164  [SLICE_INFO] #src_reg[10:1:4] #src_reg_value 15216*/
mov edx, eax	       /* [ORIGINAL_SLICE] b7e86166  [SLICE_INFO] #src_reg[10:1:4] #src_reg_value 15216*/
shr ecx, 0x1f	       /* [ORIGINAL_SLICE] b7e86168  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 15216*/
neg edx	       /* [ORIGINAL_SLICE] b7e8616b  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 15216*/
test ecx, ecx	       /* [ORIGINAL_SLICE] b7e8616d  [SLICE_INFO] #src_regreg[9:1:4,9:1:4] #dst_reg_value 0, src_reg_value 0*/
cmovnz eax, edx	       /* [ORIGINAL_SLICE] b7e8616f  [SLICE_INFO] #src_regflag[8:1:4,8:1:4] #reg_value 4294952080, flag_value TODO*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefd4)  //come with b7e86172 (move upwards)*/
mov dword ptr [0xbfffefd4], ecx	       /* [ORIGINAL_SLICE] b7e86172  [SLICE_INFO] #src_regregreg_mov[5:0:4,9:1:4,0:0:0] #base_reg_value 3221222536, reg_value 0, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e86178 (move upwards)*/
mov dword ptr [0xbfffefe4], eax	       /* [ORIGINAL_SLICE] b7e86178  [SLICE_INFO] #src_regregreg_mov[5:0:4,10:1:4,0:0:0] #base_reg_value 3221222536, reg_value 15216, index_reg_value 0*/
xor eax, eax	       /* [ORIGINAL_SLICE] b7e849cf  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 15216, src_reg_value 15216*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e849ed (move upwards)*/
mov eax, dword ptr [0xbfffefe4]	       /* [ORIGINAL_SLICE] b7e849ed  [SLICE_INFO] #src_memregreg_mov[5:0:4,bfffefe4:1:4,0:0:0] #base_reg_value 3221222536, mem_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffef70)  //come with b7e849f3 (move upwards)*/
mov dword ptr [0xbfffef70], eax	       /* [ORIGINAL_SLICE] b7e849f3  [SLICE_INFO] #src_regregreg_mov[6:0:4,10:1:4,0:0:0] #base_reg_value 3221221232, reg_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffef70)  //come with b7e81ad7 (move upwards)*/
mov ecx, dword ptr [0xbfffef70]	       /* [ORIGINAL_SLICE] b7e81ad7  [SLICE_INFO] #src_memregreg_mov[6:0:4,bfffef70:1:4,0:0:0] #base_reg_value 3221221212, mem_value 15216, index_reg_value 0*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 15216*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 15216, src_reg_value 4294952080, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 12172*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 1521, src_reg_value 1521*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 7605, src_reg_value 7605*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 15216, src_reg_value 15210*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be46*/
cmp ecx,0x6  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be46*/
push 0x0  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be46*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 1521, src_reg_value 1521*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 1521*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 1521*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 1521, src_reg_value 1521, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 1216*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 152, src_reg_value 152*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 760, src_reg_value 760*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 1521, src_reg_value 1520*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
cmp ecx,0x1  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
push 0x1  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 152, src_reg_value 152*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 152*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 152*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 152, src_reg_value 152, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 121*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 15, src_reg_value 15*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 75, src_reg_value 75*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 152, src_reg_value 150*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be42*/
cmp ecx,0x2  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be42*/
push 0x2  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be42*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 15, src_reg_value 15*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 15*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 15*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 15, src_reg_value 15, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 12*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 1, src_reg_value 1*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 5, src_reg_value 5*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 15, src_reg_value 10*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be45*/
cmp ecx,0x5  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be45*/
push 0x3  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be45*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 1, src_reg_value 1*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 1*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 1*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 1, src_reg_value 1, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 0*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 0, src_reg_value 0*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 0, src_reg_value 0*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 1, src_reg_value 0*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
cmp ecx,0x1  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
push 0x4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 0, src_reg_value 0*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 0*/
jnz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e83a9d (move upwards)*/
cmp dword ptr [0xbfffefe4], 0x0	       /* [ORIGINAL_SLICE] b7e83a9d  [SLICE_INFO] #src_mem[bfffefe4:1:4] #src_mem_value 15216*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e83aa4  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 0*/
xor edx, edx	       /* [ORIGINAL_SLICE] b7e83ad1  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 0, src_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e83b0d (move upwards)*/
cmp dword ptr [0xbfffefe4], 0x0	       /* [ORIGINAL_SLICE] b7e83b0d  [SLICE_INFO] #src_mem[bfffefe4:1:4] #src_mem_value 15216*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e83b1a  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefd4)  //come with b7e83b45 (move upwards)*/
mov eax, 0  /* [SLICE_EXTRA]//comes with b7e83b45*/
or eax, dword ptr [0xbfffefd4]	       /* [ORIGINAL_SLICE] b7e83b45  [SLICE_INFO] #src_memreg[bfffefd4:1:4,10:0:4] #mem_value 0, reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefd8)  //come with b7e83b4b (move upwards)*/
mov  dword ptr [0xbfffefd8]	    , 0   /* [SLICE_EXTRA]//comes with b7e83b4b*/
or eax, dword ptr [0xbfffefd8]	       /* [ORIGINAL_SLICE] b7e83b4b  [SLICE_INFO] #src_memreg[bfffefd8:0:4,10:1:4] #mem_value 0, reg_value 0*/
cmp eax, 0x1	       /* [ORIGINAL_SLICE] b7e83b51  [SLICE_INFO] #src_reg[10:1:4] #src_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefd4)  //come with b7e83b68 (move upwards)*/
cmp dword ptr [0xbfffefd4], 0x0	       /* [ORIGINAL_SLICE] b7e83b68  [SLICE_INFO] #src_mem[bfffefd4:1:4] #src_mem_value 0*/
jnz jump_diverge       /* [ORIGINAL_SLICE] b7e83b6f  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e83ba1 (move upwards)*/
cmp dword ptr [0xbfffefe4], 0x0	       /* [ORIGINAL_SLICE] b7e83ba1  [SLICE_INFO] #src_mem[bfffefe4:1:4] #src_mem_value 15216*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e83ba8  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 0*/
call write_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4c8)  //come with 80484db (move upwards)*/
mov eax, dword ptr [0xbffff4c8]	       /* [ORIGINAL_SLICE] 80484db  [SLICE_INFO] #src_memregreg_mov[6:0:4,bffff4c8:1:4,0:0:0] #base_reg_value 3221222576, mem_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4cc)  //come with 80484df (move upwards)*/
mov dword ptr [0xbffff4cc], eax	       /* [ORIGINAL_SLICE] 80484df  [SLICE_INFO] #src_regregreg_mov[6:0:4,10:1:4,0:0:0] #base_reg_value 3221222576, reg_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4cc)  //come with 80484e3 (move upwards)*/
mov eax, dword ptr [0xbffff4cc]	       /* [ORIGINAL_SLICE] 80484e3  [SLICE_INFO] #src_memregreg_mov[6:0:4,bffff4cc:1:4,0:0:0] #base_reg_value 3221222576, mem_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4b4)  //come with 80484e7 (move upwards)*/
mov dword ptr [0xbffff4b4], eax	       /* [ORIGINAL_SLICE] 80484e7  [SLICE_INFO] #src_regregreg_mov[6:0:4,10:1:4,0:0:0] #base_reg_value 3221222576, reg_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbffff4b4)  //come with b7e861b6 (move upwards)*/
mov eax, dword ptr [0xbffff4b4]	       /* [ORIGINAL_SLICE] b7e861b6  [SLICE_INFO] #src_memregreg_mov[10:0:4,bffff4b4:1:4,0:0:0] #base_reg_value 3221222580, mem_value 15216, index_reg_value 0*/
mov ecx, eax	       /* [ORIGINAL_SLICE] b7e86164  [SLICE_INFO] #src_reg[10:1:4] #src_reg_value 15216*/
mov edx, eax	       /* [ORIGINAL_SLICE] b7e86166  [SLICE_INFO] #src_reg[10:1:4] #src_reg_value 15216*/
shr ecx, 0x1f	       /* [ORIGINAL_SLICE] b7e86168  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 15216*/
neg edx	       /* [ORIGINAL_SLICE] b7e8616b  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 15216*/
test ecx, ecx	       /* [ORIGINAL_SLICE] b7e8616d  [SLICE_INFO] #src_regreg[9:1:4,9:1:4] #dst_reg_value 0, src_reg_value 0*/
cmovnz eax, edx	       /* [ORIGINAL_SLICE] b7e8616f  [SLICE_INFO] #src_regflag[8:1:4,8:1:4] #reg_value 4294952080, flag_value TODO*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefd4)  //come with b7e86172 (move upwards)*/
mov dword ptr [0xbfffefd4], ecx	       /* [ORIGINAL_SLICE] b7e86172  [SLICE_INFO] #src_regregreg_mov[5:0:4,9:1:4,0:0:0] #base_reg_value 3221222536, reg_value 0, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e86178 (move upwards)*/
mov dword ptr [0xbfffefe4], eax	       /* [ORIGINAL_SLICE] b7e86178  [SLICE_INFO] #src_regregreg_mov[5:0:4,10:1:4,0:0:0] #base_reg_value 3221222536, reg_value 15216, index_reg_value 0*/
xor eax, eax	       /* [ORIGINAL_SLICE] b7e849cf  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 15216, src_reg_value 15216*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e849ed (move upwards)*/
mov eax, dword ptr [0xbfffefe4]	       /* [ORIGINAL_SLICE] b7e849ed  [SLICE_INFO] #src_memregreg_mov[5:0:4,bfffefe4:1:4,0:0:0] #base_reg_value 3221222536, mem_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffef70)  //come with b7e849f3 (move upwards)*/
mov dword ptr [0xbfffef70], eax	       /* [ORIGINAL_SLICE] b7e849f3  [SLICE_INFO] #src_regregreg_mov[6:0:4,10:1:4,0:0:0] #base_reg_value 3221221232, reg_value 15216, index_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffef70)  //come with b7e81ad7 (move upwards)*/
mov ecx, dword ptr [0xbfffef70]	       /* [ORIGINAL_SLICE] b7e81ad7  [SLICE_INFO] #src_memregreg_mov[6:0:4,bfffef70:1:4,0:0:0] #base_reg_value 3221221212, mem_value 15216, index_reg_value 0*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 15216*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 15216, src_reg_value 4294952080, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 12172*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 1521, src_reg_value 1521*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 7605, src_reg_value 7605*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 15216, src_reg_value 15210*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be46*/
cmp ecx,0x6  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be46*/
push 0x5  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be46*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 1521, src_reg_value 1521*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 1521*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 1521*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 1521, src_reg_value 1521, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 1216*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 152, src_reg_value 152*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 760, src_reg_value 760*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 1521, src_reg_value 1520*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
cmp ecx,0x1  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
push 0x6  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 152, src_reg_value 152*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 152*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 152*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 152, src_reg_value 152, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 121*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 15, src_reg_value 15*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 75, src_reg_value 75*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 152, src_reg_value 150*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be42*/
cmp ecx,0x2  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be42*/
push 0x7  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be42*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 15, src_reg_value 15*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 15*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 15*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 15, src_reg_value 15, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 12*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 1, src_reg_value 1*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 5, src_reg_value 5*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 15, src_reg_value 10*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be45*/
cmp ecx,0x5  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be45*/
push 0x8  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be45*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 1, src_reg_value 1*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 1*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
mov eax, ecx	       /* [ORIGINAL_SLICE] b7e81b58  [SLICE_INFO] #src_reg[9:1:4] #src_reg_value 1*/
mov ebp, 3435973837  /* [SLICE_EXTRA]//comes with b7e81b5d*/
mul ebp	       /* [ORIGINAL_SLICE] b7e81b5d  [SLICE_INFO] #src_regregreg[10:1:4,8:1:4,5:0:4] #dst_reg_value 1, src_reg_value 1, count_reg_value 3435973837*/
shr edx, 0x3	       /* [ORIGINAL_SLICE] b7e81b5f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 0*/
lea eax, [edx+edx*4]	       /* [ORIGINAL_SLICE] b7e81b62  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 0, src_reg_value 0*/
add eax, eax	       /* [ORIGINAL_SLICE] b7e81b65  [SLICE_INFO] #src_regreg[10:1:4,10:1:4] #dst_reg_value 0, src_reg_value 0*/
sub ecx, eax	       /* [ORIGINAL_SLICE] b7e81b67  [SLICE_INFO] #src_regreg[9:1:4,10:1:4] #dst_reg_value 1, src_reg_value 0*/
pushfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
cmp ecx,0x1  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
push 0x9  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
jne index_diverge  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
add esp, 4  /* [SLICE_VERIFICATION]//comes with b7e81b6b*/
popfd  /* [SLICE_VERIFICATION]//comes with b7e81b6b (move upwards), address b7f8be41*/
mov edi, 0xb7f8be40  /* [SLICE_ADDRESSING]//comes with b7e81b6b (move upwards)*/
test edx, edx	       /* [ORIGINAL_SLICE] b7e81b69  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 0, src_reg_value 0*/
mov ecx, edx	       /* [ORIGINAL_SLICE] b7e81b6f  [SLICE_INFO] #src_reg[8:1:4] #src_reg_value 0*/
jnz jump_diverge       /* [ORIGINAL_SLICE] b7e81b73  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e83a9d (move upwards)*/
cmp dword ptr [0xbfffefe4], 0x0	       /* [ORIGINAL_SLICE] b7e83a9d  [SLICE_INFO] #src_mem[bfffefe4:1:4] #src_mem_value 15216*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e83aa4  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 0*/
xor edx, edx	       /* [ORIGINAL_SLICE] b7e83ad1  [SLICE_INFO] #src_regreg[8:1:4,8:1:4] #dst_reg_value 0, src_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e83b0d (move upwards)*/
cmp dword ptr [0xbfffefe4], 0x0	       /* [ORIGINAL_SLICE] b7e83b0d  [SLICE_INFO] #src_mem[bfffefe4:1:4] #src_mem_value 15216*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e83b1a  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefd4)  //come with b7e83b45 (move upwards)*/
mov eax, 0  /* [SLICE_EXTRA]//comes with b7e83b45*/
or eax, dword ptr [0xbfffefd4]	       /* [ORIGINAL_SLICE] b7e83b45  [SLICE_INFO] #src_memreg[bfffefd4:1:4,10:0:4] #mem_value 0, reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefd8)  //come with b7e83b4b (move upwards)*/
mov  dword ptr [0xbfffefd8]	    , 0   /* [SLICE_EXTRA]//comes with b7e83b4b*/
or eax, dword ptr [0xbfffefd8]	       /* [ORIGINAL_SLICE] b7e83b4b  [SLICE_INFO] #src_memreg[bfffefd8:0:4,10:1:4] #mem_value 0, reg_value 0*/
cmp eax, 0x1	       /* [ORIGINAL_SLICE] b7e83b51  [SLICE_INFO] #src_reg[10:1:4] #src_reg_value 0*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefd4)  //come with b7e83b68 (move upwards)*/
cmp dword ptr [0xbfffefd4], 0x0	       /* [ORIGINAL_SLICE] b7e83b68  [SLICE_INFO] #src_mem[bfffefd4:1:4] #src_mem_value 0*/
jnz jump_diverge       /* [ORIGINAL_SLICE] b7e83b6f  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 1*/
/*Eliminated [SLICE_ADDRESSING] immediate_address $addr(0xbfffefe4)  //come with b7e83ba1 (move upwards)*/
cmp dword ptr [0xbfffefe4], 0x0	       /* [ORIGINAL_SLICE] b7e83ba1  [SLICE_INFO] #src_mem[bfffefe4:1:4] #src_mem_value 15216*/
jz jump_diverge       /* [ORIGINAL_SLICE] b7e83ba8  [SLICE_INFO] #src_flag[8:1:4] #branch_taken 0*/
call write_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
call write_recheck    /* [ORIGINAL_SLICE] 00000000  [SLICE_INFO]*/
/* restoring address and registers */
/* slice finishes and return to kernel */
mov ebx, 1
mov eax, 350
int 0x80
/* function that handles jump divergence */
jump_diverge:
push eax
push ecx
push edx
call handle_jump_diverge
push edx
push ecx
push eax
/* function that handles index divergence */
index_diverge:
push eax
push ecx
push edx
call handle_index_diverge
push edx
push ecx
push eax

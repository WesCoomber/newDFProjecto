








call access_recheck 
call open_recheck 
call stat64_recheck 
call open_recheck 
call stat64_recheck 
call open_recheck 
call stat64_recheck 
call open_recheck 
call stat64_recheck 
call open_recheck 
call stat64_recheck 
call open_recheck 
call stat64_recheck 
call open_recheck 
call stat64_recheck 
call open_recheck 
call read_recheck 
MRange,fstat64 [0xbfffef68] [0xbfffef70]
MRange,fstat64 [0xbfffef50] [0xbfffef54]
MRange,fstat64 [0xbfffef60] [0xbfffef64]
MRange,fstat64 [0xbfffef58] [0xbfffef5c]
call fstat64_recheck 

mov edi dword ptr [0xbfffef68]	 

mov ecx dword ptr [0xbfffef6c]	 
mov edx 0 
xor edx ecx	 
mov eax 0 
xor eax edi	 
or edx eax	 
jz jump_diverge 
mov edx 0 
xor edx ecx	 
mov eax 0 
xor eax edi	 
or edx eax	 
jz jump_diverge 
mov edx 0 
xor edx ecx	 
mov eax 0 
xor eax edi	 
or edx eax	 
jz jump_diverge 

mov dword ptr [0xbfffee74] edi	 

mov edi	 dword ptr [0xbfffee74] 
call close_recheck 

mov eax dword ptr [0xbfffef68]	 

mov edx dword ptr [0xbfffef6c]	 

mov dword ptr [0xb7fdde98] eax	 

mov dword ptr [0xb7fdde9c] edx	 
call getpid_recheck 
mov ecx eax	 

mov dword ptr [0xb7e41728] ecx	 
mov eax ecx	 

mov dword ptr [0xbffff4c8] eax	 

cmp dword ptr [0xbffff4c8] 0x0	 
js jump_diverge 

mov eax dword ptr [0xbffff4c8]	 

mov dword ptr [0xbffff4b4] eax	 

mov dword ptr [0xbffff4a0] eax	 

mov dword ptr [0xbffff49c] ecx	 

mov ecx dword ptr [0xbffff49c]	 

mov eax dword ptr [0xbffff4a0]	 
MRange,fstat64 [0xbfffeec8] [0xbfffeed0]
MRange,fstat64 [0xbfffeeb0] [0xbfffeeb4]
MRange,fstat64 [0xbfffeec0] [0xbfffeec4]
MRange,fstat64 [0xbfffeeb8] [0xbfffeebc]
call fstat64_recheck 

mov eax dword ptr [0xbffff4b4]	 
mov ecx eax	 
mov edx eax	 
shr ecx 0x1f	 
neg edx	 
test ecx ecx	 
cmovnz eax edx	 

mov dword ptr [0xbfffefd4] ecx	 

mov dword ptr [0xbfffefe4] eax	 
xor eax eax	 

mov eax dword ptr [0xbfffefe4]	 

mov dword ptr [0xbfffef70] eax	 

mov ecx dword ptr [0xbfffef70]	 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x6 
push 0x0 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jz jump_diverge 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x1 
push 0x1 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jz jump_diverge 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x2 
push 0x2 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jz jump_diverge 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x5 
push 0x3 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jz jump_diverge 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x1 
push 0x4 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jnz jump_diverge 

cmp dword ptr [0xbfffefe4] 0x0	 
jz jump_diverge 
xor edx edx	 

cmp dword ptr [0xbfffefe4] 0x0	 
jz jump_diverge 

mov eax 0 
or eax dword ptr [0xbfffefd4]	 

mov dword ptr [0xbfffefd8]	 0 
or eax dword ptr [0xbfffefd8]	 
cmp eax 0x1	 

cmp dword ptr [0xbfffefd4] 0x0	 
jnz jump_diverge 

cmp dword ptr [0xbfffefe4] 0x0	 
jz jump_diverge 
call write_recheck 

mov eax dword ptr [0xbffff4c8]	 

mov dword ptr [0xbffff4cc] eax	 

mov eax dword ptr [0xbffff4cc]	 

mov dword ptr [0xbffff4b4] eax	 

mov eax dword ptr [0xbffff4b4]	 
mov ecx eax	 
mov edx eax	 
shr ecx 0x1f	 
neg edx	 
test ecx ecx	 
cmovnz eax edx	 

mov dword ptr [0xbfffefd4] ecx	 

mov dword ptr [0xbfffefe4] eax	 
xor eax eax	 

mov eax dword ptr [0xbfffefe4]	 

mov dword ptr [0xbfffef70] eax	 

mov ecx dword ptr [0xbfffef70]	 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x6 
push 0x5 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jz jump_diverge 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x1 
push 0x6 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jz jump_diverge 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x2 
push 0x7 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jz jump_diverge 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x5 
push 0x8 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jz jump_diverge 
mov eax ecx	 
mov ebp 3435973837 
mul ebp	 
shr edx 0x3	 
lea eax [edx+edx*4]	 
add eax eax	 
sub ecx eax	 
pushfd 
cmp ecx0x1 
push 0x9 
jne index_diverge 
add esp 4 
popfd 
test edx edx	 
mov ecx edx	 
jnz jump_diverge 

cmp dword ptr [0xbfffefe4] 0x0	 
jz jump_diverge 
xor edx edx	 

cmp dword ptr [0xbfffefe4] 0x0	 
jz jump_diverge 

mov eax 0 
or eax dword ptr [0xbfffefd4]	 

mov dword ptr [0xbfffefd8]	 0 
or eax dword ptr [0xbfffefd8]	 
cmp eax 0x1	 

cmp dword ptr [0xbfffefd4] 0x0	 
jnz jump_diverge 

cmp dword ptr [0xbfffefe4] 0x0	 
jz jump_diverge 
call write_recheck 
call write_recheck 


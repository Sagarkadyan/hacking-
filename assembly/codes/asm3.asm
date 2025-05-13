global _start

section .text
_start:
 mov ebx, 42
 mov eax,1
 jmp skip ; jump to skip  label 
 mov ebx,13;this code is spkipped by jump 
skip:
 mov ebx,17
 int 0x80 

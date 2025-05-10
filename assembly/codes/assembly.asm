;x86 assembl
; first two lines define entry point for the proagram


global  _start  ; global keyword is uded to make an identifier to linker
; here start is an identifier
_start:  ;colen after a identifier make a lael
; lale ae used o name location
  mov eax,1 ; moves integer  to eax reister 
  mov ebx, 44 ; moves integer to ebx register  
  sub ebx,29 ;suac value  
  int 0x80
  
import sys
f=open(sys.argv[1])
for line in f:
    
#   line=line.replace('movl','movq')
    if line == '.cfi_def_cfa_offset 8\n':
       line= '.cfi_def_cfa_offset 16'
    if line == '.cfi_offset 5, -8\n':
       line= '.cfi_def_cfa_offset 6 -16'
    if line == '.cfi_def_cfa_register 5\n':
       line= '.cfi_def_cfa_register 6'
    line=line.replace("rsp","rcp")
    line=line.replace('ebp','rbp')

    line=line.replace('8','16')
    line=line.replace(' 5',' 6')
    line=line.replace('esp','rsp')
    line=line.replace('pushl','pushq')
    if  '%rsp' in line:
      print''' 
        movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	$5, -12(%rbp)
	movl	$3, -8(%rbp)
	movl	-8(%rbp), %eax
	movl	-12(%rbp), %edx
	addl	%edx, %eax
	movl	%eax, -4(%rbp)
	movl	$.LC0, %eax
	movl	-4(%rbp), %edx
	movl	%edx, %esi
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf
	leave
	.cfi_def_cfa 7, 8
	ret
       .cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3"
	.section	.note.GNU-stack,"",@progbits'''
      break
    print line,
  

#	movl	%esp, %ebp
#	.cfi_def_cfa_register 5
#	andl	$-16, %esp
#	subl	$32, %esp
#	movl	$5, 20(%esp)
#	movl	$3, 24(%esp)
#	movl	24(%esp), %eax
#	movl	20(%esp), %edx
#	addl	%edx, %eax
#	movl	%eax, 28(%esp)
#	movl	$.LC0, %eax
#	movl	28(%esp), %edx
#	movl	%edx, 4(%esp)
#	movl	%eax, (%esp)
#	call	printf
#	leave

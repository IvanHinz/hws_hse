# Input a cardinal N, then N integers. Output line by line only even ones, in reversed order.
	.text
main:
	li t4, 1
	li t6, 2
	li a7, 5
	ecall
	mv t0, a0
	bnez t0, element

element:
	# entering the elements
	ecall
	addi t0, t0, -1
	rem t2, a0, t6
	beqz t2, adding
	bnez t0, element
	j end
	
adding:
	# adding only even numbers to stack
	addi sp, sp, -4
	sw a0, (sp)
	addi t5, t5, 1
	bnez t0, element
	j end
	
end:
	li a7, 1
	
	bnez t5, loading
	j main_end
	
loading:
	# load the first element from stack if it exists
	lw a0, (sp)
	ecall
	
	li a7, 11
	li   a0, '\n'
	ecall
	
	li a7, 1
	
	addi t5, t5, -1
	bnez t5, main_loading
	j main_end
	
main_loading:
	# load other elements from stack if the exist
	addi sp, sp, 4
	lw a0, (sp)
	ecall
	
	li a7, 11
	li   a0, '\n'
	ecall
	
	li a7, 1
	
	addi t5, t5, -1
	bnez t5, main_loading
	j main_end
	
main_end:


	
	
	
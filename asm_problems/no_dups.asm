# Input a cardinal N, then N integers. Output all the integers, skipping duplicated ones.
	.text
main:
	li a7, 5 # doing it to input our number of elements from the console
	# our variables
	li t3, 0 # t3 will be the current number of elements in stack
	li t6, 4 # t6 will be the stack step
	
	ecall
	mv t0, a0
	bnez t0, add_first
	j main_end
	
add_first:
	ecall
	addi sp, sp, -4
	sw a0, (sp) 
	addi t3, t3, 1
	addi t0, t0, -1
	# here we uploaded our first element, the number of elements in stack and how many elements we should continue input 
	bnez t0, weiter
	j output # we jump to ouput

weiter:
	ecall
	mv t2, t3
	li s2, 0
	j check
	
check:
	lw t5, (sp)
	addi t2, t2, -1
	
	beq t5, a0, not_passed
	bnez t2, move_pointer
	
	# our number is not in stack
	mul s3, s2, t6
        sub sp, sp, s3
        
        addi sp, sp, -4
        sw a0, (sp)
        addi t3, t3, 1
        addi t0, t0, -1
        
        bnez t0, weiter
        j output
	 
# our number is in stack
not_passed:
	mul s3, s2, t6
        sub sp, sp, s3
       
        addi t0, t0, -1
        
        bnez t0, weiter
        j output

move_pointer:
	addi sp, sp, 4
	addi s2, s2, 1
	j check	
		
output:
	# out put an element from stack
	li a7, 1
	lw a0, (sp)
	ecall
	
	li a7, 11
	li   a0, '\n'
	ecall
	
	li a7, 1
	
	addi t3, t3, -1
	
	bnez t3, change_pointer
	j main_end

# changing stack pointer	
change_pointer:
	addi sp, sp, 4
	j output
	
main_end:	
	
	

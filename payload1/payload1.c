int main(void) 
{
    asm volatile("li a0, %0\nli a1, %1\nli a2, %2\necall\n"
                 :
                 : "i"(3),"i"(0x800039A4),"i"(4)
                 : "a0", "a1","a2");      
    asm volatile("li a0, %0\nli a1, %1\nli a2, %2\necall\n"
                 :
                 : "i"(1),"i"(0),"i"(0)
                 : "a0", "a1","a2");           
    return 0;     
             
}

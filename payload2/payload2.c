#define debug_key 3557635140
#define stack_size 0
int main(void) 
{
    asm volatile("li a0, %0\nli a1, %1\necall\n"
                 :
                 : "i"(7),"i"(debug_key)
                 : "a0", "a1");
    asm volatile("li a0, %0\nli a1, %1\necall\n"
                 :
                 : "i"(5),"i"(stack_size)
                 : "a0", "a1");                  
    asm volatile("li a0, %0\nli a1, %1\necall\n"
                 :
                 : "i"(6),"i"(0x80003920)
                 : "a0", "a1");
    // asm volatile("li a0, %0\nmv a1,a5\necall\n"
    //              :
    //              : "i"(2)
    //              : "a0", "a1");                 
    // asm volatile("li a0, %0\nsrli a1,a5,%1\necall\n"
    //              :
    //              : "i"(2),"i"(0x08)
    //              : "a0", "a1");
    // asm volatile("li a0, %0\nsrli a1,a5,%1\necall\n"
    //              :
    //              : "i"(2),"i"(0x10)
    //              : "a0", "a1"); 
    // asm volatile("li a0, %0\nsrli a1,a5,%1\necall\n"
    //              :
    //              : "i"(2),"i"(0x18)
    //              : "a0", "a1");                         
    asm volatile("li a0, %0\nli a1, %1\nli a2,%2\necall\n"
                 :
                 : "i"(1),"i"(0),"i"(0)
                 : );                                                                                                                           
}

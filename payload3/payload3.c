typedef unsigned int uint32_t;

// volatile char rst_command[9];
// #define RST_A      *(volatile char*)0x20001AA0
// #define RST_T1     *(volatile char*)0x20001AA1
// #define RST_PLUS   *(volatile char*)0x20001AA2
// #define RST_R      *(volatile char*)0x20001AA3
// #define RST_S      *(volatile char*)0x20001AA4
// #define RST_T2     *(volatile char*)0x20001AA5
// #define RST_1      *(volatile char*)0x20001AA6
// #define RST_2      *(volatile char*)0x20001AA7
const char *rst_command = "AT+RST\r\n";
#define SPI_FUNC 0x20000208
int main() {
  // RST_A = 'A';
  // RST_T1 = 'T';
  // RST_PLUS = '+';
  // RST_R = 'R';
  // RST_S = 'S';
  // RST_T2 = 'T';
  // RST_1 = '\r';
  // RST_2 = '\n';
  //trigger interrupt 
  asm volatile("li a0, %0\nli a1, %1\nli a2,%2\necall\n"
                 :
                 : "i"(0x94),"i"(0),"i"(0)
                 :);       
  asm volatile("lui a0, %0\naddi a0,a0,%1\nli a1, %1\nli a2,%2\n"
                 :
                 : "i"(0x08001),"i"(0x000),"i"(0)
                 :);       
  asm volatile("lui a6, %0\naddi a6,a6,%1\njalr ra,a6,0\n"
                 :
                 : "i"(0x20000),"i"(0x208),"i"(0)
                 :);                      

  //AT_RST_COMMAND_LEN = 9;
  // AT_RST_COMMAND = (char)0x80003104;                                                                                                                                             
  return 0;   
  }
  

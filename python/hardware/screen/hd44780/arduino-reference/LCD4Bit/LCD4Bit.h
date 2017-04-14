#ifndef LCD4Bit_h
#define LCD4Bit_h

#include <inttypes.h>

class LCD4Bit {
public:
  LCD4Bit(int num_lines);
  void commandWrite(int value);
  void init();
  void print(int value);
  void printIn(char value[]);
  void clear();

  //non-core---------------
  void cursorTo(int line_num, int x);
  void leftScroll(int chars, int delay_time);
  //end of non-core--------

  //4bit only, therefore ideally private but may be needed by user
  void commandWriteNibble(int nibble);
private:
  void pulseEnablePin();
  void pushNibble(int nibble);
  void pushByte(int value);
  void WriteCGRAM(int adress, char code[]);
};
#endif
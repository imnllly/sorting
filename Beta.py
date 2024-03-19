// Библиотека для работы с текстовым дисплеем
#include <LiquidCrystal.h>
 
// Задаём имя пинов дисплея
constexpr uint8_t PIN_RS = 6;
constexpr uint8_t PIN_EN = 7;
constexpr uint8_t PIN_DB4 = 8;
constexpr uint8_t PIN_DB5 = 9;
constexpr uint8_t PIN_DB6 = 10;
constexpr uint8_t PIN_DB7 = 11;

 
LiquidCrystal lcd(PIN_RS, PIN_EN, PIN_DB4, PIN_DB5, PIN_DB6, PIN_DB7);
 
void setup() {
  // Устанавливаем размер экрана
  // Количество столбцов и строк
  lcd.begin(16, 2);
  // Устанавливаем курсор в колонку 0 и строку 0
  lcd.setCursor(0, 0);
  // Печатаем первую строку
  lcd.print("CODE: 1488");
  // Устанавливаем курсор в колонку 0 и строку 1
  lcd.setCursor(0, 1);
  // Печатаем вторую строку
  while (true)
  {
    int first[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
    for(int i = 0; i<9; i++)
    {
      lcd.print(first[i]);
    }
  }
}
 
void loop() {
}
